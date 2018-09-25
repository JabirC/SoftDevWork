#Ji-N-Ja -- Jiayang Chen & Jabir Chowdhury
#SoftDev1 pd7
#K10: Jinja Tuning
#2018-09-23

from flask import Flask,render_template
from csvscript import make_dictionary,random_job #functions from previous work

app = Flask(__name__)


@app.route("/occupations")
def occupation_table():
    occu_dict = make_dictionary("data/occupations.csv")  #makes a dictionary using occupations.csv
    return render_template("chart.html",
                           dict = occu_dict,   #passes the dictionary to a variable used in jinja
                           rand= random_job(occu_dict))  #passes a random weighted occupation from dictionary

if __name__ == "__main__":
  app.debug = True
  app.run()
