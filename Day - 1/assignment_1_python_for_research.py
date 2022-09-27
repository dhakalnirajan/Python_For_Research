# -*- coding: utf-8 -*-
"""Assignment-1 Python For Research.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_6GxTFasGlJRf-C56XJanN3QIbZlcSSu

# 1. **Write a program to swap the values in two variables**.
    num1 = 0.7
    num2 =  -3

    Expected Output:
    num1 = -3
    num2 =  0.7
"""

# Assigning values to the variables 'num1' and 'num2'
num1 = 0.7
num2 = -3

tmp = num1      # storing the value of num1 to a temporary variable called 'tmp'

num1 = num2     # overriding the value of 'num1'.

num1

num2 = tmp     # overriding the value of 'num2' by assigning from temporary value

print("num1 = ",num1)
print("num2 = ", num2)

"""# 2. **Start Python as Interpreter and use it as a calculator.**


1.   How many seconds are there in 42 minutes 42 seconds?
2.   How many miles are there in 10 Kilometers?
3.   If you run a 10-Kilometer race in 42 minutes and 42 seconds, what is your average pace (speed: miles per minutes and miles per seconds)?

### First, let's solve using classical method.

Given time = 42 minutes and 42 seconds,

Given Distance = 10 kilometres

Converting the given time in seconds, 42 * 60 + 42 = 2562 seconds

Converting the given time in minutes, 2562/60 = 42.7 minutes

Converting the given length in miles, 10 / 1.6093 = 6.21 miles

speed in miles per minute = distance in miles / time in minute

= 6.21 / 42.7

= 0.1454 miles per minute


speed in miles per seconds = distance in miles / time in second

= 6.21 / 2562

= 2.42* 10^-3 miles per seconds

pace distance = 1 mile

pace time in minutes = pace distance / speed in miles per minute

= 1 / 0.1454

= 6.877 minutes


pace time in seconds = pace distance / speed in miles per seconds

= 1 / 2.42*10^-3

=  413.22 seconds


average pace in minutes = distance in miles / pace time in minutes

= 6.21 / 6.877

= 0.9030

average pace in seconds = distance in miles / pace time in seconds

= 6.21 / 413.22

= 0.015
"""

# Given time = 42 minutes and 42 seconds
# given distance = 10 kilometres

# Assigning variables with values
seconds = (42 * 60) + 42
minutes = 42 + (42 / 60)
miles = round(10 / 1.6093, 2)

# Printing the output of the above values
print("Seconds = ", seconds)
print("Minutes = ", minutes)
print("distance in miles = ", miles)

speed_miles_per_min = miles / minutes     # Calculating the speed in miles per minutes
speed_miles_per_sec = miles / seconds     # Calculating the speed in miles per seconds

print("Speed in miles per minute = {}".format(round(speed_miles_per_min, 3)))      # output of Miles per minute
print("Speed in miles per second = {}".format(round(speed_miles_per_sec, 3)))      # output of Miles per second

# average pace in minutes and seconds
pace_distance = 6.21

pace_in_min = pace_distance / speed_miles_per_min
pace_in_sec = pace_distance / speed_miles_per_sec

print("The Average pace I acquired in a 10-Kilometre race was {} miles per minutes and {} miles per seconds".format(pace_in_min, pace_in_sec))

"""# 3. Suppose the cover price of a book is `$24.95`, but the bookstores get a 40% discount. Shipping costs `$3` for the first copy and 75 cents for each additiobal copy. What us the total wholesale cost of 60 copies?


```
cover price = 24.95
discount = 40%
shipping cost for first copy = 3
shipping cost for each additional copy = .75
total copies = 60
additional copies = 59
remaining units = 1
```


"""

costprice = 24.95
discount = 0.6      # Since the discount percentage is 40%, we have to pay 60% retail price.
shipping_cost_first = 3
shipping_cost_add = .75
total_units = 60
additional_units = total_units -1

print("costprice : ", costprice)
print('discount : ', discount)
print("First Shipping Cost : " , shipping_cost_first)
print("Additional Shipping Cost : " , shipping_cost_add)
print("Additional Units : " , additional_units)

# Discounted amount = book price * discount * total units
cost_before_shipping = (costprice * discount) * total_units

# Shipping cost = first shipping cost + remaining units * 0.75
shipping_cost = shipping_cost_first + (59 * shipping_cost_add)

# total cost = discounted amount + shipping cost
total = cost_before_shipping + shipping_cost

print("The total price for 60 books including shipping and discount is: ")

print("Total price of the books is: " + str(round(cost_before_shipping, 1)))

print("Total Shipping is: " + str(shipping_cost))

print("The Total price is: " + str(round(total, 2)))