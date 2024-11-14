import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados, schema de dados, view da minha API
    name: str
    type: str

    class Config:
        from_attributes = True

def pegar_pokemon(id: int) -> PokemonSchema:

    URL = f'https://www.pokeapi.co/api/v2/pokemon/{id}'
    response = requests.get(URL)
    data = response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list) # transformando a lista em uma string

    return PokemonSchema(name=data['name'], type=types)


if __name__ == '__main__':
    print(pegar_pokemon(10))
    print(pegar_pokemon(165))
    print(pegar_pokemon(240))