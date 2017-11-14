def yes():
    x = input("Enter any interger to see its divisors:")
    if int(x) >= 1:
        a = range(1,int(x)+1)
        b = range(int(x)*-1,0)
        for elem in b:
            g=int(x)%elem
            if g==0:
                print (elem)
        for elem in a:
            y=int(x)%elem
            if y==0:
                print (elem)
        yes()
    elif int(x) <= -1:
        a = range(1,int(x)*-1+1)
        b = range(int(x),0)
        for elem in b:
            g=int(x)%elem
            if g==0:
                print (elem)
        for elem in a:
            y=int(x)%elem
            if y==0:
                print (elem)
        yes()
    else:
        print('Insolent Fool')
        yes()
        
yes()

