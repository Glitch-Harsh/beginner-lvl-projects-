# define main function where the program logic implemented 
def main():
#
    answer = input("What is the answer to life, the universe, and everything? ").strip().lower()

    if answer =="42" or answer == "forty-two" or answer == "forty two":
        print("yes")
    else:
        print("no")

main()