# -*- coding: utf-8 -*-
"""
=================================
Wasserstein Discriminant Analysis
=================================

@author: rflamary
"""

import numpy as np
import matplotlib.pylab as pl

from ot.dr import wda, fda


#%% parameters

n = 1000  # nb samples in source and target datasets
nz = 0.2

# generate circle dataset
t = np.random.rand(n) * 2 * np.pi
ys = np.floor((np.arange(n) * 1.0 / n * 3)) + 1
xs = np.concatenate(
    (np.cos(t).reshape((-1, 1)), np.sin(t).reshape((-1, 1))), 1)
xs = xs * ys.reshape(-1, 1) + nz * np.random.randn(n, 2)

t = np.random.rand(n) * 2 * np.pi
yt = np.floor((np.arange(n) * 1.0 / n * 3)) + 1
xt = np.concatenate(
    (np.cos(t).reshape((-1, 1)), np.sin(t).reshape((-1, 1))), 1)
xt = xt * yt.reshape(-1, 1) + nz * np.random.randn(n, 2)

nbnoise = 8

xs = np.hstack((xs, np.random.randn(n, nbnoise)))
xt = np.hstack((xt, np.random.randn(n, nbnoise)))

#%% plot samples
pl.figure(1, figsize=(6.4, 3.5))

pl.subplot(1, 2, 1)
pl.scatter(xt[:, 0], xt[:, 1], c=ys, marker='+', label='Source samples')
pl.legend(loc=0)
pl.title('Discriminant dimensions')

pl.subplot(1, 2, 2)
pl.scatter(xt[:, 2], xt[:, 3], c=ys, marker='+', label='Source samples')
pl.legend(loc=0)
pl.title('Other dimensions')
pl.tight_layout()

#%% Compute FDA
p = 2

Pfda, projfda = fda(xs, ys, p)

#%% Compute WDA
p = 2
reg = 1e0
k = 10
maxiter = 100

Pwda, projwda = wda(xs, ys, p, reg, k, maxiter=maxiter)

#%% plot samples

xsp = projfda(xs)
xtp = projfda(xt)

xspw = projwda(xs)
xtpw = projwda(xt)

pl.figure(2)

pl.subplot(2, 2, 1)
pl.scatter(xsp[:, 0], xsp[:, 1], c=ys, marker='+', label='Projected samples')
pl.legend(loc=0)
pl.title('Projected training samples FDA')

pl.subplot(2, 2, 2)
pl.scatter(xtp[:, 0], xtp[:, 1], c=ys, marker='+', label='Projected samples')
pl.legend(loc=0)
pl.title('Projected test samples FDA')

pl.subplot(2, 2, 3)
pl.scatter(xspw[:, 0], xspw[:, 1], c=ys, marker='+', label='Projected samples')
pl.legend(loc=0)
pl.title('Projected training samples WDA')

pl.subplot(2, 2, 4)
pl.scatter(xtpw[:, 0], xtpw[:, 1], c=ys, marker='+', label='Projected samples')
pl.legend(loc=0)
pl.title('Projected test samples WDA')
pl.tight_layout()

pl.show()
