from src.modules.create_transaction import CreateTransactionUsecase
from src.shared.http.http_models import HttpRequest,HttpResponse

class CreateOrderController:
    def __init__(self, usecase: CreateTransactionUsecase):
        self.createTransactionUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('table') is None:
                raise MissingParameters('table')
                
            if request.body.get('flavor') is None:
                raise MissingParameters('flavor')
        