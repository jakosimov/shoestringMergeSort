from static.assets.python.interfaces import DataInterface


class Data(DataInterface):
    def __init__(self) -> None:
        self.weight: float = 0

    def setTotalWeight(self, weight: float) -> None:
        self.weight = weight

    def getTotalWeight(self) -> float:
        return self.weight