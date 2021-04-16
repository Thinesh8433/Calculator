from Calc import *


print("            #___#___#___#___#___Welcome__#__#__#__#__#__#___#")

print("\n")

print("_-_-_-_-_-_-Operations are_-_-_-_-_-_-\n"
      "\n=====> 1: Addition  =====> 2: Subtraction ====> 3: Multiplication ====> 4: Division\n "
      "\n-----> 5: Modulus -----> 6: Square_root -----> 7: Sin -----> 8: Cos -----> 9: Tan\n"
      "\n=====> 10: Ceil ====> 11: Floor =====> 12: Factorial =====> 13: Exponential=====> 14: Log ====> 15: Log2\n "
      "\n----> 16: Radian -----> 17: Degree -----> 18: interest -----> 19: marks_percent -----> 20: Fahrenheit\n"
      "\n=====> 21: Celsius")

Op = input("Enter an choice 1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21 :")


if Op in ('1', '2', '3', '4', '5', '6'):
    a = float(input("Enter a number :"))
    b = float(input("Enter a number :"))

    if Op == '1':
        print("Addition is :", add(a, b))

    elif Op == '2':
        print("Subtraction is :", sub(a, b))

    elif Op == '3':
        print('Multiplication is :', mul(a, b))
        
    elif Op == '4':
        print("Division is :", div(a, b))

    elif Op == '5':
        print("Modulus is ", mod(a, b))

    elif Op == '6':
        print("Square root is :", squa(a, b))


elif Op in ('7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'):
    
    if Op == '7':
        a = float(input("Enter a value :"))
        print("Sin of", a, "is :", sin(a))

    elif Op == '8':
        a = float(input("Enter a value :"))
        print("Cos of", a, "is :", cos(a))

    elif Op == '9':
        a = float(input("Enter a value :"))
        print("Tan of", a, "is :", tan(a))

    elif Op == '10':
        a = float(input("Enter a value :"))
        print("Ceil for the number is :", ceil(a))

    elif Op == '11':
        a = float(input("Enter a value :"))
        print("Floor for the number is :", floor(a))

    elif Op == '12':
        fact()

    elif Op == '13':
        a = float(input("Enter a value :"))
        b = float(input("Enter a value :"))
        print("Exponential value of", a, "is :", exp(a))

    elif Op == '14':
        a = float(input("Enter a value :"))
        print("Log of", a, "is :", log(a))

    elif Op == '15':
        a = float(input("Enter a value :"))
        print("Log2 value is :", log1(a))

    elif Op == '16':
        a = float(input("Enter a value :"))
        print("The radian is :",rad(a))

    elif Op == '17':
        a = float(input("Enter a value :"))
        print("The degree is :", deg(a))
        

elif Op in ('18', '19', '20', '21'):
    if Op == '18':
        p = int(input("Enter principal amount : "))
        r = float(input("Enter interest : "))
        t = float(input("Enter a time period : "))
        amount = p*r*t/100
        print(amount, "rupees for", t, "month")

    elif Op == '19':
        Total_marks_obtained = int(input("Enter your total marks obtained :"))
        Sum_of_total = int(input("Enter your Sum of total marks :"))
        percentage = Total_marks_obtained / Sum_of_total * 100
        print("Your percentage is : ", percentage)

    elif Op == '20':
        n = input("Enter your temperature in Celsius :")
        degree = int(n[:-1])
        i_convention = n[-1]
        if i_convention.upper() == 'C':
            result = int(round(9*degree) / (5 + 32))
            f_convention = 'F'
            print('The temperature in Fahrenheit is :',result,f_convention)
        else:
            print("Invalid convention")

    elif Op == '21':
        n = input("Enter your temperature in fahrenheit :")
        degree = int(n[:-1])
        print(degree)
        i_convention = n[-1]
        print(i_convention)
        if i_convention.upper() == 'F':
            result = int(round(degree - 32) * (5 / 9))
            c_convention = 'C'
            print("The temperature in Celsius is :", result, c_convention)
        else:
            print("Invalid convention")

else:
    print('Invalid input')





