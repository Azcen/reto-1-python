import os

inventory_list = [
    {
        'id': 1,
        'name': 'Guitarr',
        'quantity': 'example1',
        'price': 'example1',
        'type': 'example1',
        'dimensions': 'example1',
    },
    {
        'id': 2,
        'name': 'Bass',
        'quantity': 'example2',
        'price': 'example2',
        'type': 'example2',
        'dimensions': 'example2',
    },
    {
        'id': 3,
        'name': 'Drums',
        'quantity': 'example3',
        'price': 'example3',
        'type': 'example3',
        'dimensions': 'example3',
    }
]

def main():
    print('..::Welcome to inventory management system::..')
    showMenu()
    opt = input()
    triggerMenuOpt(opt)

    
def showMenu():
    print('select one of the following options:')
    print('1. Get inventory list')
    print('2. Search inventory Item')
    print('3. Add a new item to the list')
    print('4. Update an item of the list')
    print('5. Delete an item of the list')
    print('6. Sort list of items')
    print('7. Clear Inventory List')
    print('8. Exit')
    
def triggerMenuOpt(opt):
    if opt == '1':
        getInventoryList()
    if opt == '2':
        getInventoryItem()
    if opt == '3':
        addInventoryItem()
    if opt == '4':
        updateInventoryItem()
    if opt == '5':
        deleteInventoryItem()
    if opt == '6':
        sortInventory()
    if opt == '7':
        clearList()
    if opt == '8':
        clearList()

def getInventoryList():
    print('Inventory list')
    print(inventory_list)
    input('Press enter to go back to main menu')
    os.system('clear')
    main()
        
def getInventoryItem():
    print('Inventory Item')
    print('Please select an item criteria for serching')
    print("1. Name ")
    print("2. Id ")
    opt = int(input())
    if(opt == 1):
        criteria = 'name'
    elif (opt == 2):
        criteria = 'id'
    else:
        print('please select a valid option')
        os.system('clear')
        getInventoryItem()
        
    searchItemByCriteria(criteria)
    input('Press enter to go back to main menu')
    os.system('clear')
    main()

def addInventoryItem():
    print('Add Inventory item')
    newItem = {
        'id': getNextId(),
        'name': '',
        'quantity': '',
        'price': '',
        'type': '',
        'dimensions': '',
    }
    newItem['name']= input('Add item name: \n')
    newItem['quantity']= input('Add item quantity: \n')
    newItem['price']= input('Add item price: \n')
    newItem['type']= input('Add item type: \n')
    newItem['dimensions']= input('Add item dimensions: \n')
    inventory_list.append(newItem)
    print('New Item added successfuly')
    input('Press enter to go back to main menu')
    os.system('clear')
    main()
    
def updateInventoryItem():
    print('update Inventory item')
    index = inventory_list.index(searchItemByCriteria('id')[0])
    
    inventory_list[index]['quantity'] = input('Add new item quantity: \n')
    inventory_list[index]['price'] = input('Add new item price: \n')
    print('Item Updated successfuly')
    input('Press enter to go back to main menu')
    os.system('clear')
    main()
    
def deleteInventoryItem():
    print('Delete Inventory item')
    index = inventory_list.index(searchItemByCriteria('id')[0])
    deleted_item = inventory_list.pop(index)
    print('Item Updated successfuly')
    print(deleted_item)
    input('Press enter to go back to main menu')
    os.system('clear')
    main()
    
def sortInventory():
    print('Select a key to order the list')
    keys = getKeys()
    optKey = input()
    print("Enter a direction: ")
    print("1. Ascendent: ")
    print("2. Descendent: ")
    optDirection = input()
    sortKey = keys[int(optKey) - 1]
    sortList(sortKey, optDirection, True)
    print('1. Main menu')
    print('Press any key to exit')
    opt = input()
    if opt == '1':
        os.system('clear')
        main()
    else:
        exit()

def sortList(key, direction, show):
    inventory_list.sort(key=lambda item: item[key], reverse=int(direction) == 1)
    if(show == True):
        print(inventory_list)
    
def getKeys():
    keys = []
    count = 1
    for key in inventory_list[0].keys():
        print(f"{count}. {key}")
        count += 1
        keys.append(key)
    return keys

def searchItemByCriteria(criteria):
    if(criteria == 'name'):
        name = input('Enter the item name: \n')
        filtered_items = list(filter(lambda item: name.lower() in item['name'].lower(), inventory_list))
        
    if criteria == 'id':
        item_id = int(input('Enter the item id: \n'))
        filtered_items = list(filter(lambda item: item['id'] == item_id, inventory_list))
        
    if(len(filtered_items) > 0):
        for item in filtered_items:
            print(item)
    else:
        print('No items found')
    return filtered_items
        
def getNextId():
    sortList('id', 2, False)
    listLen = len(inventory_list)
    lastId = inventory_list[listLen - 1]['id']
    return lastId + 1

def clearList():
    inventory_list.clear()
    print('Inventory List delete successfuly')
    input('Press enter to go back to main menu')
    os.system('clear')
    main()

def exitApp():
    print('Thanks for using this app!!')
    exit()
    
main()