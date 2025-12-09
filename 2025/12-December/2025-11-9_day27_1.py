try:
    a = int(input("Enter number A : "))
    b = int(input("Enter number B : "))
    c = a/b
    print(f"{a}/{b} = {c}")

#WITH EXCEPTION VARIABLE (e)
except Exception as e :
    print("Division by zero not allowed..")
    print(e)

#EXECUTED IF TRY BLOCK RUNS OTHREWISE NOT 
else:
    print("i am in other part of the program")
    print("I am in Else part... When there is no error in try block")
