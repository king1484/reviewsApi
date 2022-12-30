from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "ok"

@app.route('reviews')
def reviews():
    title = request.form["title"]
    times = 4
    text = ""
    stars = 0
    num = 0

    for i in range(times):
        if(i==0):
            res = requests.get(f"https://imdb-api.tprojects.workers.dev/reviews/{title}?option=date&sortOrder=desc")
            for review in res.json()["reviews"]:
                text += "\n\n"
                text += review["content"]
                stars += review["stars"]
                num += 1
        else:
            res2 = requests.get("https://imdb-api.tprojects.workers.dev"+res.json()["next_api_path"])
            for review in res2.json()["reviews"]:
                text += "\n\n"
                text += review["content"]
                stars += review["stars"]
                num += 1

    return {
        "text":text,
        "stars":stars//num
    }
    

if __name__ == '__main__':
    app.run()