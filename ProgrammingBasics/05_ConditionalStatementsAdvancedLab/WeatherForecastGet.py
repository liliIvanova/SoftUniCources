import requests

city_name = input("Enter city:")

print("Display weather report for: ", city_name)

url = f"https://wttr.in/{city_name}"
result = requests.get(url)

print(result.text)
