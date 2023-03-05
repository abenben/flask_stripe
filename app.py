from flask import Flask, request, render_template
import stripe

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/charge", methods=["POST"])
def charge():
    amount = 50
    customer = stripe.Customer.create(
        email=request.form["stripeEmail"],
        source=request.form["stripeToken"]
    )
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency="jpy",
        description="Example charge"
    )
    return render_template("charge.html", amount=amount)

if __name__ == "__main__":
    app.run(debug=True)
