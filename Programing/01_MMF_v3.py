# import statement
import re
import pandas

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


# checks number of tickets lift and warns user if max is approaching
def check_tickets(tickets_sold, ticket_limit):
    # tell user how many seats left
    if ticket_count < max_tickets - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    return ""


# gets ticket price based on age
def get_ticket_price():

    # get age (between 12 and 130)
    age = int_check("Age: ")

    # check age is valid
    if age < 12:
        print("Sorry, you are too young to watch this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

# main stuff

# do stuff

max_tickets = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialize lists (to make data-frames in due course)
all_names = []
all_tickets = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets

}

# ask user if they have done ths before

# loop to get ticket details
while name != "xxx" and ticket_count < max_tickets:

    # check numbers of ticket limit has not been exceeded...
    check_tickets(ticket_count, max_tickets)

    # Get details...

    # get name, can not be blank
    name = not_blank("Name: ")
    print()

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # get ticket price based on age
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# tell user if they have unsold tickets...
if ticket_count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets still available".format(ticket_count, max_tickets - ticket_count))

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
