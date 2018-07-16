import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../MNIST-data",one_hot = True)
# model Parameters
learning_rate = 0.001
training_iters = 60000
batch_size = 128
display_step = 10

# Network Parameters
n_input = 784 # MNIST data input (img shape: 28*28)
n_classes = 10 # MNIST total classes (0-9 digits)
dropout = 0.75 # Dropout, probability to keep units
#input and labels
x = tf.placeholder(tf.float32,[None,n_input])
y = tf.placeholder(tf.float32,[None,n_classes])
#layer1
w1 = tf.Variable(tf.random_normal([3,3,1,16]))
b1 = tf.Variable(tf.random_normal([16]))
conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(tf.reshape(x,[batch_size,28,28,1]),w1,strides = [1,1,1,1],padding = 'SAME'),b1))
conv1 = tf.nn.max_pool(conv1,ksize = [1,2,2,1],strides = [1,2,2,1],padding = 'SAME')
conv1 = tf.nn.dropout(conv1,dropout)
#layer2
w2 = tf.Variable(tf.random_normal([3,3,16,32]))
b2 = tf.Variable(tf.random_normal([32]))
conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv1,w2,strides = [1,1,1,1],padding = 'SAME'),b2))
conv2 = tf.nn.max_pool(conv2,ksize = [1,2,2,1],strides = [1,2,2,1],padding = 'SAME')
conv2 = tf.nn.dropout(conv2,dropout)
#print(conv2.shape)
#layer3
w3 = tf.Variable(tf.random_normal([7*7*32,1024]))
b3 = tf.Variable(tf.random_normal([1024]))
dense1 = tf.reshape(conv2,[-1,w3.get_shape().as_list()[0]])# need -1
dense1 = tf.nn.relu(tf.add(tf.matmul(dense1,w3),b3))
dense1 = tf.nn.dropout(dense1,dropout)
#layer4
w4 = tf.Variable(tf.random_normal([1024,n_classes]))
b4 = tf.Variable(tf.random_normal([10]))
dense2 = tf.add(tf.matmul(dense1,w4),b4)
#print(dense1.shape)
#evaluation
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y,logits = dense2))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(dense2,1),tf.argmax(y,1)),tf.float32))
#main
sess = tf.Session()
sess.run(tf.global_variables_initializer())
step = 1
while(step*batch_size < training_iters):
	batch_xs,batch_ys = mnist.train.next_batch(batch_size)
	#print(step)
	sess.run(optimizer,feed_dict = {x:batch_xs,y:batch_ys})
	if step % display_step == 0:
		acc = sess.run(accuracy,feed_dict = {x:batch_xs,y:batch_ys})
		lost = sess.run(cost,feed_dict = {x:batch_xs,y:batch_ys})
		print(f'iter = {step*batch_size},acc = {acc},lost = {lost}')
	step += 1
print(f'final acc = {sess.run(accuracy,feed_dict = {x:batch_xs,y:batch_ys})}')
#0.703125