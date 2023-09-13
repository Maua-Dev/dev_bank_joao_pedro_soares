# from abc import ABC, abstractmethod


# class IRequest(ABC):

#     @property
#     def data(self) -> dict:
#         pass


# class IResponse(ABC):

#     @property
#     @abstractmethod
#     def status_code(self) -> int:
#         pass

#     @property
#     @abstractmethod
#     def data(self) -> dict:
#         pass

from enum import Enum


class HttpStatusCodeEnum(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    REDIRECT = 303
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504