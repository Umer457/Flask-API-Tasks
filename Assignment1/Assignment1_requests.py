import requests

data = {"a": 10, "b": 20}
class Calculator:

    def add(self):
        url = "http://127.0.0.1:5000/sum"
        response = requests.post(url, json=data)
        response.status_code == 200
        result = response.json()
        print("Addition Answer", result["Addition"], 'and the response is ', response.status_code)

    def multiply(self):
        url = "http://127.0.0.1:5000/multiply"
        response = requests.post(url, json=data)
        response.status_code == 200
        result = response.json()
        print("Multiplication Answer:", result["product"], " and the response is ",response.status_code)

    def subtract(self):
        url = "http://127.0.0.1:5000/subtraction"
        response = requests.post(url, json=data)
        response.status_code == 200
        result = response.json()
        print("Subtraction Answer:", result["subtraction"], " and the response is ",response.status_code)



call = Calculator()
call.multiply()
call.add()
call.subtract()



