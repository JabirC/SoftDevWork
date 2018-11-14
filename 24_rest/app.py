from flask import Flask, render_template
from urllib import request, parse
import json

app =  Flask(__name__)


@app.route("/")
def init():
    info = request.urlopen('https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=xv63WMCZcgZqZSginI4XjlA5dj7djvpftJJydNDi')
    info = info.read()
    dict  = json.loads(info)
    return render_template("site.html", image=dict['url'])




if __name__ == "__main__":
    app.debug = True
    app.run()
