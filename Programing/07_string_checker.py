

# string checking function takes in
# question and lists of valid responses
def string_checker(question, to_check):

    valid = false
    while not valid:

        response = intput(question).lower

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks if response is the first letter of
                # an item in the list
                if response == item[0]:
                    # note: returns the entire response
                    # rather then just the first letter
                    return item

        print("Sorry, that is not a valid response")


# Main Stuff
for item in range(0, 6):
    want_snacks = string_checker("So you want snacks? ", ["yes", "no"])

    print("Answer OK, you said:", want_snacks)
    print()
