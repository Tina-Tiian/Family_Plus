
# -*- coding: utf-8 -*-
from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/wechat', methods=['GET'])
def checkSignature():
    token = "Family_Plus"
    signature = request.GET.get('signature', None) 
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    if hashstr == signature:
        print("hashstr")
        print("signature")
        return echostr
    else:
        print("attack!")
        return None

if __name__ == '__main__':
    app.run(host='112.74.87.38',port='80')
