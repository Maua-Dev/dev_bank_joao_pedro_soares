from typing import Any
from app.entities.transaction import Transaction
from app.repo.transaction_repository_interface import TransactionRepository
from src.app.entities import transaction


class CreateTransactionUseCase:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo
    def __call__(self, type: str, value: float, current_balance: float,   timestamp: float):
        return self.repo.create_transaction(type=type,value=value,current_balance=current_balance,timestamp=timestamp)
    

