# Initialise snack lists...

names = ['A', 'B', 'C', 'D', 'E']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Water': water,
    'Orange Juice': orange_juice
    }

test_data = [
    [[1, 'Water'], [1, 'Pita Chips'], [1, 'M&Ms']],
    [[1, 'Water'], [1, 'Pita Chips'], [1, 'M&Ms']],
    [[1, 'Orange Juice']],
]

count = 0
for client_order in test_data:

    # assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    # print (snack_lists)

    # get order (hard coded for easy training)
    snack_order = test_data[count]
    count += 1
