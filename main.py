from tkinter import *
import requests
import json

pycripto = Tk()
pycripto.title('Crypto Portfolio')


def my_portfolio():
    api_request = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=1100'
                               '&convert=USD&CMC_PRO_API_KEY=49cb1569-1049-46d0-8358-37a8addc8c2b')

    api = json.loads(api_request.content)

    print('-' * 20)
    print('-' * 20)

    coin_dictionary = [
        {'symbol': 'CS',
         'amount_owned': 351.824466,
         'price_per_coin': 0.54356651819},

        {'symbol': 'ETH',
         'amount_owned': 1.843336056777777776,
         'price_per_coin': 103.746682162}
    ]

    general_pl = 0

    for web_pos in (range(0, 1100)):
        for dict_pos in coin_dictionary:
            if api['data'][web_pos]['symbol'] == dict_pos['symbol']:
                total_amount_invested = dict_pos['amount_owned'] * dict_pos['price_per_coin']
                current_value = dict_pos['amount_owned'] * api['data'][web_pos]['quote']['USD']['price']
                pl_per_coin = api['data'][web_pos]['quote']['USD']['price'] - dict_pos['price_per_coin']
                total_pl_per_coin = pl_per_coin * dict_pos['amount_owned']

                general_pl = general_pl + total_pl_per_coin

                print(api['data'][web_pos]['name'], ' - ', api['data'][web_pos]['symbol'])
                print('Price - {:.4f}'.format(api['data'][web_pos]['quote']['USD']['price']), 'USD')
                print('Number of the coin - {}'.format(web_pos))
                print('Total amount paid: {}'.format(total_amount_invested), 'USD')
                print('Current value: {:.4f}'.format(current_value), 'USD')
                print('P/L per coin: {:.2f}'.format(pl_per_coin), 'USD')
                print('P/L total - {:.2f}'.format(total_pl_per_coin), 'USD')
                print('-' * 20)

    print('-' * 20)
    print('General P/L: {:.2f}'.format(general_pl), 'USD')


coin_name = Label(pycripto, text='Coin Name', bg='gray', fg='black')
coin_name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycripto, text='Price', bg='white', fg='black')
price.grid(row=0, column=1, sticky=N+S+E+W)

n_coins = Label(pycripto, text='Coins Owned', bg='grey', fg='black')
n_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycripto, text='Total Amount Paid', bg='white', fg='black')
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_value = Label(pycripto, text='Current Value', bg='grey', fg='black')
current_value.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycripto, text='P/L Per Coin', bg='white', fg='black')
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

pl_total = Label(pycripto, text='Total P/L', bg='grey', fg='black')
pl_total.grid(row=0, column=6, sticky=N+S+E+W)


pycripto.mainloop()     # keeps the window open
