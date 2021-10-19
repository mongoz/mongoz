TAX = 0.07  # налог с продаж

# _цена товаров________________
price_1 = float(input("Введите цену 1-го товара: "))
price_2 = float(input("Введите цену 2-го товара: "))
price_3 = float(input("Введите цену 3-го товара: "))
price_4 = float(input("Введите цену 4-го товара: "))
price_5 = float(input("Введите цену 5-го товара: "))

# _Цена на товары без налога_
total_price = price_1 + price_2 + \
              price_3 + price_4 + \
              price_5

# _сумма налога на покупки
total_tax2 = total_price*TAX

# итоговая сумма с налогом
total = total_price + total_tax2

print(f"Цена без налога ${total_price:.2f}\n"
      f"Cумма налога ${total_tax2:.2f}\n"
      f"Итоговая сумма: ${total:.2f}")
