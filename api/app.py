import os
import time
import pymongo

from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = pymongo.MongoClient(
    f"mongodb+srv://{os.environ.get('MONGODB_USERNAME')}:{os.environ.get('MONGODB_PASSWORD')}@cluster0.glo6i2w.mongodb.net/?retryWrites=true&w=majority"
)
db = client.members
collection = db.members_count


@app.route("/")
def index():
    members_cursor = collection.find().sort([("timestamp", -1)]).limit(1)

    members_obj = members_cursor.next()

    return jsonify(
        {"members": members_obj.get("count"), "timestamp": members_obj.get("timestamp")}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
