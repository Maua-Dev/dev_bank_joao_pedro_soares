from typing import Any
from app.entities.transaction import Transaction
from app.repo.transaction_repository_interface import TransactionRepository
from src.app.entities import transaction

class CreateTransactionViewModel:
    type: str
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, transaction: Transaction):
        self.type = transaction.type
        self.value = transaction.value
        self.current_balance = transaction.current_balance
        self.timestamp = transaction.timestamp
    
    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp,
            "message": "Transaction created successfully"
        }
