from . import dice_printer

class Interface:
    def looper():

        print("Press any key to roll (space to quit)")
        try:
            key = input(">")
        except:
            print("Invalid character error")
        #loops until space is entered 
        while key != " ":
            dice_printer.Printer.print_die() #calls printer method
            try:
                key = input(">")
            except:
                print("Invalid character error")

        print("Bye!")
