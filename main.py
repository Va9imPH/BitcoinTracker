import requests
from tkinter import *
from datetime import datetime

# window
root = Tk()
root.geometry("400x500")
root.title("Bitcoin Tracker")

def bitcoinPrice():
    # get API
    response = requests.get(url=f"https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR").json()
    data = response["USD"]

    price_label.config(text = "$" + str(data))
    time = datetime.now().strftime("%H:%M:%S")
    update_label.config(text = "Updated at: " + time)

    # update
    root.after(1000, bitcoinPrice)

# fonts
f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

# name text
label1 = Label(root, font = f1, text = "Bitcoin Tracker")
label1.pack(pady = 20)

# btc price text
price_label = Label(root, font = f2)
price_label.pack(pady = 20)

# update price text
update_label = Label(root, font = f3)
update_label.pack(pady = 20)

bitcoinPrice()

mainloop()