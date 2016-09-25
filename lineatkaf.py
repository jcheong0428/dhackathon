from flask import Flask
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():
    client = MongoClient('ds021326.mlab.com',21326)
    db = client['kafline']
    if db.authenticate('admin','cingulat3!'):
        x = [x["i"] for x in db.sensorData.find()]
        linelength = x[-1]
        linestatus = "Line at KAF is " + str(linelength)
    else: 
        linestatus = "LineData not found"
    return linestatus

if __name__ == "__main__":
    app.run()