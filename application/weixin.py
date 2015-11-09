from flask import Blueprint,request
from library.weixinapi import Weixinapi
import urllib
import xml,html
weixin = Blueprint('weixin', __name__)
@weixin.route('/weixin', methods=['GET','POST'])
def add():
    b='123'
    try:
        type = request.form['type']
        fromUser = request.form['fromUser']
        message = request.form['message']
    except:
        type = 'event'
        fromUser = 'sadfasdfsa'
        message = 1234
    def text(message):
        weixinapi = Weixinapi(fromUser=fromUser, msgType=type)
        url = weixinapi.createUrl(url='http:act.qydw.net/message/response',token='passiontokenquyundong20150401')
        str = weixinapi.createText(message)
        return str
    def event(message):
        weixinapi = Weixinapi(fromUser=fromUser, msgType=type)
        str = weixinapi.createEvent(type=message)
        str = str.decode('utf8')
        str = html.escape(str)
        return str
    operator ={'text':text, 'event':event}
    Str = operator[type](message)
    return 'success % s' % Str

