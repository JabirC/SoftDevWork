
# Jabir Chowdhury
# SoftDev1 pd07
# K #08: Fill Yer Flask
# 2018-09-18  


from flask import Flask

app = Flask(__name__)

@app.route("/")
def HelloWorld():
    print("Greetings")
    return "Howdy world"

@app.route("/conv")
def ques():
    print("qs ready")
    return "How ya doin'"

@app.route("/bye")
def farewell():
    print("Farewell")
    return "Latta Latta Alligata"

if __name__ == "__main__":
    app.debug = True
    app.run()
