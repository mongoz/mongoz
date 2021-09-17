FEE = 0.03  # налог
stock = 2000
stock_price_buy = 40.00  # цена с налогом при покупке
stock_price_sell = 42.75  # цена с налогом при продаже

# Цена за покупку акций с налогом
general_stock_buy = stock * stock_price_buy

# Комиссия брокеру за покупку акций
broker_buy_fee = general_stock_buy * FEE

# Цена за продажу акций с налогом
general_stock_sell = stock * stock_price_sell

# Комиссия брокеру за продажу акций
broker_sell_fee = general_stock_sell * FEE

# Cумма денег, которая осталась у Джона после покупки/продажи (налог+)
balance = general_stock_sell - general_stock_buy

print(f"Цена за покупку акций (налог+) = {general_stock_buy}$\n"
      f"Цена за продажу акций (налог+) = {general_stock_sell}$\n"
      f"Комиссия брокеру за покупку акций = {broker_buy_fee:.2f}$\n"
      f"Комиссия брокеру за продажу акций = {broker_sell_fee:.2f}$")

if balance > 0:
    print(f"Баланс = {balance:.2f}\nДжо в плюсе!")
else:
    print(f"Баланс = {balance:.2f}\nДжо в минусе!")
