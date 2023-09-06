from typing import Dict, Optional, List
import time
# from ..enums.item_type_enum import ItemTypeEnum
from ..entities.transaction import Transaction
from .transaction_repository_interface import TransactionRepository

 
class TransactionRepositoryMock(TransactionRepository):
     transactions: list[Transaction]

     
     def __init__(self):
        self.transactions = [
     Transaction("deposit", 108.00, 567.00, int(round(time.time() * 1000))),
            Transaction("withdraw", 5.50, 123.00,int(round(time.time() * 1000))),
        ]
   
        
     def get_all_transactions(self) -> List[Transaction]:
        return self.transactions  
    
     def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions.append(transaction)
        return transaction
        
        
           
          


#     def get_item(self, item_id: int) -> Optional[Item]:
#         return self.items.get(item_id, None)
    
#     def create_item(self, item: Item, item_id: int) -> Item:
        
#         self.items[item_id] = item
#         return item
    
#     def delete_item(self, item_id: int) -> Item:
#         item = self.items.pop(item_id, None)
#         return item
        
        
#     def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#         item = self.items.get(item_id, None)
#         if item is None:
#             return None
        
#         if name is not None:
#             item.name = name
#         if price is not None:
#             item.price = price
#         if item_type is not None:
#             item.item_type = item_type
#         if admin_permission is not None:
#             item.admin_permission = admin_permission
#         self.items[item_id] = item
        
#         return item
        
    
    