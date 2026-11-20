import requests

user_message = "can you tell me the AI in the 3 to 4 lines"

request_message = {"message": user_message}

url = "https://rohitautomation.app.n8n.cloud/webhook-test/5ae9b901-3575-417a-a349-44761fe7a4d3"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json())