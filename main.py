# Step 1: Install the `requests` library
!pip install requests

# Step 2: Import necessary libraries
import requests

# Step 4: Get access token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}
headers = {'User-Agent': user_agent}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# Debugging: Print the status code and response
print('Status Code:', res.status_code)
print('Response:', res.json())

# Error handling
if res.status_code == 200 and 'access_token' in res.json():
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

    # Step 5: Get most recent posts from the top subreddit
    subreddit = 'education'  # You can change this to any subreddit you want
    response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                            headers=headers, params={'limit': 5})  # Adjust the limit as needed

    print(response.json())

    # Step 6: Print the titles and description text of the most recent posts
    for post in response.json()['data']['children']:
        title = post['data']['title']
        selftext = post['data']['selftext']
        print(f"Title: {title}\nDescription: {selftext}\n")
else:
    print('Failed to retrieve access token. Check your credentials and try again.')
