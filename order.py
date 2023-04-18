import configparser
import razorpay

parser = configparser.ConfigParser()
parser.read('resource/app.properties')
KEYID = parser['APP_PROPERTIES']['APP_KEY_ID']
SECRET = parser['APP_PROPERTIES']['APP_SECRET']

client = razorpay.Client(auth=(KEYID, SECRET))


def createorder(amount, currency, receipt):
    data = {"amount": amount, "currency": currency, "receipt": receipt}
    payment = client.order.create(data=data)
    print("id: " + payment["id"])
    print("entity: " + payment["entity"])
    print("amount: " + str(payment["amount"]))
    print("amount_paid: " + str(payment["amount_paid"]))
    print("amount_due: " + str(payment["amount_due"]))
    print("currency: " + payment["currency"])
    print("receipt: " + payment["receipt"])
    print("status: " + payment["status"])
    print("created_at: " + str(payment["created_at"]))

    return payment["id"]

