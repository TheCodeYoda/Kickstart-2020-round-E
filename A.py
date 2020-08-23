t=int(input())

for _ in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	mx=-1
	diff=a[0]-a[1]
	c=2
	for i in range(1,n-1):
		if(a[i]-a[i+1]==diff):
			c+=1
		else:
			mx=max(mx,c)
			c=2
			diff=a[i]-a[i+1]
	mx=max(mx,c)
	print("Case #{}: {}".format(_+1,mx))