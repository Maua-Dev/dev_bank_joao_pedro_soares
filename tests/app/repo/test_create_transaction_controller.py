import pytest
from src.app.repo import transaction_repository_mock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock

from src.modules.create_transaction.app import create_transaction_controller, create_transaction_usecase
from src.shared.http.http_models import HttpRequest

class Test_create_transaction_controller:    
    def test_CreateOrderController(self):
        repo = TransactionRepositoryMock()
        usecase = create_transaction_usecase(repo=repo)
        controller = create_transaction_controller(usecase=usecase)
        request= HttpRequest(
            body={
          "type":"withdraw",
          "value": 678.6,
          "current_balance": 456456.4,
          "timestamp": 123123.12
             
            }
        )
        response=controller(request=request)
        assert response.status_code == 201
        assert True