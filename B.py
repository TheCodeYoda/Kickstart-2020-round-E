t=int(input())

for _ in range(t):
	n,a,b,c=map(int,input().split())
	if(c>min(a,b) or (n==a and a==b and c<n) or (a==b and b==c and c==1 and n>c)):
		print("Case #{}: {}".format(_+1,"IMPOSSIBLE"))
	else:
		c_list=[]
		a_list=[]
		b_list=[]
		c_list=[n]*c
		rem_a=a-c
		rem_b=b-c
		if(rem_a+rem_b+c>n):
			print("Case #{}: {}".format(_+1,"IMPOSSIBLE"))
		else:
			for i in range(n-rem_a,n):
				a_list.append(i)
			b_list=[n-1]*(rem_b)
			rem_list=[n-2]*(n-(rem_a+rem_b+c))
			if(rem_a==0 and rem_b==0):
				fin=[n]*(c-1)+[n-1]*(n-c)+[n]
			elif(rem_b==0):
				fin=a_list+rem_list+c_list+b_list
			else:
				fin=a_list+c_list+rem_list+b_list
			print("Case #{}:".format(_+1),end=" ")
			print(*fin)