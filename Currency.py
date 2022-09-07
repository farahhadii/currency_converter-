from tkinter import *
from tkinter import ttk
import requests 
import json

window = Tk() # in order to create a tkinter application, we create an instance of tkinter frame by 
# doing tk()
window.title('Farah Adi - Currency Converter') # the title of the GUI
window.geometry("600x600")  #geometry method decides the size, position of screen layout
# Creating Tabs 
tabs = ttk.Notebook(window) # Notebook widget is an inbuilt widget of ttk library in tkinter
# which allows us to create Tabs in the window application 
tabs.pack(pady=15)

choices = ['AUD', 'ANG', 'AED', 'BRL', 'BHD', 'BYN', 'BGN', 'BTC', 'CAD', 'CLP', 'CRC', 'CUP', 'CHF', 'DOP','DZD','EUR', 'GBP', 'HUF', 'IQD','INR','JOD', 'KWD', 
'LBP', 'LYD', 'MAD', 'MYR','MVR', 'MKD', 'NZD', 'NOK', 'OMR', 'PLN', 'QAR','RUB', 'RON', 'SAR', 'SEK', 'TRY','USD', 'UYU', ]

# Creating three Frames 
title_page = Frame(tabs, width=580, height=580)
currency_F = Frame(tabs, width = 580, height = 580) # putting our frames inside our tabs
conversion_F = Frame(tabs, width = 580, height = 580) 

# (packs) lays out widgets onto the screen
title_page.pack(fill= "both")
currency_F.pack(fill = "both")
conversion_F.pack(fill = "both")

# Adding our tabs 
tabs.add(title_page, text = 'Home Page')
tabs.add(currency_F, text = "Currency") 
tabs.add(conversion_F, text = "Converting")


photo1 = PhotoImage(file = "img1.PNG") # file location
Label (title_page, image = photo1, bd=0) .pack(pady=25) 
#Label allows you to put something on the window 

# Create a Label 
Label (title_page, text = "Welcome to the Currency Converter!", font = "none 23 bold").pack(pady=35)

# creating the command for the START button  
def nextab():
    tabs.select(currency_F) 
    
 
# Start button
Button (title_page, text = "START", width=6, command=nextab) .pack(pady=5)

# CURRENCYYYYY
home_currency = LabelFrame(currency_F, text = "Dosmetic Currency") 
home_currency.pack(pady=20)

# The currency we want to convert from 
from_currency = ttk.Combobox(home_currency, font=("normal", 25)) # we are putting our combo box inside home_currency (LabelFrame)
# size of the box is 25 
from_currency['values'] = choices
from_currency.pack(pady=15,padx=15)

# The currency we want to convert to 
to_currency = LabelFrame(currency_F, text = "Convert Currency")
to_currency.pack(pady=25)

# Convert to Entry
conversion_box = ttk.Combobox(to_currency, font=("normal", 25)) # create the box that will go inside 
# our LabelFrame
conversion_box['values'] = choices
conversion_box.pack(pady=15,padx=15)

# command to get to the third tab
def thirdtab():
    tabs.select(conversion_F)

# NEXT BUTTON 
Button (currency_F, text = "NEXT", width=6, command=thirdtab) .pack(pady=5)


##CONVERSION STUFF
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    first_currency = from_currency.get()
    second_currency = conversion_box.get()
    quantity = amount.get()

    response = requests.request("GET", url, headers={
	"X-RapidAPI-Key": "a346f62873msh8d0b7d934dd1143p1ca78ejsn92a133f17e97",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"}, params= {"from":first_currency,"to":second_currency,"amount":quantity})
     
    results = response.json()["result"]["convertedAmount"] # note that JSON is a standardized format commonly 
    # used to transfer data as text that can be sent over a network.  
    results = "{:.2f}".format(results)
    converted_box['text'] = results + " " + second_currency


def clear():
    amount.delete(0,END) # clears the textbox 
    converted_box.delete(0,END) # clears the textbox 


amount_labelFrame = LabelFrame(conversion_F, text="Amount")
amount_labelFrame.pack(pady=25)

#Entry Box for Amount
amount = Entry(amount_labelFrame, font = ("normal", 25)) # we want to put the entry box inside of 
# our amount_label (LabelFrame)
amount.pack(pady=15,padx=15)

# Convert button 
Button(amount_labelFrame, text= "Convert", command=convert) .pack(pady=25)# we want the Button to 
# be inside our LabelFrame

# Conversion frame 
label_convert = LabelFrame(conversion_F, text= "Convert Currency") # creating another LabelFrame
# inside our Convert tab 
label_convert.pack(pady=25)

# Converted entry
converted_box = Label(label_convert, width = 20, font=("normal",25))
converted_box.pack(pady=15, padx=15)

# clear button in our Conversion_F
Button(conversion_F, text="Clear", command=clear).pack(pady=25)

# Give a bit of spacing inside our conversion_F 
Label(conversion_F, text="", width=70) .pack()

def back():
    tabs.select(currency_F)

# BACK button 
Button (conversion_F, text = "BACK", width=6, command=back) .pack(padx = 30, side = LEFT)

#exit function 
def close_window():
    conversion_F.destroy()
    exit()

# EXIT button 
Button(conversion_F, text = "EXIT", width=6, command=close_window) .pack(padx=30, side = RIGHT)


window.mainloop()

