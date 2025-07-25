#code faces
# make function that convert text into emoji
def convert(text):
    text = text.replace(":)" ,"☺️")
    text = text.replace(":(" ,"😞")
    # it gives the output to the function
    return text

#Define the main function that will control the flow of the program
def main():
    user_text = input("Enter your message: ")
    # Call the 'convert' function using the user's input and print the result
    print(convert(user_text))


main( )

