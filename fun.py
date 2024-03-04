# def cal_sum(a,b):
#     return a+b                    #returns the value means output  


# sum=cal_sum(4,6)                  #the output store in variable and then print it
# print(sum)

# def hello_world(a):
#     return a
# greetings=hello_world("Hello World, My name is Taha")
# print("This is the python world" + "." + greetings)

#code for average

# def cal_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg

# average=cal_avg(4,5,6)
# print(average)

# print("Taha", end=" ")       #end parameter for display output in a single line
# print("Babar")

# def cal_mult(a=2,b=5):
#     print(a*b)
#     return a*b
# cal_mult()

cities=["Lahore Qalandars", "Karachi Kings" , "Peshawar Zalmi" , "Islamabad United" , "Quetta Gladiators" , "Multan Sultans"]
# players=["Taha Ahmed" ,  "Babar Azam" , "Shaheen Afridi" , "Fkahr Zaman" , "Naseem Shah"]

# def len_list(list):
#         print(len(list))
# len_list(cities)
# len_list(players)

# for city in cities:
#     print(city, end="")


# def single_line(list):
#     for item in list:
#          print(item, end=" ")

# single_line(cities)


# def currency_conv(usd_value):
#     pkr_value= usd_value * 289
#     print(usd_value , "Usd" , "=", pkr_value , "Pkr")
#     return pkr_value

# usd=int(input("Enter no of Dollars : "))
# currency_conv(usd)

# def sing_line(list):
#     for city in cities:
#         print(city , end=" ")
#     return city

# sing_line(cities)



# def check_in(num):
#     if num % 2 == 0:
#          print(f"{num} is Even Number")
#     else:
#         print(f"{num} is Odd Number ")

# num_val=int(input("Enter a number "))
# check_in(num_val)


# def check_even_odd(number):
#     # Check if the number is even or odd
#     if number % 2 == 0:
#         print(f"The number {number} is even.")
#     else:
#         print(f"The number {number} is odd.")

# # Prompt the user to input a number
# user_number = int(input("Enter a number: "))

# # Call the function with the user input as an argument
# check_even_odd(user_number)

# n=int(input("Enter a number : "))
# fact=1
# for i in range(1,n+1):
#     fact *=i

# print("The factorial is : ",fact)




def cal_fact(k):
    fact=1
    for i in range(1,k+1):
        fact *= i
    print(fact)
fact_cal=int(input("Enter a number : "))
cal_fact(fact_cal)





    






   



