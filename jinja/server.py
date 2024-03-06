from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url).json()
    gender = gender_response["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url).json()
    age = age_response["age"]

    return render_template("guess.html", person=name, sex=gender, num=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/4b1f09c5ff6f37774376"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", post=blog_data)


if __name__ == "__main__":
    app.run(debug=True)