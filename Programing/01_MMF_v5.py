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


# string checker
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it locks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# Gets list of snacks
def get_snack():

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # ,and possible abbreviations ect>

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj", "o", "juice", "e"]
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate into two.
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check that string is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        # check snack amount it valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack and amount to list...

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

# main stuff

# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

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

    # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        print()
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    # if they say yes, ask what snacks they want (and add to list)
    if check_snack == "Yes":
        get_order = get_snack()

    else:
        get_order = []

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

# show snack orders
print()
if len(get_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered:")

    '''for item in snack_order:
        print(item)'''

    print(get_order)

    # Ask payment method and work out surcharge if credit is chosen
    # surcharge of *0.05

    # work out total cost of ticket/snacks/surcharge

# check that no more than 150 seats(loop until 150 or exit code)

# out put ticket details

# out put amount of snacks required

# calculate profit.
