#interpreter.py
expression = input("Expression: ").strip()
x, y, z = expression.split(" ")
num1 = float(x)
num2 = float(z)
if y == "+":
    result = num1 + num2
elif y == "-":
    result = num1 - num2
elif y == "*":
    result = num1 * num2
elif y == "/":
    result = num1 / num2
print(result)
