m_pocket = int(input('Масса пакета в граммах: '))

if m_pocket <= 200:
    print('Цена 150р.')
elif 200 < m_pocket <= 600:
    print('Цена 300р.')
elif 600 < m_pocket <= 1000:
    print('Цена 400р.')
elif m_pocket > 1000:
    print('Цена 475р.')
