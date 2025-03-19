import requests

url = "http://127.0.0.1:5000/query"
query = {"query": "What is LangChain?"}

response = requests.post(url, json=query)

# Ensure UTF-8 encoding when printing response
print("Response:", response.text.encode("utf-8").decode())
