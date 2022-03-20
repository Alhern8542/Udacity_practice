import time
import adventure_extension
import random


# combines print and sleep() default is 2 seconds
def print_delay(string, delay=2):
    print(string)
    time.sleep(delay)


# introduction to the game
def intro(creature, item):
    print_delay("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_delay(f"Rumor has it that a {creature} is somewhere around here.")
    print_delay("It has been terrifying the nearby village.")
    print_delay("In front of you is a house.")
    print_delay("To your right is a dark cave.")
    print_delay("In your hand you hold your trusty "
                f"(but not very effective) {item}.")


def fight_run():
    choose = input("Would you like to (1) fight or"
                   " (2) run away?\n")
    return choose


def game_over():
    again = input("Do you want to play again? (y/n)\n").lower()
    if again == "y":
        main()
    elif again == "n":
        print_delay("Thanks for playing! See you next time.")
        quit()
    else:
        game_over()


def cave(item, super_weapon, is_super):
    print_delay("You peer cautiously into the cave.")
    if is_super:
        print_delay("You've been here before, and gotten all"
                    " the good stuff.")
        print_delay("It's just an empty cave now.")
    else:
        print_delay("It turns out to be only a very small cave.")
        print_delay("Your eye catches a glint of shine "
                    "behind a rock.")
        print_delay(f"You have found {super_weapon}!")
        print_delay(f"You discard your silly old {item} and take the"
                    f" {super_weapon} with you.")
        is_super = True
    print_delay("You walk back out to the field.")
    return is_super


def house(item, creature, super_weapon, is_super, lives):
    print_delay("You approach the door of the house.")
    print_delay("You are about to knock when the door opens and "
                f"out steps a {creature}.")
    print_delay(f"Eep! This is the {creature}'s house!")
    print_delay(f"The {creature} attacks you!")
    lives -= 1
    print_delay(f"you have {lives} life left!")
    if lives == 0:
        print_delay("You have been defeated!")
        game_over()
    elif is_super:
        while True:
            choose = fight_run()
            if choose == "1":
                print_delay(f"As the {creature} moves to attack, "
                            f"you unleash your {super_weapon}.")
                print_delay(f"{super_weapon} shines brightly in "
                            "your hand as you brace yourself for the"
                            " attack.")
                print_delay(f"But the {creature} takes one look at "
                            "your shiny new toy and runs away!")
                print_delay("You have rid the town "
                            f"of the {creature}.\n"
                            "You are victorious!")
                game_over()
            elif choose == "2":
                print_delay("You run back into the field. Luckily, "
                            f"you don't seem to have been followed.")
                break
            else:
                print_delay("Invalid input")
    else:
        print_delay(f"You feel a bit under-prepared for this, "
                    f"what with only having a tiny {item}.")
        while True:
            choose = fight_run()
            if choose == "1":
                print_delay("You do your best...")
                print_delay(f"but your {item} is no match for"
                            f" the {creature}.")
                print_delay("You have been defeated!")
                game_over()
            elif choose == "2":
                print_delay("You run back into the field. Luckily, "
                            f"you don't seem to have been followed.")
                break
            else:
                print_delay("Invalid input")
    return lives


def play_game(item, creature, super_weapon, lives, is_super):
    intro(creature, item)
    while True:
        print_delay("Enter 1 to knock on the door of the house.")
        print_delay("Enter 2 to peer into the cave.")
        choice = input("What would you like to do?\n"
                       "(Please enter 1 or 2.)\n")
        if choice == "1":
            lives = house(item, creature, super_weapon, is_super, lives)
        elif choice == "2":
            is_super = cave(item, super_weapon, is_super)
        else:
            print_delay("Invalid input")


def main():
    item = random.choice(adventure_extension.items)
    creature = random.choice(adventure_extension.creatures)
    super_weapon = random.choice(adventure_extension.super_weapons)
    lives = 2
    is_super = False
    play_game(item, creature, super_weapon, lives, is_super)


main()
