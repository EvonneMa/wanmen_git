# 读取文字描述,查看大概数据情况
# 整理标签
# 整理summary文字,建立语料库
# 建模
# 结果
# 思路：
#		利用正负面描述的词语频率预测Amazon商品评价
import nltk

import pandas as pd
import numpy as np
import scipy as sp
import sklearn as sk
import os.time,re,string
from sklearn.model_selection import train_test_split,KFold
from sklearn import metrics
import matplotlib.pyplot as plt

from nltk import FreqDist
# supervised learning
# 一、读取文字描述,查看大概数据情况
data = pd.read_csv('amazon-fine-food-reviews/Reviews.csv')
#查看数据粗略统计,为后续处理提供思路
data.info()
#生成数据的大概描述
df_uni = pd.DataFrame(index = range(10), columns = ['Feature','No. of NAs','No. of Unique Values','# of total samples','Unique percentage(%)'])
for i,col in enumerate(data.columns):
    feat_na = data[col].isnull().sum(axis = 0)
    feat_uni = data[col].unique().shape[0]
    perc = feat_uni/data[col].shape[0]*100
    df_uni.iloc[i,:] = [col,feat_na,feat_uni,data.shape[0],perc]
data = data.dropna()
# 二、创建标签列
label = data['Score'].apply(lambda x:1 if x > 3 else 0)
# 三、整理summary,建立语料库
# 3.1 整理summary
#	1.去标点符号
s = data['Summary'].apply(lambda text:text.lower())
s_new = []
for i in range(s.shape[0]):
	s_new.append(re.sub('[\W]+',' ',s.iloc[i]))
Summary = pd.Series(s_new)
# 	2.分词(从这里开始是对每一步进行熟悉,不是最后的代码,最终代码见第四步第一部分)
from nltk import word_tokenize
words = [word_tokenize(text) for text in Summary] 
#word_tokenize的参数为一个句子,返回一个由词汇构成的list
#	3.去掉stopwords
from nltk.corpus import stopwords
#stopwords.words('language')可以查看目标语言的stopwords,是个list	
def remove_stopwords(sub_words):
	return[word for word in sub_words if word not in stopwords.words('english')]
words_without_stopwords = [remove_stopwords(sub_words) for sub_words in words]
#这种写法更PYTHON
#注意list.append和list.extend的区别,以及np.hstack()的使用
words_wo_sw_h = np.hstack(words_without_stopwords) #合并所有的子列表,形成一个大列表
#注意：stopwords含有not等词汇,需要进一步考虑,如构造not_happy等词汇
#	4.词干提取stemming、词性还原lemmatization,这两个包都不是很权威
from nltk.stem import PorterStemmer
porter = PorterStemmer() #删除时态
from nltk import WordNetLemmatizer
wnl = WordNetLemmatizer() #删除单复数
stem_words = [porter.stem(word) for word in words_wo_sw_h]
lem_words = [wnl.lemmatize(word) for word in words_wo_sw_h]
fdist_wo = pd.DataFrame(list(FreqDist(words_wo_sw_h).items()),columns = ['word','freq'])
fdist_w = pd.DataFrame(list(FreqDist(np.hstack(words)).items()),columns = ['word','Freq'])
#学习这种从dict构造DataFrame的方式,借助了list
# 3.2 创建语料库
from nltk import ngrams
bigram_w = []
for token in words:
	bigram = nltk.bigram(token)
	for item in bigram:
		bigram_w.append(item)
bigram_wo = []
for token in words_without_stopwords:
	bigram = nltk.bigram(token)
	for item in bigram:
		bigram_wo.append(item)
bifqw = pd.DataFrame(list(FreqDist(bigram_w).items()),columns = ['bi_w','bicount_w'])
bifqwo = pd.DataFrame(list(FreqDist(bigram_wo).items()),columns = ['bi_wo','bicount_wo'])
bifqw.sort_values(by = 'bicount_w',inplace = True,ascending = False)
bifqwo.sort_values(by = 'bicount_wo',inplace = True,ascending = False)
# 四、建模(这里首先对第三步进行了整合,因此有些工作是重复的)
#  	1.预处理——将数据转化成频率
def stem_tokens(tokens,stemmer = PorterStemmer()):
	'''
	输入为分词后的一句话,对每个单词去时态,返回list
	'''
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed
def tokenize(text):
	'''
	输入为一句话,先分词,后去时态,最后以' '连接每个单词构成字符串形式的一句话
	'''
	tokens = nltk.word_tokenize(text)
	stems = stem_tokens(tokens)
	return ' '.join(stems)
def build_corpus(dataset):
	'''
	输入为每一条评论构成的list,对每一条评论调用tokenize()
	'''
	corpus = []
	for text in dataset:
		corpus.append(tokenize(text))
	return corpus
n = 10000
X = Summary[:n]
y = label[:n]
seed = 2018
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = seed)
train_token = build_corpus(X_train)
test_token = build_corpus(X_test)
#TF-IDF
#	TF=词汇i在文章j中出现的频率
#	IDF=log(文章总篇数/带有词汇i的文章篇数)
#	以TF*IDF作为评价将词汇i认定为文章j的关键词的标准
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec = TfidfVectorizer()
X_train_tfidf_vec = tfidf_vec.fit_transform(train_token)
X_test_tfidf_vec = tfidf_vec.fit_transform(test_train)
#返回一个稀疏矩阵(行数为总评论条数,列数为不重复单词的个数),指出哪些位置的元素不为零
#可以使用tfidf_vec.get_feature_names()来观察都有哪些单词
#	2.调用模型
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
lr = LogisticRegression().fit(X_train_tfidf_vec,y_train_tfidf_vec)
rfc = RandomForestClassifier(n_estimators = 50, max_depth = 10)
models = {'lr':lr,'rfc':rfc}
results = pd.DataFrame(index = ['lr','rfc'],columns = ['f1','pre','recall','auc'])
for (name,model) in models.items():
	y_pred = model.predict(X_text_tfidf_vec)
	f1 = metrics.f1_score(y_test,y_pred)
	pre = metrics.precision_score(y_test,y_pred)
	recall = metrics.recall_score(y_test,y_pred)
	auc = metrics.roc_auc_score(y_test,y_pred)
	results.loc[name,:] = [f1,pre,recall,auc]


