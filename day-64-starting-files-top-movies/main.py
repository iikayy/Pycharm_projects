from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new_movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(String(250), nullable=True)
    review: Mapped[str] = mapped_column(String(250),  nullable=True)
    img_url = "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    # READING ALL MOVIES:
    all_movies = db.session.execute(db.select(Movie)).scalars()
    return render_template("index.html", movies=all_movies)


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    done = SubmitField(label='Done')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    rate_movie_form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if rate_movie_form.validate_on_submit():
        movie.rating = float(rate_movie_form.rating.data)
        movie.review = rate_movie_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=rate_movie_form)


@app.route("/delete")
def delete():
    with app.app_context():
        movie_id = request.args.get("id")
        movie = db.get_or_404(Movie, movie_id)
        db.session.delete(movie)
        db.session.commit()
        return render_template("index.html", movie=movie)


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title")
    add_movie = SubmitField(label='Add Movie')


@app.route("/add", methods=['GET', 'POST'] )
def add():
    movie_url = "https://api.themoviedb.org/3/search/movie"
    API_KEY = "0e765a5c56436edf3fec7d3b4ab24c03"
    API_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZTc2NWE1YzU2NDM2ZWRmM2ZlYzdkM2I0YWIyNGMwMyIsInN1YiI6IjY1ZDVmODk4YjA0NjA1MDE3YjA5MTU2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7aCU_e-sA6P-uEF3eHS96Ip9df0alaqnqwzzFqMc41c"
    find_movie_form = FindMovieForm()
    if find_movie_form.validate_on_submit():
        movie_title = find_movie_form.title.data
        response = requests.get(movie_url, params={
        "accept": "application/json",
        "Authorization": API_TOKEN,
        "query": movie_title,
        "api_key": API_KEY,
    })
        data = response.json()["results"]
        return render_template("select.html", movies=data)
    return render_template("add.html", form=find_movie_form)


@app.route("/find", methods=['GET', 'POST'] )
def find():
    movie_id = request.args.get("id")
    if movie_id:
        movie_url = "https://api.themoviedb.org/3/movie"
        movie_endpoint = f'{movie_url}/{movie_id}'
        API_KEY = "0e765a5c56436edf3fec7d3b4ab24c03"
        API_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZTc2NWE1YzU2NDM2ZWRmM2ZlYzdkM2I0YWIyNGMwMyIsInN1YiI6IjY1ZDVmODk4YjA0NjA1MDE3YjA5MTU2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7aCU_e-sA6P-uEF3eHS96Ip9df0alaqnqwzzFqMc41c"
        movie_db_url = "https://image.tmdb.org/t/p/original/%5Bposter_path%5D"
        response = requests.get(movie_endpoint, params={
            "accept": "application/json",
            "Authorization": API_TOKEN,
            "api_key": API_KEY,
            "language": "en-US",
        })
        data = response.json()
        new_movie = Movie(
            title = data["title"],
            year = data['release_date'].split("-")[0],
            description = data['overview'],
            img_url = f"{movie_db_url}/{data['poster_path']}"
        )
        # movie_to_update = db.get_or_404(Movie, movie_id)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)

