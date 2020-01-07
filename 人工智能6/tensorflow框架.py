# import tensorflow as tf
import numpy as np
# tf.compat.v1.disable_v2_behavior()
import tensorflow as tf


#1、创建常量
a = tf.constant([[3, 3]], name='a')
#2、创建常量
b = tf.constant([[2], [3]], name='b')
#3、创建乘法
c = tf.matmul(a, b)
print(c)

#4、占位符
input1 = tf.compat.v1.placeholder(tf.float32)
input2 = tf.compat.v1.placeholder(tf.float32)

#5、使用占位符创建乘法阶段
output = tf.multiply(input1, input2)
# with tf.compat.v1.Session() as sess:
#     print(sess.run(output, feed_dict={input1: 3, input2: 7.0}))

#6、案例
x = np.random.rand(100)
y = x*0.1 + 0.2

#7、构建线程模型

b = tf.Variable(0.)
k = tf.Variable(0.)

Y = k*x + b

#线性回归算法目的：使得损失函数最小
loss = tf.reduce_mean(tf.square(y - Y))
#优化loss：使得loss最小：
optimizer= tf.train.GradientDescentOptimizer(0.01).minimize(loss)#0.2学习率

#
train = optimizer.minimize(loss)

#初始化变量
init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for step in range(400):
        sess.run(train)
        if step%20 == 0:
            print(step, sess.run([k, b]))

