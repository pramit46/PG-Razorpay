import configparser
import razorpay


parser = configparser.ConfigParser()
parser.read('resource/app.properties')
KEYID = parser['APP_PROPERTIES']['APP_KEY_ID']
SECRET = parser['APP_PROPERTIES']['APP_SECRET']

client = razorpay.Client(auth=(KEYID, SECRET))


def validate(razorpay_order_id, razorpay_payment_id, razorpay_signature):
    #the below line is to inject forced failure of signature verification. Comment it for normal run
    #razorpay_signature=razorpay_signature+"1"
    client.utility.verify_payment_signature({
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        'razorpay_signature': razorpay_signature
    })
