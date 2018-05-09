import jieba
import re
import copy
from sklearn.preprocessing import LabelEncoder
import numpy as np
from collections import OrderedDict
f = open('data/hongloumeng.txt',encoding = 'UTF-8')
context = f.read()
f.close()
context = re.sub('[.��]','��',context)
context = re.sub('[^\u4E00-\u9FA5������\t\n]','',context)   #re.sub�����滻
context = re.split('[������\n\t]+',context)
f = open('data/clean_hlm.txt','w')
for str in context:
f.write(str+'\n')
f.close()
words = [list(jieba.cut(s)) for s in context]
generate_ngram = lambda sentence,n : zip(*[sentence[i:] for i in range(n)])
def ngrams_parameter_estimate(sentences,n):
    '''
    ����n_gram�������ֵ�{Ԫ�飺����}����������
    '''
    sentences_copy = copy.deepcopy(sentences)
    ngram_dict = {}
    num_ngrams = 0
    for words in sentences_copy:
        for i in range(n-1):
            words.insert(0,'*')  #�ھ������һ������*
        words.append('#')
        ngrams = generate_ngram(words,n)
        for ngram in ngrams:
            ngram_dict[ngram] = ngram_dict.get(ngram,0.0)+1.0  
            #get:�ж�ӦԪ����ֱ��ȡ����û���򴴽�������0
            num_ngrams = num_ngrams+1 #���ص�ǰ���ӵ�ngram����
    return ngram_dict,num_ngrams
n_samples = len(words)
n_valid = int(n_samples*0.1)
n_test = int(n_samples*0.2)
permutation = np.random.permutation(n_samples)
new_words = np.array(words)[permutation]
train = new_words[:n_samples-n_test-n_valid]
valid = new_words[n_samples-n_test-n_valid:n_samples-n_test]
test = new_words[n_samples-n_test:]
unigram_dict,n_unigram = ngrams_parameter_estimate(train,1)
bigram_dict,n_bigram = ngrams_parameter_estimate(train,2)
trigram_dict,n_trigram = ngrams_parameter_estimate(train,3)
def jsgl(sentence,n,num_grams,ngrams_dict,n_lgrams_dict=None):
    '''
    ����ÿһ��Ԫ��ĳ���Ƶ�ʣ�n=0�������������
    n_lgrams_dictΪn-1��dict
    ���������λΪһ�仰
    '''
    ngrams = generate_ngram(sentence,n+1)
    log_prob,has_unknown_ngram = 0,False
    for ngram in ngrams:
        if ngram in ngrams_dict:
            if n == 0:  #һԪģ��ֱ�Ӽ���
                log_prob += np.log2(ngrams_dict[ngram]/num_grams)
            else:       #��Ԫģ����Ҫʹ��ǰһ��Ԫ�صķֲ�
                log_prob += np.log2(ngrams_dict[ngram]/n_lgrams_dict[ngram[:n]])
        else:
            has_unknown_ngram = True
    return 0 if has_unknown_ngram else log_prob
ngram_dicts = [unigram_dict,bigram_dict,trigram_dict]
number = np.arange(len(ngram_dicts))
num_grams = [n_unigram,n_bigram,n_trigram]
model_name = ['uni','bi','tri']
for num in number:
    sum_log_prob = 0.0
    for gram in test:    
        if num == 0:
            n_lgrams_dict = None
        else:
            n_lgrams_dict = ngram_dicts[num-1]
        prob = jsgl(gram,num,num_grams[num],ngram_dicts[num],n_lgrams_dict)
        #print(prob)
        sum_log_prob += prob
    perplexity = 2**(-sum_log_prob/np.sum(len(s) for s in test))
    print(f"The perplexity of model {model_name[num]} is {perplexity}")            