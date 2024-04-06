import requests

def get_data():
    api_key = "c20aa73bf54d4eff8de2627c71956efe"
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",  
        "pageSize": 5, 
        "apiKey": api_key, 
        "language": "fr" 
    }
    
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        articles = response.json()['articles']
        
        for article in articles:
            print(f"Titre: {article['title']}, URL: {article['url']}")
    else:
        print("Erreur lors de la récupération des articles")

get_data()