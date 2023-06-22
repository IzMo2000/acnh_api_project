# Setup Instructions
The following libraries must be installed:
* [requests](https://pypi.org/project/requests/) - enables GET requests to ACNH API
* [pandas](https://pandas.pydata.org/docs/getting_started/install.html) - converts json dictionary to readable dataframe
* [sqlalchemy](https://pypi.org/project/SQLAlchemy/) - enables data enhine

# How to Run
Can be run on a command line using the following command while in the project directory:

```python3 acnh_api.py```

# Overview
This program searches for and displays the database of a villager from the video game
Animal Crossing: New Horizons using [ACNH API](http://acnhapi.com/).

It will prompt the user for a villager number to be entered, then display the villager's 
name along with their database. The program may be reprompted for further inputs 

