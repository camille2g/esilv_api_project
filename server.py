from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def index():
    # HTML avec un bouton qui pointe vers '/get_data'
    return '''
    <html>
        <head>
            <title>Accueil</title>
        </head>
        <body>
            <h1 style="font-family:verdana;color:rgb(250, 99, 0);text-align:center;">Bienvenue sur le site de Quentin, Camille et Alix!</h1>
            <form action="/get_data">
                <input type="submit" value="Afficher les articles sur l'IA (\get_data)" />
            </form>
        </body>
    </html>
    '''
@app.route('/get_data')
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
        articles_details = "<h1>Articles sur l'Intelligence Artificielle</h1>"
        for article in articles:
            articles_details += f"<p><b>Titre:</b> {article['title']}, <b>URL:</b> <a href='{article['url']}'>{article['url']}</a></p>"
        
        return articles_details
    else:
        return "Erreur lors de la récupération des articles"

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run()