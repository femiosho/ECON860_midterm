
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
plt.title("Followers vs Following and Repositories")
plt.ylabel("Followers")

plt.scatter(logfollowing, logfollowers, color = "green", marker = "o", label = "Following")
plt.scatter(logpublic_repo, logfollowers, color = "blue", marker = "o", label = "No. of repositories")
plt.legend()
plt.savefig('data_files/figure.png')
