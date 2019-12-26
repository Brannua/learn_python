import requests
import itchat

# 和机器人进行交互
def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key' : '填入自己的图灵机器人key(若没有可在网上申请)',
		'userid' : 'wechat-robot',
		'info' : msg,
	}
	try: 
		r = requests.post(apiUrl, data=data).json()
		return r.get('text')
	except:
		return
		
# 获取微信消息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	reply = get_response(msg['Text'])
	defaultReply = 'I received: ' + msg['Text']
	return reply or defaultReply

# 防止多次扫码实现的热更新
itchat.auto_login(hotReload=True)
itchat.run()