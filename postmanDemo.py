import re
from sys import version
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import requests
def getProxy():
    resip = requests.get("http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=0&sb=0&pb=4&mr=1&regions=").text
    if re.match(r'(?:(?:25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', resip) is None:
        exit("IP 不正确")
    ip_arr = resip.split(":")
    proxyHost = ip_arr[0]
    proxyPort = ip_arr[1]
    proxyMeta = "http://%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }
    proxies = {
    "http": proxyMeta,
    "https": proxyMeta
    }
    return proxies


def searchWith(values):
    #print(values)
    search_name=values[3]
    proxies=getProxy()
    if values[0]==False :
        url='http://www.baidu.com/s?wd='+search_name
    else :
        url='http://'+values[1]
    #print(url)
    if values[4]==True:
        r=requests.get(url,proxies=proxies)
    elif values[5]==True:
        data={'wd':search_name}
        r=requests.post(url,data,proxies=proxies)
    elif values[6]==True:
        r=requests.head(url,proxies=proxies)
    else :
        r=requests.put(url,proxies=proxies)
    r.encoding='utf8'
    sg.popup("success"if r.status_code==200 else "false")

    #TODO：通过beautifulsoup，进行html的解析以及展示
    soup=BeautifulSoup(r.text,"html5lib")
    res=soup.prettify()
    #print("open file")
    file_s=open("baidu.html","wb")
    file_s.write(res.encode("utf-8"))
    file_s.close()

def openGUI():
    #TODO:编写GUI图形界面，实现搜索框以及提交按钮
    text_url=[sg.Radio('URL','Work'),sg.Text("请输入网址：")]
    search_url=[sg.Input()]
    text_title=[sg.Radio('Search','Work',default=True),sg.Text("请输入搜索内容：")]
    search_entry=[sg.Input()]
    ok_btn=[sg.OK()]
    cancel_btn=[sg.Button('Cancel')]
    summit_type=[[sg.Text("选择请求方式：")],
                [sg.Radio('Get','Type',default=True),sg.Radio('Post','Type'),sg.Radio('Head','Type'),sg.Radio('Put','Type')]]
    layout=[text_url,
            search_url,
            text_title,
            search_entry,
            summit_type,
            ok_btn,cancel_btn];

    window=sg.Window("Postman").Layout(layout)
    return window

#TODO:打开界面
window=openGUI();
while(True):
    event,values=window.read()
    if event in(None,'OK'):
        searchWith(values)
    if event in(None,'Cancel') :
        break
window.close()


