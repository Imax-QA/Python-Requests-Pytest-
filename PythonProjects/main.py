import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a6ecc3e8759c49e31b44d01d02a0a3c'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "max.meleshko@yandex.ru",
    "password": "Iloveqa1"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Автобуль",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name_change = {
    "pokemon_id":pokemon_id,
    "name": "Autobul"
}

body_add_pokeball = {
    "pokemon_id":pokemon_id
}

response_name_change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

