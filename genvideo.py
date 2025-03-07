import requests

API_KEY="QWFyeWEgUHJhamFwYXQ6QEFhcnlhMzExMg=="

url = "https://api.d-id.com/talks"

def genvideo(img_url,summary,v_id):

    payload = {
        "source_url":img_url,
        "script": {
            "type": "text",
            "input": summary,
            "provider": {
                "type": "microsoft",
                "voice_id": v_id,
                "voice_config":{
                    "style":"Default"
                }
            }
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Basic {API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)

    id=response.json()["id"]
    print(id)
    return id