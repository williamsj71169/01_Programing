# function goes here


# checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer in not entered, display an error
        except ValueError:
            print(error)

# Main routine
age = int_check("Age: ")

# check age is valid
if age < 12:
    print("Sorry, you are too young to watch this movie")
    # continue

elif age > 130:
    print("That is very old - it looks like a mistake")
    # continue
