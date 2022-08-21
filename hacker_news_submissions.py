from urllib import response
import requests

from operator import itemgetter

# Make an API call and store the respnses.

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code: ", r.status_code)

# Process information about each submission.
subsmission_ids = r.json()
subsmission_dicts = []
for submission_id in subsmission_ids[:30]:
    # Make a separate APi call for each submission.
    url =  ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    subsmission_r = requests.get(url)
    print(subsmission_r.status_code)
    response_dict = subsmission_r.json()
    
    subsmission_dict = {
        'title': response_dict['title'],
        'link':  'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)   
        }
    subsmission_dicts.append(subsmission_dict)
    
subsmission_dicts = sorted(subsmission_dicts,  key=itemgetter('comments'), reverse=True)

for submission_dict in subsmission_dicts:
    print("\nTitle: ", subsmission_dict['title'])
    print("Discussion Link: ", submission_dict['link'])
    print("Comments: ", submission_dict['comments'])
    

    
    
