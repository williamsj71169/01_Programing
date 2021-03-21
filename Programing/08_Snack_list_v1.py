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

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = snack_menu_dict[to_find]
            add_list[-1] = amount

print()
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips: ", snack_lists[2])
print("Water: ", snack_lists[3])
print("Orange Juice: ", snack_lists[4])
