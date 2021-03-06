import numpy as np
from nn2 import *

class Sda(object):
	def __init__(self,architecture,activation_function='sigm',learningRate = 1,momentum = 0.5,weightPenaltyL2 = 0,sparsityparameter = 0,beta=0.5,inputzeroMaskedFraction=0.5,output = 'sigm',jacobi_penalty = 0,scaling_learningRate = 0.99,dropout = 0.1):
		self.size = architecture
		self.n = len(architecture)
		self.activation_function=activation_function
		self.da = {}
		self.momentum=momentum
		self.weightPenaltyL2 = weightPenaltyL2
		self.sparsityparameter = sparsityparameter
		self.beta = beta
		self.inputzeroMaskedFraction=inputzeroMaskedFraction
		self.output = output
		self.jacobi_penalty = jacobi_penalty
		self.scaling_learningRate=scaling_learningRate
		self.learningRate=learningRate
		self.dropout = dropout
		for i in range(1,self.n):
			sub_architecture = [self.size[i-1],self.size[i],self.size[i-1]]
#			self.da[str(i)] = NN(sub_architecture,architecture,activation_function,learningRate,output,scaling_learningRate)
			self.da[str(i)] = NN(sub_architecture,activation_function=self.activation_function,learningRate = self.learningRate,momentum = self.momentum,weightPenaltyL2 = self.weightPenaltyL2,sparsityparameter = self.sparsityparameter,beta=self.beta,inputzeroMaskedFraction=self.inputzeroMaskedFraction,output = self.output,jacobi_penalty = self.jacobi_penalty,scaling_learningRate = self.scaling_learningRate,dropout = self.dropout)
	def train(self,x,batchsize,numepochs):
		for i in range(1,self.n):
			print '%d/%d the AE' % (i,self.n)
			self.da[str(i)].nntrain(x,x,batchsize,numepochs)
	#		print i
			self.da[str(i)].nnff(x,np.zeros((np.shape(x)[0],self.da[str(i)].size[-1])))
			t = self.da[str(i)].a['2']
			x = t.copy()
		
