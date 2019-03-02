from threading import Thread
import requests
from kivy.app import App
from kivy.uix.widget import Widget


class MainWindow(Widget):

    def check_price(self):
        self.button.text = 'Checking price now...'
        self.button.background_color = (.8, .1, .1, 1)
        bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'

        data = requests.get(bitcoin_price_url).json()

        price_in_usd = data['bpi']['USD']['rate']
        self.price_text.text = "$" + price_in_usd
        self.button.text = 'Check price'
        self.button.background_color = (.2, 1, .2, 1)

    def update_price_text(self):
        Thread(target=self.check_price).start()


class BitcoinCheckerApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window


if __name__ == '__main__':
    app = BitcoinCheckerApp()
    app.run()
