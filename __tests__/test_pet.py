# 1 - biblioteca
import json
import pytest
import requests     # framework de teste de API
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

# 2 - classe (opcional no Python, em muitos casos)


# 2.1 - atributos ou variáveis
# consulta e resultado esperado
pet_id = 702190001          # código do animal
pet_name = "Lupin"         # nome do animal
pet_category = 1            # código do animal
pet_category_name = "dog"   # titulo da categoria
pet_tag_id = 1              # código do rótulo
pet_tag_name = "vacinado"   # titulo do rótulo
pet_status = "available"    # status do animal

# informações em comum
url = 'https://petstore.swagger.io/v2/pet'              # endereço
headers = {'Content-Type': 'application/json'}          # formato dos dados trafegados

# 2.2 - funções / métodos

def test_post_pet():
    # configura
    # dados de entrada estão no arquivo json
    pet=open('./fixtures/json/pet1.json')             # abre o arquivo json
    data=json.loads(pet.read())                       # ler o conteudo e carrega como json em uma variável data
    # dados de saída / resultado esperado estão nos atibutos acima das funções

    # executa
    response = requests.post(
        url=url,                                        # endereço
        headers=headers,                                # cabeçalho / informações extras
        data=json.dumps(data),                          # a mensagem = json
        timeout=5,                                      # tempo limite da transmissão em segundos            
        verify=False                                    # opção para continuar o desenvolvimento em ambiente restrito
    )


    # valida
    response_body = response.json()                     # cria uma variável e carrega a resposta em formato json

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name

