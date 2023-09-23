
from src.modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from src.modules.create_transaction.app.create_transaction_viewmodel import CreateTransactionViewModel
from src.shared.http.http_models  import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError
from src.app.errors.domain_errors import EntityError
from src.app.errors.controller_errors import MissingParameters

class CreateOrderController:
    def __init__(self, usecase: CreateTransactionUseCase):
        self.createTransactionUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('type') is None:
                raise MissingParameters('type')
                
            if request.body.get('value') is None:
                raise MissingParameters('value')
            if request.body.get('current_balance') is None:
                raise MissingParameters('current_balance')
                
            if request.body.get('timestamp') is None:
                raise MissingParameters('timestamp')       
                 
            transaction = self.CreateTransactionUseCase(type=str[request.body["type"]],value=float[request.body["value"]], current_balance=float(request.body["current_balance"]),timestamp=float(request.body["timestamp"]))
            viewmodel = CreateTransactionViewModel(transaction=transaction)
            
            return Created(viewmodel.to_dict())
        
        except EntityError as err:
            return BadRequest(body=err.message)
            
        except MissingParameters as err:
            return BadRequest(body=err.message)    
            
        except Exception as err:
            return InternalServerError(body=err.args[0])


        