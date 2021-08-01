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
# def input_data_to_register():

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
    print("Please enter one of the following options to progress:")
    print('- Enter "input" to add trainee data to the database')
    print('- Enter "search" to search for trainee data')

def program_branch():

def main_program_call():
    """
    This function is the main function in the program through which
    all other functions are called.
    """
    welcome_function()


main_program_call()