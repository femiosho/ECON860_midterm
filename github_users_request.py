import requests
import os

#Create a file to store the html data
if not os.path.exists("data_files"):
    os.mkdir("data_files")

headers = {
   'accept': '*/*',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
   'referer': 'https://www.google.com/',
}

# Open file to write the html data to
f = open("data_files/github_users.html", "w")

#Scrape the html data
response = requests.get("http://45.56.117.197/index.html/")

#Convert html to readable format
html = response.text
#print(html)

# Write to file
f.write(html)
f.close()

print("done")