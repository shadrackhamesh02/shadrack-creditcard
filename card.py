#if-elif-else condition


print('Welcome to SBI Credit Card')
acc_no = input('Enter Account No: ')
days = int(input('Enter no of days missed for SBI Credit Card repayment: '))
due_amount = int(input('Enter Due Amount: '))
print('--------------Invoice--------------')
print('Account No:', acc_no)
print('Days Missed:', days)
print('Due Amount:', due_amount)

# Calculate fine amount

if days == 0:

    fine_amount = due_amount * 0 / 100

    print('Fine Amount:', fine_amount)

    print('Total Payable Amount:', due_amount + fine_amount)

elif 1 <= days <= 15:

    fine_amount = due_amount * 5 / 100

    print('Fine Amount:', fine_amount)

    print('Total Payable Amount:', due_amount + fine_amount)

elif 16 <= days <= 28:

    fine_amount = due_amount * 10 / 100

    print('Fine Amount:', fine_amount)

    print('Total Payable Amount:', due_amount + fine_amount)

else:

    print('Due date passed more than 20 days, contact Admin!...')

    print('Thank You for using SBI Credit Card')