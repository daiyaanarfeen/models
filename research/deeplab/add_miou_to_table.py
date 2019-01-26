import numpy as np
import sys
import tensorflow as tf

reader = tf.train.NewCheckpointReader("./deeplab/miou.ckpt")
miou = reader.get_tensor("miou")
sigma = sys.argv[1]
res = sys.argv[2]
dat = np.load('./deeplab/robust_eval.npy')
dat[[0, 5, 10, 15, 20, 25].index(int(float(sigma))), int(int(float(res)) / 100 - 2)] = float(miou)
print(dat)
np.save('./deeplab/robust_eval.npy', dat)
