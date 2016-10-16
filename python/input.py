#name = raw_input('What is your name? ')
#print('Hi ' + name)

# name = raw_input('What is your name?')
# age = raw_input('How old are you?')
# print(name + ' is ' + age + ' years old.')


# age = raw_input('How old are you?')
# dog_years = age * 7
# print('You are ' + dog_years + 'old in dog years.')

# age = raw_input('How old are you? ')
# dog_years = int(age) * 7
# print('You are ' + str(dog_years) + ' years old in dog years.')

meal_price = float(raw_input('How much was your meal? '))
tip = float(meal_price) * .20
total_price = float(meal_price + tip)
print('You should tip $ ' + str(tip) + ' .')
print('Your total cost would be ' + str(total_price) + ' . ')