#INSTRUCTIONS

The simplest way to keep track of your personal budget is to record all income and expenses.
Please write a book-keeping program that helps you with this task. It should be able to record
transactions and give you an overview of your budget. Further, the program should be able
to:

- Read a file of previous transactions from disk
- Write additional transactions to the file
- The file is structured to include a description, the amount and the date of the
transaction
 - You can choose txt, csv, json or xlsx as format for the transaction file
INTERACTION:
- Your program should ask the user what it should do next (record a transaction,
calculate the current budget or exit the program)
- Transaction
- Your program should ask the user to insert the description, the date and
the amount of a transaction (positive for income, negative for expenses)
- Your program reacts with a confirmation that the transaction has been
saved to file and returns the current budget
- Bonus: The user is able to insert multiple transactions at once
CURRENT BUDGET:
- Your program returns the current budget and the last 10 transactions
- Bonus: The user can specify how many transactions the program should
return
- Bonus: The user can specify a date range for the transactions to be
returned (e.g. all transactions in January 2021)
- Exit the program
- The program shuts down gracefully without any error messages

The program should be standalone and executable from a standard computer
with minimal amount of dependencies. The transaction file should be saved in the same
directory. The interaction can be via a graphical user interface or a terminal.
