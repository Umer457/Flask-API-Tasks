import requests

response = requests.get('http://127.0.0.1:5000/data')

if response.status_code == 200:
    assert response.json() == [{'email': 'umer.nadeem@gmail.com', 'name': 'Umer Nadeem'},
                               {'email': 'usamarashid@gmail.com', 'name': 'Usama Rashid'},
                               {'email': 'durazesaqib@gmail.com', 'name': 'Duraze Saqib'}]
    print(response.status_code)
else:
    print('Failed to fetch data')