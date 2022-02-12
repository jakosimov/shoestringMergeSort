import json
import os
from static.assets.python.interfaces import InventoryManagementSystemInterface
from static.assets.python.shelf import Shelf
from typing import List, Union, Dict
from datetime import datetime
from pysondb import db
from pysondb.db import JsonDatabase
from json.decoder import JSONDecodeError


# HELPER FUNCTIONS
def filterDict(dictionary: Dict, filter_keys: List) -> Dict:
    """
    :param dictionary: The dictionary to be filtered
    :param filter_keys: The keys that we want to filter
    :return: The filtered dictionary
    """
    return {
        key: value for key, value in dictionary.items() if key in filter_keys
    }


class InventoryManagementSystem(InventoryManagementSystemInterface):
    def __init__(self) -> None:
        self.shelves: Dict[int, Shelf] = {}
        self.threshold = 2
        self.datapath: str = ""
        self.datetime_format = ""

    def checkItems(self) -> None:
        """
        A function to loop over all shelves and raise an alertK if the item count is below the threshold
        """
        for shelf in self.shelves.values():
            if shelf.getItemCount() < self.threshold:
                self.raiseAlert(shelf.getShelfId())

    def raiseAlert(self, shelfId) -> None:
        """
        A function to raise an alert if there is something to do with a given shelf
        :param shelfId: The ID of the shelf which raised the alert
        """
        raise NotImplementedError

    def plotDemand(self):
        """
        A function to plot the demand over the historical data
        :return:
        """
        raise NotImplementedError

    def saveShelfStates(self) -> None:
        """
        A function to save the current state of the shelves into the
        JSON database pointed to by self.datapath (databases/database.json by default)
        """

        # IF DATAPATH IS EMPTY, INITIALIZE TO DEFAULT VALUE
        if self.datapath == "":
            self.initializeDatabase()

        # IF DATETIME FORMAT DOES NOT EXIST, INITIALIZE TO DEFAULT VALUE
        if self.datetime_format == "":
            self.setDatetimeFormat()

        # GET CURRENT DATETIME IN STRING FORMAT (USED AS A KEY FOR THE DATABASE)
        current_date = datetime.now()
        date_string = self.datetimeToString(current_date)

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

    def getShelfStates(self) -> Dict[str, Dict[int, Dict[str, Union[int, str]]]]:
        """
        :return: A dictionary of all the historical state data of the shelves.
        """
        shelf_states: Dict[str, Dict[int, Dict[str, Union[int, str]]]] = {}
        with open(self.datapath, "r") as data_file:
            try:
                old_states = json.load(data_file)
                print("here")
            except JSONDecodeError:
                pass
        return shelf_states

    def getShelfStatesAtTime(self, timestamp: datetime) -> Dict[int, Dict[str, Union[int, str]]]:
        """
        :param timestamp: The data of all shelves at a given timestamp
        :return: All the shelf states at the timestamp
        """
        shelf_states = self.getShelfStates()
        date_string = self.datetimeToString(timestamp)
        return shelf_states[date_string]

    def getShelfState(self, shelfIndices: List[int]):
        """
        :param shelfIndices: A list of indices of shelves where we want to get the data
        :return: A dictionary of all the historical data for all the shelves which have an index in the shelfIndices
        """
        states = self.getShelfStates()
        return {
            date: filterDict(state, shelfIndices) for date, state in states.items()
        }

    def getShelfStateAtTime(self, shelfIndices: List[int], timestamp: datetime):
        """
        :param shelfIndices: A list of indices of shelves where we want to get the data
        :param timestamp: The date where we want to get the data
        :return: A dictionary of the data for all the shelves which have an index in the shelfIndices at a given timestamp
        """
        states = self.getShelfStatesAtTime(timestamp)
        return filterDict(states, shelfIndices)

    def addShelf(self, shelf: Shelf) -> None:
        """
        :param shelf: A Shelf to be added to the list of shelves. If there is a shelf with that id, raise exception
        """
        if shelf.getShelfId() in self.shelves.keys():  # IF A SHELF WITH THE ID EXISTS, RAISE ERROR
            raise IndexError
        self.shelves[shelf.getShelfId()] = shelf  # ADD SHELF TO SHELVES

    def removeShelf(self, shelfId):
        """
        A function to remove a shelf from the shelves database
        :param shelfId: The ID of the shelf to be removed
        """
        self.shelves.pop(shelfId)

    def getShelfIdFromQRCode(self, imageProcessor):  # TODO: Implement
        raise NotImplementedError

    def initializeDatabase(self, name: str = "database") -> None:
        """
        A function to setup a database where historical data gets saved
        :param name: The name of the database file (without extension)
        """
        current_directory = os.path.dirname(__file__)
        self.datapath = os.path.join(current_directory, "..", "..", "..", "databases", name + ".json")

    def getDatetimeFormat(self) -> str:
        """
        :return: The datetime formatting string of the store
        """
        return self.datetime_format

    def setDatetimeFormat(self, datetime_format: str = "%d/%m/%Y %H:%M:%S") -> None:
        """
        :param datetime_format: The datetime formatting of the store
        :param format: The datetime format to be used as the key of the database
        """
        self.datetime_format = datetime_format

    def datetimeToString(self, date: datetime) -> str:
        """
        :param date: A datetime object to be formatted to a string
        :return: A string using the datetime format of the current store
        """
        return date.strftime(self.getDatetimeFormat())
