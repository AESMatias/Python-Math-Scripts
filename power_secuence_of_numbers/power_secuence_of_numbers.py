
#This does not have been proved with negative cases yet, that's why the numbers must be
#positive. Also, this code need to be refactored with validation functions for the 
#inputs and, of course, the input option to choose between positive and negative 
#combinations of the secuence, the possible cases for the sign of the chased term,
# and extra features.
print("This code reach and print some number at the secuence of powered numbers")
print("based on a base specified number by the user, with alternate signs in its secuence")
base_number = int(input("Enter a positive number for the base of the secuence: "))
while(base_number <= 0):
    print("The input must be a positive number")
    base_number = int(input("Enter a positive number for the base of the secuence: "))
minimal_number_to_reach = int(input("Enter the minimal positive number to reach: "))
while(minimal_number_to_reach <= 0):
    print("The input must be a positive number")
    minimal_number_to_reach = int(input("Enter the minimal positive number to reach: "))

def joining_numbers(*args):
    k = 0 # Index of the list in the secuence of numbers
    args = list(args)
    printed_numbers = ""
    while k < len(args):
        printed_numbers = ' + '.join(map(str, args[k]))
        k+=1
    return printed_numbers

def calculate_hits(base_number, minimal_number_to_reach):
    current_number = 0
    pow = 0
    hits=0
    number_list = []
    while current_number < minimal_number_to_reach:
        if (pow % 2 == 0): # Check if the power is even, to change the sign of the secuence
            number_list.append(+base_number**pow)
            current_number = sum(number_list)
            pow+=1
            hits+=1
        else: # Check if the power is odd, to change the sign of the secuence
            number_list.append(-(base_number**pow))
            current_number = sum(number_list)
            pow+=1
            hits+=1
        current_number = sum(number_list)
        printed_numbers = joining_numbers(number_list)
        print(f'{printed_numbers} = {sum(number_list)}')
    return current_number,hits

current_number,hits = calculate_hits(base_number, minimal_number_to_reach)
print(f'''The minimal number to reach in the secuence was '{minimal_number_to_reach}'
and was reached at the '{hits}' number of the secuence,
which correspond to the number "{current_number}"''')
