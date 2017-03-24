# -*- coding: utf-8 -*-
from flask import Flask, request
import hashlib

app = Flask(__name__)


@app.route('/', methods=['GET'])
def wechat_verify():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    token = 'Family_Plus'
    tmplist = [token, timestamp, nonce]
    print(tmplist)
    tmplist.sort()
    tmpstr = "%s%s%s" % tuple(tmplist)
    hashstr = hashlib.sha1(tmpstr.encode('utf-8')).hexdigest()

    if hashstr == signature:
        return echostr
    return 'access verification fail'
