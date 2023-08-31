from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API para mostrar el primer artículo
@app.route("/get-article")
def get_article():

    return 'Escribir código para mostrar el primer objeto en la lista all_articles'


# API para mover el artículo a la lista de artículos que me gustan
@app.route("/liked-article")
def liked_article():

    return 'Escribir código para mover el primer artículo a la lista liked_articles'


# # API para mover el artículo a la lista de artículos que no me gustan
@app.route("/unliked-article")
def unliked_article():

    return 'Escribir código para cambiar el primer artículo a la lista not_liked_articles'

# ejecuta la app
if __name__ == "__main__":
    app.run()
