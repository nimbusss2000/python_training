Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname> and <lastname>
  When I add a contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | lastname  |
  | firstname1 | lastname1 |
  | firstname2 | lastname2 |


Scenario Outline: Delete some contact
  Given a non-empty contact list
  Given a random contact in list
  When I delete the contact in list
  Then the new contact list is equal to the old list without the deleted contact