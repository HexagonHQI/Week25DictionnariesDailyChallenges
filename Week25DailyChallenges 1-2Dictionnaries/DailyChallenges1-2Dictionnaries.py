#Challenge 1: Indexes of Each Letter in a Word


word = input("Enter a word: ")
letter_indexes = {}
for index, letter in enumerate(word):
    if letter not in letter_indexes:
        letter_indexes[letter] = []
    letter_indexes[letter].append(index)

print(letter_indexes)

{"d": [0, 2], "o": [1, 3]}
{"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}

#Challenge 2: Items Affordable in the Store

# The items with prices String
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

# Amount in the wallet
wallet = "$300"

# Convert wallet to integer
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# List
affordable_items = []

for item, price in items_purchase.items():
    item_price = int(price.replace("$", "").replace(",", ""))

    if item_price <= wallet_amount:
        affordable_items.append(item)

affordable_items.sort()

# Result:
if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
