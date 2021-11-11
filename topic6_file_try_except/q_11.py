def main():
    name = input('Введи имя: ')
    description = input('Введи описание: ')
    write(name, description)


def write(name, description):
    file_html = open('x.html', 'w', encoding='utf-8')
    file_html.write(f"""<html>
    <head>
    </head>
    <body>
        <center>
            <hl>{name}</hl>
        </center>
        <hr />
        {description}
        <hr />
    </body>
    </html>""")


main()
