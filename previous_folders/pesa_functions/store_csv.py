def store_data_csv(current_date, fund_type, fund_size, purpose, net_fund_size):
    "Store the following items into a csv file "
    # data items are : current_date, fund_type, fund_size, purpose, net_fund_size
    current_date = str(current_date)

    data = str(current_date) + "," + str(fund_type) + "," + str(fund_size) + "," + str(purpose) + "," + \
           str(net_fund_size) + "\n"

    with open("Kiplelgo_funds_record.csv", "a") as f:
        f.write(data)
