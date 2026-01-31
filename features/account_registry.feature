Feature: Account registry

Scenario: User is able to create 2 accounts
    Given Account registry is empty
    When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
    And I create an account using name: "tadeusz", last name: "szcześniak", pesel: "79101011234"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "89092909246" exists in registry
    And Account with pesel "79101011234" exists in registry

Scenario: User is able to update surname of already created account
    Given Account registry is empty
    And I create an account using name: "nata", last name: "haydamaky", pesel: "95092909876"
    When I update "last_name" of account with pesel: "95092909876" to "filatov"
    Then Account with pesel "95092909876" has "last_name" equal to "filatov"

Scenario: User is able to update name of already created account
    Given Account registry is empty
    And I create an account using name: "john", last name: "doe", pesel: "12345678909"
    When I update "first_name" of account with pesel: "12345678909" to "nathan"
    Then Account with pesel "12345678909" has "first_name" equal to "nathan"

Scenario: Created account has all fields correctly set
    Given Account registry is empty
    And I create an account using name: "dwayne", last name: "johnson", pesel: "93847510283"
    Then Account with pesel "93847510283" has "first_name" equal to "dwayne"
    And Account with pesel "93847510283" has "last_name" equal to "johnson"

Scenario: User is able to delete created account
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    When I delete account with pesel: "01092909876"
    Then Account with pesel "01092909876" does not exist in registry
    And Number of accounts in registry equals: "0"

Scenario: User is performing an incoming transfer
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    When Account with pesel "01092909876" performs an incoming transfer worth 17.0
    Then Account with pesel "01092909876" has "balance" equal to "17.0"

Scenario: User is performing an outgoing transfer
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    Then Account with pesel "01092909876" performs an incoming transfer worth 40.0
    When Account with pesel "01092909876" performs an outgoing transfer worth 17.0
    Then Account with pesel "01092909876" has "balance" equal to "23.0"

Scenario: User is performing an express transfer
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    Then Account with pesel "01092909876" performs an incoming transfer worth 40.0
    When Account with pesel "01092909876" performs an express transfer worth 17.0
    Then Account with pesel "01092909876" has "balance" equal to "22.0"