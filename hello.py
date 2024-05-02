"""
The application is defined using the Flask class from the flask module.
The route("/") function is a decorator that maps the root URL to the hello function.
The hello function returns a string containing the text "Hello World!".
The if __name__ == "__main__": block starts the Flask application when the file is executed.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    This function returns a string containing the text "Hello World!".
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run()
