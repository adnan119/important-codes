def primes(n):
    q=[x for i in range(2,int(n/10)) for x in range(i*2,n,i)]
    y= list(range(1,n))
    z=[]
    for w in y:
        if w not in q:
            z.append(w)
    print(z)
    
