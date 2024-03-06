from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://media.giphy.com/media/kiBcwEXegBTACmVOnE/giphy-downsized-large.gif'width=500"
            "<p>hello kitty</p>")
# Different routes using the app.route decorator
@app.route("/bye")
def bye():
    return "bye"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old"


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)






#
# def outer_function():
#     print("i'm outer")
#
#     def nested_function():
#         print("i'm inner")
#     return nested_function
#
#
# inner = outer_function()
#
# inner()
#
# import time
#
# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970
#
#
# # Write your code below 👇
#
# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#     return wrapper_function()
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i
#
#
# fast_function()
# slow_function()
