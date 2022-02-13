from time import sleep
import unittest

from static.assets.python.shelf import Shelf
from static.assets.python.inventory_management_system import InventoryManagementSystem


def fake_scale_measurement() -> float:
    fake_measurement = random.uniform(0.0, 4421.8)
    return fake_measurement


if __name__ == '__main__':
    store = InventoryManagementSystem()
    nameList1 = ["mango", "bubble tea", "I am tired"]
    nameList2 = ["I", "AM", "A", "GENIUS"]

    for i, name in enumerate(nameList1):
        shelf = Shelf()
        shelf.setShelfId(i)
        shelf.setItemName(name)
        shelf.setItemWeight(100 * (i + 1))
        shelf.currentWeight = i * (i + 1) * 100 + 3
        store.addShelf(shelf)

    store.saveShelfStates()

    for i in range(len(nameList1)):
        store.removeShelf(i)

    sleep(5)

    for i, name in enumerate(nameList2):
        shelf = Shelf()
        shelf.setShelfId(i)
        shelf.setItemName(name)
        shelf.setItemWeight(100 * (i + 1))
        shelf.currentWeight = i * (i + 1) * 100 + 3
        store.addShelf(shelf)

    store.saveShelfStates()
