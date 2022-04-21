import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'resultmaps.neis-one.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://resultmaps.neis-one.org/osm-change-tiles',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

days = 7

response = requests.get('https://resultmaps.neis-one.org/osm-change-get-tiles?days=' + str(days) + '&bbox=-98.70443344116211,29.269394959498655,-98.34394454956056,29.577643234328875', headers=headers)

data = response.json()["features"]

# print(len(data))

users = []

comments = []

for feature in data:
    this_user = feature["properties"]["username"]

    if this_user not in users:
        users.append(this_user)

    # list_of_users = [value for user in users
    #                   for value in user.values()]

    # tile = feature["properties"]["tile"]
    # time = feature["properties"]["tmpstmp"]
    # notes = feature["properties"]["comment"]
    
    # edit = {'tile': tile, 'timestamp': time, 'comments': notes}

    # for k,v in users.items():
    #     if v == this_user:

    # else:
    #     entry = {'username': this_user, 'profile': {}, 'edits': []}
    #     entry["edits"].append(edit)
    #     users.append(entry)

        
    # print(feature["properties"]["username"] + " - " + feature["properties"]["comment"])
    comments.append(feature["properties"]["tmpstmp"] + "\n\n" + feature["properties"]["username"] + ": \n\n " + feature["properties"]["comment"])
    # comments.append(feature["properties"]["username"] + " changed the map on " + feature["properties"]["tmpstmp"] + " saying:\n\n '" + feature["properties"]["comment"] +"'")

users = sorted(users, key=lambda s: s.lower())
# comments = sorted(comments, key=lambda s: s.lower())

print("# WHOSE HANDS DRAW THE MAP?")
print(" \n\n\n\n\n\n\n ")
print("### The Last\n") 
print("# " + str(days) + '\n')
print("### Days of Edits to\n")
print("### Open Street Map\n")
print("### in\n")
print("# San Antonio\n\n\n") 
print("#### A Scrape-book by Emily Bowe \pagebreak") 

for user in users:
    profile = requests.get('https://www.openstreetmap.org/user/' + user)
    print('## ' + user)
    print('\n')
    soup = BeautifulSoup(profile.text, "html.parser")
    # stats = soup.find("span", class_="count-number").contents
    # print(stats[0])
    bio = soup.find("div", class_="content-body").div.div.text
    # print(user + '\n' + bio)
    print(bio)
    print('\n--------------\n')

print("\pagebreak")
for comment in comments:
    print(comment)
    print('\n--------------\n') 