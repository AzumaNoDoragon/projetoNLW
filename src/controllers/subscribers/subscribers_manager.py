from src.http_types.http_request import HttpsRequest
from src.http_types.http_response import HttpsResponse
from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManager:
    def __init__(self, susbcribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = susbcribers_repo
        
    def get_subscriber_by_link(self, http_request: HttpsRequest) -> HttpsResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subs = self.__subscribers_repo.select_subscribers_by_link(link, event_id)
        return self.__format_subs_by_link(subs)
    
    def get_event_ranking(self, http_request: HttpsRequest) -> HttpsResponse:
        event_id = http_request.param["event_id"]
        event_ranking = self.__subscribers_repo.get_ranking(event_id)
        return self.__format_event_ranking(event_ranking)

    def __format_subs_by_link(self, subs: list) -> HttpsResponse:
        formatted_subscriber = []
        for sub in subs:
            formatted_subscriber.append(
                {
                    "nome": sub.nome,
                    "email": sub.email,
                }
            )
        return HttpsResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_subscriber),
                    "subscribers": formatted_subscriber
                }
            },
            status_code=200
        )
    
    def __format_event_ranking(self, event_ranking: list) -> HttpsResponse:
        formatted_event_ranking = []
        for position in event_ranking:
            formatted_event_ranking.append(
                {
                    "Link": position.link,
                    "total_subscribers": position.total,
                }
            )
        return HttpsResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "ranking": formatted_event_ranking
                }
            },
            status_code=200
        )
                                      
