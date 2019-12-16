import random
import minizinc
import time


N = 30
refill = 2
filename = 'test_case'
time_list = [0 for j in range (N)]


for i in range (1,N+1):

	f = open(filename+str(i)+'.txt','r+')
	# f = open('test_case10.txt','r+')

	lines = f.readlines()
	items = [[]for j in range(4)]
	count = 0
	for line in lines:
		items[count]= line.strip().split(',')
		count += 1
	num = int(items[0][1])
	cap = 5
	refill = i
	fun = []
	# for k in range (i):
	for k in range (i):
		fun.append(int(items[3][k+1]))


	print('num = ',num)
	print('fun = ',fun)

	model = minizinc.Model('Sequential_Games.mzn')

	solver = minizinc.Solver.lookup('gecode')
	# solver = minizinc.Solver.lookup('chuffed')

	inst = minizinc.Instance(solver, model)
	inst["num"] = num
	inst["cap"] = cap
	# inst["K"] = K
	inst["fun"] = fun
	inst["refill"] = refill

	# # with inst.branch() as opt:
	# # 	opt.add_string("solve maximize ;\n")
	# # 	res = opt.solve()
	# # 	obj = res["objective"]

	# # inst.add_string("constraint sum(i in 1..num)(p[i] * fun[i]) = {obj};\n")
	for k in range (5):
		time_start = time.time()
		result = inst.solve()
		# for i in range(len(result)):
		print('p = ',result['p'])
		# print('t = ',result['t'])
		# print('=====================')
		time_end = time.time()
		time_list [i-1] += (time_end-time_start)
	time_list[i-1] /= 5
	print(time_list[i-1])

	# for i in range(len(result)):
	# print('p = ',result['p'])
	# print('t = ',result['t'])
	# print('=====================')

print(time_list)

