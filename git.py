def fact(n):
    if( n==0 or n==1):
        return 1
    return(n * fact(n-1))
num=int(input("Enter a number : "))
print(f"The factorial of {num} is " , fact(num))

def calculate_sum(n):
    if(n==0):
        return 0
    return n + calculate_sum(n-1)
add=int(input("Enter a number : "))
print(calculate_sum(add))


def cal_list(list,index=0):
    if(len(list)==index):
        return
    print(list[index])
    cal_list(list,index + 1)

list=["Taha", "Babar" , "Shadab" , "Shaheen"]
cal_list(list,index=0)
