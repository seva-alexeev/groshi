from flask import Flask
from flask import render_template, request
import pymongo
from datetime import datetime
from hashlib import md5
from databaser import CoinBase

app = Flask(__name__)
coin_base = CoinBase()


def checker(string):
    if md5(string.encode('utf8')).hexdigest()[:5] == '00000':
        return True


def id_checker(user):
    if user.isdigit():
        return True


@app.route('/', methods=['GET', 'POST'])
def index():
    res = []
    if request.method == "POST":
        hashes = request.form["hashes"].strip().split()
        for h in hashes:
            splited_hash = h.split('-')
            if len(splited_hash) > 1:
                if checker(splited_hash[1]) and coin_base.already(splited_hash[1]) and id_checker(splited_hash[0]):
                    res.append((splited_hash[1], 'ok'))
                    coin_base.coin_adder(splited_hash[1], splited_hash[0])
                    print(coin_base.printer())
                else:
                    res.append((splited_hash[1], 'error'))
            else:
                res.append((splited_hash[0], 'error'))

    return render_template('index.html', res=res)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

