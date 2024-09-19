from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "BUT HOW CAN I LOSE WHEN I CAME WITH NOTHING?"

if __name__ == '__main__':
    app.run(debug=True)

