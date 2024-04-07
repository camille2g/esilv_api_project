from flask import Flask, request, jsonify, render_template_string, redirect
import requests
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        article_number = request.form.get('article_number')
        if article_number:
            return redirect(f'/article/{article_number}')
    return '''
    <html>
        <head>
            <title>Accueil</title>
        </head>
        <body>
            <h1 style="font-family:verdana;color:rgb(250, 99, 0);text-align:center;">Bienvenue sur le site de Quentin, Camille et Alix!</h1>
            <form action="/get_data">
                <input type="submit" value="Afficher les articles sur l'IA (/get_data)" />
            </form>
            <form action="/articles">
                <input type="submit" value="Afficher plus d'articles sur l'IA (/articles)" />
            </form>
            <br>
            <form action="/" method="post">
                <input type="number" name="article_number" min="1" placeholder="Numéro d'article">
                <input type="submit" value="Voir détails de l'article">
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
        "pageSize": 10, 
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

@app.route('/articles')
def articles():
    api_key = "c20aa73bf54d4eff8de2627c71956efe"  
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",  
        "pageSize": 10,
        "apiKey": api_key,
        "language": "fr"
    }
    
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        articles_details = "<h1>Articles sur l'Intelligence Artificielle</h1>"
        for index, article in enumerate(articles, start=1):
            title = article.get('title', 'Titre non disponible')
            published_at = article.get('publishedAt', 'Date non disponible')
            source_name = article.get('source', {}).get('name', 'Source non disponible')
            article_url = article.get('url', 'URL non disponible')
            
            if published_at != 'Date non disponible':
                published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y, %H:%M")
                
            articles_details += f"<p>Article #{index}: <b>Titre:</b> {title}, <b>Date de publication:</b> {published_at}, <b>Source:</b> {source_name}, <b>URL:</b> <a href='{article_url}'>{article_url}</a></p>"
        return articles_details
    else:
        return "Erreur lors de la récupération des articles"

@app.route('/article/<int:number>')
def get_article(number):
    api_key = "c20aa73bf54d4eff8de2627c71956efe"
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",
        "pageSize": 10,  
        "apiKey": api_key,
        "language": "fr"
    }
    
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        if number - 1 < len(articles):
            article = articles[number - 1]  
            article_url = article.get('url', None)
            
            if article_url:
                return redirect(article_url)  
            else:
                return "URL de l'article non disponible", 404
        else:
            return "Numéro d'article non valide ou hors de portée", 404
    else:
        return "Erreur lors de la récupération des articles depuis l'API NewsAPI", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
