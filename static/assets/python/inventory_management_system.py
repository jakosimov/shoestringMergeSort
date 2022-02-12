from interfaces import InventoryManagementSystemInterface


class InventoryManagementSystem(InventoryManagementSystemInterface):
    def checkItems(self):
        raise NotImplementedError

    def plotDemand(self):
        raise NotImplementedError

    def saveShelfStates(self):
        raise NotImplementedError

    def getShelfStates(self, timeStamp):
        raise NotImplementedError

    def getShelfState(self, timeStamp, shelfIndices):
        raise NotImplementedError

    def raiseAlert(self, shelfIndex):
        raise NotImplementedError

    def addShelf(self, shelf):
        raise NotImplementedError

    def removeShelf(self, shelfId):
        raise NotImplementedError

    def getShelfIdFromQRCode(self):
        raise NotImplementedError
