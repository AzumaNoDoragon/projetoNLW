from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpsRequest
from src.http_types.http_response import HttpsResponse

class SubscribersCreator:
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo

    def create(self, http_request: HttpsRequest) -> HttpsResponse:
        subscriber_info = http_request.body["data"]
        subscriber_email = subscriber_info["email"]
        evento_id = subscriber_info["evento_id"]

        self.__check_subs(subscriber_email, evento_id)
        self.__insert_subs(subscriber_info)
        return self.__format_response(subscriber_info)

    def __check_subs(self, subscriber_email: str, evento_id: int) -> None:
        response = self.__subs_repo.select_subscriber(subscriber_email, evento_id)
        if response: raise Exception("Subscriber Already Exists!")

    def __insert_subs(self, subscriber_info: dict) -> None:
        self.__subs_repo.insert(subscriber_info)

    def __format_response(self, subscriber_info: dict) -> HttpsResponse:
        return HttpsResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": 1,
                    "attributes":subscriber_info
                }
            },
            status_code=201
        )