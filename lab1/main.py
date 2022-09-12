# рефлексивним, антирефлексивним,
# симетричним, антисиметричним, асиметричним, транзитивним. 
# Відшукати для нього 
#	найбільший, найменший , максимальний та мінімальний елементи, якщо такі існують,
#   і побудувати обернене й додаткове відношення.
import numpy as np

class Point:
	def __init__(self, i, count):
		self.i = i
		self.count = count

	def __str__(self):
		return f"({self.i+1}):{self.count}"

def get_max(M: list) -> Point:
	max_el = Point(0, 0)
	for i in range(len(M)):
		c = sum(M[i])
		if c > max_el.count:
			max_el = Point(i, c)
	return max_el

def get_min(M: list) -> Point:
	max_el = Point(0, 0)
	for i in range(len(M)):
		c = sum(M[i])
		if c < max_el.count:
			max_el = Point(i, c)
	return max_el


def get_strict(M: list):
	r = [i for i in [Mi for Mi in M]]
	for i in range(len(M)): # antireflexive
		r[i][i] = 0

	for i in range(len(M)): # antisymmetrical
		for j in range(len(M[i])):
			if i != j and r[i][j] == 1 and r[j][i] == 1:
				r[j][i] = 0
	return r

def get_addative(M: list):
	for i in range(len(M)):
		for j in range(len(M[i])):
			M[i][j] = 0 if M[i][j] == 1 else 1
	return M

def get_reverse(M: list):
	return np.transpose(M)

def is_reflexive(M: list) -> bool:
	for i in range(len(M)):
		if M[i][i] == 0:
			return False
	return True

def is_antireflexive(M: list) -> bool:
	for i in range(len(M)):
		if M[i][i] == 1:
			return False
	return True

def is_symmetrical(M: list) -> bool:
	for i in range(len(M)):
		for j in range(i + 1):
			if (M[i][j] == 1 or M[j][i] == 1) and M[i][j] != M[j][i]:
				return False
	return True

def is_asymmetrical(M: list) -> bool:
	for i in range(len(M)):
		for j in range(i + 1):
			if (M[i][j] == 1 or M[j][i] == 1) and M[i][j] == M[j][i]:
				return False
	return True

def is_antisymmetrical(M: list) -> bool:
	for i in range(len(M)):
		for j in range(i + 1):
			if i != j and (M[i][j] == 1 or M[j][i] == 1) and M[i][j] == M[j][i]:
				return False
	return True

def is_transitive(M: list, verbose = False) -> bool:
	r2 = np.matmul(M, M)
	if verbose:
		print("R^2:")
		print(r2)
	flag = True
	for i in range(len(M)):
		for j in range(i + 1):
			flag = flag and (r2[i][j] >= M[i][j])
	return flag


#x    1 2 3 4 5	    x 
M = [[0,0,0,1,0], # 1
	 [1,1,1,1,0], # 2
	 [1,1,1,0,1], # 3
	 [0,1,1,1,1], # 4
	 [0,1,0,1,1]] # 5

print("relation R:")
print(np.array(M))
print("-----------")
print(f"greatest element {get_max(M)}")
print(f"smallest element {get_min(M)}")
print("Reverse relation:")
print(np.array(get_reverse(M)))
print("Addative relation:")
print(np.array(get_addative(M)))
print("Strict relation:")
print(np.array(get_strict(M)))
print("--------------------------------------------------")
print(f'R {"is" if is_reflexive(M) else "is not"} reflexive')
print(f'R {"is" if is_antireflexive(M) else "is not"} antireflexive')
print(f'R {"is" if is_symmetrical(M) else "is not"} symmetrical')
print(f'R {"is" if is_asymmetrical(M) else "is not"} assymmetrical')
print(f'R {"is" if is_antisymmetrical(M) else "is not"} antisymmetrical')
print(f'R {"is" if is_transitive(M) else "is not"} transitive')