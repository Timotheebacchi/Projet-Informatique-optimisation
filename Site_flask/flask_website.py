from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'key'

@app.route("/")
def user():
    return render_template("Username.html")

@app.route("/check_username", methods=["POST"])
def check_username() :
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    if nom == "Roy" and prenom == "Valerie" :
        return render_template("Pass.html")
    else :
        session["nom"] = nom
        session["prenom"] = prenom
        session["connecte"] = "eleve"
        return render_template("Choice_Page.html")

@app.route("/check_pass", methods=["POST"])
def check_pass() :
    pword = request.form["motdepasse"]
    if pword == "7LcN8R3k84qceJ" :
        session["connecte"] = "prof"
        return render_template("Teacher1.html")

@app.route("/save_choice", methods = ['POST'])
def save() :
    request.json #<- dictionnaire qui contient les choix
    session #<- dictionnaire de l'identité

@app.route("/Teacher1")
def teach1() :
    return render_template("Teacher1.html")

@app.route("/Teacher2")
def teach2() :
    # content est la chaine de caractères html
    return render_template("Teacher2.html",content="")

liste = [["a"],["b","lien.fr"],["c"]]

@app.route("/Choice_Page")
def choi() :
    return render_template("Choices.html",choices=str(liste))

if __name__ == "__main__":
    app.run(debug=True)