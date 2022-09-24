import json
import os
import threading
import time
import warnings

# ignore warning created by Rocketry about future default execution type
warnings.simplefilter("ignore", FutureWarning)

from pprint import pprint

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from rocketry import Rocketry

app = Flask(__name__)
scheduler = Rocketry()


def getCookie():
    with open("cookie.json", "r") as f:
        cookie_file = json.load(f)

    if "cookie" in cookie_file:
        return cookie_file["cookie"], None
    else:
        return None, "Could not load cookie from cookie.json"


def setCookie(cookie):
    with open("cookie.json", "w") as f:
        json.dump({"cookie": cookie}, f)


def getMembers():
    url = "https://student-dashboard.sums.su/groups/124"

    cookie, err = getCookie()
    if err:
        return None, err

    headers = {"cookie": cookie}

    response = requests.request("GET", url, headers=headers)

    if "set-cookie" in response.headers:
        cookie = response.headers["set-cookie"].split(";")[0]
        setCookie(cookie)

    response_html = response.text

    if "Sorry you're not authenticated." in response_html:
        return None, "Authentication Error"

    soup = BeautifulSoup(response_html, "html.parser")

    members_parent_anchor = soup.find_all(href="/groups/124/members")[1]
    members = members_parent_anchor.find("h4").string

    return int(members), None


@scheduler.task("every 1 min", execution="thread")
def fetchMembers():
    members, err = getMembers()
    if err:
        print(err)
    else:
        print(members)


@app.route("/")
def index():
    members, err = getMembers()
    if err:
        return jsonify({"error": err})

    return jsonify({"members": members})


if __name__ == "__main__":
    # setCookie(os.environ.get("STARTING_COOKIE"))
    threading.Thread(target=lambda: app.run(debug=False), daemon=True).start()
    scheduler.run()
