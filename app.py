from flask import Flask, request, render_template

import verifySignature
from order import createorder
import traceback

app = Flask(__name__)
app.config['SECRET_KEY'] = '5c94782e54b41890a2895615f59365950efdaf60b84b6941'


@app.route('/callback/', methods=['POST', 'GET'])
def index():
    razorpay_order_id = request.form.get('razorpay_order_id')
    razorpay_payment_id = request.form.get('razorpay_payment_id')
    razorpay_signature = request.form.get('razorpay_signature')
    print(razorpay_order_id)
    print(razorpay_payment_id)
    print(razorpay_signature)
    try:
        verifySignature.validate(razorpay_order_id, razorpay_payment_id, razorpay_signature)
    except:
        traceback.print_exc()

    return render_template('callback_landing.html')


@app.route('/', methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        # Then get the data from the form
        amount = str(request.form['amount'])
        currency = str(request.form['currency'])
        receipt = str(request.form['receipt'])

        print("creating order with: ", amount, currency, receipt)
        order_id = '"'+createorder(amount, currency, receipt)+'"'
        amount = '"'+amount+'"'
        currency = '"'+currency+'"'
        print("Order ID is: " + order_id)
        return render_template('checkout_callback.html', order_id=order_id, amount=amount, currency=currency)
    return render_template('fill_order.html')
