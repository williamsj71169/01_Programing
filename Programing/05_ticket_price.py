profit = 0

name = ""
while name != "XXX":
    name = input("Name: ")  # replace with function caall

    # if name is exit code, break out of loop
    if name == "XXX":
        break

    age = int(input("Age: "))  # replace with function call

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_price))

print("Profit from Tickets: ${:.2f}".format(profit))
