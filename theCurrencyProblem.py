n=int(input())
curr=[2000,500,200,100,50,20,10,5,2,1]
for i in range(n):
	amt=int(input())
	s=0
	for j in (curr):
		if(amt>=j):
			k=amt//j
			amt=amt-(k*j)
			s=s+k
	print(s)
