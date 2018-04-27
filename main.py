from flask import Flask
from flask import render_template, request
import pymongo
from datetime import datetime
from hashlib import md5

app = Flask(__name__)

client = pymongo.MongoClient("localhost", 27017)


@app.route('/', methods=['GET', 'POST'])
def index():
    res = []
    if request.method == "POST":
        hashes = request.form["hashes"].strip().split()
        for h in hashes:
            splited_hash = h.split('-')
            if len(splited_hash)>1:
                if md5(splited_hash[1].encode('utf8')).hexdigest()[:4] == '0000':
                    res.append((splited_hash[1], 'ok'))
                    client.db.coins.insert_one(
                        {
                            "string": splited_hash[1],
                            "time": datetime.utcnow(),
                            "user": splited_hash[0],
                        }
                    )
                    print(client.db.coins.find_one({'user': '1'}))
                else:
                    res.append((splited_hash[1], 'error'))
            else:
                res.append((splited_hash[0], 'error'))

    return render_template('index.html', res=res)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

