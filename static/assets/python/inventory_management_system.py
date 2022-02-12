import json
import os
from static.assets.python.interfaces import InventoryManagementSystemInterface
from static.assets.python.shelf import Shelf
from typing import List, Union
from datetime import datetime
from pysondb import db
from pysondb.db import JsonDatabase


class InventoryManagementSystem(InventoryManagementSystemInterface):
    def __init__(self) -> None:
        self.shelves: List[Shelf] = []
        self.threshold = 2
        self.database: Union[JsonDatabase, None] = None

    def checkItems(self) -> None:
        """
        A function to loop over all shelves and raise an error if the item count is below the threshold
        """
        for shelf in self.shelves:
            if shelf.getItemCount() < self.threshold:
                self.raiseAlert(shelf.getShelfId())

    def plotDemand(self):
        raise NotImplementedError

    def saveShelfStates(self) -> None:
        currentState = {
            datetime.now():
                [
                    {
                        shelf.getShelfId(): [
                            shelf.getItemName(),
                            shelf.getItemCount()
                        ]
                    } for shelf in self.shelves
                ]
        }
        jsonObject: str = json.dumps(currentState, indent=2)
        print(jsonObject)

    def getShelfStates(self, timeStamp: datetime):
        raise NotImplementedError

    def getShelfState(self, timeStamp, shelfIndices):
        raise NotImplementedError

    def raiseAlert(self, shelfIndex):
        raise NotImplementedError

    def addShelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def removeShelf(self, shelfId):
        raise NotImplementedError

    def getShelfIdFromQRCode(self, imageProcessor):  # TO BE CHANGED
        raise NotImplementedError

    def initializeDatabase(self, name: str = "database") -> None:
        self.database = db.getDb(os.path.join("database", name + ".json"))
