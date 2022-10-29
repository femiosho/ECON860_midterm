import pandas
from bs4 import BeautifulSoup

import os
import re

# Function to remove all punctuations
def cleantext(text):
    for letters in text:
        if letters in """  [] ! . , " " ! —@ ; ' : # $ % ^ & * () + / ? """:
            text = text.replace(letters, " ")
    return text

# Create data columns
df = pandas.DataFrame(columns=['Login ID', 'Repo Count', 
	'Follower Count', 'Member Since'])

# Open file
file_name = "data_files/github_users.html"
f =  open(file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

# Find blocks of html containing required information
users_list = soup.find("div", {"class": "text-gray-700 text-sm"})
users_row_list = users_list.find_all("div", {"class": "grid grid-cols-4 gap-4"})

for users_row in users_row_list:
	# Get login ID details
	user_ID = users_row.find("div", {"class": "userid"})
	if not user_ID is None:
		user_ID = user_ID.text
		user_ID = cleantext(user_ID)
		user_ID = user_ID.strip()
		#user_ID = user_ID.replace(" ", "")
	
	# Get repo count
	repo_count = users_row.find("div", {"class": "repocount"})
	if not repo_count is None:
		repo_count = repo_count.text
		repo_count = cleantext(repo_count)
		repo_count = repo_count.strip()
		
	# Get follower count
	follower = users_row.find("div", {"class": "followercount"})
	if not follower is None:
		follower = follower.text
		follower = cleantext(follower)
		follower = follower.strip()
		
	# Get date of membership
	member = users_row.find("div", {"class": "membersince"})
	if not member is None:
		member = member.text
		member = cleantext(member)
		member = member.strip()
	
	temp = pandas.DataFrame({"Login ID": [user_ID],
		"Repo Count": [repo_count],
		"Follower Count": [follower],
		"Member Since": [member]})
	
	# Concatenate current information to df
	df = pandas.concat([df, temp], ignore_index=True)

# Drop the first row because it is empty
df = df.drop([0])

# Drop duplicate rows
df = df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=True)

# Drop invalid login IDs (with member since date of 0000-00-00)
df.drop(df.loc[df['Member Since']=='0000-00-00'].index, inplace=True)

# Reset the index to start from 0
df = df.reset_index(drop=True)

# Store the data in a csv file
df.to_csv("data_files/github_users_dataset.csv", index=False)

print("done")