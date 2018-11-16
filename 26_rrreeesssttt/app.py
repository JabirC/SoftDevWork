
'''
  Jabir Chowdhury
  SoftDev1 pd07
  K#26: Getting More REST
  2018-11-16
'''

import urllib.request as urlrequest
import urllib.parse as parse
import json

from flask import Flask, render_template , request

tastedive_access_key = "323804-Flask-19VPBGR7"

food2fork_API_key = "82364dfdfe2b35fa818a5c03b3ae55a8"

calendarindex_API_key = "278b497e8bb4f9f65d1f2466d6f145d3977bead1"


app = Flask(__name__)

@app.route("/")
def init():
    #TasteDive API
    url_stub="https://tastedive.com/api/similar?q=titanic&info=1&k="
    url= url_stub + tastedive_access_key
    print(url)
    response = urlrequest.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    info = urlrequest.urlopen(response)
    info =json.load(info)

    #Food2Fork API
    url_stub2 = "https://www.food2fork.com/api/get?key="
    food_id = "&rId=47024"
    url2 = url_stub2 + food2fork_API_key + food_id
    print(url2)
    response = urlrequest.Request(url2 , headers={'User-Agent': 'Mozilla/5.0'})
    info2 = urlrequest.urlopen(response)
    info2 = json.load(info2)

    #CalendarIndex api
    url_stub3 ="https://www.calendarindex.com/api/v1/holidays?country=CA&year=2018&api_key="
    url3 = url_stub3 + calendarindex_API_key
    print(url3)
    response = urlrequest.Request(url3, headers={'User-Agent': 'Mozilla/5.0'} )
    info3 = urlrequest.urlopen(response)
    info3 = json.load(info3)

    return render_template("site.html", name=info['Similar']['Results'][1]['Name'], summary=info['Similar']['Results'][1]['wTeaser'],video=info['Similar']['Results'][1]['yID'], pic = info2['recipe']['image_url'], recipe = info2['recipe']['ingredients'] , holidays=info3['response']['holidays'])


if __name__ == "__main__":
    app.debug = True
    app.run()
