# code go here
print("--------------------------------------")
print("*** Welcome to gas station program ***")
print("--------------------------------------")
print("Please select the type of purchase:")
print("G: Gas")
print("O: Oil")
selection = input(">>>").upper()

#DEFINE CONSTANTS HERE vvvvvvv

#^^^^^^^^^

match selection:
    case "O":
        # Oil option

        pass #TODO: remove me when code is added
    case "G":
        # Gas option

        pass #TODO: remove me when code is added
    case _:
        print("Invalid input, you should enter g/G or o/O")
        exit()

#taxes and output


gst_percent = 0.0
price_final = 2.0       # placeholder, will be assigned above based on input

province_code = 'ab'    # placeholder, will be assigned above in province input

match province_code:
    case 'ab':  # Alberta
        gst_percent = 0.05
    case 'bc':  # British Columbia
        gst_percent = 0.05
    case 'on':  # Ontario
        gst_percent = 0.13
    case _:     # Everywhere else
        gst_percent = 0.15

price_final += price_final * gst_percent