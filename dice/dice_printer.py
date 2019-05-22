from . import dice_generator

class Printer:
    def print_die():
        print("die:", dice_generator.DiceGenerator.dice_roll())
