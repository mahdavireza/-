a = 'aababbatta'
b = {}

for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1   