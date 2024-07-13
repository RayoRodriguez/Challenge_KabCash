from ledger import Ledger, Transaction

def test_ledger_balance_loan():
    loanA = "loanA"

    ledger = Ledger([
        Transaction(
            loan_id=loanA,
            amount=100,
            transaction_type="CREATE_LOAN"
        ),
        Transaction(
            loan_id=loanA,
            amount=10,
            transaction_type="LOAN_PAYMENT"
        ),
        Transaction(
            loan_id=loanA,
            amount=80,
            transaction_type="LOAN_PAYMENT"
        )
    ])
    ledger.execute_transactions()
    assert ledger.get_loan_receivable(loanA) == 10


def test_total_debt():
    loanA = "loanA"
    loanB = "loanB"
    loanC = "loanC"
    ledger = Ledger([
        # Loan A gets created, plus we add a payment
        Transaction(
            loan_id=loanA,
            amount=100,
            transaction_type="CREATE_LOAN"
        ),
        Transaction(
            loan_id=loanA,
            amount=10,
            transaction_type="LOAN_PAYMENT"
        ),
        # Loan B gets created
        Transaction(
            loan_id=loanB,
            amount=300,
            transaction_type="CREATE_LOAN"
        ),
        # Loan C gets created, plus we add a payment
        Transaction(
            loan_id=loanC,
            amount=400,
            transaction_type="CREATE_LOAN"
        ),
        Transaction(
            loan_id=loanC,
            amount=40,
            transaction_type="LOAN_PAYMENT"
        ),
    ])
    # Nothing should execute before running transactions
    assert ledger.get_total_loans_receivable() == 0

    # Now we execute transactions
    ledger.execute_transactions()

    # Now we check total loan balance
    assert ledger.get_total_loans_receivable() == 750

    # Now check individual loan balances
    assert ledger.get_loan_receivable(loanA) == 90
    assert ledger.get_loan_receivable(loanC) == 360


if __name__=="__main__":
    test_ledger_balance_loan()
    test_total_debt()