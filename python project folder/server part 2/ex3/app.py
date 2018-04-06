"""it doesn't work for some reason"""
from flask import Flask, render_template, request


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pay")
def pay():
    amount = int(request.args.get("amount", 0))
    return render_template("output.html", amount=amount, valuta=payment(amount).items())


def payment(amount):
    payments={}
    VALUES=[500,100,50,20,10,5,1]
    for val in VALUES:
        while(True):
            if overzero(amount,val):
                if val not in payments:
                    payments[str(val)]=1
                    amount-=val
                else:
                    payments[str(val)]=payments[val]+1
                    amount-=val
            elif amount ==0:
                print(payments)
                return payments
            else:
                break





def overzero(amount,value):
    if amount-value>=0:
        return True
    else:
        return False

if __name__ == "__main__":
    app.run()
