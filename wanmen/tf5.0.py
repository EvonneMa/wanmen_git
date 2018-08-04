import tensorflow as tf
import numpy as np
import time
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../MNIST-data",one_hot = True)
def pool(img,k = 2):
	return tf.nn.max_pool(img,ksize = [1,k,k,1],strides = [1,k,k,1],padding = 'SAME')
def conv1(_x,_w,_b):
	res = tf.nn.relu(tf.nn.bias_add(tf.nn.depthwise_conv2d(_x,_w,strides = [1,1,1,1],padding = 'SAME'),_b))
	return res
def conv(_x,_w,_b,POOL = True,pre_conv = False):
	if pre_conv:
		return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(_x,_w,strides = [1,1,1,1],padding = 'SAME'),_b))
	temp = conv1(_x,_w[0],_b[0])
	temp = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(temp,_w[1],strides = [1,1,1,1],padding = 'SAME'),_b[1]))
	if POOL:
		return pool(temp,k = 2)
	else:
		return temp
def conv_net(_x,_w,_b,_dropout,_conv_layers,_fc_layers):
    #layer1
    #print(_x.shape)
    conv_res = tf.reshape(_x,[-1,28,28,1])
    
    for i in range(_conv_layers):
    	if i == 0:
    		conv_res = conv(conv_res,_w['w'+str(i)],_b['b'+str(i)],POOL = False,pre_conv = True)
    		continue
    	conv_res = conv(conv_res,_w['w'+str(i)],_b['b'+str(i)],POOL = i%2,pre_conv = False)
    #print(i,conv_res.shape)
    #layer5
    dense = tf.reshape(conv_res,[-1,_w['w'+str(_conv_layers)].get_shape().as_list()[0]])# need -1
    dense = tf.nn.relu(tf.add(tf.matmul(dense,_w['w'+str(_conv_layers)]),_b['b'+str(_conv_layers)]))
    dense = tf.nn.dropout(dense,_dropout)
    #print(dense.shape)
    #layer6
    dense = tf.add(tf.matmul(dense,_w['w'+str(_conv_layers+1)]),_b['b'+str(_conv_layers+1)])
    #print(dense.shape)
    return dense
def gen_weight(weights,RGB = False):
	weight = {}
	if RGB:
		channel = 3
	else:
		channel = 1
	for i in range(len(weights)-2):
		if i == 0:
			weight['w'+str(i)] = tf.Variable(tf.random_normal([3,3,channel,weights[i]]))
		else:
			#using depth conv
			temp = 'w'+str(i)
			weight[temp] = {}
			weight[temp][0] = tf.Variable(tf.random_normal([3,3,weights[i-1],1]))
			weight[temp][1] = tf.Variable(tf.random_normal([1,1,weights[i-1],weights[i]]))
	weight['w4'] = tf.Variable(tf.random_normal([7*7*64,weights[-2]]))
	weight['w5'] = tf.Variable(tf.random_normal([weights[-2],weights[-1]]))
	#print(weight.shape)
	return weight
def gen_bias(biases,RGB = False):
	bias = {}
	if RGB:
		channel = 3
	else:
		channel = 1
	for i in range(len(biases)):
		if i == 0:
			bias['b'+str(i)] = tf.Variable(tf.random_normal([biases[i]]))
		else:
			temp = 'b'+str(i)
			bias[temp] = {}
			bias[temp][0] = tf.Variable(tf.random_normal([biases[i-1]]))
			bias[temp][1] = tf.Variable(tf.random_normal([biases[i]]))
	bias['b5'] = tf.Variable(tf.random_normal([biases[-1]]))
	bias['b4'] = tf.Variable(tf.random_normal([biases[-2]]))
	return bias
#main
def main():
    #parameters
	learning_rate = 0.001
	training_iters = 60000
	batch_size = 128
	display_step = 10
	n_input = 784 # MNIST data input (img shape: 28*28)
	n_classes = 10 # MNIST total classes (0-9 digits)
	dropout = 1 # Dropout, probability to keep units
	epochs = 10
	#input and labels
	x = tf.placeholder(tf.float32,[None,n_input])
	y = tf.placeholder(tf.float32,[None,n_classes])
	droprate = tf.placeholder(tf.float32)
	#wb
	conv_layers = 4
	fc_layers = 2
	layers = [32,32,64,64,128,n_classes]
	w = gen_weight(layers,RGB = False)
	b = gen_bias(layers,RGB = False)
	#evaluations
	pred = conv_net(x,w,b,droprate,conv_layers,fc_layers)
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y,logits = pred))
	optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
	accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(pred,1),tf.argmax(y,1)),tf.float32))
	#sess
	sess = tf.Session()
	sess.run(tf.global_variables_initializer())
	#begin
	for i in range(epochs):
		step = 1
		while(step*batch_size < training_iters):
			batch_xs,batch_ys = mnist.train.next_batch(batch_size)
			#print(step)
			time1 = time.time()
			sess.run(optimizer,feed_dict = {x:batch_xs,y:batch_ys,droprate:dropout})
			delta = time.time() - time1
			if step % display_step == 0:
				acc = sess.run(accuracy,feed_dict = {x:batch_xs,y:batch_ys,droprate:1})
				lost = sess.run(cost,feed_dict = {x:batch_xs,y:batch_ys,droprate:1})
				print(f'epoch = {i},iter = {step*batch_size},acc = {acc},lost = {lost},time = {delta}')
			step += 1
		print(f'final acc = {sess.run(accuracy,feed_dict = {x:mnist.test.images[:512],y:mnist.test.labels[:512],droprate:1})}')
if __name__ == '__main__':
	main()
	#0.875,0.8555(3*3*32*64*64*1024,0.75) 5 layers
	#0.8045,0.7852(3*3*32*32*64*64*1024,0.75) 6 layers
	#0.9453,0.92(3*3*32*32*64*64*1024,1) 6 layers
	#0.8984,0.8574(3*3*32*32*64*64*128,1) 6 layers
	#1 0.9629(3*3*32*32*64*64*128,1) 10 epochs 6 layers
	#0.9921 0.9512(depthwise)
	# 0.8s faster