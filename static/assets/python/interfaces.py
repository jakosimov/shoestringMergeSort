from abc import ABC, abstractmethod


class ScaleInterface(ABC):
    @abstractmethod
    def measure(self):
        pass


class DataInterface(ABC):
    @abstractmethod
    def getTotalWeight(self):
        pass


class ShelfInterface(ABC):
    @abstractmethod
    def getItemCount(self):
        pass

    @abstractmethod
    def processNewData(self, data):
        pass

    @abstractmethod
    def setItemWeight(self, coeff):
        pass

    @abstractmethod
    def getItemName(self):
        pass

    @abstractmethod
    def setItemName(self, itemName):
        pass

    @abstractmethod
    def initializeShelf(self, scale):
        pass


class InventoryManagementSystemInterface(ABC):
    @abstractmethod
    def checkItems(self):
        pass

    @abstractmethod
    def plotDemand(self):
        pass

    @abstractmethod
    def saveShelfStates(self):
        pass

    @abstractmethod
    def getShelfStates(self, timeStamp):
        pass

    @abstractmethod
    def getShelfState(self, timeStamp, shelfIndices):
        pass

    @abstractmethod
    def raiseAlert(self, shelfIndex):
        pass

    @abstractmethod
    def addShelf(self, shelf):
        pass

    @abstractmethod
    def removeShelf(self, shelfId):
        pass