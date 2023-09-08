import os
import socket
import requests

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print text in aqua color
def print_aqua(text):
    aqua = "\033[96m"  # ANSI escape code for aqua color
    reset_color = "\033[0m"  # Reset color to default

    print(f"{aqua}{text}{reset_color}")

# Function to print ASCII art in aqua color
def print_ascii_art():
    aqua = "\033[96m"  # ANSI escape code for aqua color
    reset_color = "\033[0m"  # Reset color to default

    ascii_art = f"""
{aqua} @@@@@@@  @@@  @@@  @@@@@@  @@@@@@@  @@@  @@@@@@   @@@@@@@
 @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@ @@! @@!  @@@ !@@
 @!@@!@!  @!@!@!@! @!@  !@! @!@!@!@  !!@ @!@!@!@! !@!
 !!:      !!:  !!! !!:  !!! !!:  !!! !!: !!:  !!! :!!
  :        :   : :  : :. :  :: : ::  :    :   : :  :: :: :
{reset_color}
"""

    print(ascii_art)

# Function to perform IP Lookup with additional geolocation
def ip_lookup():
    print_aqua("IP Lookup:")

    # Get user input for IP address or domain name
    print("\033[96m", end="")  # Set aqua color
    target = input("Enter an IP address or domain name: ")
    print("\033[0m", end="")  # Reset color to default

    try:
        # Perform the IP lookup
        ip_address = socket.gethostbyname(target)
        print_aqua(f"IP address for {target}: {ip_address}")

        # Use ipinfo.io API to gather geolocation data
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()

        print_aqua(f"City: {data.get('city', 'N/A')}")
        print_aqua(f"Region: {data.get('region', 'N/A')}")
        print_aqua(f"Country: {data.get('country', 'N/A')}")
        print_aqua(f"Location: {data.get('loc', 'N/A')}")
        print_aqua(f"Organization: {data.get('org', 'N/A')}")

        print("\033[96m", end="")  # Set aqua color
        input("Press Enter to continue...")
        print("\033[0m", end="")
    except KeyboardInterrupt:  # Handle Ctrl+C gracefully
        print_aqua("IP Lookup canceled.")
    except socket.gaierror:
        print_aqua(f"Could not resolve the host: {target}")
        print("\033[96m", end="")
        input("Press Enter to continue...")
        print("\033[0m", end="")
    except requests.exceptions.RequestException as e:
        print_aqua(f"An error occurred during geolocation lookup: {e}")
        print("\033[96m", end="")
        input("Press Enter to continue...")
        print("\033[0m", end="")
    except Exception as e:
        print_aqua(f"An error occurred: {e}")
        print("\033[96m", end="")
        input("Press Enter to continue...")
        print("\033[0m", end="")

# Function for the Tools menu
def tools_menu():
    while True:
        clear_screen()
        print_ascii_art()
        print_aqua("\nTools Menu:")
        print_aqua("1. IP Lookup")
        print_aqua("2. Tool 2")
        print_aqua("3. Back to Main Menu")
        print("\033[96m", end="")  # Set aqua color
        choice = input("Enter your tool choice (or '3' to go back to the Main Menu): ")
        print("\033[0m", end="")  # Reset color to default

        if choice == "1":
            ip_lookup()  # Call the IP Lookup function
        elif choice == "2":
            print_aqua("You selected Tool 2.")
            # Add Tool 2 functionality here
        elif choice == "3":
            break
        else:
            print_aqua("Invalid choice. Please select a valid option.")

# Main menu
def main_menu():
    while True:
        clear_screen()
        print_ascii_art()
        print_aqua("\nMain Menu:")
        print_aqua("1. Tools")
        print_aqua("2. Settings")
        print_aqua("3. Exit")
        print("\033[96m", end="")  # Set aqua color
        choice = input("Enter your choice: ")
        print("\033[0m", end="")  # Reset color to default

        if choice == "1":
            tools_menu()  # Call the Tools menu
        elif choice == "2":
            print_aqua("You selected Settings.")
            # Add your Settings functionality here
        elif choice == "3":
            print_aqua("Exiting program. Goodbye!")
            break
        else:
            print_aqua("Invalid choice. Please select a valid option.")

# Run the main menu
main_menu()
