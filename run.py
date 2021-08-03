import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Learnpulse-Training-Register")

training = SHEET.worksheet('register')


def welcome_function():
    """
    This function is the welcome function, it is called
    first in the main_program_call function. The function
    prints a welcome message and instructions to the user.
    """
    print("WELCOME TO LEARNPULSE")
    print("Through this program you can submit and search for \n"
          "staff training information")
    print("\n")
    print("What would you like to do?")

    while True:
        print("\n")
        print("Please enter one of the following options to progress:")
        print('\n- Enter "input" to add trainee data to the database')
        print('- Enter "search" to search for trainee data')
        user_branch_choice = input("\nPlease input your command: ")
        if user_branch_choice == "input":
            return user_branch_choice
        elif user_branch_choice == "search":
            return user_branch_choice
        else:
            print("\nYou entered an invalid command.\n"
                  "Please try again...")
            continue


def input_function_check():
    """
    This function asks the user whether they want to
    input data incase they inputted the incorrect command.
    The users input is limited to a Y/N for yes or no,
    if the user inputs something other than the above, the
    input loops and prints a command invalid message.
    If the user enters N, the main_program_call function is called again.
    If the user enters Y, the return is passed back to the main function
    and assessed so that the next function in the input branch of the program
    can be called.
    """
    while True:
        print("\n")
        print("Based on your command, you want to input data -")
        print("Is this right?")
        print("\nPlease enter one of the following commands to progress:")
        print('\n- Enter "Y" for yes')
        print('- Enter "N" for no\n')
        branch_input_check = input("Please enter your command: ")
        print("")
        if branch_input_check == "Y":
            return branch_input_check
        if branch_input_check == "N":
            print("\nBacking up to the start of the application.\n")
            return main_program_call()
        else:
            print("\nThat command was invalid, please try again...")
            continue


def search_function_check():
    print("Search function calling...")


def collect_trainee_data():
    """
    This function collects and validates trainee data by asking for
    user input whilst at the same time loops the inputs and provides
    guidance if the user inputs invalid data.
    """
    print("LEARNPULSE DATA INPUT FUNCTION RUNNING....")
    trainee_data_row = []
    """ - FULL NAME
    - This input asks the user for their full name.
    - The block is contained in a while loop to loop if invalid data
    - If valid alpha data only is provided, the loop breaks and the input
    from user is appended to the trainee_data_row list.
    """
    while True:
        full_name = input("Enter the trainee's full name (alpha chars only): ")
        n = full_name
        if (n >= "a" and n <= "z") or (n >= "A" and n <= "Z"):
            trainee_data_row.append(n)
            print("Input successfull, thank you...")
            break
        else:
            print("Sorry, that data was invalid, please try again...")
            continue

    """ - EMPLOYEE NUMBER
    - This input requests a five digit number from the user
    - The block is looped if invalid data is provided.
    - If valid data is provided, loop is broken and data is
    appended to trainee_data_row list.
    """
    while True:
        emp_number = input("\nEnter the trainee's 5 digit employee number: ")
        if emp_number.isdigit() and len(emp_number) == 5:
            print("Employee number accepted, thank you...")
            trainee_data_row.append(emp_number)
            break
        else:
            print(f"You entered {emp_number}, you must enter five digits""\n")
            continue

    print("\nTo select the trainee's team, issue a following command:")
    print('\n- Enter "1" to assign the trainee to Team 1')
    print('- Enter "2" to assign the trainee to Team 2')
    trainee_team = int(input("\nPlease issue a team assignment command: "))
    if trainee_team == 1:
        trainee_team = "Team 1"
    elif trainee_team == 2:
        trainee_team = "Team 2"
    trainee_data_row.append(trainee_team)
    print(trainee_data_row)


def validate_user_input():
    print("This is the validation function")


def main_program_call():
    """
    This function is the main function in the program through which
    all other functions are called.
    """
    branching_variable = welcome_function()
    if branching_variable == "input":
        input_check_proceed = input_function_check()
        if input_check_proceed == "Y":
            collect_trainee_data()
    else:
        search_function_check()


main_program_call()
