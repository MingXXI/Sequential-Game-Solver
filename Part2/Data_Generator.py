import random
import time


N = 250000		## initial input size
D = 10000 		## gap of input gap
number = 30		## number of case

filename = 'test_case'

for i in range (N,N+number*D,D):
	num = i
	cap = 5
	# K = -10*N
	fun = [0 for j in range(i)]

	for j in range (i):
		fun[j] = random.randint(0,6)
		if(random.random()<0.5):
			fun[j] *= -1

	f = open(filename+str(int((i-N)/D+1))+'.dzn','w+')
	f.write('% test'+ str(i) + '\n\n\n')
	f.write('num = ' + str(i) + ';' + '\n')
	f.write('cap = ' + str(cap) + ';' + '\n')
	f.write('refill = 2' + ';' + '\n')
	f.write('fun = ' + str(fun) + ';' + '\n')
	f.close()

	f = open(filename+str(int((i-N)/D+1))+'.txt','w+')
	f.write('num,' + str(i) + '\n')
	f.write('cap,' + str(cap) + '\n')
	f.write('refill,2' + '\n')
	f.write('fun,')
	for k in range(i):
		f.write(str(fun[k])+',')
	f.write('\n')
	f.close()


