from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = "base"

    @abstractmethod
    def run(self, query):
        pass