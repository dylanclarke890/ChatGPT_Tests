import time

def game_start():
    print("You wake up in a dark room. You have no idea how you got there.")
    time.sleep(1)
    print("There are three doors in front of you.")
    time.sleep(1)
    print("Which one do you choose?")

    choice = input("Type 1, 2, or 3 and press Enter: ")
    if choice == "1":
        door_1()
    elif choice == "2":
        door_2()
    elif choice == "3":
        door_3()
    else:
        print("Invalid input. Please try again.")
        game_start()

def door_1():
    print("You open the door and enter a room filled with treasure.")
    time.sleep(1)
    print("Congratulations, you win!")

def door_2():
    print("You open the door and fall into a pit of snakes.")
    time.sleep(1)
    print("Game over.")

def door_3():
    print("You open the door and find yourself in a room with two doors.")
    time.sleep(1)
    print("Which one do you choose?")

    choice = input("Type 1 or 2 and press Enter: ")
    if choice == "1":
        door_1()
    elif choice == "2":
        door_2()
    else:
        print("Invalid input. Please try again.")
        door_3()

game_start()
