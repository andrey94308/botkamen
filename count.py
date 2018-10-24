def count(x,y):
    g=x+y
    try:
        #with open(g'.txt','r') as f:
        f = open('log/'+g+'.txt','r')
        n=int(f.read())
        f.close()
    except:
        n = 0
    n+=1
    f=open('log/'+g+'.txt','w')
    a=str(n)
    f.write(a)
    f.close()
   

