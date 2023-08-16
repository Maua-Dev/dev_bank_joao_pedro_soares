from typing import Dict, Optional, List

# from ..enums.item_type_enum import ItemTypeEnum
from ..entities.item import Cliente
from .item_repository_interface import IItemRepository

 
class ItemRepositoryMock(IItemRepository):
     clientes: Dict[int, Cliente]
    
     def __init__(self):
        self.clientes = {
             Cliente(name="Vitor Soller",agency="0000",account="0000-0",current_balance=1000.0,cliente_id=1),
             Cliente(name="João Brancas",agency="0001",account="0000-1",current_balance=1001.0,cliente_id=2),
             Cliente(name="Rodrigo",agency="0002",account="0000-2",current_balance=1002.0,cliente_id=3),
             Cliente(name="Pedro",agency="0003",account="0003-0",current_balance=1003.0,cliente_id=4)
        }
        
     def get_all_items(self) -> List[Cliente]:
        return self.clientes
    
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
        
    
    