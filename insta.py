#made by Reza Moradi

import tkinter
from tkinter import *
import requests
import time

root=Tk()
root.title('insta GUI')
root.resizable(0,0)
root.config(width='325',height='250')

try:    
    r=requests.get('https://www.instagram.com/anonymous83046/?__a=1').json()
    follower=r['graphql']['user']['edge_followed_by']['count']
    following=r['graphql']['user']['edge_follow']['count']    
    label1=Label(root,text='followers',bg='blue',fg='white')
    label1.config(width='20',height='2')
    label1.place(x='10',y='30')
    label2=Label(root,text='following',bg='red',fg='white')
    label2.config(width='20',height='2')
    label2.place(x='170',y='30')
    label3=Label(root,text=follower,bg='gray',fg='white')
    label3.config(width='20',height='10')
    label3.place(x='10',y='65')
    label4=Label(root,text=following,bg='gray',fg='white')
    label4.config(width='20',height='10')
    label4.place(x='170',y='65')
    label5=Label(root,text='ID: anonymous83046')
    label5.place(x='10',y='1')
    time.sleep(3)
except:
    print('Connection Error...')












    
    
