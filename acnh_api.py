###############################################################################
# Animal Crossing Villager Name Lookup by ID
# written by Izaac Molina
# last updated 6/21/23
# this program allows villager databases from Animal Crossing: New Horizons to
# be searched from an ID number.
# uses ACNH API (v1)
###############################################################################

# import necessary libraries
import requests
import pandas as pd
import sqlalchemy as db

# define global constants
MIN_VILLAGER_ID = 1
MAX_VILLAGER_ID = 391


# Title: fetch_villager_dict
# Description: uses GET request to obtain villager based on given id, returns
#              result as json dictionary
# Input: villager id number (int)
# Output / Display: None
# Output / Returned: villager json (dict)
def fetch_villager_dict(id_number: int) -> dict:

    # send GET request to ACNH API to obtain the desired villager
    villager = requests.get("http://acnhapi.com/v1/villagers/" +
                            str(id_number))

    # convert response to usable json dictionary, return result
    return villager.json()


# Title: json_to_sql
# Description: converts json dictionary to SQL database, returns created engine
# Input: villager json data (dict)
# Output / Display: None
# Output / Returned: engine used to create database
def json_to_sql(input_json: dict):

    # upload villager dictionary into a dataframe
    villager_df = pd.DataFrame.from_dict(input_json)

    # create database engine based on villager database
    engine = db.create_engine('sqlite:///villager.db')

    # convert dataframe to sql database using engine
    villager_df.to_sql('villager_table', con=engine, if_exists='replace',
                       index=False)

    # return database conversion engine
    return engine


# Title: print_villager_database
# Description: prints villager database from given database engine
# Input: None
# Output / Display: displays database as specified
# Output / Returned: None
def print_villager_database(engine) -> None:

    # print villager database using connect method
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM \
                                          villager_table;")).fetchall()
        print(pd.DataFrame(query_result))


# Title: print_title
# Description: prints program title
# Input: None
# Output / Display: displays title as specified
# Output / Returned: None
def print_title() -> None:

    # print program title
    print('\nFind Animal Crossing Villager Database by Number ID')
    print('=================================================')


# Title: prompt_for_id
# Description: prompts user for villager ID, validates input
# Input: None
# Output / Display: displays prompt and possible error message
# Output / Returned: villager id number (int)
def prompt_for_id() -> int:

    # loop while input is invalid
    while True:

        # prompt user to input villager ID
        villager_num = input("\nEnter the villager number you would like to" +
                             "see the database for (1-391): ")

        # ensure valid type entered
        if not villager_num.isdigit():
            print("\nERROR: invalid input type, try again:")

        # ensure villager ID is within bounds, print error if bounds are broken
        elif (int(villager_num) < MIN_VILLAGER_ID or
              int(villager_num) > MAX_VILLAGER_ID):

            print("\nERROR: input out of bounds, try again:")

        # conditions are met, break from input loop by returning id
        else:
            return int(villager_num)


# Title: rerun
# Description: prompts user for option to rerun program, validates and
#              returns input
# Input: None
# Output / Display: displays prompt and possible error message(s)
# Output / Returned: result indicating whether user would like to rerun (bool)
def rerun() -> bool:

    # get program reset input from user
    while True:

        # prompt user to ask if program should run again
        break_input = input("\nRun Program Again? (y/n): ")

        # validate input
        if not (isinstance(break_input, str) or
                break_input in ('y', 'Y', 'N', 'n')):

            break

        # input not valid, print error message and reprompt
        print("\nInvalid Input Detected - Try Again")

    # check for user's input
    if (break_input == 'y' or break_input == 'Y'):
        return True

    # user doesn't want to rerun, return false
    return False


# print title
print_title()

# loop input until user wishes to exit
while True:

    # prompt user to input villager ID
    villager_num = prompt_for_id()

    # get json dictionary of villager data
    villager = fetch_villager_dict(villager_num)

    # convert villager data to sql database, store engine in variable
    engine = json_to_sql(villager)

    # print message containing the input number and name of found villager
    print(f'\nVillager {villager_num}: {villager["name"]["name-USen"]}.\n')
    print("Their database is as follows:\n")

    # display corresponding villager database
    print_villager_database(engine)

    # if user wishes, end program, else, continue
    if not rerun():
        break
