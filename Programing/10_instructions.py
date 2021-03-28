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


def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?")
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("*** Mega Movie Fundraiser Instructions ***")
        print()
        print("Instructions")

    return ""


# main stuff
# valid options for yes/no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


# ask if instructions are needed
instructions(yes_no)
print()
print('Program launches...')
