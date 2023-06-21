import requests

villager_10 = requests.get("http://acnhapi.com/v1/villagers/10")

print(villager_10.json())