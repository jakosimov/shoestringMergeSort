import math
from time import sleep

from static.assets.python.shelf import Shelf
from static.assets.python.inventory_management_system import InventoryManagementSystem


class FakeScale(Scale):
    def measure(self):
        fake_measurement = random.uniform(0.0, 4421.8)
        return fake_measurement


store = InventoryManagementSystem()
nameList1 = ["mango", "bubble tea", "I am tired"]
nameList2 = ["I", "AM", "A", "GENIUS"]

for j in range(10):
    for i, name in enumerate(nameList1):
        shelf = Shelf()
        shelf.setShelfId(i)
        shelf.setItemName(name)
        shelf.setItemWeight(100 * (i + 1))
        shelf.currentWeight = (i + math.factorial(j)) * (i + 1) * 100 + 3
        store.addShelf(shelf)

    store.saveShelfStates()

    for i, name in enumerate(nameList1):
        store.removeShelf(i)

    sleep(1)

store.plotDemand(0)
