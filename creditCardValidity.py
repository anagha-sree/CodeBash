n=int(input())
def ItoL(a):
	return [int(x) for x in str(a)]	
for i in range(n):
	s=0
	a=int(input())
	a=ItoL(a)
	a.reverse()
	for j in range(len(a)):
		if(j%2==0):
			s=s+a[j]
		else:
			S=a[j]*2
			if(S>=10):
				s=s+S%10
				S=S/10
				s=s+int(S%10)
			else:
				s=s+S
	if(s%10!=0):
		print("INVALID")
	else:
		print("VALID")
