def extract_date ():
    """generate the date object at time of the recording"""
    global current_date
    from datetime import date
    print()
    print("date_of_transaction")
    print("***************************************************")
    print( "1) Today's date\n"
          "2) Custom date")
    print("___________________________________________________")
    user_option = int(input("insert: "))
    print("***************************************************")

    if user_option == 1:
        current_date = date.today()

    elif user_option == 2:
        custom_date = int(input("date:"))
        custom_month = int(input("month:"))
        custom_year = int(input("year:"))
        print("***************************************************")

        current_date = date(custom_year, custom_month, custom_date)

    # format date to string format
    current_date =current_date.strftime('%Y-%m-%d %H:%M:%S')
    
    return current_date

if __name__ == "__main__":
    date = extract_date()
    print(date)

