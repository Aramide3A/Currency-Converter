from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.geometry('500x500')

me = Frame(root, width=500, height=200, bg= 'light green')
me.grid(row=0, column=0)

icon = Image.open('images.png')
icon= icon.resize((150,150))
icon= ImageTk.PhotoImage(icon)

name= Label(root, image= icon,compound= LEFT, text= 'Aboki wire',padx= 20, pady= 10,anchor= CENTER, font=('serif 35 bold'), bg= 'light blue')
name.place(x=20, y=20)

currency= ['NGN','USD', 'GBP', 'CAD', 'EUR']
base = Label(root,text='Local currency', font=('serif 10 bold'), bg='black', fg='white', height= 1)
base.place(x= 30, y=250)

base_currency= ttk.Combobox(root,font=('san-serif 8 bold'), height= 1 )
base_currency['values']= currency
base_currency.place(x =150, y= 250)

quote = Label(root,text='Foreign currency', font=('serif 10 bold'), bg='black', fg='white', height= 1)
quote.place(x= 30, y=300)


quote_currency= ttk.Combobox(root,font=('san-serif 8 bold'), height= 1 )
quote_currency['values']= currency
quote_currency.place(x =150, y= 300)


def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1= base_currency.get()
    currency_2 = quote_currency.get()
    amount= entry_1.get()
    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'NGN':
        symbol = '₦'
    elif currency_2 == 'GBP':
        symbol = '€'
    elif currency_2 == 'CAD':
        symbol = '$'
    elif currency_2 == 'EUR':
        symbol = '€'
    
    headers = {
	"X-RapidAPI-Key": "75f128b6b9msh89d8d45f7e43d00p131477jsn2fe8f20a506a",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount= data['result']['convertedAmount']
    formatted= symbol + '{:,.2f}'.format(converted_amount)
    resul['text']= formatted
    print(response.text)

entry_1 = Entry(root,relief= SOLID)
entry_1.place(x= 30 , y= 350)

resul = Label(root,text='', relief= SOLID, width= 16, height=2,font=('san-serif 10 bold'))
resul.place(x= 250 , y= 350)

convert= Button(root, text='convert',bg='green', command=convert)
convert.place(x = 180, y=350)

root.mainloop()


