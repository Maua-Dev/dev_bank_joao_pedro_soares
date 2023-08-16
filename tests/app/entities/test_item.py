import pytest
# from src.app.entities.item import Item
# from src.app.enums.item_type_enum import ItemTypeEnum
# from src.app.errors.entity_errors import ParamNotValidated

    
from src.app.entities.item import Cliente
from src.app.errors.entity_errors import ParamNotValidated



class Test_Item:
    def test_item(self):
        cliente = Cliente(name="Vitor Soller", agency="0000",account= "00000-0",current_balance= 1000.0,cliente_id= 1)

        assert cliente.name=="Vitor Soller"
        assert cliente.agency=="0000"
        assert cliente.account== "00000-0"
        assert cliente.current_balance== 1000.0
        assert cliente.cliente_id== 1    

    def test_item_agencia_errada(self):
        name="Vitor Soller"
        with pytest.raises(ParamNotValidated):
          cliente = Cliente(name, agency="00000",account= "00000-0",current_balance= 1000.0,cliente_id= 1)

       

#         item = Item("test", 1.0, ItemTypeEnum.FOOD, admin_permission=True)
#         assert item.name == "test"
#         assert item.price == 1.0
#         assert item.item_type == ItemTypeEnum.FOOD
        
#     def test_item_dict(self):
#         item = Item("test", 1.0, ItemTypeEnum.FOOD, admin_permission=True)
#         assert item.to_dict() == {'admin_permission': True, 'item_type': 'FOOD', 'name': 'test', 'price': 1.0}
    
#     def test_item_name_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_name_is_not_string(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name=1.0, price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_name_is_too_short(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="te", price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_price_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_price_is_not_float(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price="1.0", item_type=ItemTypeEnum.FOOD, admin_permission=True)
#     def test_item_price_is_negative(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=-1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_type_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, admin_permission=True)
            
#     def test_item_type_is_not_enum(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, item_type="FOOD", admin_permission=True)
            
#     def test_item_admin_permission_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, item_type=ItemTypeEnum.FOOD)
        
#     def test_item_admin_permission_is_not_bool(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission="True")