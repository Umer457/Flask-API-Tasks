import requests

response = requests.get("http://127.0.0.1:5000/info")

print(response)
print(response.json())


def test_get_info():
    response = requests.get("http://127.0.0.1:5000/info")
    assert response.status_code == 200
    assert response.json() == {'Users': [{'email': 'umer.nadeem@gmail.com', 'name': 'Umer Nadeem'},
           {'email': 'usamarashid@gmail.com', 'name': 'Usama Rashid'},
           {'email': 'durazesaqib@gmail.com', 'name': 'Duraze Saqib'}]}

def test_get_info_with_incorrect_url():
    response = requests.get("http://127.0.0.1:5000//invalid")
    assert response.status_code == 404