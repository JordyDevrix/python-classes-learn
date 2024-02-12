import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTFkOTU4YWQtYjA3Yy00NGEzLTkwN2UtNjI1NzU5ZWMwNzExIiwidHlwZSI6ImFwaV90b2tlbiJ9.Ne8gmvIsM13o5okQbm_ODZG4O2WM5oETPuaMpo6Pc5s"}

url = "https://api.edenai.run/v2/image/question_answer"
json_payload = {
    "providers": "alephalpha",
    "file_url": "🔗 URL of your image",
    "question": "What are the logos on the image ?",
    "fallback_providers": ""
}

response = requests.post(url, json=json_payload, headers=headers)

result = json.loads(response.text)
print(result['alephalpha']['answers'])
