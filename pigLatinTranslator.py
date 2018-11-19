n=int(input())
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(n):
	st=input()
	st=st.split()
	for j in st:
		w=j
		if(w[0] in vowels):
			print(w+"ay",end=" ")
		else:
			print(w[1:]+w[0]+"ay", end=" ")
	print()
