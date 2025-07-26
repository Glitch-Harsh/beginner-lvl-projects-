def main():
    Greeting = input("Enter your greeting? :").strip()
    
    if Greeting.startswith("Hello"):
        print("$0")
    elif Greeting.startswith("H"):
        print("$20")
    else:
        print("$100")

main()