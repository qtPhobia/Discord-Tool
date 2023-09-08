import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    ascii_art = """
 @@@@@@@  @@@  @@@  @@@@@@  @@@@@@@  @@@  @@@@@@   @@@@@@@
 @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@ @@! @@!  @@@ !@@     
 @!@@!@!  @!@!@!@! @!@  !@! @!@!@!@  !!@ @!@!@!@! !@!     
 !!:      !!:  !!! !!:  !!! !!:  !!! !!: !!:  !!! :!!     
  :        :   : :  : :. :  :: : ::  :    :   : :  :: :: :
"""
    print(ascii_art)

def tools_menu():
    clear_screen()
    print("\nTools Menu:")
    print("1. Tool 1")
    print("2. Tool 2")
    print("3. Back to Main Menu")

def main_menu():
    clear_screen()
    print_ascii_art()
    print("\nMain Menu:")
    print("1. Tools")
    print("2. Settings")
    print("3. Exit")

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            tools_menu()
            choice = input("Enter your tool choice (or '3' to go back to the Main Menu): ")

            if choice == "1":
                print("You selected Tool 1.")
                # Add Tool 1 functionality here
            elif choice == "2":
                print("You selected Tool 2.")
                # Add Tool 2 functionality here
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please select a valid option.")
    elif choice == "2":
        print("You selected Settings.")
        # Add your Settings functionality here
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        