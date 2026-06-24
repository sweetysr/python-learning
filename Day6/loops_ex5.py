print("Write a program that asks the user for a number and prints its multiplication table from 1 to 10.")


user = int(input("Enter a number for multiplication table: "))

for i in range(1, 11) :
    print(user, "*", i, "=", user * i)


    print("Write a program that asks the user for a number and prints its multiplication table from 1 to 10. Example Input: Enter a number: Output:5 x 1 = 5, 5 x 2 = 10")

user = int(input("Enter your number"))

for i in range(1, 11) :
        print(user, "*" , i , "=" , user * i)
