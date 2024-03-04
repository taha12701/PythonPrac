# def show(n):
#     if(n==-1):
#         return
#     print(n)
#     show(n-1)
# show(5)

def fact(n):
    if( n==0 or n==1):
        return 1
    return(n * fact(n-1))
num=int(input("Enter a number : "))
print(f"The factorial of {num} is " , fact(num))
