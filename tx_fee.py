#globals

transaction_list = []
header = False

class Transaction:
    total_fees = 0.0
    max_fee = 0.0
    min_fee = float('inf')
    num_tx = 0

    def __init__(self, hash, block_num, date_time, receiver, fee, method):
        self.hash = hash
        self.block_num = block_num
        self.date_time = date_time
        self.receiver = receiver
        self.fee = fee
        self.method = method

        Transaction.total_fees += self.fee
        Transaction.num_tx += 1

        if self.fee < Transaction.min_fee:
            Transaction.min_fee = self.fee
        
        if self.fee > Transaction.max_fee:
            Transaction.max_fee = self.fee
    
    def display(self):
        return f'|{self.hash:<70s}|{self.block_num:<15d}|{self.date_time:25s}|{self.receiver:45s}|{self.fee:<15f}|{self.method:20s}|'

    @classmethod
    def total_fee(cls):
        return cls.total_fees

    @classmethod
    def compute_average_fees(cls):
        if cls.num_tx > 0:
            avg = cls.total_fees / cls.num_tx
        else:
            avg = None
        
        return avg
    
    @classmethod
    def summary_string(cls):
        avg_fees = cls.compute_average_fees()
        output_str = cls.line(65) + f'\n|{"Total Fees":<15s}|{"Max Fees":<15s}|{"Mininum Fees":<15s}|{"Average Fees":<15s}|\n' + cls.line(65)
        output_str += f'\n|{cls.total_fees:<15f}|{cls.max_fee:<15f}|{cls.min_fee:<15f}|{avg_fees:<15f}|\n' + cls.line(65)
        return output_str

    @staticmethod
    def header():
        return Transaction.line() + f'\n|{"Tx hash":<70s}|{"Block Number":<15s}|{"Date/Time":25s}|{"Receiver":45s}|{"Fees (ETH)":<15s}|{"Method":20s}|\n' + Transaction.line()
    
    @staticmethod
    def line(multiplier = 197):
        return '-' * multiplier

#functions
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

    if not transaction_list:
        print('No data!')
        return

    print(Transaction.header())
    
    for transaction in transaction_list:
        print(transaction.display())
    
    print(Transaction.line())

def summary():
    global transaction_list
    
    if not transaction_list:
        print('No data!')
        return
    
    print(Transaction.summary_string())

#main
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