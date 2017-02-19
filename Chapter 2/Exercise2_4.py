# coding=utf-8
# The volume of a sphere with radius r is 4/3 πr^3 . What is the volume of a sphere with radius 5?
# Hint: 392.6 is wrong!
import math
r = 5
volume = (4 * math.pi * math.pow(r, 3))/3  # math.pow == r**3
print("The answer is", volume)

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping
# costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale
# cost for 60 copies?
one_book = 0.4 * 24.95
x_books = one_book * 60
print("Total cost for 60 copies is", x_books)

shipping_cost = 3 + 59 * 0.75
print("Total wholesale for 60 copies is", x_books + shipping_cost)
