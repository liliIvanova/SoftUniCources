KID_AGE = 14
TEEN_AGE = 18
YOUNG_ADULT_AGE = 21

age = int(input())

if age <= KID_AGE:
    drink = 'drink toddy'
elif age <= TEEN_AGE:
    drink = 'drink coke'
elif age <= YOUNG_ADULT_AGE:
    drink = 'drink beer'
else:
    drink = 'drink whisky'

print(drink)