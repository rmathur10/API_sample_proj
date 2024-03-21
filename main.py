import requests

main_url = "https://reqres.in/api/users"
num_of_users = 0

# Sending a GET request to the API and getiing the first page
response = requests.get(main_url, params='page':1)
data = response.json()


# Getting the total count from the first response
total_count = data['total']

# Adding the number of users from the first page to the total count of the users
total_users += len(data['data']) 

data_per_page = data['per_page']  # Number of items per page
total_pages = total_count // data_per_page  # Total number of pages
if total_count % data_per_page > 0:
    total_pages += 1

# Iterating through the remaining pages and adding the number of users to the total count
for i in range(2, total_pages + 1):
    pass
