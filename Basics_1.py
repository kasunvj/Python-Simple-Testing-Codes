a = ["a0","b0","c","t0"]

for file in a:
	print(file)

print("--------------")

for file in a:
	if "0" in file:
		print(file)

# a0
# b0
# c
# t0
# --------------
# a0
# b0
# t0

print("--------------")

b= [[0,0,0,0],["a","b","c","d"]]

print(len(b))

for line in b:
	if "a" in line:
		print("hey i found a")

# a0
# b0
# t0
# 2
# hey i found a

print("--------------")

for line in b:
	if "b" in line:
		print("hey i found b")
	else:
		print("neh")

# neh
# neh

print("--------------")
for line in b:
	print (line)

# [0, 0, 0, 0]
# ['a', ' b', 'c', 'd']

print("--------------")

for line in b:
	for column in line:
		if "b" in line:
			print("hey i found b")
		else:
			print("neh")