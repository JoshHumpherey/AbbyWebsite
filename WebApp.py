from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('websiteMainpage.html')

@app.route("/Abby")
def AbbyWebpage():
    return render_template('abbyMainpage.html')

@app.route("/Josh")
def JoshWebpage():
    return render_template('joshMainpage.html')

if __name__ == "__main__":
    app.run()
