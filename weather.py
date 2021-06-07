import requests,json
dd="Welcome To Live Weather Api By Dhruv Parikh"
print(f"{dd:-^40}")
city=input("Enter the city for the weather?")
url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={API KEY}" # Take key and account from openweathermap.org for free of cost
response=requests.get(url)
if response.status_code==200:
  data=response.json()
  main=data['main']
  temp=main['temp']
  hum=main['humidity']
  pressure=main['pressure']
  temp_feel=main['feels_like']
  report=data['weather']
  print(f"{city:-^40}")
  print(f"Temperature :{temp-272} Celcius")
  print(f"Humidity :{hum}")
  print(f"Pressure :{pressure}")
  print(f"It feels like {temp_feel-272} Celcuis")
  print(f"Report:{report}")
else:
  print("Error in the HTTP Request")
