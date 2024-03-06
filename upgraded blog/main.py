from flask import Flask, render_template
import requests
import datetime as dt

blog_url = "https://api.npoint.io/669f8fddc413b7759562"
posts = requests.get(blog_url).json()
post_objects = []
for post in posts:
    post_objects.append(post)

app = Flask(__name__)


@app.route('/')
def home():
    current_year = dt.datetime.now().date()
    return render_template("index.html", all_posts=post_objects, year=current_year)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    current_year = dt.datetime.now().date()
    requested_post = None
    for blog_post in post_objects:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)

# @app.route("/blog")
# def get_blog():
#     blog_url = "https://api.npoint.io/4b1f09c5ff6f37774376"
#     blog_response = requests.get(blog_url)
#     blog_data = blog_response.json()
#     return render_template("index.html", post=blog_data)


if __name__ == "__main__":
    app.run(debug=True)