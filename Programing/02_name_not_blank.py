# import statements


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


# Main Routine Goes Here
name = not_blank("Name: ")
