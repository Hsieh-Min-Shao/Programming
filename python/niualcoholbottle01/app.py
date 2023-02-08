from flask import Flask, request, abort,render_template,jsonify

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from flask import render_template

from linebot.exceptions import LineBotApiError



#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
from datetime import datetime
import time
import pymysql
import demjson
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('JT4aMV8E5sEgB3L/Wk+fKYWIMDIcgQXaarWB+K2JTyUocLqyHnXOaWSFbzof+LB4XW2zbtzJZsYFFO0stAWO4k+QUT9OFYn1wMiVuZywzAXBPVsiZTEJ7L0GGE544UOBa8ZrPVsBHfr3TnP3Z9NfUQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fe8e2d2e974c90e547e85e310ba6dccb')
x=" Good "
y="100"
z="times"
ID="test"
IDType="test2"
rowI="test3"
rowType="test4"
xx=0

temperature="1"
humidity="1"
c02="1"
nh33="1"
fan="0"
water="0"
light="0"



""" --------------------------------------------------------------- """
@app.route('/setT/')
def setT():
    db = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )
    cursor = db.cursor()
    sql = "SELECT * FROM alcoholbottle"
    t=cursor.execute(sql)
    results = cursor.fetchall()

    Name=[]
    Longitude=[]
    Latitude=[]
    Level=[]
    Move=[]
    StealTime=[]

    for i in range(t): 
        Name.append((results[i][2]))
        Longitude.append((results[i][3]))
        Latitude.append(results[i][4])
        Level.append((results[i][5]))
        Move.append((results[i][6]))
        StealTime.append((results[i][7]))    
    chart={'Name':Name,'Longitude':Longitude,'Latitude':Latitude,'Level':Level,'Move':Move,'StealTime':StealTime}

    return jsonify(chart)
@app.route('/api',methods=['POST']) #路由
def api():
	
    global xx
    global ID
    global IDType
    xx=0
    print(request.headers)  #獲取http header的內容
    print(request.form)     #獲取json資料內容
    print("位置：")
    print(request.form['Name']) #獲取內容
    print("經度：")
    print(request.form['Longitude'])    #獲取內容
    print("緯度：")
    print(request.form['Latitude'])
    print("ID")
    print(request.form['BottleID'])
    ID=request.form['Longitude']
    #IDType=type(request.form['Longitude'])
	
    db = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )

    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

	# SQL 查询语句
    sql = "SELECT * FROM alcoholbottle"
    cursor.execute(sql)
    results = cursor.fetchall()
	
	
    

    for row  in results:
	
	    
	    #print(row[1])
	    if(row[1]==request.form['BottleID']):

		    
			
			
		    """
			'INSERT INTO pig(a,b,c,d,e)''VALUES(%s,%s,%s,%s,%s);',(a,b,c,d,e)
			'INSERT INTO products (name, descr, price) ''VALUES ("葵花寶典", "蓋世武功密集", 990);'

			
			db.commit()

			
		    """
			
		    
		    xx=1
	    



    if(xx==0):	
	    dbs = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )
	    cursors = dbs.cursor()
	    command = "INSERT INTO alcoholbottle(BottleID,Name, Longitude, Latitude)VALUES(%s, %s, %s,%s)"
	    cursors.execute(command, (request.form['BottleID'],request.form['Name'],request.form['Longitude'],request.form['Latitude']))
	    dbs.commit()
	    dbs.close()
    db.close()

	
    return ""

@app.route('/apiintt',methods=['POST']) #路由
def apiintt():
	
    global xx
    
    global rowI
    global rowType
    global z
    
   
    #z=request.form['data']

    xx=0
    #print(request.headers)  #獲取http header的內容
    print(request.form)     #獲取json資料內容
    print("BottleID")
    print(request.form['BottleID']) #獲取內容
    print("Level")
    print(request.form['Level'])    #獲取內容
    db = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )

    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

	# SQL 查询语句
    sql = "SELECT * FROM alcoholbottle"
    cursor.execute(sql)
    results = cursor.fetchall()

    rowI=request.form['Level']
    #rowType=type(request.form['Level'])
    for row  in results:

        
        #print(type(row[1]))
        #print(type(request.json['Warning']))
        if(request.form['Warning']=="1"):
            
            dbs = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )
            cursors = dbs.cursor()
            command = "UPDATE alcoholbottle SET Move = %s WHERE BottleID = %s"
            BottleID=request.form['BottleID']
            Move=request.form['Warning']
            cursors.execute(command, (Move, BottleID))
             
            dbs.commit()
            dbs.close()

            dbs = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )
            StealTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cursorsT=dbs.cursor()
            command = "UPDATE alcoholbottle SET Time = %s WHERE BottleID = %s"
            cursorsT.execute(command, (StealTime, BottleID))
            dbs.commit()
            dbs.close()
            

        if(row[1]==request.form['BottleID']):

            Level=request.form['Level']
            BottleID=request.form['BottleID']

            dbs = pymysql.connect("remotemysql.com", "snwzWlaEnW", "qO0tm19aQ1", "snwzWlaEnW", charset='utf8' )
            cursors = dbs.cursor()
            
            #print("yeeeeeeeeeeeeeeeeeeeeee")
            print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
            

			


			
			#print(Name)
			#print(row[4])
			#print(Level)
            command = "UPDATE alcoholbottle SET Level = %s WHERE BottleID = %s"
            cursors.execute(command, (Level, BottleID))
            dbs.commit()
            dbs.close()
			
			
            """
			'INSERT INTO pig(a,b,c,d,e)''VALUES(%s,%s,%s,%s,%s);',(a,b,c,d,e)
			'INSERT INTO products (name, descr, price) ''VALUES ("葵花寶典", "蓋世武功密集", 990);'

			
			db.commit()

			
            """
			
		    
            xx=1

	
    return ""



""" --------------------------------------------------------------- """


@app.route('/') 
def map():
    return render_template("map.html")

# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@app.route('/mov',methods=['POST']) #路由
def mov():
    global x
    x=request.form['data']
    line_bot_api.broadcast(TextSendMessage(text='酒精瓶1被移動了'))
    return 'OKK'


@app.route('/alc',methods=['POST']) #路由
def alc():
    global y
    y=request.form['data']
    line_bot_api.broadcast(TextSendMessage(text='酒精瓶1酒精不夠了'))
    return 'OKKay'


@app.route('/Ale',methods=['POST']) #路由
def Ale():
    line_bot_api.broadcast(TextSendMessage(text='豬場大門尚未關閉，請盡速關上!!'))
    return 'OKKay'


@app.route('/prcent',methods=['POST']) #路由
def prcent():
    global z
    z=request.form['data']
    return 'OKKay'

#環境感測器

@app.route('/tmptr',methods=['POST']) #路由
def tmptr():
    global temperature
    temperature=request.form['data']
    return 'OKKay'

@app.route('/humid',methods=['POST']) #路由
def humid():
    global humidity
    humidity=request.form['data']
    return 'OKKay'

@app.route('/co2',methods=['POST']) #路由
def co2():
    global c02
    c02=request.form['data']
    return 'OKKay'
    
@app.route('/nh3',methods=['POST']) #路由
def nh3():
    global nh33
    nh33=request.form['data']
    return 'OKKay'
    
@app.route('/fans',methods=['POST']) #路由
def fans():
    global fan
    fan=request.form['data']
    return 'OKKay'
    
@app.route('/waters',methods=['POST']) #路由
def waters():
    global water
    water=request.form['data']
    return 'OKKay'
    
@app.route('/lights',methods=['POST']) #路由
def lights():
    global light
    light=request.form['data']
    return 'OKKay'
    
    
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    global x
    global temperature
    global humidity
    global c02
    global nh33
    global fan
    global water
    global light
    
    msg = event.message.text
    """
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
    
    """
    if '剩餘多少' in msg:
        message = TextSendMessage(text='剩餘'+"75"+'%')
        line_bot_api.reply_message(event.reply_token, message)

    if '豬場環境' in msg:
        message = TextSendMessage(text='豬場大門尚未關閉，請盡速關上!!')
        line_bot_api.reply_message(event.reply_token, message)
    if 'ID' in msg:
        message = TextSendMessage(text=ID+IDType+"----ID")
        line_bot_api.reply_message(event.reply_token, message)
    if '還在嗎' in msg:
        if(x=="Move"):
            message = TextSendMessage(text='被移動了')
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TextSendMessage(text='還在原地')
            line_bot_api.reply_message(event.reply_token, message)
    if '環境資料' in msg:
        message = TextSendMessage(text='【'+str(datetime.now().strftime('%Y/%m/%d %H:%M'))+'】\n✅環境資料正常\n溫度 : '+"24.6"+' °C\n濕度 : '+"80.7"+' %\n二氧化碳 : '+"2245.71"+' ppm\n氨氣 : '+"0.85"+' ppm')
        line_bot_api.reply_message(event.reply_token, message)
    if '設備開關' in msg:
        message = TextSendMessage(text='【'+str(datetime.now().strftime('%Y/%m/%d %H:%M'))+'】\n設備狀態\n\n風扇 : '+"開啟"+'\n保溫燈 : '+"關閉"+'\n水簾 : '+"關閉"+'')
        line_bot_api.reply_message(event.reply_token, message)
		
	
    """
    message = TextSendMessage(text=msg+x+' ID '+user_id)
    line_bot_api.reply_message(event.reply_token, message)
    if(x=="Move"):
        message = TextSendMessage(text=x)
        line_bot_api.reply_message(event.reply_token, message)
    """
        


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
