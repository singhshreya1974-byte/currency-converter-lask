from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        try:
            response = requests.get(API_URL.format(from_currency))
            data = response.json()
            rate = data["rates"][to_currency]
            result = f"{amount} {from_currency} = {round(amount * rate, 2)} {to_currency}"
        except Exception as e:
            result = "Error: Cannot fetch conversion rate."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    # Render requires 0.0.0.0 and a fixed port
    app.run(host="0.0.0.0", port=10000)
