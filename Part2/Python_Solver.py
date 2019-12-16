import time
import math


N = 250000		## initial input size
D = 10000 		## gap of input gap
number = 30		## number of cases
filename = 'test_case'
time_list = [0 for j in range (number)]


def Seq_Solver(num, cap, refill, fun):
	## according to algorithm discussed with classmates: George He
	max_fun = 0
	max_index = 0
	token = [0 for i in range (num)]
	cur_token = cap
	future_token = 0
	play = [0 for i in range (num)]

	for i in range (num):
		play[i] += 1
		cur_token -= 1
		if (fun[i] <= 0):
			max_fun += fun[i]
			cur_token = min(cur_token+refill, cap)
		else:
			future_token = refill
			next_game = i+1
			reserve = 0
			while (future_token < cap):
				if (next_game<num):
					if (fun[next_game] > fun[i]):
						reserve = cap - future_token
						if (reserve > cur_token):
							reserve = cur_token
						break
				else:
					break
				next_game += 1
				future_token += refill-1
			play[i] += cur_token - reserve
			max_fun += play[i]*fun[i]
			cur_token = min(reserve+refill, cap)







for i in range (1,number+1):

	# f = open(filename+str(i)+'.txt','r+')
	f = open('test_case15.txt','r+')

	lines = f.readlines()
	items = [[]for j in range(4)]
	count = 0
	for line in lines:
		items[count]= line.strip().split(',')
		count += 1
	num = int(items[0][1])
	cap = 5
	refill = 2
	fun = []

	# for k in range (N+(i-1)*D):
	for k in range (N+14*D):
		fun.append(int(items[3][k+1]))

	for k in range (5):
		time_start = time.time()
		Seq_Solver(num,cap,refill,fun)
		time_end = time.time()
		time_list [i-1] += (time_end-time_start)
	time_list[i-1] /= 5
	print('case',i, 'runs:', time_list[i-1])
	f.close()

	# for i in range(len(result)):
	# print('p = ',result['p'])
	# print('t = ',result['t'])
	# print('=====================')

print(time_list)

