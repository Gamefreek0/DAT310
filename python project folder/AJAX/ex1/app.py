"""
Exercise #1: Checking username
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/check_username")
def check_username():
    # this list contains the usernames taken
    USERNAMES = ["johnsmith", "maryjane", "johndoe", "smith"]

    # TODO
    # get the username parameter from the URL (/check_username?username=xxx)
    # check that
    # - The username is minimum 3 characters long;
    # - It contains only alphanumerical characters (letters or digits);
    # - It has not been used before (for now a static list contains the used usernames).
    username=request.args.get("username", None)
    if not username:
        return ""
    if len(username)<3:
        return "Username is too short"
    elif not username.isalnum():
        return "Only alphanumerical"
    elif username in USERNAMES:
        return "Username is already in use"
    return ""


@app.route("/")
def index():
    return app.send_static_file("exercise1.html")


if __name__ == "__main__":
    app.run()
