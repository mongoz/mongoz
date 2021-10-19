food_price = float(input("Стоимость еды в ресторане: "))
tip = food_price*0.18
tax = food_price*0.07
total = food_price + tip + tax
print(f"Цена еды: ${food_price:.2f}\n"
      f"Чаевые: ${tip:.2f}\n"
      f"Налог с продаж: ${tax:.2f}\n"
      f"Итоговая сумма: ${total:.2f}")
