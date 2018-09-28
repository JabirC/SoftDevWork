#Jabir Chowdhury
#SoftDev1 pd7
#K13: Echo Echo Echo
#2018-09-26

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def submit():
    return render_template("form.html")

@app.route("/auth")
def authenticate():
    return render_template("result.html",
                            user=request.args["username"],
                            method= request.method)



if __name__ == "__main__":
  app.debug = True
  app.run()
