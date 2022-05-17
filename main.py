import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    '''
    input: search keywords
    output: list of first 10 results as list of objetcs (title,link)
        [
            {
                title: asd
                link: 'www.asd.com'
            }
        ]
    '''
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    items = res['items']
    results = []
    for item in items:
        results.append(
            {
                'title': item['title'],
                'link': item['link']
            }
        )
    return results


if __name__ == "__main__":
    # load env variable from .env files
    load_dotenv()
    api_key = os.getenv('API_KEY')
    cse_id = os.getenv('CSE_ID')
    
    keywords = input("Type Search Keyword(s): ")
    keywords = keywords.replace(' ', '+')
    for re in google_search(keywords, api_key, cse_id):
        print(re)
