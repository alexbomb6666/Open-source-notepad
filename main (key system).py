import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
def login(username, password):
  getreq = requests.get(url=f'https://own-key-system.alexbomb6666.repl.co/login/{username}/{password}', verify=False)
  if getreq.status_code == 200:
    print("Logged in!")
  elif getreq.status_code == 300:
    print("Invalid password!")
  elif getreq.status_code == 400:
    print("Didnt find such account!")
  

login(input("Username: "), input("Password: "))