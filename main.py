import requests

url = "https://random-avatar-daddy.p.rapidapi.com/rnd"
filename = "response.png" #output file

headers = {
	"X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
	"X-RapidAPI-Host": "random-avatar-daddy.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
with open(filename, "wb") as f:
    f.write(response.content)
