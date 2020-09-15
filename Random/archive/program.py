filesystem = {}
pwdPath = []
pwd = filesystem

for _ in range(int(input())):
    try:
        args = input().split()
        a = args[0]
        b = args[1]
        if a == "cd":
            x = pwdPath[:]
            for p in b.split("/"):
                if p == "..":
                    x.pop()
                else:
                    x.append(p)
                d=filesystem
                for c in x:
                    d = d[c]
                    if type(d)!=type({}):
                        raise d
            pwd = d
            pwdPath = x
        if a == "mkdir" and b not in pwd:
            pwd[b] = {}
        if a == "touch" and b not in pwd:
            pwd[b] = 1
        if a == "rm":
            if b in pwd and pwd[b]:
                del pwd[b]
            if b == "-r":
                del pwd[args[2]]
    except:pass

print("/")


def show(d, depth=1):
    for k, v in d.items():
        print(" "*depth, k)
        if v!=1:
            show(v, depth+1)


show(filesystem)
