p=f={}
P=[]
for _ in range(int(input())):
 try:
  a,b=args=input().split()
  if a=="cd":
   x=P[:]
   for c in b.split("/"):
    if c=="..":x.pop()
    else:x.append(c)
    d=f
    for c in x:d=d[c]
   p=d;P=x
  if a=="mkdir" and b not in p:p[b]={}
  if a=="touch" and b not in p:p[b]=1
  if a=="rm":
   if b in p and p[b]:del p[b]
   if b == "-r":del p[args[2]]
 except:pass
def s(d,D=1):
 for k,v in d.items():
  print(" "*D, k);v!=1 or s(v,D+1)
print("/");s(f)