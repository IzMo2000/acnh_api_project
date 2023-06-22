
################################################################################
# Animal Crossing Villager Name Lookup by ID
# written by Izaac Molina
# last updated 6/21/23
# this program allows villager databases from Animal Crossing: New Horizons to
# be searched from an ID number.
# uses ACNH API (v1)
################################################################################

# import necessary libraries
import requests
import pandas as pd
import sqlalchemy as db

# define global constants
MIN_VILLAGER_ID = 1
MAX_VILLAGER_ID = 391

# print program title
print('\nFind Animal Crossing Villager Database by Number ID')
print('=================================================')

# loop input until user wishes to exit
while True:

    # prompt user to input villager ID
    villager_num = int(input("\nEnter the villager number you would like to" +
                        "see the database for (1-391): "))

    # ensure villager ID is within bounds
    if villager_num >= MIN_VILLAGER_ID and villager_num <= MAX_VILLAGER_ID:

        # send GET request to ACNH API to obtain the desired villager json
        villager = requests.get("http://acnhapi.com/v1/villagers/" + 
                                                             str(villager_num))

        # convert response to usable json dictionary
        villager = villager.json()

        # upload villager dictionary into a dataframe
        villager_df = pd.DataFrame.from_dict(villager)

        # create database engine based on villager database
        engine = db.create_engine('sqlite:///villager.db')

        # convert dataframe to sql database using engine
        villager_df.to_sql('villager_table', con=engine, if_exists='replace', 
                                                                    index=False)

        # print message containing the input number and name of found villager, 
        # followed by database
        print(f'\nVillager {villager_num}: {villager["name"]["name-USen"]}.\n')
        print("Their database is as follows:\n")

        # print villager database
        with engine.connect() as connection:
            query_result = connection.execute(db.text("SELECT * \
                                              FROM villager_table;")).fetchall()
            print(pd.DataFrame(query_result))

    # ID out of bounds, print error message
    else:
        print("\nInvalid villager number, name not found")

    # get program reset input from user
    while True:

        # prompt user to ask if program should run again
        break_input = input("\nRun Program Again? (y/n): ")

        # validate input
        if break_input in ('y', 'Y', 'N', 'n'):
          break
        
        # input not valid, print error message and reprompt
        print("\nInvalid Input Detected - Try Again")

    # if user wishes to quit ('n' or 'N' was entered), end program
    if break_input in ('n', 'N'):
        break
