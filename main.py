from flask import Flask, jsonify, request
import csv

articles = []

with open('articles.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)

@app.route("/get-articles")
def get_article():
    return jsonify({
        "Welcome!": "The first article in the dataset",
        "data": articles[0],
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    global articles
    article = articles[35]
    articles.pop(35)
    liked_articles.append(article)
    return jsonify({
        "data": liked_articles,
        "status": "success"
    }), 201

@app.route("/disliked-articles", methods=["POST"])
def disliked_article():
    global articles
    article = articles[358]
    articles.pop(358)
    disliked_articles.append(article)
    return jsonify({
        "data": disliked_articles,
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()

# Mam, you have to see the output in postman.
# The liked articles and disliked articles become more as you keep pressing the send button
# :)