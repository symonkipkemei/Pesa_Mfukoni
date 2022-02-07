def extract_date ():
    """generate the date object at time of the recording"""
    global current_date
    from datetime import date
    print("Insert \n"
          "1) Today's date\n"
          "2) Custom date")

    user_option = int(input("insert: "))

    if user_option == 1:
        current_date = date.today()

    elif user_option == 2:
        custom_date = int(input("date:"))
        custom_month = int(input("month:"))
        custom_year = int(input("year"))

        current_date = date(custom_year, custom_month, custom_date)
    return current_date
