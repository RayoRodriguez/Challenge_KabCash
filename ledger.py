class Ledger(object):
    def __init__(self, transaction_list):
        self.transaction_list = transaction_list

    def execute_transactions(self):
        for transaction in self.transaction_list:
            transaction.execute()

    def get_loan_receivable(self, loan):
        for row in Transaction.bd_transactions:
            if row.get("loan_id") == loan:
                return row.get("amount")

    def get_total_loans_receivable(self):
        result = 0
        if not Transaction.bd_transactions:
            return result
        else:
            for row in Transaction.bd_transactions:
                result = result + row.get("amount")
            return result


class Transaction(object): 
    bd_transactions = []   

    def __init__(self, loan_id, amount, transaction_type):
        self.loan_id = loan_id
        self.amount = amount
        self.transaction_type = transaction_type
        
    def execute(self):
        if self.transaction_type == "CREATE_LOAN":
            self.create()
        if self.transaction_type == "LOAN_PAYMENT":
            self.payment()

    def create(self):
        """ Codigo para agrupar el amount si es que ya existe el usuario """
        
        #if not Transaction.bd_transactions:
        #    loan_data = {
        #        "loan_id": self.loan_id,
        #        "amount": self.amount
        #    }
        #    Transaction.bd_transactions.append(loan_data)
        #else:
        #    for loan in Transaction.bd_transactions:
        #        if loan.get('loan_id') == self.loan_id:
        #            loan['amount'] = loan.get('amount') + self.amount
        #            break

        """ Codigo para agregar todos los nuevos prestamos a la BD """
        loan_data = {
            "loan_id": self.loan_id,
            "amount": self.amount
        }
        Transaction.bd_transactions.append(loan_data)

    def payment(self):
        for loan in Transaction.bd_transactions:
            if loan.get('loan_id') == self.loan_id:
                loan['amount'] = loan.get('amount') - self.amount
                break


     
