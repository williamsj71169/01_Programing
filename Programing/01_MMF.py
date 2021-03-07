# import statement


# functions go here


# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (and repeat loop)
        else:
            print("Sorry - this can't be blank")
            print("please enter your name")


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

name = ""
count = 0
max_tickets = 5

while name != "XXX" and count < max_tickets:

    # tell user how many seats left
    if count < 4:
        print("You have {} seats left".format(max_tickets - count))

    # warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    # Get details...
    name = not_blank("Name: ")
    print()

    # end the loop if the exit code is entered
    if name == "XXX":
        break

    # get age (between 12 and 130)
    age = int_check("Age: ")

    # check age is valid
    if age < 12:
        print("Sorry, you are too young to watch this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    count += 1


if count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets still available".format(count, max_tickets - count))

    # Ask for users age, 12-130, integer and not blank

    # work out price for ticket depending on users age

    # Ask what snacks they would like (display snacks and prices(including surcharge for if using credit) )
    # popcorn:2.5 m&m:3 pita:4.5 oj:3.25 water:2.

    # Ask payment method and work out surcharge if credit is chosen
    # surcharge of *0.05

    # work out total cost of ticket/snacks/surcharge

# check that no more than 150 seats(loop until 150 or exit code)

# out put ticket details

# out put amount of snacks required

# calculate profit.
