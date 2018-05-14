# ��ȡ��������,�鿴����������
# �����ǩ
# ����summary����,�������Ͽ�
# ��ģ
# ���
# ˼·��
#		���������������Ĵ���Ƶ��Ԥ��Amazon��Ʒ����
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
# һ����ȡ��������,�鿴����������
data = pd.read_csv('amazon-fine-food-reviews/Reviews.csv')
#�鿴���ݴ���ͳ��,Ϊ���������ṩ˼·
data.info()
#�������ݵĴ������
df_uni = pd.DataFrame(index = range(10), columns = ['Feature','No. of NAs','No. of Unique Values','# of total samples','Unique percentage(%)'])
for i,col in enumerate(data.columns):
    feat_na = data[col].isnull().sum(axis = 0)
    feat_uni = data[col].unique().shape[0]
    perc = feat_uni/data[col].shape[0]*100
    df_uni.iloc[i,:] = [col,feat_na,feat_uni,data.shape[0],perc]
data = data.dropna()
# ����������ǩ��
label = data['Score'].apply(lambda x:1 if x > 3 else 0)
# ��������summary,�������Ͽ�
# 3.1 ����summary
#	1.ȥ������
s = data['Summary'].apply(lambda text:text.lower())
s_new = []
for i in range(s.shape[0]):
	s_new.append(re.sub('[\W]+',' ',s.iloc[i]))
Summary = pd.Series(s_new)
# 	2.�ִ�(�����￪ʼ�Ƕ�ÿһ��������Ϥ,�������Ĵ���,���մ�������Ĳ���һ����)
from nltk import word_tokenize
words = [word_tokenize(text) for text in Summary] 
#word_tokenize�Ĳ���Ϊһ������,����һ���ɴʻ㹹�ɵ�list
#	3.ȥ��stopwords
from nltk.corpus import stopwords
#stopwords.words('language')���Բ鿴Ŀ�����Ե�stopwords,�Ǹ�list	
def remove_stopwords(sub_words):
	return[word for word in sub_words if word not in stopwords.words('english')]
words_without_stopwords = [remove_stopwords(sub_words) for sub_words in words]
#����д����PYTHON
#ע��list.append��list.extend������,�Լ�np.hstack()��ʹ��
words_wo_sw_h = np.hstack(words_without_stopwords) #�ϲ����е����б�,�γ�һ�����б�
#ע�⣺stopwords����not�ȴʻ�,��Ҫ��һ������,�繹��not_happy�ȴʻ�
#	4.�ʸ���ȡstemming�����Ի�ԭlemmatization,�������������Ǻ�Ȩ��
from nltk.stem import PorterStemmer
porter = PorterStemmer() #ɾ��ʱ̬
from nltk import WordNetLemmatizer
wnl = WordNetLemmatizer() #ɾ��������
stem_words = [porter.stem(word) for word in words_wo_sw_h]
lem_words = [wnl.lemmatize(word) for word in words_wo_sw_h]
fdist_wo = pd.DataFrame(list(FreqDist(words_wo_sw_h).items()),columns = ['word','freq'])
fdist_w = pd.DataFrame(list(FreqDist(np.hstack(words)).items()),columns = ['word','Freq'])
#ѧϰ���ִ�dict����DataFrame�ķ�ʽ,������list
# 3.2 �������Ͽ�
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
# �ġ���ģ(�������ȶԵ���������������,�����Щ�������ظ���)
#  	1.Ԥ������������ת����Ƶ��
def stem_tokens(tokens,stemmer = PorterStemmer()):
	'''
	����Ϊ�ִʺ��һ�仰,��ÿ������ȥʱ̬,����list
	'''
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed
def tokenize(text):
	'''
	����Ϊһ�仰,�ȷִ�,��ȥʱ̬,�����' '����ÿ�����ʹ����ַ�����ʽ��һ�仰
	'''
	tokens = nltk.word_tokenize(text)
	stems = stem_tokens(tokens)
	return ' '.join(stems)
def build_corpus(dataset):
	'''
	����Ϊÿһ�����۹��ɵ�list,��ÿһ�����۵���tokenize()
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
#	TF=�ʻ�i������j�г��ֵ�Ƶ��
#	IDF=log(������ƪ��/���дʻ�i������ƪ��)
#	��TF*IDF��Ϊ���۽��ʻ�i�϶�Ϊ����j�Ĺؼ��ʵı�׼
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec = TfidfVectorizer()
X_train_tfidf_vec = tfidf_vec.fit_transform(train_token)
X_test_tfidf_vec = tfidf_vec.fit_transform(test_train)
#����һ��ϡ�����(����Ϊ����������,����Ϊ���ظ����ʵĸ���),ָ����Щλ�õ�Ԫ�ز�Ϊ��
#����ʹ��tfidf_vec.get_feature_names()���۲춼����Щ����
#	2.����ģ��
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


