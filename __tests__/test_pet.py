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
pet_name = "Lupin"          # nome do animal
pet_category_id = 1            # código do animal
pet_category_name = "dog"   # titulo da categoria
pet_tag_id = 1              # código do rótulo
pet_tag_name = "vacinado"   # titulo do rótulo

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


def test_get_pet():
    # configura
    # dados de entrada e saída / resultado esperado estão na seção antes das funções


    # executa
    response = requests.get(
        url=f'{url}/{pet_id}',  # chama o endereço do get/consulta passando o código do animal
        headers=headers,
        verify=False            # é utilizando apenas quando há erro no certificado
        # não tem corpo da mensagem / body
    )


    # valida
    response_boby = response.json()

    assert response.status_code == 200
    assert response_boby['name'] == pet_name
    assert response_boby['category']['id'] == pet_category_id
    assert response_boby['tags'][0]['id'] == pet_tag_id
    assert response_boby['status'] == "available"
    assert response_boby['tags'][0]['name'] == pet_tag_name


def test_put_pet():
    # configura
    # dados de entrada vem de um arquivo json
    pet = open('./fixtures/json/pet2.json')
    data = json.loads(pet.read())

    # executa
    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5,
        verify=False  
    )

    # valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == "sold"


def test_delete_pet():
    # configura
    # dados de entrada e saída virão dos atributos

    # executa
    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers,
        verify=False
    )

    # valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)

