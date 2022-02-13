from interfaces import ShelfInterface
from scale import Scale
from data import Data


class Shelf(ShelfInterface):
    def __init__(self) -> None:
        self.currentWeight: float = 0
        self.itemWeight: float = 0
        self.itemName: str = ""
        self.shelfId: int = 0

    def getItemCount(self) -> int:
        item_weight = self.getItemWeight()
        total_weight = self.currentWeight
        item_count = round(total_weight / item_weight)
        if item_count < 0:
            raise AssertionError
        return item_count

    def processNewData(self, data: Data) -> None:
        self.currentWeight = data.getTotalWeight()

    def setItemWeight(self, coeff: float) -> None:
        self.itemWeight = coeff

    def getItemWeight(self) -> float:
        return self.itemWeight

    def setShelfId(self, id: int) -> None:
        self.shelfId = id

    def getShelfId(self) -> int:
        return self.shelfId

    def getItemName(self) -> str:
        return self.itemName

    def setItemName(self, itemName: str) -> None:
        self.itemName = itemName

    def initializeShelf(self, scale: Scale) -> None:
        total_weight = scale.measure()
        self.currentWeight = total_weight
