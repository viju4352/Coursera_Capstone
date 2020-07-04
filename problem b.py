start=int(input())
end=int(input())
l=[]
k=[]
y=[]
a=0
count=0
e=end-start
if(start>=2 and end <=100 and e>=35):
   for num in range(start, end + 1):
      if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                  break
          else:
              l.append(num)
   for i in range(0,len(l)):
       for j in range(0,len(l)):
           if(l[i]!=l[j]):
               a=str(l[i])+str(l[j])
           b=int(a)
           if(b not in k):
               k.append(b)
   k.remove(0)            
   for num in k:
       if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                  break
          else:
              y.append(num)                 
   min=min(y)
   max=max(y)
   f=len(y)
   x,y=min,max
   while(count<(f-2)):
      z=x+y
      x=y
      y=z
      count+=1
   print(y)


