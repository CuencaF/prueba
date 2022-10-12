from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Esto es una prueba, hola"

if __name__ =='__main__':
    app.run()