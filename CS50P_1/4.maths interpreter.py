def main():
    expression = input("Enter a mathematical expression: ").strip()

    x, y ,z = expression.split()
    x = float(x)    
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z 
    elif y == "/":
        result = x / z

    print(f"The result is: {result}")
 
main()