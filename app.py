from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

if __name__ == "__main__":
    #instrucciones por pasos
    app.run(debug=True)
