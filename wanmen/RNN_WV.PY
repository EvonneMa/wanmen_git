from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import SimpleRNN, LSTM, GRU
from keras.optimizers import RMSprop
from keras.initializers import RandomNormal, Identity
#from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np
import random
from gensim.models import Word2Vec
import jieba
import tensorflow as tf
import copy
#import re
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.allow_growth=True
set_session(tf.Session(config=config))
#代码正式开始
def load_text(path):
	with open(path,'r',encoding = 'utf-8') as f:
		text = f.read()
	text = text.replace('\n','')
	text = text.replace(' ','')
	text = text.replace('“','')
	text = text.replace('”','')
	#text = text.decode('utf-8')
	return text
#至此生成了需要的样本
def cut_sentence(text):
	start = 0
	i = 0
	tokens = text[i+1]
	sentence = []
	punc = '.!?~． 。！？,，～\n'
	for word in text:
		if word in punc and tokens not in punc:
			sentence.append(text[start:i])
				# i+1 含有句末的标点符号一起记录
				# i 不含标点
			start = i + 1
			i += 1
		else:
			i += 1
			tokens = list(text[start:i+2]).pop()
	if start < len(text):
		sentence.append(text[start:])
	#print(sentence)
	return sentence
def Gensim_data(path,maxlen,step,text_length = 500000,size = 40):
	text = load_text(path)
	text = text[:text_length]#选择一部分文本做示范
	words = []
	sens = cut_sentence(text)
	for sen in sens:
		words.append([w for w in jieba.cut(sen)])
	#利用jieba完成了分词
	a = []
	for ele in words:
		a.extend(ele)
	text = copy.deepcopy(a)
	#print('第一回' in set(text))
	# text为由单词构成的文章而不是由每一个汉字
	a = sorted(list(set(a)))
	char_index = {}
	index_char = {}
	for i,c in enumerate(a):
		char_index[c] = i
		index_char[i] = c
	#print('第一回' in set(text))
	model = Word2Vec(words,size = size,min_count = 1)
	#print('第一回' in model.wv.vocab)
	model.save('hlm_wv.model.bin')
	sentences = [] # 真正用来生成句子
	next_char = []
	#print(len(text),len(a))
	for i in range(0,len(text)-maxlen-step-1,step):
		sentences.append(text[i:i+maxlen])
		next_char.append(text[i+maxlen])
		#print(i)
	return sentences,next_char,char_index,index_char,i+1,text,len(a),model
def Generator(char_index,sentences,next_char,maxlen,len_sen,len_char,size,model,batch_size = 128):
	'''
	采用生成器yield,是因为每个epochs都要用到(x,y),但是不想每次都调用Generator,因此用了yield
	值得注意的是:由于每次的样本都一样,因此这里其实可以直接生成一套(x,y),然后循环使用
	学习一下yield的用法
	'''
	wv = model.wv.vocab
	#print('第一回' in wv)
	while(1):
		for i in range(int(len_sen/batch_size - 1)):
			x = np.zeros((batch_size,maxlen,size),dtype = np.bool) 
			#使用bool可以减少空间资源使用
			y = np.zeros((batch_size,len_char),dtype = np.bool)
			batch_sentences = sentences[i*batch_size:(i+1)*batch_size]
			batch_label = next_char[i*batch_size:(i+1)*batch_size]
			for j,sentence in enumerate(batch_sentences):
				y[j,char_index[batch_label[j]]] = 1
				for k,char in enumerate(sentence):
					x[j,k,:] = wv[char]
			yield x,y
			# 这里yield就相当于return
def gen_model(maxlen,size,len_char,output_dim,lr,activation,loss):
	'''
	开始搭建模型
	'''
	model = Sequential()
	#核心用法就是model.add()
	model.add(LSTM(output_dim,input_shape = (maxlen,size)))
	# LSTM(输出神经元个数,input_shape = (xt的个数,每个xt被转换成的向量的维度))
	# LSTM自动计算batch_size
	# 输出神经元个数决定了ht的维度,ht = x * W + ht-1 * U, x = input
	# 参数return_sequences决定是否输出每一个ht,如果为否则只输出最后一个
	model.add(Dense(len_char))
	# 添加一个全连接层,共有len(chars)个神经元,象征预测结果对应的向量
	# 由于添加了一个全连接层,因此LSTM的输出神经元个数就可以灵活一点
	model.add(Activation(activation))
	# 激活函数,需要概率因此使用softmax
	optimizer = RMSprop(lr = lr)
	# 优化器,推荐使用RMSprop,Adam效果比较差
	model.compile(loss = loss,optimizer = optimizer)
	# 定义损失函数
	return model
def sample(preds,diversity = 1.0):
	'''
	稍稍改变一下概率,使得输出多样性(即‘我’可以输出‘是’也可以输出‘喜欢’等等)
	'''
	preds = np.asarray(preds).astype(np.float64)
	preds = np.log(preds)/diversity
	preds = np.exp(preds)
	preds = preds/np.sum(preds)
	probas = np.random.multinomial(1,preds,1)
	# 随机选取一个字,每个字被选中的概率为preds[i]
	return np.argmax(probas)
def on_epoch_end(length,text,model,index_char,char_index,maxlen,text_length,size,wv_model,diversity = 1.0):
	wv = wv_model.wv.vocab
	start_index = random.randint(0,text_length-maxlen-1)
	# 随机生成开始的词语
	content = ''
	x = text[start_index:start_index+maxlen]
	#print(content)
	content += ''.join(x)
	for i in range(length):
		'''
		每生成一个字都做相应的改变
		'''
		x_pred = np.zeros((1,maxlen,size),dtype = bool)
		# 注意,这里的1不能省略,因为维度必须是3
		for pos,char in enumerate(x):
			x_pred[0,pos,:] = wv[char]
		res = model.predict(x_pred,verbose = 0)[0]
		# 注意,这里的[0]同样不能省,res还是向量
		char_index_pred = sample(res,diversity)
		char_pred = index_char[char_index_pred]
		# 得到真正的预测单词
		content += char_pred
		x = x[1:]
		x.append(char_pred)
	return content
def main():
	'''
	定义一下参数
	'''
	text_length = 500000
	maxlen = 40
	step = 1
	size = 100
	batch_size = 128
	lr = 0.01
	activation = 'softmax'
	loss = 'categorical_crossentropy'
	output_dim = 128
	diversity = 1.0 
	epoch  = 10 #训练次数
	length = 400 #要预测多长的句子
	path = 'd:/file/selflearning/ml/Week2_NLP/data/sstt.txt'
	sentences,next_char,char_index,index_char,len_sen,text,len_char,wv_model = Gensim_data(path,maxlen,step,text_length,size)
	generator = Generator(char_index,sentences,next_char,maxlen,len_sen,len_char,size,wv_model,batch_size)
	model = gen_model(maxlen,size,len_char,output_dim,lr,activation,loss)
	model.fit_generator(generator,steps_per_epoch = int(len_sen/batch_size),epochs = epoch)
	# 这里就不是简单的fit了
	res = on_epoch_end(length,text,model,index_char,char_index,maxlen,text_length,size,wv_model,diversity)
	print(res)
if __name__ == '__main__':
	main()