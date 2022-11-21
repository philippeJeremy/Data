
import requests
request = requests.get("https://swapi.dev/api/people/1/")
dic = request.json()


michel = ["Hello", "I", "Michel", "am"]


for i in michel:
    print(i)
    
michel.insert(2,michel[3])
michel.pop(4)
print(michel)

##########

age = [12, 16, 34, 58, 9]
age.sort()
print(age)

for i in dic:
    print(i)
   
   
name = dic["name"] 
height = dic["height"]
mass = dic["mass"]
birth_year = dic["birth_year"]

print(f"{name} is {height} cm tall and weighs {mass} kg. He was born in {birth_year}")

##########


kilometres_travelled = [50, 10, 100, 25, 1000, 21, 12,30]
moyen = 0

for i in kilometres_travelled:
    moyen += i
    
print(moyen / len(kilometres_travelled))    


kilometres_travelled = [50, 10, 100, 25, 21, 12,30]
moyen = 0

for i in kilometres_travelled:
    moyen += i
    
print(moyen / len(kilometres_travelled)) 