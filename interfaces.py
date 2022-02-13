from abc import ABC, abstractmethod
from typing import List, Dict, Union
from datetime import datetime


class DataInterface(ABC):
    @abstractmethod
    def getTotalWeight(self) -> float:
        pass

    @abstractmethod
    def setTotalWeight(self, weight: float) -> None:
        pass


class ScaleInterface(ABC):
    @abstractmethod
    def measure(self) -> List[Data]:
        pass


class ShelfInterface(ABC):
    @abstractmethod
    def getItemCount(self) -> int:
        pass

    @abstractmethod
    def processNewData(self, data: DataInterface) -> None:
        pass

    @abstractmethod
    def setItemWeight(self, coeff: float) -> None:
        pass

    @abstractmethod
    def getItemWeight(self) -> float:
        pass

    @abstractmethod
    def setShelfId(self, id: int) -> None:
        pass

    @abstractmethod
    def getShelfId(self) -> int:
        pass

    @abstractmethod
    def getItemName(self) -> str:
        pass

    @abstractmethod
    def setItemName(self, itemName: str) -> None:
        pass

    @abstractmethod
    def initializeShelf(self, scale: ScaleInterface) -> None:
        pass


class InventoryManagementSystemInterface(ABC):
    @abstractmethod
    def checkItems(self) -> None:
        pass

    @abstractmethod
    def plotDemand(self, shelfId: int) -> str:
        pass

    @abstractmethod
    def saveShelfStates(self) -> None:
        pass

    @abstractmethod
    def getShelfStates(self) -> Dict[str, Dict[int, Dict[str, Union[int, str]]]]:
        pass

    @abstractmethod
    def getShelfStatesAtTime(self, timestamp: datetime) -> Dict[int, Dict[str, Union[int, str]]]:
        pass

    @abstractmethod
    def getShelfState(self, shelfIndices: List[int]):
        pass

    @abstractmethod
    def getShelfStateAtTime(self, shelfIndices: List[int], timestamp: datetime):
        pass

    @abstractmethod
    def raiseAlert(self, shelfIndex: int) -> None:
        pass

    @abstractmethod
    def addShelf(self, shelf: ShelfInterface) -> None:
        pass

    @abstractmethod
    def removeShelf(self, shelfId: int) -> None:
        pass

    @abstractmethod
    def getShelfIdFromQRCode(self, imageProcessor: any) -> int:  # TODO: Define type of imageProcessor
        pass

    @abstractmethod
    def initializeDatabase(self, path: str) -> None:
        pass

    @abstractmethod
    def getDatetimeFormat(self) -> str:
        pass

    @abstractmethod
    def setDatetimeFormat(self, datetime_format: str) -> None:
        pass

    @abstractmethod
    def datetimeToString(self, date: datetime) -> str:
        pass
