#Jabir Chowdhury
#SoftDev1 pd7
#K09 -- Solidify
#2018-09-20

from flask import Flask
app = Flask(__name__)


@app.route("/")
def Hello():
    return "Howdy world"

if __name__ == "__main__":
  app.debug = True
  app.run()
