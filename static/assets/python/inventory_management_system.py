import json
import os
from static.assets.python.interfaces import InventoryManagementSystemInterface
from static.assets.python.shelf import Shelf
from typing import List, Union, Dict
from datetime import datetime
from pysondb import db
from pysondb.db import JsonDatabase
from json.decoder import JSONDecodeError


class InventoryManagementSystem(InventoryManagementSystemInterface):
    def __init__(self) -> None:
        self.shelves: Dict[int, Shelf] = {}
        self.threshold = 2
        self.datapath: str = ""

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
        if self.datapath == "":
            self.initializeDatabase()

        current_date = datetime.now()
        date_string = current_date.strftime("%y/%m/%d %H:%M:%S")

        currentState = {
            shelf.getShelfId(): {
                "name": shelf.getItemName(),
                "amount": shelf.getItemCount()
            } for shelf in self.shelves.values()
        }

        old_states = {}
        with open(self.datapath, "r") as data_file:
            try:
                old_states = json.load(data_file)
                print("here")
            except JSONDecodeError:
                pass

        with open(self.datapath, "w") as data_file:
            old_states[date_string] = currentState
            json.dump(old_states, data_file, indent=2)
            data_file.truncate()
            print(json.dumps(old_states, indent=2))

    def getShelfStates(self, timeStamp: datetime):
        raise NotImplementedError

    def getShelfState(self, timeStamp, shelfIndices):
        raise NotImplementedError

    def raiseAlert(self, shelfIndex):
        raise NotImplementedError

    def addShelf(self, shelf: Shelf):
        self.shelves[shelf.getShelfId()] = shelf

    def removeShelf(self, shelfId):
        self.shelves.pop(shelfId)

    def getShelfIdFromQRCode(self, imageProcessor):  # TO BE CHANGED
        raise NotImplementedError

    def initializeDatabase(self, name: str = "database") -> None:
        current_directory = os.path.dirname(__file__)
        self.datapath = os.path.join(current_directory, "..", "..", "..", "databases", name + ".json")
