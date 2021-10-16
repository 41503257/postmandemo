import requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup

class PostManDemoWithSearch :
    def __init__(self) :
        gui();
    
    def gui():
        text_title=[sg.Text('请输入搜索内容')]
        search_entry=[sg.Input()]
        ok_btn=[sg.OK()]
        layout=[text_title,
                search_entry,
                ok_btn]
        window=sg.Window('百度搜索').Layout(layout)
        event,values=window.read()
        search_name=values[0]

a=PostManDemoWithSearch();