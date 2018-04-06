from flask import Flask, url_for
app = Flask(__name__)

postcodes = {
    "0001": "Oslo",
    "4036": "Stavanger",
    "4041": "Hafrsfjord",
    "7491": "Trondheim",
    "9019": "Tromsø"
}

@app.route('/postcode/<pc>')
def lookupCode(pc):
    if pc in postcodes:
        return "Post code {} is {}".format(pc, postcodes[pc])
    else:
        return "Unknown post code ({})".format(pc)

@app.route('/')
def index():
    url = url_for("lookupCode", pc="4041")
    return "Postcode lookup service. Example usage: <a href='{url}'>{url}</a>".format(url=url)

if __name__ == "__main__":
    app.run()
