from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Abby")
def AbbyWebpage():
    return render_template('abbyMainpage.html')

@app.route("/Josh")
def JoshWebpage():
    return render_template('joshMainpage.html')

if __name__ == "__main__":
    app.run()
