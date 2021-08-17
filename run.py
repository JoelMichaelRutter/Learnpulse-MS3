import gspread
from google.oauth2.service_account import Credentials
import re

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
    print("Through this program you can submit and search for"
          " staff training information\n")
    print("What would you like to do?")

    while True:
        print("\nPlease enter one of the following options to progress:")
        print('\n- Enter "input" to add trainee data to the database')
        print('- Enter "search" to search for trainee data')
        user_branch_choice = input("\nPlease input your command:\n")
        branch_choice_lower = user_branch_choice.lower()
        if branch_choice_lower == "input":
            return branch_choice_lower
        elif branch_choice_lower == "search":
            return branch_choice_lower
        else:
            print("\nYou entered an invalid command.\n"
                  "Please try again...")
            continue


# Branching function checks are completed here
def input_function_check():
    """
    This function asks the user whether they want to
    input data incase they inputted the incorrect command.
    The users input is limited to a Y/N for yes or no,
    if the user inputs something other than the above, the
    input loops and prints a command invalid message.
     - If the user enters N, the main_program_call function is called again.
     - If the user enters Y, the return is passed back to the main function
    and assessed so that the next function in the input branch of the program
    can be called.
    """
    while True:
        print("\nBased on your command, you want to input data -")
        print("Is this right?")
        print("\nPlease enter one of the following commands to progress:")
        print('\n- Enter "Y" for yes')
        print('- Enter "N" for no\n')
        branch_input_check = input("Please enter your command:\n")
        input_check_upper = branch_input_check.upper()
        if input_check_upper == "Y":
            return input_check_upper
        if input_check_upper == "N":
            print("\nBacking up to the start of the application.\n")
            return main_program_call()
        else:
            print("\nThat command was invalid, please try again...")
            continue


def search_function_check():
    """
    This function asks the user whether or not they would like
    to proceed with the data search functionality of the program.
    It allows the user to get out of the functionality if their previous
    input was accidentally incorrect.
    The users input is limited to a Y/N for yes or no,
    if the user inputs something other than the above, the
    input loops and prints a command invalid message.
     - If the user enters N, the main_program_call function is called again.
     - If the user enters Y, the return is passed back to the main function
    and assessed so that the next function in the search branch of the program
    can be called.
    """
    while True:
        print("\nBased on your command, you want to search for trainee data -")
        print("Is this right?")
        print("\nPlease enter one of the following commands to progress:")
        print('\n- Enter "Y" for yes')
        print('- Enter "N" for no\n')
        branch_search_check = input("Please enter your command:\n")
        search_check_upper = branch_search_check.upper()
        if search_check_upper == "Y":
            return search_check_upper
        if search_check_upper == "N":
            print("\nBacking up to the start of the application.\n")
            return main_program_call()
        else:
            print("\nThat command was invalid, please try again...")
            continue


# Data input functionality begins here
def collect_trainee_personell_data():
    """
    This function collects and validates trainee data by asking for
    user input whilst at the same time loops the inputs and provides
    guidance if the user inputs invalid data.
    """
    print("\nLEARNPULSE DATA INPUT FUNCTION RUNNING....")
    trainee_personell_data_row = []
    """ - FULL NAME:
    - This input asks the user for their full name.
    - The block is contained in a while loop to loop if invalid data is
    provided.
    - If valid alpha data only is provided, the loop breaks and the input
    from user is appended to the trainee_personell_data_row list.
    CODE REFERENCE - I used a reg ex from the answers on this
    stack overflow thread:
    https://bit.ly/2VIyBJU
    """
    while True:
        print("You must only use alphabetical characters (a-z & A-Z)\n"
              "when inputting a trainee's name.\n")
        full_name = input("Enter the trainee's full name:\n")
        if re.match("^[a-z A-Z]*$", full_name):
            trainee_personell_data_row.append(full_name)
            print("Input successfull, thank you...")
            break
        else:
            print("\nSorry, that data was invalid, please try again...")
            continue

    """ - EMPLOYEE NUMBER:
    - This input requests a five digit number from the user
    - The block is looped if invalid data is provided.
    - If valid data is provided, loop is broken and data is
    appended to trainee_data_row list.
    """
    while True:
        emp_number = input("\nEnter the trainee's 5 digit employee number:\n")
        if emp_number.isdigit() and len(emp_number) == 5:
            print("Employee number accepted, thank you...")
            trainee_personell_data_row.append(emp_number)
            break
        else:
            print(f"You entered {emp_number}, you must enter five digits""\n")
            continue

    """ - TEAM ASSIGNMENT:
    - This code block asks for the user to input a command to
    asign the trainee to a team.
    - Based on the command inputted, the trainee_team variable is
    assigned a value of 'Team One' or Team 2"
    - If valid command is entered, variable value is appended to trainee_
    data_row list and while loop is broken.
    - Error and guidance printed to user if invalid command is entered.
    """
    while True:
        print("\nTo select the trainee's team, issue a following command:")
        print('\n- Enter "1" to assign the trainee to Team 1')
        print('- Enter "2" to assign the trainee to Team 2')
        trainee_team = int(input("\nPlease issue a team"
                                 " assignment command:\n"))
        if trainee_team == 1:
            trainee_team = "Team 1"
            trainee_personell_data_row.append(trainee_team)
            print("\nTeam assignment successful, thank you.")
            break
        elif trainee_team == 2:
            trainee_team = "Team 2"
            trainee_personell_data_row.append(trainee_team)
            print("\nTeam assignment successful, thank you.")
            break
        else:
            print(f"You entered {trainee_team}, which is an invalid command.")
            print("Please try again....\n")
    return trainee_personell_data_row


def collect_trainee_training_dates(module):
    """
    This function is a refactored version of the large
    function I created to obtain trainee data. It
    collects the date that the trainee sat the module
    passed in via the module parameter each time the function is
    called. It asks the user for input and verifies that the
    input is formatted in DD/MM/YYYY format using Regular Expressions.
    - If correct data inputted, function returns the value to main.
    - If incorrect data inputted, loop continues until the data is correct.
    CODE ACKNOWLEDGEMENT FOR REG EX -
    https://blog.softhints.com/python-regex-match-date/#regexmatchingdate10102015
    """
    while True:
        print("\nEnter the date that the trainee sat their"
              f" {module} Module")
        print("The date must be formatted DD/MM/YYYY\n")
        mod_date = input("Please enter the date:\n")
        date = re.findall(r"[\d]{2}/[\d]{2}/[\d]{4}", mod_date)
        if date:
            print("\n"f'{mod_date} is a valid input, thank you...')
            return mod_date
        else:
            print('Your input was formatted incorrectly')
            print(f"You entered {mod_date}, follow DD/MM/YYYY format.")
            continue


def collect_assessment_scores(ass_name, ass_score_total):
    """
    This function collects the users assessment scores.
    The function takes two arguments:
    - ass_name: This takes the assessment name that must be entered
    when the function is called.
    - ass_score_total - This takes the assessment total score and
    is again entered as an argument when the function is called.
    This allows for the scope for this function to be universal
    """
    while True:
        print("\nPlease input the trainee's"
              f" {ass_name} assessment score")
        print(f"This assessment is out of {ass_score_total}")
        ass_score = input(f"Enter the trainee's {ass_name}"
                          " assessment score:\n")
        ass_score = int(ass_score)
        if ass_score <= int(ass_score_total):
            print("Input successful")
            print(f"The trainee scored {ass_score}/{ass_score_total}")
            return ass_score
        else:
            print(f"Sorry, you entered {ass_score}, that data was invalid.")
            print("You must input a digit value that is greater than"
                  f" or equal too {ass_score_total} ")
            continue


def update_training_register(comp_data_row):
    """
    This function is passed the completed trainee data row
    for insertion into the training register. Prior to insertion,
    the data is displayed to the user to be checked and the user
    is asked for a command to continue. The code from the command
    request is duplicated from the input_check function.
    """
    while True:
        print("\n\nData collection complete, all inputs valid...")
        print("Displaying data for review....\n")
        print(f"Trainee Name: {comp_data_row[0]}")
        print(f"Employee Number: {comp_data_row[1]}")
        print(f"Assigned Team: {comp_data_row[2]}")
        print("\n"f"Introduction Module Completed: {comp_data_row[3]}")
        print(f"Health & Safety Module Completed: {comp_data_row[4]}")
        print(f"Policy Adherence Module Completed: {comp_data_row[5]}")
        print(f"Regulatory Module Completed: {comp_data_row[6]}")
        print(f"Regulatory Assessment Score: {comp_data_row[7]}/33")
        print("\nWould you like to insert the above data into the register:")
        print('\n- Enter "Y" for yes')
        print('- Enter "N" for no\n')
        update_register = input("Please enter your command:\n")
        update_register_upper = update_register.upper()
        if update_register_upper == "Y":
            print("\nSkynet activating........ Just kidding ;D.\n")
            print("Updating Learnpulse Training Register.....")
            register = SHEET.worksheet("register")
            register.append_row(comp_data_row)
            print("Learnpulse Training Register updated successfully...")
            print("Exit function running...")
            break
        elif update_register_upper == "N":
            print("It's not like I was made for this! Restarting....")
            main_program_call()
        else:
            print("\nThat command was invalid, please try again...")
            continue


# Search functionality begins here.
def search_function():
    """
    This function runs once the user answers "Y" to the
    search_function_check question.
    Guidance is provided to user as to what they need to do
    and an input for a trainee name is provided.
    There is a try/except block:
     - In the try block, the register is parsed for the text
    content of the search variable and if a row with that text content
    exists, try block will execute the row from the spreadsheet will be
    assigned to the data_exists variable and returned to the main function.
     - If the data does not exist or if there is a typo from the user, the
    except block will execute and the user can either search again or exit
    the program.
    CODE REFERENCE - I found advice on the code to implement in the search
    function from this stack overflow thread:
    https://bit.ly/2VMS4cc
    """
    print("\nLEARNPULSE DATA SEARCH FUNCTION RUNNING....\n")
    print("This function will search the training"
          " register and return a learning report\n")
    print("Please note: should you mis-spell the trainee's name\n"
          "or if the trainee does not exist, you will receive an error.")
    search = input("\nPlease enter the name of the trainee you wish"
                   " to search for:\n")
    try:
        data_exists = training.row_values(training.find(search).row)
        return data_exists
    except gspread.exceptions.GSpreadException:
        while True:
            print("\nSorry, you have searched incorrectly or data for the\n"
                  "specified trainee does not yet exist")
            print("\nWould you like to search again or exit the program?")
            print("Please enter one of the following commands:")
            print('\n- Enter "S" to search again')
            print('- Enter "E" to exit the program')
            data_error_cont = input("\nPlease enter your command:\n")
            data_error_cont_upper = data_error_cont.upper()
            if data_error_cont_upper == "S":
                search_function()
            elif data_error_cont_upper == "E":
                print("Exiting the program, goodbye for now!")
                break
            else:
                print("That command was invalid, please try again...")
                continue


def display_searched_data(found_row):
    """
    This function receives the list from returned from the
    search_function where a match has been found in the
    register google sheet and displays the training data for
    the trainee the user searched for.
    """
    print("\nTrainee located, displaying learning report:\n")
    print(f"Trainee Name: {found_row[0]}")
    print(f"Employee Number: {found_row[1]}")
    print(f"Assigned Team: {found_row[2]}")
    print("\n"f"Introduction Module Completed: {found_row[3]}")
    print(f"Health & Safety Module Completed: {found_row[4]}")
    print(f"Policy Adherence Module Completed: {found_row[5]}")
    print(f"Regulatory Module Completed: {found_row[6]}")
    print(f"Regulatory Assessment Score: {found_row[7]}/33")
    print("\nThank you for using Learnpulse.")
    while True:
        print("Would you like to search for another trainee or exit?")
        print("\nEnter one of the following commands to proceed:")
        print('\n- Enter "S" to search again')
        print('- Enter "E" to exit the program')
        search_again = input("\nPlease enter your command:\n")
        search_again_upper = search_again.upper()
        if search_again_upper == "S":
            return search_again_upper
        elif search_again_upper == "E":
            return search_again_upper
        else:
            print("That command was invalid, please try again...")
            continue


def main_program_call():
    """
    This function is the main function in the program through which
    all other functions are called.
    """
    branching_variable = welcome_function()
    if branching_variable == "input":
        input_check_proceed = input_function_check()
        if input_check_proceed == "Y":
            trainee_data_row = collect_trainee_personell_data()
            intro_mod_date = collect_trainee_training_dates("Introduction")
            trainee_data_row.append(intro_mod_date)
            hs_mod_date = collect_trainee_training_dates("Health & Safety")
            trainee_data_row.append(hs_mod_date)
            pam_mod_date = collect_trainee_training_dates("Policy Adherence")
            trainee_data_row.append(pam_mod_date)
            reg_mod_date = collect_trainee_training_dates("Regulatory")
            trainee_data_row.append(reg_mod_date)
            reg_ass_score = collect_assessment_scores("Regulatory", "33")
            trainee_data_row.append(reg_ass_score)
            update_training_register(trainee_data_row)
    else:
        search_check_proceed = search_function_check()
        if search_check_proceed == "Y":
            existing_trainee_data = search_function()
            search_loop = display_searched_data(existing_trainee_data)
            while True:
                if search_loop or existing_trainee_data == "S":
                    existing_trainee_data = search_function()
                    search_loop = display_searched_data(existing_trainee_data)
                    continue
                else:
                    print("Exiting the program, goodbye for now!")
                    break


main_program_call()
