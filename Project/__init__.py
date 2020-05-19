from flask import Flask, request, abort
import requests
import json
from Project.Config import *
import mechanicalsoup
app = Flask(__name__)


def GET_Drug_Car(message):
    try :
        message2 = message.replace('#', '')
        browser = mechanicalsoup.StatefulBrowser()

        browser.open("http://thailpr.com/nsb/")

        # print(browser.get_url())

        browser.select_form('form')
        browser["name"] = "tanongsak.tho"
        browser["password"] = "8393"

        browser.submit_selected()

        browser.open("http://thailpr.com/center/search_011/search_0111.php")
        browser.select_form('form[action="/center/search_011/search_0111.php"]')
        browser["f_search"] = message2
        #ptint(message2)
        browser["calendar1"] = " "

        browser.submit_selected()

        soup2 = browser.get_current_page().find_all('a')

        #print(type(soup2))

        links_list = []


        for link in soup2:
            links_list.append(link)

        #print(type(links_list))

        links1 = links_list[1]
        links2 = links_list[9]
        links3 = links_list[17]
        links4 = links_list[25]
        links5 = links_list[33]


        # list to string
        links_list1 = []
        links_list2 = []
        links_list3 = []
        links_list4 = []
        links_list5 = []


        for link1 in links1:
            links_list1.append(link1)

        for link2 in links2:
            links_list2.append(link2)

        for link3 in links3:
            links_list3.append(link3)

        for link4 in links4:
            links_list4.append(link4)

        for link5 in links5:
            links_list5.append(link5)

            #print(type(links_list1))
            #print(links_list1)

        links_list1 = [str(strlink1) for strlink1 in links_list1]    # map to a list of strings
        img1 = ''.join(links_list1)
        itemimg1 = img1.split('"')
        itemimg1send = "http://thailpr.com/nsb/center"+itemimg1[3].strip('.')

        links_list2 = [str(strlink2) for strlink2 in links_list2]    # map to a list of strings
        img2 = ''.join(links_list2)
        itemimg2 = img2.split('"')
        itemimg2send = "http://thailpr.com/nsb/center"+itemimg2[3].strip('.')

        links_list3 = [str(strlink3) for strlink3 in links_list3]    # map to a list of strings
        img3 = ''.join(links_list3)
        itemimg3 = img3.split('"')
        itemimg3send = "http://thailpr.com/nsb/center"+itemimg3[3].strip('.')

        links_list4 = [str(strlink4) for strlink4 in links_list4]    # map to a list of strings
        img4 = ''.join(links_list4)
        itemimg4 = img4.split('"')
        itemimg4send = "http://thailpr.com/nsb/center"+itemimg4[3].strip('.')

        links_list5 = [str(strlink5) for strlink5 in links_list5]    # map to a list of strings
        img5 = ''.join(links_list5)
        itemimg5 = img5.split('"')
        itemimg5send = "http://thailpr.com/nsb/center"+itemimg5[3].strip('.')


        soup = browser.get_current_page().find_all('tr')
        #text

        links_list00 = []



        for link00 in soup:
            links_list00.append(link00)



        links00 = links_list00[7] 
        links01 = links_list00[9] 
        links02 = links_list00[11] 
        links03 = links_list00[13]
        links04 = links_list00[15]

        # list to string
        links_list01 = []
        links_list02 = []
        links_list03 = []
        links_list04 = []
        links_list05 = []


        links_list01 = [str(strlink00) for strlink00 in links00]    # map to a list of strings
        img00 = ''.join(links_list01)
        itemimg00 = img00.split('=')
        itemimg00send = itemimg00[11].strip('&amp;Province')+" "+itemimg00[12].strip('&amp;id')+" "+itemimg00[14].strip('&amp;Time_i')+" "+itemimg00[15].strip('&amp;Date_i')+" "+itemimg00[16].strip('" target')

        links_list02 = [str(strlink01) for strlink01 in links01]    # map to a list of strings
        img01 = ''.join(links_list02)
        itemimg01 = img01.split('=')
        itemimg01send = itemimg01[11].strip('&amp;Province')+" "+itemimg01[12].strip('&amp;id')+" "+itemimg01[14].strip('&amp;Time_i')+" "+itemimg01[15].strip('&amp;Date_i')+" "+itemimg01[16].strip('" target')

        links_list03 = [str(strlink02) for strlink02 in links02]    # map to a list of strings
        img02 = ''.join(links_list03)
        itemimg02 = img02.split('=')
        itemimg02send = itemimg02[11].strip('&amp;Province')+" "+itemimg02[12].strip('&amp;id')+" "+itemimg02[14].strip('&amp;Time_i')+" "+itemimg02[15].strip('&amp;Date_i')+" "+itemimg02[16].strip('" target')

        links_list04 = [str(strlink03) for strlink03 in links03]    # map to a list of strings
        img03 = ''.join(links_list04)
        itemimg03 = img03.split('=')
        itemimg03send = itemimg03[11].strip('&amp;Province')+" "+itemimg03[12].strip('&amp;id')+" "+itemimg03[14].strip('&amp;Time_i')+" "+itemimg03[15].strip('&amp;Date_i')+" "+itemimg03[16].strip('" target')

        links_list05 = [str(strlink04) for strlink04 in links04]    # map to a list of strings
        img04 = ''.join(links_list05)
        itemimg04 = img04.split('=')
        itemimg04send = itemimg04[11].strip('&amp;Province')+" "+itemimg04[12].strip('&amp;id')+" "+itemimg04[14].strip('&amp;Time_i')+" "+itemimg04[15].strip('&amp;Date_i')+" "+itemimg04[16].strip('" target')
        
        Drug_Car = ("\n"+itemimg00send+"\n"+itemimg1send+"\n"+itemimg01send+"\n"+itemimg2send+"\n"+itemimg02send+"\n"+itemimg3send+"\n"+itemimg03send+"\n"+itemimg4send+"\n"+itemimg04send+"\n"+itemimg5send)

        return Drug_Car
    
    except IndexError:
        message2 = message.replace('#', '')
        browser = mechanicalsoup.StatefulBrowser()

        browser.open("http://thailpr.com/nsb/")

        # print(browser.get_url())

        browser.select_form('form')
        browser["name"] = "tanongsak.tho"
        browser["password"] = "8393"

        browser.submit_selected()

        browser.open("http://thailpr.com/center/search_011/search_0111.php")
        browser.select_form('form[action="/center/search_011/search_0111.php"]')
        browser["f_search"] = message2
        #ptint(message2)
        browser["calendar1"] = " "

        browser.submit_selected()

        soup2 = browser.get_current_page().find_all('a')

        #print(type(soup2))

        links_list = []


        for link in soup2:
            links_list.append(link)

        #print(type(links_list))

        links1 = links_list[1]

        # list to string
        links_list1 = []

        for link1 in links1:
            links_list1.append(link1)


            #print(type(links_list1))
            #print(links_list1)

        links_list1 = [str(strlink1) for strlink1 in links_list1]    # map to a list of strings
        img1 = ''.join(links_list1)
        itemimg1 = img1.split('"')
        itemimg1send = "http://thailpr.com/nsb/center"+itemimg1[3].strip('.')


        soup = browser.get_current_page().find_all('tr')
        #text

        links_list00 = []

        for link00 in soup:
            links_list00.append(link00)

        links00 = links_list00[7] 
     
        # list to string
        links_list01 = []
 

        links_list01 = [str(strlink00) for strlink00 in links00]    # map to a list of strings
        img00 = ''.join(links_list01)
        itemimg00 = img00.split('=')
        itemimg00send = itemimg00[11].strip('&amp;Province')+" "+itemimg00[12].strip('&amp;id')+" "+itemimg00[14].strip('&amp;Time_i')+" "+itemimg00[15].strip('&amp;Date_i')+" "+itemimg00[16].strip('" target')


        Drug_Car2 = ("\n"+itemimg00send+"\n"+itemimg1send+"\n")
  
        return Drug_Car2



        
@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        
        print(message)
        if '#' in message :
            Reply_messasge = 'ข้อมูลรถผ่านด่าน : {}'.format(GET_Drug_Car(message))
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif '#' in message :
            Reply_messasge = 'ข้อมูลรถผ่านด่าน : {}'.format(GET_Drug_Car2(message))
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
       
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world book',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200