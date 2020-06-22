from tkinter import *
import requests
import json

pycripto = Tk()
pycripto.title('Crypto Portfolio')

pycripto.iconbitmap('coin.ico')


def font_color(number):
    if number >= 0:
        return 'green'
    else:
        return 'red'


def my_portfolio():
    api_request = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=1100'
                               '&convert=USD&CMC_PRO_API_KEY=49cb1569-1049-46d0-8358-37a8addc8c2b')

    api = json.loads(api_request.content)

    coin_dictionary = [
        {'symbol': 'CS',
         'amount_owned': 351.824466,
         'price_per_coin': 0.54356651819},

        {'symbol': 'ETH',
         'amount_owned': 1.843336056777777776,
         'price_per_coin': 103.746682162}
    ]

    total_current_value = 0
    general_pl = 0
    counter = 1

    for web_pos in (range(0, 1100)):
        for dict_pos in coin_dictionary:
            if api['data'][web_pos]['symbol'] == dict_pos['symbol']:
                total_amount_invested = dict_pos['amount_owned'] * dict_pos['price_per_coin']
                current_value_f = dict_pos['amount_owned'] * api['data'][web_pos]['quote']['USD']['price']
                pl_per_coin = api['data'][web_pos]['quote']['USD']['price'] - dict_pos['price_per_coin']
                total_pl_per_coin = pl_per_coin * dict_pos['amount_owned']

                general_pl = general_pl + total_pl_per_coin
                total_current_value += current_value_f

                coin_name_f = Label(pycripto, text=api['data'][web_pos]['name'], bg='#E8DAEF', fg='black', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
                coin_name_f.grid(row=counter, column=0, sticky=N + S + E + W)

                price_f = Label(pycripto, text='$ {:.4f}'.format(api['data'][web_pos]['quote']['USD']['price']), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                price_f.grid(row=counter, column=1, sticky=N + S + E + W)

                n_coins_f = Label(pycripto, text='{:.2f}'.format(dict_pos['amount_owned']), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                n_coins_f.grid(row=counter, column=2, sticky=N + S + E + W)

                amount_paid_f = Label(pycripto, text='$ {:.2f}'.format(total_amount_invested), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                amount_paid_f.grid(row=counter, column=3, sticky=N + S + E + W)

                current_value_f = Label(pycripto, text='$ {:.2f}'.format(current_value_f), bg='#E8DAEF', fg='black', font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                current_value_f.grid(row=counter, column=4, sticky=N + S + E + W)

                pl_coin_f = Label(pycripto, text='$ {:.2f}'.format(pl_per_coin), bg='#E8DAEF', fg=font_color(float('{:.2f}'.format(pl_per_coin))), font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                pl_coin_f.grid(row=counter, column=5, sticky=N + S + E + W)

                pl_total_f = Label(pycripto, text='$ {:.2f}'.format(total_pl_per_coin), bg='#E8DAEF', fg=font_color(float('{:.2f}'.format(total_pl_per_coin))), font='Lato 12', padx='5', pady='5', borderwidth=2, relief='groove')
                pl_total_f.grid(row=counter, column=6, sticky=N + S + E + W)

                counter += 1

    pl_total_f = Label(pycripto, text='$ {:.2f}'.format(general_pl), bg='#E8DAEF', fg=font_color(float('{:.2f}'.format(general_pl))), font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    pl_total_f.grid(row=counter, column=6, sticky=N + S + E + W)

    total_current_value_f = Label(pycripto, text='$ {:.2f}'.format(total_current_value), bg='#E8DAEF', fg='black', font='Lato 12', borderwidth=2, relief='groove')
    total_current_value_f.grid(row=counter, column=4, sticky=N + S + E + W)

    api= ''

    update = Button(pycripto, text='UPDATE!', command=my_portfolio, bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    update.grid(row=counter + 1, column=6, sticky=N + S + E + W)


coin_name = Label(pycripto, text='Coin Name', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
coin_name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycripto, text='Price', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
price.grid(row=0, column=1, sticky=N+S+E+W)

n_coins = Label(pycripto, text='Coins Owned', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
n_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycripto, text='Total Amount Paid', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_value = Label(pycripto, text='Current Value', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
current_value.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycripto, text='P/L Per Coin', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

pl_total = Label(pycripto, text='Total P/L', bg='#4B0082', fg='white', font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
pl_total.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycripto.mainloop()     # keeps the window open
