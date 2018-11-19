n=int(input())
line=input()
a=line.split()[0]
b=int(line.split()[1])
def rrot(a,b):
	w=a
	for i in range(b):
		w=w[-1]+w[:-1]
	print(w)
def lrot(a,b):
	w=a
	for i in range(b):
		w=w[1:]+w[0]	
	print(w)
for i in range(n):
	if(b<0):
		lrot(a,abs(b))
	else:
		rrot(a,b)
