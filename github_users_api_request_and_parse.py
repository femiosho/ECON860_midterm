import requests
import json
import pandas


df = pandas.DataFrame(columns=['User ID', 'Avatar URL', 'URL', 'Number of Followers',
	'Following', 'Public Repository Count', 'Starred URL', 'Full Name', 
	'Company', 'Blog', 'Location', 'Email', 'Hireable', 'Bio', 
	'Starting Time', 'Last Update Time'])

# Assign personal access token file name to a variable
file_name = "data_files/pat.csv"

# Open and read from personal access token file
f =  open(file_name, "r")
pat = f.read()
f.close()

# Request session using user name and personal access token
github_session = requests.Session()
github_session.auth = ( "femiosho", pat)

# Open and read from parsed data file
user_data = pandas.read_csv("data_files/github_users_dataset.csv")

# Select the user ID column
user_ID_column = user_data['Login ID']

for i in user_ID_column.index:
	user_ID = user_ID_column[user_ID_column.index[i]]
	response_text = github_session.get("https://api.github.com/users/" + user_ID)
	response_text = response_text.text
	json_text = json.loads(response_text)

	try:
		avatar_url = json_text['avatar_url']
		url = json_text['url']
		follower_count = int(json_text['followers'])
		following_count = int(json_text['following'])
		public_repos = int(json_text['public_repos'])
		starred_url = json_text['starred_url'] 
		full_name = json_text['name'] 
		company = json_text['company'] 
		blog = json_text['blog'] 
		location = json_text['location'] 
		email = json_text['email']
		hireable = json_text['hireable']
		bio = json_text['bio']
		starting_time = json_text['created_at'] 
		last_update_time = json_text['updated_at']

		temp = pandas.DataFrame({"User ID": [user_ID], "Avatar URL": [avatar_url],
				"URL": [url], "Number of Followers": [follower_count],
				"Following": [following_count], "Public Repository Count": [public_repos],
				"Starred URL": [starred_url], "Full Name": [full_name],
				"Company": [company], "Blog": [blog],
				"Location": [location], "Email": [email], 
				"Hireable": [hireable], "Bio": [bio],
				"Starting Time": [starting_time], "Last Update Time": [last_update_time]})
		
		df = pandas.concat([df, temp], ignore_index=True)

	except:
		print("Error obtaining user information")

df.to_csv("data_files/github_users_api_dataset.csv", index=False)