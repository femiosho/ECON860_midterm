
# Import libraries
import pandas
import numpy
import matplotlib.pyplot as plt

# Read dataset
dataset = pandas.read_csv("data_files/github_users_api_dataset.csv")

# Present a summary of numerical data
# print(dataset.describe())


sub_dataset = dataset[(dataset['Number of Followers']>0) & (dataset['Following']>0) &
(dataset['Public Repository Count']>0)]

followers = sub_dataset['Number of Followers']
following = sub_dataset['Following']
public_repo = sub_dataset['Public Repository Count']

logfollowers = numpy.log(followers)
logfollowing = numpy.log(following)
logpublic_repo = numpy.log(public_repo)

# Plot
plt.scatter(logfollowing, logfollowers)
plt.title("Following Count and Followers Count")
plt.xlabel("Number of Following")
plt.ylabel("Number of Followers")
plt.savefig('data_files/figure1.png')

plt.scatter(logpublic_repo, logfollowers)
plt.title("Number of Repositories and Followers Count")
plt.xlabel("Number of Repositories")
plt.ylabel("Number of Followers")
plt.savefig('data_files/figure2.png')