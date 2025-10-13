print("ELIJE 3 NUMEROS Y TE DIRE CUAL ES EL MAYOR")
num1 = input(int)
num2 = input(int)
num3 = input(int)

if (num1 >= num2 and num1 >= num3 and num2 >= num3):
    print(num1,num2,num3)
elif(num2 >= num1 and num2 >= num3 and num1 >= num3):
    print(num2,num1,num3)
elif(num3 >= num1 and num3 >= num2 and num1 >= num2):
    print(num3,num1,num2)
elif(num1 >= num2 and num1 >= num3 and num3 >= num2):
    print(num1,num3,num2)
elif(num2 >= num1 and num2 >= num3 and num3 >= num1):
    print(num2,num3,num1)
elif(num3 >= num1 and num3 >= num2 and num2 >= num1):
    print(num3,num2,num1)
else:
    print("numero equivocao")
