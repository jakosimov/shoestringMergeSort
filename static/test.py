from static.assets.python.shelf import Shelf
from static.assets.python.inventory_management_system import InventoryManagementSystem

store = InventoryManagementSystem()
nameList = ["mango", "bubble tea", "I am tired"]

for i, name in enumerate(nameList):
    shelf = Shelf()
    shelf.setShelfId(i)
    shelf.setItemName(name)
    shelf.setItemWeight(100 * (i + 1))
    shelf.total_weight = i * (i + 1) * 100 + 3
    store.addShelf(shelf)

store.saveShelfStates()



