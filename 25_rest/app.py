import json

from flask import Flask, render_template , request
import houndify

app = Flask(__name__)
clientId = "MsX70vzsQjNbSx31FX87OQ=="   #Replace with your credentials if website not working (Most likely went over credit limit)
clientKey = "0mk1n0mBX_q9nXSlabXe8caqmAh1J_pohbCV5rLeMwkO8ccImxN6Z8BTPZ6U5E2vTv6C93AIH4eeSTMu7h2zqw==" #Replace with your credentials if website not working (Most likely went over credit limit)
userId = "Admin"


@app.route("/")
def init():
    return render_template("site.html")

@app.route("/results" , methods=["POST"])
def searchresults():
    client = houndify.TextHoundClient(clientId, clientKey, userId)
    response = client.query(request.form.get("query"))
    listresults = response["AllResults"]
    dictresults = listresults[0]
    dictresults = dictresults["HTMLData"]
    stringResults = dictresults["LargeScreenHTML"]
    return render_template("results.html" , htmlcode= stringResults )


if __name__ == "__main__":
    app.debug = True
    app.run()
