dic1={
"A":"Alpha",
"B":"Bravo",
"C":"Charlie",
"D":"Delta",
"E":"Echo",
"F":"Foxtrot",
"G":"Golf",
"H":"Hotel",
"I":"India",
"J":"Juliet",
"K":"Kilo",
"L":"Lima",
"M":"Mike",
"N":"November",
"O":"Oscar",
"P":"Papa",
"Q":"Quebec",
"R":"Romeo",
"S":"Sierra",
"T":"Tango",
"U":"Uniform",
"V":"Victor",
"W":"Whiskey",
"X":"Xray",
"Y":"Yankee",
"Z":"Zulu",
"0":"Zero",
"1":"One",
"2":"Two",
"3":"Three",
"4":"Four",
"5":"Five",
"6":"Six",
"7":"Seven",
"8":"Eight",
"9":"Nine"
}
dic2=dict((v, k) for k, v in dic1.items())
n=int(input())
for i in range(n):
	st=input()
	inp=input()
	if(st=="english"):
		inp=inp.upper()	
		for j in range(len(inp)):
			x=inp[j]
			a=dic1[x]
			print(a, end=" ")
		print()
	else:
		inp=inp.split()
		l=[]
		for k in range(len(inp)):
			if(k>=1):
				L=dic2[inp[k]].lower()
			else:
				L=dic2[inp[k]]
			l.append(L)
		for i in l:
			print(i,end="")
		print()
