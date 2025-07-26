def main():
    # Ask the user to enter the time and remove extra spaces
    time = input("What time is it?").strip()

    # Convert the time string to a float representing the hour
    hour = convert(time)

    # Check the time range and print the appropriate meal time
    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("Lunch time")
    elif 18.0 <= hour <= 19.0:
        print("Dinner time")

# Convert "HH:MM" format to float hours
def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

# Run the program
main()


