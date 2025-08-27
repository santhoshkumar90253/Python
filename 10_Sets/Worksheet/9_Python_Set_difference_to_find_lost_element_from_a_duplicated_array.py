'''Python Set difference to find lost element from a duplicated array
Tip: What does set(yesterday) - set(today) give you?'''

import ast
yesterday = input("Enter the list yesterday:")
today =input("Enter the list today:")
yesterday=ast.literal_eval(yesterday)
today=ast.literal_eval(today)
lost = set(yesterday) - set(today)

print("Lost item:", lost)