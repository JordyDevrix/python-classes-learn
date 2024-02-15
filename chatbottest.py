import json
import requests

headers = {"Authorization": "Bearer "}

url = "https://api.edenai.run/v2/image/question_answer"
json_payload = {
    "providers": "Google",
    "file_url": "🔗 URL of your image",
    "question": "What are the logos on the image ?",
    "fallback_providers": ""
}

response = requests.post(url, json=json_payload, headers=headers)

result = json.loads(response.text)
print(result['alephalpha']['answers'])
