from flask import Flask, render_template, request, url_for

app = Flask(__name__)

notes = []
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'GET':
        notes.clear()

    elif request.method == 'POST':
        note = request.form.get("note")
        if note != '':
            notes.append(note)
        return render_template("notes.html", notes=notes)
        
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)