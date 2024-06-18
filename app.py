from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def principal():
    return "Hola"



if __name__ =="__main__":
    app.run()