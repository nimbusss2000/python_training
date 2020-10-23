*** Settings ***
Library  rf.AddressBook
Library  Collections  # стандарт. библиотека для добавления объекта в список
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}   # преобразуем сторки в числа, метод из станд. библиотеки Collections
    ${index}=  Evaluate  random.randrange(${len})  random   # с помощью метода Evaluate, из станд. библиотеки BuiltIn, выбираем элемент из списка
    ${group}=  Get From List  ${old_list}  ${index}   # метод из библиотеки Collections
    Delete Group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

