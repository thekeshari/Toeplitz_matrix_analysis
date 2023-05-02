import numpy as np
from scipy.linalg import toeplitz
import itertools
import sympy 

x = int(input("Enter a number"))
values = [0,1]
while True:
	y = np.random.choice(values,(2*x-1))
	print(y)
	z = toeplitz(y[:x], y[x-1:(2*x)+2])
	det = np.linalg.det(z)
	#print(det)
	if det != 0:
		break

print(z)


lst = list(map(list, itertools.product([0, 1], repeat=x))) #list of all vectors of given length

print(lst)

def vectr_mul(vectr):
	res = [0 for y in range(x)]
	for i in range(x):
		for k in range(x):
	 
		    # resulted matrix
		    res[i] += z[i][k] * vectr[k] 
	res = [y%2 for y in res]
	return res

#print(len(lst))
#print(lst)
def rept_mul_lst(vectr):
	final_lst=[vectr]
	new_vectr= vectr
	for i in range(x-1):
		new_vectr= vectr_mul(new_vectr)
		final_lst.append(new_vectr)
	return final_lst

def find_a_rank(final_lst):	
	mat = np.array(final_lst)
	_, inds = sympy.Matrix(mat).T.rref()
	rank=len(inds)
	return rank
	
ranks= [find_a_rank(rept_mul_lst(vectr)) for vectr in lst]

print(ranks)
total_elements_greater = 0
for j in ranks:
	if j>=3:
		total_elements_greater = total_elements_greater+1
print(total_elements_greater)

	
