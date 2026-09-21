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