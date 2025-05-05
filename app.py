from flask import Flask, request

app = Flask(__name__)

@app.route("/api/calcs/<number>", methods=["GET"])
def calculate(number):
    try:
        num = int(number)
        if num <= 0:
            return "", 404
        
        return {
            "dec": num - 1,
            "hex": hex(num)
        }
    except ValueError:
        return "", 400