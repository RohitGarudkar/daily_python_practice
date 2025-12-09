try:
    a = int(input("Enter number A : "))
    b = int(input("Enter number B : "))
    c = a/b
    
    
except:
    print("Can't divide by Zero")
    

#EXECUTED IF TRY BLOCK RUNS OTHREWISE NOT 
else:
    print(f"{a}/{b} = {c}")
    print("I am in Else part... When there is no error in try block")
