import time
import adventure_extension


# combines print and sleep()
def print_delay(string):
    print(string)
    time.sleep(2)


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


def user_input():
    choose = input("What would you like to do?\n"
                   "(Please enter 1 or 2.)\n")
    return choose


def field_choices():
    print_delay("Enter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")


def house(creature, item, super_weapon, is_super, lives):
    print_delay("You approach the door of the house.")
    print_delay("You are about to knock when the door opens and "
                f"out steps a {creature}.")
    print_delay(f"Eep! This is the {creature}'s house!")
    print_delay(f"The {creature} attacks you!")
    lives -= 1
    print_delay(f"you have {lives} life left!")
    if lives == 0:
        print_delay("You have been defeated!")
    elif is_super:
        fight_run = input("Would you like to (1) fight or (2) run away?\n")
        if fight_run == "1":
            print_delay(f"As the {creature} moves to attack, you unleash "
                        f"your {super_weapon}.")
            print_delay(f"{super_weapon} shines brightly in your hand as "
                        "you brace yourself for the attack.")
            print_delay(f"But the {creature} takes one look at your shiny "
                        "new toy and runs away!")
            print_delay(f"You have rid the town of the {creature}.\n"
                        "You are victorious!")
        elif fight_run == "2":
            print_delay("You run back into the field. Luckily, "
                        f"you don't seem to have been followed.")
            field_choices()
    else:
        print_delay(f"You feel a bit under-prepared for this, "
                    f"what with only having a tiny {item}.")
        fight_run = input("Would you like to (1) fight or (2) run away?\n")
        if fight_run == "1":
            print_delay("You do your best...")
            print_delay(f"but your {item} is no match for the {creature}.")
            print_delay("You have been defeated!")
    game_over()


def cave(item, super_weapon, is_super):
    print_delay("You peer cautiously into the cave.")
    if is_super:
        print_delay("You've been here before, and gotten all the good stuff.")
        print_delay("It's just an empty cave now.")
    else:
        print_delay("It turns out to be only a very small cave.")
        print_delay("Your eye catches a glint of shine behind a rock.")
        print_delay(f"You have found {super_weapon}!")
        print_delay(f"You discard your silly old {item} and take the"
                    f" {super_weapon} with you.")
        is_super = True
    print_delay("You walk back out to the field.")
    field_choices()


def game_over():
    again = input("Do you want to play again? (y/n)\n").lower
    if again == "y":
        play_game()
    elif again == "n":
        print_delay("Thanks for playing! See you next time.")
    else:
        game_over()


def play_game():
    intro(adventure_extension.creature, adventure_extension.item)
    field_choices()
    choice = user_input()
    if choice == "1":
        house(adventure_extension.creature, adventure_extension.item,
              adventure_extension.super_weapon, adventure_extension.is_super,
              adventure_extension.lives)
    elif choice == "2":
        cave(adventure_extension.item, adventure_extension.super_weapon,
             adventure_extension.is_super)
    else:
        print_delay("Invalid input")
        field_choices()

play_game()
