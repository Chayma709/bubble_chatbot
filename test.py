import requests
import json

rasa_endpoint = 'https://1164-196-203-180-253.ngrok-free.app/webhooks/rest/webhook'
headers = {'Content-Type': 'application/json'}
payload = {'message': 'hi'}

response = requests.post(rasa_endpoint, headers=headers, json=payload)
# print(response.json([0]))
print(response.text)