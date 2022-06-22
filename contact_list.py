from tkinter.messagebox import NO
from typing import List


class ContactList():
  
  def __init__(self, name, contact) -> None:
    print(f"Creating new contact list '{name}'...")
    self.name = name
    self.contacts = []
    
    for item in contact:
      print(f'Adding contact {item} to {self.name}...')
      self.contacts.append(item)
    
    print('Done...\n')

  def __str__(self) -> str:
    result = f'Contact List: {self.name}\n'
    for contact in self.contacts:
      result += f'{contact}\n'

    return result

  def add_contact(self, new_contact) -> None: 
    print(f'Adding contact {new_contact} to {self.name}...')
    self.contacts.append(new_contact)
    self.contacts.sort(key = lambda x: x['name'])
    print('Done...\n')

  def remove_contact(self, name) -> None:
    print(f'Removing contact {name} from {self.name}...')
    
    temp = list(filter(lambda item: item['name'] == name, self.contacts))

    print('Found the following contacts:')
    for i, result in enumerate(temp):
      print(f'{i+1}: {result}')

    idx = input('Select a number to remove: ')
    self.contacts.remove(temp[int(idx)-1])
    
    print('Done...\n')

  def find_shared_contacts(self, new_name, contact_list):
    print(f'Finding shared contacts in {self.name} and {contact_list.name}...')
    intersect = []
    for item in self.contacts:
      for item_other in contact_list.contacts:
        if item == item_other:
          intersect.append(item)

    results = ContactList(new_name, intersect)
    print('Done...\n')
    return results


# Driver Code
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]

work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
my_friends_list.add_contact({'name':'Amber','number':'990-1187'})
my_friends_list.add_contact({'name':'Zack','number':'990-3252'})
my_work_buddies.add_contact({'name':'Zack','number':'990-3252'})
friends_i_work_with = my_friends_list.find_shared_contacts('Friends I work with', my_work_buddies)

print(my_friends_list)
print(my_work_buddies)
print(friends_i_work_with)
