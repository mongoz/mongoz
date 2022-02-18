def main():
    # get the date from the user.
    date = get_date()

    # convert date to like March 12, 2014
    literal_date, date_list = convert(date)
    print(date_list)
    print("The date is below.")
    print(literal_date)


def get_date():
    date = input("Enter the date as mm/dd/yyyy: ")
    return date


def convert(date):
    # first separate the string.
    date_list = date.split("/")

    # create a list for months.
    months = ['Январь', 'Февраль', 'Март',
              'Апрель', 'Май', 'Июнь', 'Июль',
              'Август', 'Сентябрь', 'Октябрь',
              'Ноябрь', 'Декабрь']

    # lets concatenate each value.
    # if month is entered as 01 it should be January. But January's index is 0.
    # that is why int(date_list[0]-1)
    new_date = str(months[int(date_list[0])-1]) + " " + str(date_list[1]) + "," + " " + str(date_list[2])
    return new_date, date_list


# call the main function
main()
