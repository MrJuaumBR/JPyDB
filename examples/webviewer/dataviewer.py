from JPyDB import pyDatabase

try:
    from flask import Flask, request, render_template,redirect
except Exception as err:
    raise(err)

try:
    from webbrowser import open as webopen
    webBrowser = True
except:
    webBrowser = False






"""
Will require webbrowser to open the URL

Acess: http://localhost:5000


::::: What is this? :::::
- A Visualizer for pydb archives, using JPyDB!


::::: Requirements :::::
- flask
- webbrowser
- JPyDB

"""





app = Flask(__name__)

app.template_folder = "."

@app.route('/',methods=["POST","GET"])
def main():
    if request.method == "POST":
        if 'load' in request.form:
            f = request.form.get('fileload')
            if f:
                return redirect(f'/load?p={f}')
    return render_template('base.html')

@app.route('/load')
def load():
    if 'p' in request.args:
        datafile = request.args.get('p')
        dbh = pyDatabase()
        dbh.database.filename = datafile
        dbh.database.startup() # restart
        
        db = dbh.db()
        
        return render_template('load.html',f=datafile,database=db)

if webBrowser:
    webopen('http://localhost:5000')
if __name__ == "__main__":
    app.run(debug=True)