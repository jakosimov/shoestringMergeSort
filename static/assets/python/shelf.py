from interfaces import ShelfInterface
from data import Data
import typing

class Shelf(ShelfInterface):
    def getItemCount(self):
        raise NotImplementedError

    def processNewData(self, data: Data):
        raise NotImplementedError

    def setItemWeight(self, coeff):
        raise NotImplementedError

    def getItemName(self):
        raise NotImplementedError

    def setItemName(self, itemName):
        raise NotImplementedError

    def initializeShelf(self, scale):
        raise NotImplementedError