from interfaces import InventoryManagementSystemInterface
from typing import List
from shelf import Shelf
from datetime import datetime


class InventoryManagementSystem(InventoryManagementSystemInterface):
    def _init__(self) -> None:
        self.shelves: List[Shelf] = []
        self.threshold = 2

    def checkItems(self) -> None:
        """
        A function to loop over all shelves and raise an error if the item count is below the threshold
        """
        for shelf in self.shelves:
            if shelf.getItemCount() < self.threshold:
                self.raiseAlert(shelf.getShelfId())

    def plotDemand(self):
        raise NotImplementedError

    def saveShelfStates(self):
        raise NotImplementedError

    def getShelfStates(self, timeStamp: datetime):
        raise NotImplementedError

    def getShelfState(self, timeStamp, shelfIndices):
        raise NotImplementedError

    def raiseAlert(self, shelfIndex):
        raise NotImplementedError

    def addShelf(self, shelf):
        raise NotImplementedError

    def removeShelf(self, shelfId):
        raise NotImplementedError

    def getShelfIdFromQRCode(self, imageProcessor):  # TO BE CHANGED
        raise NotImplementedError
