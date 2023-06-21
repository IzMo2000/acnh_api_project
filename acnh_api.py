
###############################################################################################
# Animal Crossing Villager Name Lookup by ID
# written by Izaac Molina
# last updated 6/21/23
# this program allows villager names from Animal Crossing: New Horizons to be searched based on
# an ID number.
# uses ACNH API (v1)
###############################################################################################

# import req
import requests

# define global constants
MIN_VILLAGER_ID = 1
MAX_VILLAGER_ID = 391


# print program title
print('\nFind Animal Crossing Villager Name by Number ID')
print('=================================================')

# loop input until user wishes to exit
while True:

  # prompt user to input villager ID
  villager_num = int(input("\nEnter the villager number you would like to see the name for (1-391): "))

  # ensure villager ID is within bounds
  if villager_num >= MIN_VILLAGER_ID and villager_num <= MAX_VILLAGER_ID:

    # send GET request to ACNH API to obtain the desired villagr json
    villager = requests.get("http://acnhapi.com/v1/villagers/" + str(villager_num))

    # print message containing the input number and name of found villager
    print(f'\nVillager {villager_num} is named {villager.json()["name"]["name-USen"]}.\n')
  
  # ID out of bounds, print error message
  else:
    print("\nInvalid villager number, name not found\n")
  
  # get program reset input from user
  while True:

    # prompt user to ask if program should run again
    break_input = input("Run Program Again? (y/n): ")

    # validate input
    if break_input in ('y', 'Y', 'N', 'n'):
      break
    
    # input not valid, print error message and reprompt
    print("\nInvalid Input Detected - Try Again")
  
  # if user wishes to quit ('n' or 'N' was entered), end program
  if break_input in ('n', 'N'):
    break




