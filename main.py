import requests
import time

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"
    
    def findUser(self, username):
        response = requests.get(self.api_url+"/users/"+username)
        return response.json()
    
    def getRepos(self, username):
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()

github = Github()

while True:
    
    choice = input("1-Find User\n2-Get Repositories\n3-Exit\nChoice: ")
    
    if choice == "1":
        username = input("Username: ")
        result = github.findUser(username)
        print("-"*30)
        print(f"name: {result['name']}\nrepos: {result['public_repos']}\nfollowers: {result['followers']}\nemail: {result['email']}")
        print("-"*30)
    elif choice == "2":
        username = input("Username: ")
        result = github.getRepos(username)
        print("-"*30)
        for repo in result:
            print(repo["name"])
        print("-"*30)
    elif choice == "3":
        print("Exiting...")
        time.sleep(2)
        break
    else:
        print("Error!Choose again.")
        continue
    
