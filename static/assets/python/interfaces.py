from abc import ABC, abstractmethod
from typing import List
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
    def measure(self) -> DataInterface:
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
    def plotDemand(self) -> None:
        pass

    @abstractmethod
    def saveShelfStates(self) -> None:
        pass

    @abstractmethod
    def getShelfStates(self, timeStamp: datetime) -> List[List[ShelfInterface]]:
        pass

    @abstractmethod
    def getShelfState(self, timeStamp: datetime, shelfIndices: List[int]) -> List[List[ShelfInterface]]:
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
