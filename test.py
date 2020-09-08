#! /usr/bin/env pytest-3.8
import pytest
import requests
workUrl = 'http://127.0.0.1:8091/bear'
payload = [
    {"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5},
    {"bear_type":"GUMMY","bear_name":"Toka","bear_age":1.5},    
    {"bear_type":"POLAR","bear_name":"Chumka","bear_age":1.7}]

def setup_module():
    print("run")
    requests.delete(workUrl)

def test_get_bear_check_status_code_empy_body():
    response = requests.get(workUrl)
    assert response.status_code == 200
    assert not response.json()

def test_post_bear_check_status_code_body():
    response = requests.post(workUrl, json=payload[0])
    assert response.status_code == 200
    body = response.text
    assert body
    #assert response["bear_type"] == payload["bear_type"]

    response = requests.get(workUrl + '/' + str(body))
    assert response.status_code == 200
    body = response.json()
    assert body["bear_type"] == payload[0]["bear_type"]
    #assert body["bear_name"] == payload["bear_name"]
    assert body["bear_age"] == payload[0]["bear_age"]
    
    
@pytest.fixture()
def resource_setup(request):
    response = requests.post(workUrl, json=payload[1])
    return response.text


def test_get_bear_check_status_code_body_id(resource_setup):
    response = requests.get(workUrl + '/' + str(resource_setup))
    assert response.status_code == 200
    body = response.text

    #assert body["bear_type"] == payload[1]["bear_type"]
    #assert body["bear_name"] == payload[1]["bear_name"]
    #assert body["bear_age"] == payload[1]["bear_age"]
    
    
#def test_put_bear_check_status_code_body(resource_setup):
    #response = requests.put(workUrl + '/' + str(resource_setup), json=payload[2])
    #assert response.status_code == 200
    #body = response.text
    #assert body
    #assert response["bear_type"] == payload["bear_type"]

    #response = requests.get(workUrl + '/' + str(resource_setup))
    #assert response.status_code == 200
    #body = response.json()
    #assert body["bear_type"] == payload[2]["bear_type"]
    #assert body["bear_name"] == payload[2]["bear_name"]
    #assert body["bear_age"] == payload[2]["bear_age"]
    
    
def test_delete_bear_check_status_code_body_id(resource_setup):
    len_list = len(requests.get(workUrl).json())
    response = requests.delete(workUrl + '/' + str(resource_setup))
    assert response.status_code == 200
    body = response.text
    #print (body)
    #assert not body
    
    len_list_check = len(requests.get(workUrl).json())
    assert len_list == len_list_check+1
    
    response = requests.get(workUrl + '/' + str(resource_setup))
    body = response.text
    print (body)
    
    #print (requests.get(workUrl).text)
    
def test_delete_bear_check_status_code_body():
    
    response = requests.delete(workUrl)
    assert response.status_code == 200
    body = response.text
    print (body)
    #assert not body
    
    response = requests.get(workUrl)
    assert not response.json()

    
