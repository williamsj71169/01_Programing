# start of loop

# initialise loop so that it runs at least once.
name = ""
count = 0
MAX_TICKETS = 5

while name != "XXX" and count < MAX_TICKETS:
    print("You have {} seats left".format(MAX_TICKETS - count))

    # Get details...
    name = input("Name: ")
    if name != "XXX":
        count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} tickets still available".format(count, MAX_TICKETS - count))
