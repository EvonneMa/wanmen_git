import numpy as np
from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt
figsize(11,9)
import scipy.stats as stats
dist = stats.beta 
n_trials = 1000
data = stats.bernoulli.rvs(0.5,size = n_trials)
x = np.linspace(0,1,100)
def tests(N):
	#figsize = (6,5)
	plt.figure(figsize=(6,5))
	plt.xlabel('P')
	heads = data[:N].sum()
	y = dist.pdf(x,1+heads,1+N-heads)
	plt.plot(x,y,label = f'{heads} head in N tests')
	plt.fill_between(x,0,y,color = '#348ABD',alpha = 0.4)
	plt.vlines(0.5,0,4,color = 'k',linestyles = '-',lw = 1)
	leg = plt.legend()
	leg.get_frame().set_alpha(0.4)
	plt.autoscale(tight = True)
	plt.suptitle('oh yeah')
	plt.tight_layout()
tests(10)