# A NeverLand Island Adventure game : inspired by the cartoon- Jake and the Never Land Pirates
import random

collected_coins  = 0
def intro():
    print("JAKE AND THE NEVERLAND PIRATES")
    print("""Just off the shores of Never Land, a hideaway at sea
    Yo ho, yo ho, let's go, let's go
    A pirate band outwits the plans
    Of Captain and Smee
    Yo ho, yo ho, let's go, let's go """)
    print("\nAhoy mateys! Do you wonna join my pirate crew?")
    print("Say 'Yes' to continue with the Adventure.")
    print("Type anything else to quit. :(")
    start_game = input().strip().lower()
    if start_game == "yes":
        level1()
    else:
        print("See you again next time!")
        exit()

def level1():
    print("\nLet's start today's adventure!")
    print("Yo-Ho-Ho!")
    print("Now let's become the character you want! Anything is possible on the NeverLand Island.")
    print("Choose (1) to become Jake, (2) to become Izzy, (3) to become Cubby or (4) to become Skully.")
    choice = int(input())
    character = { 1: "Jake", 2: "Izzy", 3: "Cubby", 4: "Skully"}
    if choice in character:
        print(f"Ahoy! {character[choice]}")
        level2()
    else:
        print("Please choose a valid option.")
        level1()

def level2():
    global collected_coins
    print("\nNow let's follow the map and see where it leads us.")
    map = ["CROCODILE CREEK", "NEVERPEAK MOUNTAIN", "SKULL ROCK", "CAVE OF ICE", "PIXIE HOLLOW"]
    location = random.choice(map)
    coins = random.randint(3, 11)
    print(f"\nYo-Ho! You have chosen your location for adventure and you got {coins} gold coins. Let's keep it safe for now.")
    collected_coins += coins
    print(f"Let's go to {location}.")
    print("Choose (1) if you encounter Captain Hook and (2) if you encounter the Tick-Tock the Crocodile.")
    choice = int(input())
    if choice == 1:
        captain_hook()
    elif choice == 2:
        ticktock_crocodile()
    else:
        print("Please choose a valid option.")
        level2()
 

def captain_hook():
    global collected_coins
    hook_health = 100
    print("\nCaptain Hook is again upto no good. Let's go and fight against his evil plans.")
    print("Attack with your sword until Captain Hook accepts defeat.")
    while (hook_health > 0):
        attack_temp = int(input("Enter any number to attack."))
        print("ATTACK!")
        attack = random.randint(30, 70)
        hook_health -= attack
        print(f"Captain Hook's health has decreased by {hook_health}")
        
    print("\nYo-Ho! Captain Hook accepted his defeat and is going back to his ship Jolly Rogers.")
    coins = random.randint(3, 11)
    print(f"You got {coins} gold coins. Let's keep it safe for now.")
    collected_coins += coins
    print("Choose (1) if you wish to return to the map and choose (2) to deposit all collected coins in the team's gold chest.")
    choice = int(input())
    if choice == 1:
        level2()
    elif choice == 2:
        deposit_coins()
    else:
        print("Please choose a valid option.")
        captain_hook()


def ticktock_crocodile():
    global collected_coins
    print("Tick-Tock the Crocodile seems to be in trouble. It's trapped in a net, setup by Sharky and Bones, Captain Hook's henchmen.")
    trap = 50
    print("Let's cut the net using sword until Tick-Tock is free.")
    while (trap > 0):
        cut_temp = int(input("Enter any number to cut the net."))
        print("CUT!")
        cut = random.randint(15, 30)
        trap -= cut
        print(f"Trap strength is now at {trap}")
    print("Yo-Ho! Tick-Tock the Crocodile is free.")
    coins = random.randint(3,11)
    print(f"You got {coins} gold coins. Let's keep it safe for now.")
    collected_coins += coins
    print("Choose (1) if you wish to return to map and choose (2) to deposit all collected coins in the team's gold chest.")
    choice = int(input())
    if choice == 1:
        level2()
    elif choice == 2:
        deposit_coins()
    else:
        print("Please choose a valid option.")
        ticktock_crocodile()

def deposit_coins():
    print("""Wayy Heyy Well Done Crew.""")
    print(f"Ahoy! You collected {collected_coins}. Let's keep it in the treasure box.")
    print("Thank you for helping us young pirate! Let's meet again very soon.")
    exit()
    
intro()
