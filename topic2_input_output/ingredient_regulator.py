sugar48 = 1.5
butter48 = 1
flour48 = 2.75
cookies48 = 48
user_cookies = int(input("Сколько хотите булочек? "))
sugar = (user_cookies * sugar48) / cookies48
butter = (user_cookies * butter48) / cookies48
flour48 = (user_cookies * flour48) / cookies48
print(f"Количество булочек: {user_cookies}\n"
      f"Cахар = {sugar:.2f} стакана.\n"
      f"Масло = {butter:.2f} cтакана.\n"
      f"Мука = {flour48:.2f} cтакана.")