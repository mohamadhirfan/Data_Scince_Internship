from flask import Flask, request, render_template
import re

app = Flask(__name__,template_folder='templates')



@app.route('/')
def home_page():
    return '<h1>Welcome to Home Page</h1>'

@app.route('/regex_101', methods=['GET','POST'])
def add_fun():
    if request.method == 'POST':
        a = str(request.form.get('text'))
        b = str(request.form.get('pattern'))
        c = []
        c.extend(re.findall(b,a))
        d = int(len(c))
        if a=='' or b == '':
            return render_template('about.html')
        else:
            return render_template('result.html', c = c, d = d, a=a, b=b)
    return render_template('about.html')

@app.route('/about')
def hello():
     return 'about page'


if __name__ == '__main__':
    app.run(debug=True)