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
        print('- Enter "input" to add trainee data to the database')
        print('- Enter "search" to search for trainee data')
        user_branch_choice = input("Please input your command: ")
        if user_branch_choice == "input":
            return user_branch_choice
        elif user_branch_choice == "search":
            return user_branch_choice
        else:
            print("\nYou entered an invalid command.\n"
                  "Please try again...")
            continue


def input_function_check():
    while True:
        print("\n")
        print("Based on your command, you want to input data -")
        print("Is this right?")
        print("Please enter one of the following commands to progress:")
        print('- Enter "Y" for yes')
        print('- Enter "N" for no\n')
        branch_input_check = input("Please enter your command: ")
        if branch_input_check == "Y":
            return branch_input_check
        if branch_input_check == "N":
            print("Taking you back, hold on...")
            return welcome_function()
        else:
            print("\nThat command was invalid, please try again...")
            continue


def search_function_check():
    print("Search function calling...")


def input_data_to_register():
    print("FIRST INPUT")


def main_program_call():
    """
    This function is the main function in the program through which
    all other functions are called.
    """
    branching_variable = welcome_function()
    if branching_variable == "input":
        input_check_proceed = input_function_check()
        if input_check_proceed == "Y":
            input_data_to_register()
    else:
        search_function_check()


main_program_call()
