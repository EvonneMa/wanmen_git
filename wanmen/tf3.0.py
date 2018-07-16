import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../MNIST-data",one_hot = True)
def pool(img,k = 2):
	return tf.nn.max_pool(img,ksize = [1,k,k,1],strides = [1,k,k,1],padding = 'SAME')
def conv_net(_x,_wb,_dropout):
    #layer1
    _x = tf.reshape(_x,[-1,28,28,1])
    conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(_x,_wb['w1'],strides = [1,1,1,1],padding = 'SAME'),_wb['b1']))
    conv1 = pool(conv1,k = 2)
    conv1 = tf.nn.dropout(conv1,_dropout)
    #layer2
    conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv1,_wb['w2'],strides = [1,1,1,1],padding = 'SAME'),_wb['b2']))
    conv2 = pool(conv2,k = 2)
    conv2 = tf.nn.dropout(conv2,_dropout)
    #layer3
    dense1 = tf.reshape(conv2,[-1,_wb['w3'].get_shape().as_list()[0]])# need -1
    dense1 = tf.nn.relu(tf.add(tf.matmul(dense1,_wb['w3']),_wb['b3']))
    dense1 = tf.nn.dropout(dense1,_dropout)
    #layer4
    dense2 = tf.add(tf.matmul(dense1,_wb['w4']),_wb['b4'])
    return dense2
#main
def main():
    #parameters
	learning_rate = 0.001
	training_iters = 60000
	batch_size = 128
	display_step = 10
	n_input = 784 # MNIST data input (img shape: 28*28)
	n_classes = 10 # MNIST total classes (0-9 digits)
	dropout = 0.75 # Dropout, probability to keep units
	#input and labels
	x = tf.placeholder(tf.float32,[None,n_input])
	y = tf.placeholder(tf.float32,[None,n_classes])
	droprate = tf.placeholder(tf.float32)
	#wb
	wb = {'w1':tf.Variable(tf.random_normal([5,5,1,32])),
	'w2':tf.Variable(tf.random_normal([5,5,32,64])),
	'w3':tf.Variable(tf.random_normal([7*7*64,512])),
	'w4':tf.Variable(tf.random_normal([512,n_classes])),
    'b4':tf.Variable(tf.random_normal([n_classes])),
    'b3':tf.Variable(tf.random_normal([512])),
    'b2':tf.Variable(tf.random_normal([64])),
    'b1':tf.Variable(tf.random_normal([32]))
	}
	#evaluations
	pred = conv_net(x,wb,droprate)
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y,logits = pred))
	optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
	accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(pred,1),tf.argmax(y,1)),tf.float32))
	#sess
	sess = tf.Session()
	sess.run(tf.global_variables_initializer())
	#begin
	step = 1
	while(step*batch_size < training_iters):
		batch_xs,batch_ys = mnist.train.next_batch(batch_size)
		#print(step)
		sess.run(optimizer,feed_dict = {x:batch_xs,y:batch_ys,droprate:dropout})
		if step % display_step == 0:
			acc = sess.run(accuracy,feed_dict = {x:batch_xs,y:batch_ys,droprate:1})
			lost = sess.run(cost,feed_dict = {x:batch_xs,y:batch_ys,droprate:1})
			print(f'iter = {step*batch_size},acc = {acc},lost = {lost}')
		step += 1
	print(f'final acc = {sess.run(accuracy,feed_dict = {x:mnist.test.images[:256],y:mnist.test.labels[:256],droprate:1})}')
if __name__ == '__main__':
	main()
	#0.9375,0.9492(5*5*32*64*1024,0.75)
	#0.9453,0.918(5*5*32*64*512,0.75)