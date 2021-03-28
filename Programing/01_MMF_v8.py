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
    print()

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
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&Ms", "m&ms", "mms", "mm", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h2o", "d"],
        ["orange juice", "oj", "o", "juice", "orange", "e"]
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []

        # ask user for desired snack and put in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx" or desired_snack == "n":
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
        if snack_choice != "xxx" and snack_choice != "invalid choice" and snack_choice != "n":
            snack_order.append(snack_row)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main stuff

# set up lists needed to hold data

# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# valid options for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

max_tickets = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialize lists (to make data-frames in due course)
all_names = []
all_tickets = []

# snack lists...
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_multi_list = []

# lists to store summary data...
summary_headings = ["Popcorn", "Water", "Pita Chips", "M&Ms",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_multi_list
}

# summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25,
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

    # get snacks
    snack_order = get_snack()

    # assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Get payment method (ie: work out if surcharge in needed)
    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit)?").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_multi_list.append(surcharge_multiplier)

# end of that loop

# print details...
# create data frame and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and ticket

movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Snacks"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame['Sub Total'] + \
    movie_frame['Surcharge']

# shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# set up summary data frame
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    total = sum(item)
    summary_data.append("{:.0f}".format(total))

# get snack profit
# get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append("${:.2f}".format(snack_profit))

# get ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append("${:.2f}".format(ticket_profit))

# work out total profit and add to list
total_profit = snack_profit + ticket_profit

# format dollar amounts and add to list...
dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = "${:.2f}".format(item)
    summary_data.append(item)


# create summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# set up columns to be printed...
pandas.set_option('display.max_columns', None)

# *** pre printing / export ***
# Format currency values so they have $'s

# ticket details formatting (uses currency function)
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# write each frame to separate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")


print()
print("*** Ticket / Snack Information ***")
print("Note: for full details, please see the excel file called ")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)

# tell user if they have unsold tickets...
if ticket_count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets still available".format(ticket_count, max_tickets - ticket_count))


# check that no more than 150 seats(loop until 150 or exit code)

# out put ticket details

# out put amount of snacks required

# calculate profit.
