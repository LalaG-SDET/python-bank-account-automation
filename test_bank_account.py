import pytest
from bank_account import BankAccount

@pytest.fixture
def account():
    return BankAccount("Müştəri", 100)

def test_initial_balance(account):
    assert account.show_balance() == 100

def test_deposit(account):
    assert account.deposit(50) == 150

def test_withdraw(account):
    assert account.withdraw(30) == 70

def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError, match="Kifayət qədər vəsait yoxdur"):
        account.withdraw(200)
