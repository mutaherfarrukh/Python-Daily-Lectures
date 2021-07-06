# ===============
# Basics
# ===============

# 1) Print all integers from 1-255

# def printTo255():
#     for i in range(1, 256, 2):
#         print(i)

# printTo255()

# 2) Given an list, find and print its largest element
#[1,2,3,4,5,6,7,8,9]--> 31

# def printLargestElement(lst):
#     max = lst[0]
#     for i in range(0, len(lst), 1):
#         if i > max:
#             max = lst[i]
#     print(max)

# printLargestElement([1,2,31,4,5,6,7])
# 3) Return a given list, after setting any negative numbers to zero
#[-1,-2,4,5,-4,7]-->[0,0,4,5,0,7]

def negativeToZero(lst):
    for i in range(0, len(lst), 1):
        if lst[i] < 0:
            lst[i] = 0
    return lst

print(negativeToZero([-1,-2,4,5,-4,7]))


# ===============
# Bit More advanced...
# ===============

# For Loop II - Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


def reverseList(lst):
    for i in range(0, len(lst)//2, 1):
        temp = lst[i]
        lst[i] = lst[len(len(lst - i -1))]
        lst[len(lst) - 1 -i] = temp



# Functions Basic II - This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

# ===============
# Heckin' Loopin'
# ===============

schools = {
    'locations': ['UC Berkeley', 'UC Davis', 'UC LA', 'UC Irvine'],
    'professors': ['John', 'Jacob', 'JingleHeimer', 'Schmidt']
}


# Print the name of the school location, and the professor that corresponds to that school

schools['locations'][1]= "UC Santa Cruz"

def printSchoolsWithProfessor(dict):
    for i in range(0, len(dict['locations']), 1):
        print(f"{dict['locations'][1]} - and the professor is {dict['professor'][i]}")

# printSchoolsWithProfessor(schools)

dog_owners = [
        {'first_name':  'Kaysee', 'last_name' : 'Webs', 'dog' : {'name' : 'Stella', 'breed' : 'mystery'}},
        {'first_name' : 'Nick', 'last_name' : 'Moral', 'dog' : {'name' : 'Spud', 'breed' : 'chihuahua'}},
        {'first_name' : 'Robert', 'last_name' : 'Sant', 'dog' : {'name' : 'Rocket', 'breed' : 'bulldog'}},
    ]

# # print the first name of the owner, and the name of their dog

def printDogNames(lst):
    for i in range(0, len(lst), 1):
        print(f"{lst[i]['first_name']}'s dog's name is  {lst[i]['dog']['breed']}")
        # print(lst[i]['dog']['name'], "and the breed is", lst[i]['dog']['breed'])

printDogNames(dog_owners)