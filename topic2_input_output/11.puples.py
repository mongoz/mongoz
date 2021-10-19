girls = int(input())
guys = int(input())
SUM = girls + guys
percent_gls = (girls/SUM)*100
percent_guys = (guys/SUM)*100
print(f"Количество мальчиков = {guys}\n"
      f"Количество девочек = {girls}\n"
      f"Всего учеников = {SUM}\n"
      f"Процент девушек в классе = {percent_gls:.0f}%\n"
      f"Процент мальчиков в классе {percent_guys:.0f}%\n")
