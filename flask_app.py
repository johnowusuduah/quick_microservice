from flask import Flask
from flask import jsonify
app = Flask(__name__)

def convert(amount_in_dollars):
    # calculate the resultant change and store the result (res)
    amount_dollar = amount_in_cedi * 6.4
    return amount_dollar


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("This is your simple US Dollar to Ghana Cedi Convertor")
    return 'Hello World! I can convert your US Dollar to Ghana Cedi: /convert'

@app.route('/convert')
def convertroute(USdollar):
    print(f"Convert {USdollar}")
    amount = f"{USdollar}"
    result = convert(float(amount))
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)