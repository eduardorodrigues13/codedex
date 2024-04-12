# Write code below 💖
#import math library
import math
#title
print('=================')
print('Area Calculator 📐')
print('=================')
# empty space
print('')
# options
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
print('')

# option input
option = input('Which shape: ')
print('')
#loop in case the user doesn't type an integer.
while option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
  print('Option not encountered.')
  print('')
  option = input('Which shape: ')
  print('')

#for triangle: 
if option == "1":
  #asks the base  
  base = input('Base: ')
  #loop in case the user doesn't type a number
  while base.isdigit() == False:
    base = input('Please, enter a valid number for the base: ')
  #asks the height
  height = input('Height: ')
  #loop in case the user doesn't type a number
  while height.isdigit() == False:
    height = input('Please, enter a valid number for the height: ')
  #formula for the triangle
  triangle_area = (float(height) * float(base)) / 2
  print('')
  #returns value
  print(f'The area is {triangle_area}.')

#for rectangle
elif option == "2":
  #asks for the length
  length = input('Length: ')
  #loop in case the user doesn't type a number
  while length.isdigit() == False:
    length = input('Please, enter a valid number for the length: ')
  #asks for the width
  width = input('Width: ')
  #loop in case the user doesn't type a number
  while width.isdigit() == False:
    width = input('Please, enter a valid number for the width: ')
  #formula
  rectangle_area = float(length) * float(width)
  print('')
  #returns value
  print(f'The area is {rectangle_area}.')

#for square
elif option == "3":
  #asks for the side
  side = input('Side: ')
  #loop in case the user doesn't type a number
  while side.isdigit() == False:
    side = input('Please, enter a valid number for the side: ')
  #formula
  square_area = float(side) ** 2
  #returns value
  print(f'The area is {square_area}.')

#for circle
elif option == "4":
  #asks for the radius
  radius = input('Radius: ')
  #loop in case the user doesn't type a number
  while radius.isdigit() == False:
    radius = input('Please, enter a valid number for the radius: ')
  #formula
  circle_area = math.pi * (float(radius) ** 2)
  #returns value
  print(f'The area is {circle_area}.')

#exit message
else:
  print('Bye! At.te., Eduardo.')