def menu():
    contin="yes"
    while(contin=="yes"):
        print("enter range of numbers (a,b) :")
        a= int(input("enter a = "))
        b=int(input("enter b = "))
        alist=list(range(a,b+1))
        for i in alist:
            print(i,end=' ')
        order=input("\nselect order : 'des'  or 'asc'")
        if(order=="des"):
            alist.reverse()
        for i in alist:
            if(i%2!=0):
                print(i,end=' ')
        contin = input("\ncontinue? 'yes' or 'no'\n ")
    
menu()
