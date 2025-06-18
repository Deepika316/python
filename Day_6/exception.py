try:
    n1=int(input("Enter number1:"))
    n2=int(input("Enter number2:"))
    print("output:",n1/n2)
except Exception as error:
    print(f"Error is {error}")
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Value error")
finally:
    print("program is end")