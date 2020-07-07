from tkinter import *
import requests
import json
import sqlite3


pycripto = Tk()  # creating a tkinter application
pycripto.title('Crypto Portifolio')

pycripto.iconbitmap('coin.ico')  # setting a icon for the application window

connection = sqlite3.connect('coin.db')  # opening connection with database
cursor_obj = connection.cursor()

cursor_obj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount REAL, price REAL)")
connection.commit()


def my_portfolio():
    api_request = requests.get('YOU PUT YOUR API KEY HERE!')  # fetch API data from internet

    api = json.loads(api_request.content)  # store API data in a variable

    cursor_obj.execute("SELECT * FROM coin")  # fetching values from database
    your_coin = cursor_obj.fetchall()

    def font_color(number):  # setting different colors depending on whether there are losses or profits
        if number >= 0:
            return 'green'
        else:
            return 'red'

    general_pl = 0
    total_current_value = 0
    total_invest = 0
    counter = 1

    for web_pos in (range(0, 1100)):
        for dict_pos in your_coin:
            if api['data'][web_pos]['symbol'] == dict_pos[1]:
                total_amount_invested = dict_pos[2] * dict_pos[3]
                current_value_f = dict_pos[2] * api['data'][web_pos]['quote']['USD']['price']
                pl_per_coin = api['data'][web_pos]['quote']['USD']['price'] - dict_pos[3]
                total_pl_per_coin = pl_per_coin * dict_pos[2]

                general_pl += total_pl_per_coin
                total_current_value += current_value_f
                total_invest += total_amount_invested

                portfolio_id_f = Label(pycripto, text=dict_pos[0], bg='#E8DAEF', fg='black', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
                portfolio_id_f.grid(row=counter, column=0, sticky=N + S + E + W)

                coin_name_f = Label(pycripto, text=api['data'][web_pos]['name'], bg='#E8DAEF', fg='black', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
                coin_name_f.grid(row=counter, column=1, sticky=N + S + E + W)

                price_f = Label(pycripto, text='$ {:.4f}'.format(api['data'][web_pos]['quote']['USD']['price']), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                price_f.grid(row=counter, column=2, sticky=N + S + E + W)

                n_coins_f = Label(pycripto, text='{:.2f}'.format(dict_pos[2]), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                n_coins_f.grid(row=counter, column=3, sticky=N + S + E + W)

                amount_paid_f = Label(pycripto, text='$ {:.2f}'.format(total_amount_invested), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                amount_paid_f.grid(row=counter, column=4, sticky=N + S + E + W)

                current_value_f = Label(pycripto, text='$ {:.2f}'.format(current_value_f), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                current_value_f.grid(row=counter, column=5, sticky=N + S + E + W)

                pl_coin_f = Label(pycripto, text='$ {:.2f}'.format(pl_per_coin), bg='#E8DAEF', fg=font_color(float('{:.2f}'.format(pl_per_coin))), font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                pl_coin_f.grid(row=counter, column=6, sticky=N + S + E + W)

                pl_total_f = Label(pycripto, text='$ {:.2f}'.format(total_pl_per_coin), bg='#E8DAEF', fg=font_color(float('{:.2f}'.format(total_pl_per_coin))), font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                pl_total_f.grid(row=counter, column=7, sticky=N + S + E + W)

                counter += 1  # increase row number

    total_invest_f = Label(pycripto, text='$ {:.2f}'.format(total_invest), bg='#E8DAEF', fg='black', font='Lato 12', borderwidth=2, relief='groove')
    total_invest_f.grid(row=counter, column=4, sticky=N + S + E + W)

    total_current_value_f = Label(pycripto, text='$ {:.2f}'.format(total_current_value), bg='#E8DAEF', fg='black', font='Lato 12', borderwidth=2, relief='groove')
    total_current_value_f.grid(row=counter, column=5, sticky=N + S + E + W)

    pl_total_f = Label(pycripto, text='$ {:.2f}'.format(general_pl), bg='#E8DAEF', fg=font_color(float('{:.2f}'.format(general_pl))), font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    pl_total_f.grid(row=counter, column=7, sticky=N + S + E + W)

    api = ''  # resets api information

    refresh = Button(pycripto, text='REFRESH!', command=my_portfolio, bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    refresh.grid(row=counter + 1, column=7, sticky=N + S + E + W)


def app_header():
    portfolio_id = Label(pycripto, text='Portfolio ID', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    portfolio_id.grid(row=0, column=0, sticky=N+S+E+W)

    coin_name = Label(pycripto, text='Coin Name', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    coin_name.grid(row=0, column=1, sticky=N+S+E+W)

    price = Label(pycripto, text='Price', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    price.grid(row=0, column=2, sticky=N+S+E+W)

    n_coins = Label(pycripto, text='Coins Owned', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    n_coins.grid(row=0, column=3, sticky=N+S+E+W)

    amount_paid = Label(pycripto, text='Total Amount Paid', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    amount_paid.grid(row=0, column=4, sticky=N+S+E+W)

    current_value = Label(pycripto, text='Current Value', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    current_value.grid(row=0, column=5, sticky=N+S+E+W)

    pl_coin = Label(pycripto, text='P/L Per Coin', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    pl_coin.grid(row=0, column=6, sticky=N+S+E+W)

    pl_total = Label(pycripto, text='Total P/L', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    pl_total.grid(row=0, column=7, sticky=N+S+E+W)


app_header()
my_portfolio()

pycripto.mainloop()     # keeps the window open

cursor_obj.close()  # close connection with database
connection.close()
