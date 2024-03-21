import requests

main_url = "https://reqres.in/api/users"
num_of_users = 0

# Sending a GET request to the API and getiing the first page
response = requests.get(main_url, params={'page':1})
data = response.json()

print(data)

# Getting the total count from the first response
total_count = data['total']

# Adding the number of users from the first page to the total count of the users
num_of_users += len(data['data']) 

data_per_page = data['per_page']  # Number of items per page
total_pages = total_count // data_per_page  # Total number of pages

# Checking to see if there are any remainder, if there is then it means there are additional items that don't completely fill a complete page
if total_count % data_per_page > 0:
    total_pages += 1

# Iterating through the remaining pages and adding the number of users to the total count
for i in range(2, total_pages + 1):
    response = requests.get(main_url, params={"page": i})
    data = response.json()
    num_of_users += len(data['data'])

# Checking to see if the total count accurately matches the actual number of users that are fetched
if num_of_users == total_count:
    print(f"The total count is accurate. Total users: {total_count}")
else:
    print(f"Total count is not accurate.")