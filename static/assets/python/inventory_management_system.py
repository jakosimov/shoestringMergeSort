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
        """
        A function to save the current state of the shelves into the
        JSON database pointed to by self.datapath (databases/database.json by default)
        """

        # IF DATAPATH IS EMPTY, INITIALIZE TO DEFAULT VALUE
        if self.datapath == "":
            self.initializeDatabase()

        # GET CURRENT DATETIME
        current_date = datetime.now()
        date_string = current_date.strftime("%y/%m/%d %H:%M:%S")

        # GET CURRENT STATE PARAMETERS OF THE SHELVES (name/amount)
        currentState: Dict[int, Dict[str, Union[int, str]]] = {
            shelf.getShelfId(): {
                "name": shelf.getItemName(),
                "amount": shelf.getItemCount()
            } for shelf in self.shelves.values()
        }

        # TRY TO GET OLD STATES
        old_states: Dict[str, Dict[int, Dict[str, Union[int, str]]]] = {}
        with open(self.datapath, "r") as data_file:
            try:
                old_states = json.load(data_file)
                print("here")
            except JSONDecodeError:
                pass

        # UPDATE OLD STATES WITH CURRENT STATES
        with open(self.datapath, "w") as data_file:  # OPEN THE DATABASE
            old_states[date_string] = currentState  # ADD CURRENT STATE TO OLD STATE
            json.dump(old_states, data_file, indent=2)  # OVERWRITE THE DATABASE BY THE UPDATED STATES
            data_file.truncate()  # TRUNCATE TO AVOID ERRORS
            # print(json.dumps(old_states, indent=2))  DEBUG

    def getShelfStates(self, timeStamp: datetime):
        raise NotImplementedError

    def getShelfState(self, timeStamp, shelfIndices):
        raise NotImplementedError

    def raiseAlert(self, shelfIndex):
        raise NotImplementedError

    def addShelf(self, shelf: Shelf) -> None:
        """
        :param shelf: A Shelf to be added to the list of shelves. If there is a shelf with that id, raise exception
        """
        if shelf.getShelfId() in self.shelves.keys():  # IF A SHELF WITH THE ID EXISTS, RAISE ERROR
            raise IndexError
        self.shelves[shelf.getShelfId()] = shelf  # ADD SHELF TO SHELVES

    def removeShelf(self, shelfId):
        self.shelves.pop(shelfId)

    def getShelfIdFromQRCode(self, imageProcessor):  # TO BE CHANGED
        raise NotImplementedError

    def initializeDatabase(self, name: str = "database") -> None:
        current_directory = os.path.dirname(__file__)
        self.datapath = os.path.join(current_directory, "..", "..", "..", "databases", name + ".json")
