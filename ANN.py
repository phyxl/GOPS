#!/bin/python

#an attempt at a neural net

import numpy as np

HIDDENLAYERS = 1
HIDDENLAYERWIDTH = 20
ITERATIONS = 1000000
INPUTSIZE = 27
SAMPLESIZE = 2**(INPUTSIZE-2)
OUTPUTSIZE = 13


def generateGeneration(num, hiddenwidth, hiddencount, inputwidth, outputwidth):
  if hiddencount < 0 : hiddencount = 0
  syn = [ [] ]
  for n in range(num):
    syn[n].append(2*np.random.random((inputwidth,hiddenwidth)) - 1) #generate random synapses from -1 to 1
    for h in range(hiddencount):
      syn[n].append(2*np.random.random((hiddenwidth,hiddenwidth)) - 1)
    syn[n].append(2*np.random.random((hiddenwidth,outputwidth)) - 1)
  return syn

def nonlin(x,deriv=False): #a function of a neural node (sigmoid)
  if(deriv):
    return x*(1-x)
  return 1/(1+np.exp(-x))

def evaluateNN(inputnodes, syn, l):
  l[0] = inputnodes
  for i in range(1, len(syn[0])+1):
    l[i] = nonlin(np.dot(l[i-1],syn[0][i-1]))
  return l


#we need a sample input to train and to test the ANN

inputnodes = np.random.randint(2, size=(SAMPLESIZE,INPUTSIZE))
expectedOutput = -1*inputnodes[::,:OUTPUTSIZE] + 1
print(inputnodes[0])
print(expectedOutput[0])

syn = generateGeneration(1, HIDDENLAYERWIDTH, HIDDENLAYERS, INPUTSIZE, OUTPUTSIZE)
l_error = []
l_delta = []
layers = []
layers.append(inputnodes)
for i in range(1, len(syn[0])+1):
  layers.append(nonlin(np.dot(layers[i-1],syn[0][i-1])))
for le in range(len(syn[0])+1):
  l_error.append(inputnodes)
  l_delta.append(inputnodes)
#train the network by adjusting synapses
#def regression(iterations, input, expectedOutput):
averageerror = 1.0
count = 0
for j in xrange(ITERATIONS):
  layers = evaluateNN(inputnodes, syn, layers) #evaluate the ANN
  

  l_error[-1] = expectedOutput - layers[-1]
  l_delta[-1] = l_error[-1] * nonlin(layers[-1],True)
  for e in range(len(syn[0])-1, 0, -1):
    l_error[e] = l_delta[e+1].dot(syn[0][e].T)
    l_delta[e] = l_error[e] * nonlin(layers[e],True)
    
  for f in xrange(len(syn[0])):
    syn[0][f] += np.dot(layers[f].T,l_delta[f+1])
  if(j % 10000 == 0):
    averageerror = np.sum(np.sum(np.absolute(expectedOutput - layers[-1]), axis=0) / SAMPLESIZE) / OUTPUTSIZE
    print(averageerror)
    if(averageerror < 0.01):
      break
  count += 1
  
def GA():
  currentGen = generateGeneration(20, 20, 39, 13)
  
  
print np.rint(layers[-1][0])
print "error after training "
print averageerror
print('with count of: ', count)
