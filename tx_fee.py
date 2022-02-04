#globals
transaction_list = []
header = False

class Transaction:
    total_fees = 0.0

    def __init__(self, hash, block_num, date_time, receiver, fee, method):
        self.hash = hash
        self.block_num = block_num
        self.date_time = date_time
        self.receiver = receiver
        self.fee = fee
        self.method = method

        Transaction.total_fees += self.fee
    
    def display(self):
        return f'|{self.hash:>70s}|{self.block_num:>10d}|{self.date_time:>25s}|{self.receiver:>45s}|{self.fee:>10f}|{self.method:>15s}|'

    def header(self):
        return f'|{"Tx hash":>70s}|{"Block Number":>10d}|{"Date/Time":>25s}|{"Receiver":>45s}|{"Fees (ETH)":>10f}|{"Method":>15s}|'
    
    @classmethod
    def total_fee(cls):

        return cls.total_fees

#function
def load():
    with open('txinputs.csv', 'r') as infile:
        lines = infile.readlines()
    
    for line in lines:
        process_line(line)

    transactions_loaded = len(lines) - 1
    print(f'Total of {transactions_loaded:d} transactions loaded.')

def process_line(input_str):
    global transaction_list, header

    if not header:
        header = True
        return

    inlist = input_str.split(',')
    hash = inlist[0].strip('"')
    block_num = int(inlist[1].strip('"'))
    date_time = inlist[3]
    receiver = inlist[5].strip('"')
    fee = float(inlist[10].strip('"'))
    method = inlist[15].strip('"')

    transaction = Transaction(hash, block_num, date_time, receiver, fee, method)
    transaction_list.append(transaction)

def display():
    global transaction_list
    
    for transaction in transaction_list:
        print(transaction.display())

def summary():
    print('Under construction')

#main

print('Total Fees spent: ', Transaction.total_fee(),'ETH')
quit = False
while not quit:
    print('1.Load 2.Summary 3.Display 4.Quit')
    choice = int(input('Enter choice: '))

    if choice == 1:
        load()
    elif choice == 2:
        summary()
    elif choice == 3:
        display()
    elif choice == 4:
        quit = True
    else:
        print('Invalid Choice!')