from urllib import response
import requests

# Make an API request and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)

# Store the API response in a variable.
response_dict = r.json()

# Process the results.
print(response_dict.keys())

# Working with the response in a dictionary.
print("Total Repositories:", response_dict['total_count'] )

# Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories Returned:", len(repo_dicts) )

# Examining the first repository.
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
    
# Pulling out some values for some of the keys in trhe first repository.
print("\nSelected information is for the first Repository: ")
print('Name: ', repo_dict['name'].title())
print('Owner: ', repo_dict['owner']['login'])
print('Stars: ', repo_dict['stargazers_count'])
print('Repository: ', repo_dict['html_url'])
print('Created: ', repo_dict['created_at'])
print('Updated: ', repo_dict['updated_at'])
print('Description: ', repo_dict['description'])

# Summarizing the top Repositories
print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

