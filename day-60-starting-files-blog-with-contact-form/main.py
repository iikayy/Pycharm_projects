from flask import Flask, render_template, request
import requests
import smtplib

my_email = "benblacck@gmail.com"
password = "nqaonvxsembaeazn"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)




@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# @app.route("/form-entry", methods=['POST'])
# def receive_data():
    # name = request.form["name"]
    # email_address = request.form["email"]
    # phone_number = request.form["phone"]
    # message = request.form['message']
    # print(f"{name} {email_address} {phone_number}, {message}")
    ############################# YOU CAN USE THE CODE ABOVE OR THE ONE BELOW##########


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="benblacck@outlook.com",
            msg=email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
