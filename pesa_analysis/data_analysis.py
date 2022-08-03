
def select_month():
    """select the month to display  """
    # months dictionary
    year = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
            11: "Nov", 12: "Dec"}

    # list index in year dictionary
    available_months = list(year)

    print("\n*********************** KIPLELGO FINANCIAL REPORT**************************")

    # loop through the month
    for months in year:
        print(f"{months}.{year[months]}" , end=" ")

    # check if selected month is in the dictionary
    correct = True
    while correct:
        print("\n")
        select = int(input("Select your month of Choice: "))
        if select in available_months:
            return select
        else:
            print("selected month not available")
            correct = False


def compound_fund_uses(month):
    """ Compound all the fund uses identified by the user for the selected month """
    import csv

    # year dictionary

    year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
            9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER"}

    # variables representing the sum of their respective representatives
    TOTAL = 0
    TRANSPORT = 0
    LUNCH = 0
    BREAKFAST = 0
    CREDIT = 0
    CSR = 0
    THANKSGIVING = 0
    BUNDLES = 0
    NHIF = 0
    CLOTHES = 0
    KINYOZI = 0
    WITHDRAWN = 0
    INVESTMENT = 0
    SUPPER = 0
    ARTEFACTS = 0
    SHOPPING = 0
    RETREAT = 0


    # Abstract the 2d list from the csv to be used for analysis

    with open("Kiplelgo_funds_record.csv", "r") as f:
        iterable = csv.reader(f)
        # 2d list
        dd_list = list(iterable)

        # Establish the month for data to be analyzed

        for item in dd_list:
            # Month of transaction (item) determined
            date = list(item[0])

            # date format : 2022-02-09 ; abstract [02] from date and concatenate to form month
            month_from_date = date[5] + date[6]
            month_from_date = int(month_from_date)

            # Filter data based on your selected month
            if month_from_date == month:
                # Total expenditure determined
                if item[1] == "EXPENDITURE":
                    TOTAL += int(item[2])
                if item[3] == "TRANSPORT":
                    TRANSPORT += int(item[2])
                if item[3] == "LUNCH":
                    LUNCH += int(item[2])
                if item[3] == "BREAKFAST":
                    BREAKFAST += int(item[2])
                if item[3] == "CREDIT":
                    CREDIT += int(item[2])
                if item[3] == "CSR":
                    CSR += int(item[2])
                if item[3] == "THANKSGIVING":
                    THANKSGIVING += int(item[2])
                if item[3] == "BUNDLES":
                    BUNDLES += int(item[2])
                if item[3] == "NHIF":
                    NHIF += int(item[2])
                if item[3] == "CLOTHES":
                    CLOTHES += int(item[2])
                if item[3] == "NHIF":
                    NHIF += int(item[2])
                if item[3] == "KINYOZI":
                    KINYOZI += int(item[2])
                if item[3] == "WITHDRAWN":
                    WITHDRAWN += int(item[2])
                if item[3] == "INVESTMENT":
                    INVESTMENT += int(item[2])
                if item[3] == "SUPPER":
                    SUPPER += int(item[2])
                if item[3] == "ARTEFACTS":
                    ARTEFACTS += int(item[2])
                if item[3] == "SHOPPING":
                    SHOPPING += int(item[2])
                if item[3] == "RETREAT":
                    RETREAT += int(item[2])


        print(f"\nSUMMARY OF SPENDING IN THE MONTH OF {year[month]}\n")
        print(f"TOTAL: {TOTAL}")
        print(f"TRANSPORT: {TRANSPORT}")
        print(f"LUNCH: {LUNCH}")
        print(f"BREAKFAST: {BREAKFAST}")
        print(f"CREDIT: {CREDIT}")
        print(f"CSR: {CSR}")
        print(f"THANKSGIVING: {THANKSGIVING}")
        print(f"BUNDLES: {BUNDLES}")
        print(f"NHIF: {NHIF}")
        print(f"CLOTHES: {CLOTHES}")
        print(f"KINYOZI: {KINYOZI}")
        print(f"WITHDRAWN: {WITHDRAWN}")
        print(f"INVESTMENT: {INVESTMENT}")
        print(f"SUPPER: {SUPPER}")
        print(f"ARTEFACTS: {ARTEFACTS}")
        print(f"SHOPPING: {SHOPPING}")
        print(f"RETREAT: {RETREAT}")

        print(f"\nPERCENTAGES OF EXPENDITURE {year[month]}")
        print(f"TRANSPORT:{round(TRANSPORT / TOTAL * 100, 2)}%")
        print(f"LUNCH:{round(LUNCH / TOTAL * 100, 2)}%")
        print(f"BREAKFAST:{round(BREAKFAST / TOTAL * 100, 2)}%")
        print(f"CREDIT:{round(CREDIT / TOTAL * 100, 2)}%")
        print(f"CSR:{round(CSR / TOTAL * 100, 2)}%")
        print(f"THANKSGIVING:{round(THANKSGIVING / TOTAL * 100, 2)}%")
        print(f"BUNDLES:{round(BUNDLES / TOTAL * 100, 2)}%")
        print(f"NHIF:{round(NHIF / TOTAL * 100, 2)}%")
        print(f"CLOTHES:{round(CLOTHES / TOTAL * 100, 2)}%")
        print(f"KINYOZI:{round(KINYOZI / TOTAL * 100, 2)}%")
        print(f"WITHDRAWN:{round(WITHDRAWN / TOTAL * 100, 2)}%")
        print(f"INVESTMENT:{round(INVESTMENT / TOTAL * 100, 2)}%")
        print(f"SUPPER:{round(SUPPER / TOTAL * 100, 2)}%")
        print(f"ARTEFACTS:{round(ARTEFACTS / TOTAL * 100, 2)}%")
        print(f"SHOPPING:{round(SHOPPING / TOTAL * 100, 2)}%")
        print(f"RETREAT:{round(RETREAT / TOTAL * 100, 2)}%")