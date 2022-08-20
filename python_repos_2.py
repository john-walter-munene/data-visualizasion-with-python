from tkinter.ttk import Style
from urllib import response
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as Ls 

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

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories Returned:", len(repo_dicts))
 
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

# Visualizing repositories using pygal
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        # Add clickable links to the graphs
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)
# Male the visualizastion
my_style = Ls('#333366', base_style=LCS)

# Refined style for my pygal
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most stared python projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_2.svg')

