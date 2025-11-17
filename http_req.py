import requests
import time

start_time = time.time()

#making 151 api calls
for i in range(1,151):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
    resp = requests.get(url)
    #print(resp.status_code)
    pokemon = resp.json()
    print(pokemon['name'])

#total time: execution =  11.040177822113037


end_time = time.time()

print("execution = ",end_time-start_time)
