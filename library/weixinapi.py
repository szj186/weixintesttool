import xml.etree.cElementTree as ET
import time,hashlib
import unicodedata
import html
class Weixinapi:
    def __init__(self, fromUser, msgType):
        self.atTime = str(int(time.time()))
        self.root = ET.Element("xml")
        toUserName = ET.SubElement(self.root, "ToUserName")
        toUserName.text = '<[!CDATA[test]]>'
        fromUserName = ET.SubElement(self.root, "FromUserName")
        fromUserName.text = '<[!CDATA[%s]]>' % fromUser
        createTime = ET.SubElement(self.root, 'CreateTime')
        createTime.text = self.atTime
        messageType = ET.SubElement(self.root, 'MsgType')
        messageType.text = '<[!CDATA[%s]]>' % msgType
    def createUrl(self, url, token):
        nonce = '1234'
        tmpArr = [token, self.atTime, nonce]
        tmpArr.sort()
        tmpStr = ''.join(tmpArr)
        tmpStr = tmpStr.encode()
        signature = hashlib.sha1(tmpStr).hexdigest()
        url ='?signature=%s&timestamp=%s&nonce=%s' % (signature,atTime,nonce)
        return url
    def createText(self, data):
        content = ET.SubElement(self.root, 'Content')
        content.text = "<!CDATA[[%s]]>" % data
        messageId = ET.SubElement(self.root, 'MsgId')
        messageId =  '12323433'
        return ET.tostring(self.root)
    def createEvent(self, type):
        event = ET.SubElement(self.root, 'Event')
        event.text = '<!CDATA[%s]>' % type
        return ET.tostring(self.root)
        pass

