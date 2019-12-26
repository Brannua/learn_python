from aip import AipOcr
import re
APP_ID=''
API_KEY =''
SECRECT_KEY=''
client=AipOcr(APP_ID,API_KEY,SECRECT_KEY)
i=open(r'C:\Users\Administrator\Desktop\图片1.png','rb')
img=i.read()
message=client.basicGeneral(img)
for i in message.get('words_result'):
 print(i.get('words'))