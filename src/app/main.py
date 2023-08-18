from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

# from .repo.item_repository_mock import ItemRepositoryMock

# from .errors.entity_errors import ParamNotValidated

# from .enums.item_type_enum import ItemTypeEnum

# from .entities.item import Item


app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/")
def get_all_items():
    print("Entrando no get all itens")
    clientes = repo.get_all_items()
    print(clientes)
    clientes_list = list()
    for cliente in clientes:
        clientes_list.append(cliente.to_dict())
    return clientes_list[0]

@app.post("/deposit")
def deposit(request: dict):

    adition=0
    newBalance = 1000
    notes_2 =request.get("2")
    notes_5 =request.get("5")
    notes_10 =request.get("10")   
    notes_20 =request.get("20")
    notes_50 =request.get("50")
    notes_100 =request.get("100")
    notes_200 =request.get("200")    
    
    addition=notes_2*2.0 + notes_5*5.0+notes_10*10.0+notes_20*20.0+notes_50*50.0+notes_100*100.0+notes_200*200.0

    newBalance=newBalance+addition
    cliente = repo.update_balance(0,newBalance)
    return {
        "current_balance": newBalance,
        "timestamp": 1690482853890 
}  
   

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     return {
#         "item_id": item_id,
#         "item": item.to_dict()    
#     }

# @app.post("/items/create_item", status_code=201)
# def create_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
#     if item is not None:
#         raise HTTPException(status_code=409, detail="Item already exists")
    
#     name = request.get("name")
#     price = request.get("price")
#     item_type = request.get("item_type")
#     if item_type is None:
#         raise HTTPException(status_code=400, detail="Item type is required")
#     if type(item_type) != str:
#         raise HTTPException(status_code=400, detail="Item type must be a string")
#     if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
#         raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
#     admin_permission = request.get("admin_permission")
    
#     try:
#         item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
#     except ParamNotValidated as err:
#         raise HTTPException(status_code=400, detail=err.message)
    
#     item_response = repo.create_item(item, item_id)
#     return {
#         "item_id": item_id,
#         "item": item_response.to_dict()    
#     }
    
# @app.delete("/items/delete_item")
# def delete_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
    
#     item_deleted = repo.delete_item(item_id)
    
#     return {
#         "item_id": item_id,
#         "item": item_deleted.to_dict()    
#     }
    
# @app.put("/items/update_item")
# def update_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
    
#     name = request.get("name")
#     price = request.get("price")
#     admin_permission = request.get("admin_permission")
    
#     item_type_value = request.get("item_type")
#     if item_type_value != None:
#         if type(item_type_value) != str:
#             raise HTTPException(status_code=400, detail="Item type must be a string")
#         if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
#             raise HTTPException(status_code=400, detail="Item type is not a valid one")
#         item_type = ItemTypeEnum[item_type_value]
#     else:
#         item_type = None
        
#     item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
    
#     return {
#         "item_id": item_id,
#         "item": item_updated.to_dict()    
#     }
    


handler = Mangum(app, lifespan="off")
