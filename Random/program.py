t = """e(q(ac3c4!.a,qih)n.((yf a5f a5".a,qih)n.((yf a5f a5
=3=3=h)h);rcq)nr.(j[b*oin1oin);rcq)nr.(j[b*oin1oin)
c3c4"r;r;bee+;t(j[os[5rng)rng]bee+;t(j[os[5rng)rng]
h)h)e(q(a=p(ap(1o'itx]  e]  e)=p(ap(1o'itx]  e]  e)
r;r;=3=3=ale+rc0i'nr+)yr()xr()ale+rc0i'nr+)yr()xr()"""
arr = []
for line in t.split("\n"):
    a = []
    for c in line:
        a.append(c)
    arr.append(a)

for x in range(len(arr[0])):
    for y in range(len(arr)):
        print(arr[y][x], end="")