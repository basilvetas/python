#!/usr/bin/python

from __future__ import division
from random import randint
import sys
import numpy as np
import matplotlib.pyplot as plt

# runs = int(sys.argv[1]) 
# dist = {}

# size = int(sys.argv[2]) 
# total = 0
x = []
y = []

for size in range(1, 10000):  
  total = 0
  for i in range (0, size):
      r = randint(1, 6)
      # print i+1, ": ", r
      total += r
      # print "Sample mean: ", total / size

  mean = total / size

  x.append(size)
  y.append(mean)

   # if mean in dist:
   #     dist[mean] += 1
   # else:
   #     dist[mean] = 1

# for mean in sorted(dist):  
#   print "%s: %s" % (mean, dist[mean]);

plt.plot(x, y)
plt.show()


