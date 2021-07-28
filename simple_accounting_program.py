import csv
import time
from datetime import datetime, date

opened_file = open("accounting_sheet.csv")
read_file = csv.reader(opened_file)
transaction_data = list(read_file)
headers = transaction_data[0]

#main user navigation panel
def activity():
     while True:   
        print_pause('To run the program enter:\n')
        choice = input( "1 - to record a new transaction\n"
                            "2 - to show the latest budget\n"
                            "3 - to quit the program\n"
                            "\n")
        if choice == '1':
            new_transaction()
            current_budget()

        elif choice == '2':
            current_budget()
            past_transactions()
        elif choice == '3':
            print_line(50)
            print_pause('Thank you for using our accounting system. Until ne!')
            print_line(50)
            break
        else:
            print('Not a valid choice! Please enter a number between 1-3.')
            continue
#records new transactions in the CSV file on a disk
def new_transaction():
    print('NEW TRANSACTION DETAILS\n')
    while True:
        row_list = []
        while True:
            description = str(input('Description: '))
            while True:
                try:
                    amount = float(input("Amount in EUR: "))
                except ValueError:
                    print("!Amount must be a number. Please try again!")
                else:
                    break
            allowed_date_formats = ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y")
            while True:
                transaction_date = str(input('Date: ')).strip()
                transaction_date_dt = input_date(transaction_date)
                if transaction_date_dt is False:
                    continue
                else:
                    break

            transaction_date_str = datetime.strftime(transaction_date_dt, "%d/%m/%Y")
            # print(date_output)
            row = [description,amount,transaction_date_str]
            row_list.append(row)
            print_line()
            another_transaction = input('Record another transaction? Y/N: ').strip().lower()
            if another_transaction in ('n','no'):
                break
            else:
                continue
            break
        break
    # print(row_list)
    with open('accounting_sheet.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        for i in row_list:
            writer.writerow(i)
    if len(row_list) > 1:
        print_line()
        print("Your transactions were recorded successfully.")
    else:
        print_line()
        print("Your transaction was recorded successfully.")
#returns the latest budget recorded in the CSV file
def current_budget():
    sum_budget = 0
    with open('accounting_sheet.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            sum_budget += round(float(row[1]), 2)
    print_line()
    print(f"The current budget is {sum_budget} EUR")
    print_line()
#returns a number transactions within a date range, both specified by a user
def past_transactions(latest=10):

    #user input of No. of transactions to view, and date range
    print("SPECIFY TRANSACTIONS TO DISPLAY\n")    
    while True:
        try:
            latest = int(input("How many latest transactions do you wish to view?: "))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    while True:
        date_from = str(input("Date from: ")).strip()
        date_from_dt = input_date(date_from)
        if date_from_dt is False:
            continue
        else:
            break
    while True:
        date_until = str(input("Date until: ")).strip()
        date_until_dt = input_date(date_until)
        if date_until_dt is False:
            continue
        else:
            break
        
    transactions = []
    with open('accounting_sheet.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            date = row[2]
            date_dt = datetime.strptime(date ,"%d/%m/%Y")
            if date_from_dt <= date_dt <= date_until_dt:
                transactions.append(row)
    print_line(50)        
    headers.insert(0, '#')
    print(*headers, sep=' | ')
    print(' ')
    transaction_no = 0
    while True:
        for i in transactions[-(latest):]:
            transaction_no+=1
            i.insert(0, str(transaction_no)+'.')
            print(*i, sep=' | ')
        break
    print_line(50)
    print_pause(f"The total no. of transactions recorded in the selected date range: {len(transactions)}\n")
#checks whether the date string input is in a valid date format, if valid, returns datetime variable
def input_date(userdate):
    allowed_date_formats = ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y")
    check_date = False
    for i in allowed_date_formats:
        try:
            date_dt = datetime.strptime(userdate, i)
            check_date = True
        except ValueError:
            check_date = False
            pass
        else:
            break
    if check_date is False:
        print("No valid date format found. Please enter the date again.")
        return False
    else:
        userdate_str = datetime.strftime(date_dt, "%d/%m/%Y")
        userdate = datetime.strptime(userdate_str, "%d/%m/%Y")
        return userdate
#prints messages with delay of 1 second
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)
#prints line to visually separate results in terminal
def print_line(length=40):
    print('-'*length)
#runs main user navigation panel
activity()