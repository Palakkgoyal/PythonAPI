import requests # Not an inbuilt module

#This will send a fetch request to the url mentioned
request = requests.get("http://127.0.0.1:8000")
print(request.json())