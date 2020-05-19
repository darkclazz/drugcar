import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
message = "@บธ 180"
message2 = message.replace('@', '')

browser.open("http://thailpr.com/nsb/")

# print(browser.get_url())

browser.select_form('form')
browser["name"] = "tanongsak.tho"
browser["password"] = "8393"

browser.submit_selected()

browser.open("http://thailpr.com/center/search_011/search_0112.php")
browser.select_form('form[action="/center/search_011/search_0112.php"]')
browser["f_search"] = message2

browser.submit_selected()

soup = browser.get_current_page().find_all('tr')

#print(soup)
        
    
item = soup[7].text.strip('1').strip('เส้นทาง')
item1 = soup[9].text.strip('2').strip('เส้นทาง')
item2 = soup[11].text.strip('3').strip('เส้นทาง')
item3 = soup[13].text.strip('4').strip('เส้นทาง')
item4 = soup[15].text.strip('5').strip('เส้นทาง')
item5 = soup[17].text.strip('6').strip('เส้นทาง')
item6 = soup[19].text.strip('7').strip('เส้นทาง')
item7 = soup[21].text.strip('8').strip('เส้นทาง')
item8 = soup[23].text.strip('9').strip('เส้นทาง')
item9 = soup[25].text.strip('10').strip('เส้นทาง')
item10 = soup[27].text.strip('11').strip('เส้นทาง')
        
Drug_Car = ("\n"+item+"\n"+item1+"\n"+item2+"\n"+item3+"\n"+item4+"\n"+item5+"\n"+item6+"\n"+item7+"\n"+item8+"\n"+item9+"\n"+item10)

print(type(Drug_Car))