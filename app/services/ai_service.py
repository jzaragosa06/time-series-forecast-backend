import json
import os
import requests

def generateResponse(prompt): 
    response = requests.post(
        url='https://openrouter.ai/api/v1/chat/completions', 
        headers={
            "Authorization": f"Bearer {os.environ.get('OPEN_ROUTER_KEY')}",
            "Content-Type": "application/json", 
        },
        data=json.dumps({
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {
                    "role": "system",
                    "content": "Respond naturally and briefly. Avoid lists, code, or formatting. Provide plain paragraph text only."
                },
                {
                    "role": "user",
                    # "content": "What is the meaning of life?"
                    "content": prompt
                }
            ]
        }) 
    )
    
    return response.json()['choices'][0]['message']['content']