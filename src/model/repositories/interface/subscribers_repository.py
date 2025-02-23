from abc import ABC, abstractmethod
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class SubscribersRepository:
    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None: pass

    @abstractmethod   
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: pass
