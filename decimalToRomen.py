# This program may not work properly if Python versionis less than  3.7

TEXT_START = """
... This program converts decimal numbers to Roman Numerals ...
(To exit the program, please type 'exit')
"""
TEXT_ASK_INPUT = "Please enter a number between 1 and 3999, inclusively: "
TEXT_EXIT = "\nExiting the program\n...Good Bye...\n" 
TEXT_ERROR = "Not a valid input! Please enter a decimal number between 1-3999 inclusively\n"

LETTERS = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}

SPECIAL_NUMBERS = {
    'DCCCC': 'CM',
    'CCCC': 'CD',
    'LXXXX': 'XC',
    'XXXX': 'XL',
    'VIIII': 'IX',
    'IIII': 'IV'
}

###########################################################################

print(TEXT_START)

def converter():
    user_input = input(TEXT_ASK_INPUT)
    if user_input.lower() == "exit":
        print(TEXT_EXIT)
    
    else:
        try:
            user_input = int(user_input)
        
        except ValueError:
            print(TEXT_ERROR)
            converter()
        
        else:
            if not 1 <= user_input <= 3999:
                print(TEXT_ERROR)
                converter()
            
            else:
                divisors = LETTERS.keys()
                in_roman_list = []
                remainder = user_input
                
                for divisor in divisors:
                    quotient = remainder // divisor
                    [in_roman_list.append(LETTERS[divisor]) for _ in range(quotient)]
                    remainder = remainder % divisor

                in_roman = ''.join(in_roman_list)
                
                for k, v in SPECIAL_NUMBERS.items():
                    #print("before", k, v, in_roman)
                    in_roman = in_roman.replace(k ,v)
                    #print("after", k,v,in_roman)

                print(f"\n{user_input} in Roman Numerals is: {in_roman}\n")
                converter()

if __name__ == '__main__':
    converter()
    