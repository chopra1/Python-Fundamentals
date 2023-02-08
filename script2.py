my_name = "Chetan Chopra"
print("Hello & Welcome " + my_name + "!") #output: Hello & Welcome Chetan Chopra!
#comments
print("Hello World") #output: Hello World

print('Chetan Chopra') #output: Chetan Chopra
print("Chetan Chopra") #output: Chetan Chopra

message_string = "Hello there"
# Prints "Hello there"
print(message_string) #output: Hello there

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast: ") #output: Breakfast: An english muffin
print(meal)

# Now update meal to be lunch!
meal = "Parantha"

# Printing out lunch
print("Lunch:") #output: Lunch: Parantha
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Dinner: ") #output: Dinner: Parantha
print(meal)

an_int = 2
a_float = 2.1
 
print(an_int + 3) 
# Output: 5

#Define the release and runtime integer variables below:
release_year = 2023
runtime = 987

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 8.5

#arithmedic Expressions
# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)

# Prints "50"
print(5*10)

# Prints 1700.4642857142858
print(25*68+13/28)

#updating value
coffee_price = 1.50
number_of_coffees = 4
 
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# First we create the variables
quilt_width = 8
quilt_length = 12

# Then we print the size = 96
print(quilt_width * quilt_length)

# Whoops! That's a little too large
quilt_length = 8

# Let's see how large it is now = 64
print(quilt_width * quilt_length)

# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

print(6 ** 2) #prints 36
print(7 ** 2) #prints 49
print(8 ** 2) #prints 64
print(6 ** 4) #Prints 1296

#modulo % gives remainder of division
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

my_team = 27 % 4
print(my_team) #prints 3 
print(26 % 4) #prints 2
print(28 % 4) #prints 0

#Concatenation
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

message = string1 + string2 + string3 + string4 + string5 + string6

print(message)

#+= operator
# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
print(hike_caption)
#prints: What an amazing time to walk through nature! #nofilter #blessed

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += 59.00
print("The total price is", total_price) #output: The total price is 109.0

#multi line strings
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
print(leaves_of_grass)

# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""
print(to_you)

my_age = 26
half_my_age = my_age/2
greeting = "Hi!"
name = "Chetan Chopra"
greeting_with_name = greeting + name
print(greeting_with_name) #output: Hi!Chetan Chopra
