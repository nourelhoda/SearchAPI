import os
import json
from dotenv import load_dotenv
import requests
from fastapi import FastAPI

app = FastAPI(
    title="Google Search",
)

# load env variable from .env files
load_dotenv()
api_key = os.getenv('API_KEY')
cse_id = os.getenv('CSE_ID')

@app.get("/search")
async def google_search(keyword):
    '''
        the endpoint input is search keyword(s)
    '''
    keyword = keyword.replace(' ', '+')
    params = {
        'q': keyword,
        'num': 10,
        'safe': 'active',
        'cx': cse_id,
        'start': 0,
        'client': 'google-csbe',
        'key': api_key
    }
    response = requests.get(
        url="https://www.googleapis.com/customsearch/v1",
        params=params,
    )
    results = []
    for item in json.loads(response.content.decode("UTF-8"))['items']:
        results.append(
            {
                'title': item['title'],
                'link': item['link'],
            }
        )
    return {"message": results}
