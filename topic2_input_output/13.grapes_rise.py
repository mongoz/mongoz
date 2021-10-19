lenght_bed = int(input())
end_bear = int(input())
area = int(input())

quantity_grapes = (lenght_bed - (2*end_bear))/area
print(f"Количество виноградных лоз по заданным параметрам"
      f" = {int(quantity_grapes)}")