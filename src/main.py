
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def app_home():
    css_url = url_for('static', filename='css/styles.css')
    return render_template('child.html', css_url=css_url)


    
if __name__ == '__main__':
    app.run(debug=True)