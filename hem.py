#guessing random number
# import random
 
# rand = random.randint(1,100)
# guess = int(input('Enter any number:'))

# while rand!= guess:
#     if guess < rand:
#         print('too low')
#         guess = int(input('Enter any number:'))
#     elif guess > rand:
#         print('too high')
#         guess = int(input('Enter any number:'))
#     else :
#         break        #breaking while loop 
# print('youre correct' )   #outside the while loop



#guessing random number with counts
# import random
 
# rand = random.randint(1,10)
# guess = int(input('Enter any number:'))
# attempt = 0

# while rand!= guess:
#     if guess < rand:
#         attempt +=1
#         print('too low')
#         guess = int(input('Enter any number:'))
#     elif guess > rand:
#         attempt+=1
#         print('too high')
#         guess = int(input('Enter any number:'))
#     else :
#         break        #breaking while loop 

# attempt +=1

# print(f'youre correct in {attempt} attempts' )   #outside the while loop



#leap year checker

leap = input("Do you want to input a year or check a range? (input/range): ").strip().lower()

if leap == 'input':

    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
elif leap == 'range':
    print("Leap years from 2012 to 3040 are:")
    for year in range(2012, 3041):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
else:
    print("Invalid option. Please select either 'input' or 'range'.")


