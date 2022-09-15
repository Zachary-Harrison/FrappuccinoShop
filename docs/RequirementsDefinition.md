# Requirements Definition

### Introduction and Context

This application will include many essential functions for the success of Dan’s Frappuccino Paradise.  These functions include interfaces for customers, employees, and the shop manager to interact with the shop inventory, financials, and the selling of product.

Customers will be able to purchase their drinks online, or in the store so long as they have an account username and password.  They will also be able to browse preset options or customize their own menu items for easy ordering.

Employees will be able to charge customers and make purchases for them.  They will also be able to adjust shop inventory depending on the drinks that are sold.  Employees will also be responsible for tracking their work hours using this system.  Employees may also access any customer view so they too can enjoy the drinks that they sell.

Managers oversee the paying of employees for their recorded working hours, as well as keeping the shop inventories full.  A manager will also be able to edit any of the menu items to promote the sell of additional beverages.  The manager will also have access to any other views in case they need to cover for an employee, or if they also would like to purchase a drink from the store.

This will all be hosted from a web application for easy access.

### Users and their Goals

##### *Figure 1 - Customer Ordering a Drink*

![](../images/UseCaseDiagram1.drawio.png)



Participating Actor:

-  Actor

Entry Conditions:

-  condition 1

Exit Conditions:

-  condition 1

Event Flow:

1)  event 1

##### *Figure 2 - Employee submitting timecard*

![](C:\Users\zacha\Zachary-Harrison\Computer%20Science\3450\DansFrappuccinoParadise\images\UseCaseDiagram2.drawio.png)

Participating Actor:

- Actor

Entry Conditions:

- condition 1

Exit Conditions:

- condition 1

Event Flow:

1. event 1



*This section contains identifies of the users of the proposed system and their goals, illustrated and supported by Use Case diagrams.   Here “users” is a board term that could include other software systems.*

The following UML use case diagrams will describe the system's actors and the actors' goals.

*Figure 1 - Customer orders Frappuccino*

*USE CASE DIAGRAM HERE*

Participating Actor: Customer

Entry Conditions:

    - Customer wants to purchase a drink.

Exit Conditions:

    - Customer order is fulfilled.
    - Customer decides not to order drink.

Event Flow:
1. Customer logs on to system.
2. Customer requests to view drink menu.
3. System displays available drinks.
4. Customer inputs their order.
5. System verifies customer has sufficient funds.
6. Customer pays for the drink.
7. System displays purchase confirmation and deducts items from inventory.


*Figure 2 - Employee updates timecard*

*USE CASE DIAGRAM HERE*

Participating Actor: Employee

Entry Conditions:

    - Employee wants to input the number of hours they've worked.

Exit Conditions:

    - Employee chooses not to input hours.
    - Employee's timecard is updated.

Event Flow:
1. Employee views area to update timecard.
2. Employee inputs hours worked.
3. System updates employee's total hours worked.

*Figure 3 - Manager pays employees*

*USE CASE DIAGRAM HERE*

Participating Actor: Manager

Entry Conditions:

    - Manager wants to pay employees based on hours worked.

Exit Conditions:

    - Employees are successfully paid.

Event Flow:
1. Manager views area where employees can be paid.
2. Manager pushes button to pay all employees.
3. Employee timecards are verified.
4. System ensures sufficient funds are available in manager's account.
5. System updates each employee's balance, and their timecard is reset to 0 hours.

*Figure 4 - Manager restocks inventory*

*USE CASE DIAGRAM HERE*

Participating Actor: Manager

Entry Conditions:

    - Manager wants to purchase additional inventory stock.

Exit Conditions:

    - Manager chooses not to restock.
    - Inventory is successfully restocked.

Event Flow:
1. Manager views inventory page.
2. Manager orders items to be restocked.
3. System ensures sufficient funds are available in the manager's balance.
4. Manager pays for items.
5. System updates inventory to include the purchased items

*Figure 5 - Manager adds new drink to menu*

*USE CASE DIAGRAM HERE*

Participating Actor: Manager

Entry Conditions:

    - Manager wants to add new menu item.

Exit Conditions:

    - Manager chooses not to add new item.
    - Drink is added to menu.

Event Flow:
1. Manager logs into their account.
2. Manager requests to add new drink to menu.
3. Manager sets cost, ingredients, and image for drink.
4. System verifies that ingredients listed are possible ingredients.
5. System adds drink to menu.

*Figure 6 - Customer adds money to their account*

*USE CASE DIAGRAM HERE*

Participating Actor: Customer

Entry Conditions:

    - Customer wants to update their account balance.

Exit Conditions:

    - Customer chooses not to add money.
    - Customer's balance is increased.

Event Flow:
1. Customer logs into their account.
2. Customer views field to input their desired amount to add.
3. Customer inputs desired amount.
4. System increases customer's balance by requested amount.

*Figure 7 - Manager removes item from menu*

*USE CASE DIAGRAM HERE*

Participating Actor: Manager

Entry Conditions:

    - Manager wants to remove item from menu.

Exit Conditions:

    - Manager chooses not to remove item.
    - Manager successfully removes item.

Event Flow:
1. Manager logs into their account.
2. Manager removes item from menu,
3. System updates menu to reflect removal of item.

*Figure 8 - Customer creates account*

*USE CASE DIAGRAM HERE*

Participating Actor: Customer

Entry Conditions:

    - Customer wants to create account.

Exit Conditions:

    - Customer chooses not to create account.
    - Customer account is successfully created.

Event Flow:
1. Customer navigates to account creation.
2. Customer inputs username and password.
3. System verifies that the input username is unique, has not been used by a previous customer.
4. System encrypts password and account information is added to database.

### Functional Requirements

- User Authentication and Access
  - The application must require all users to log in with a unique username and password before allowing them to access any views.
  - Members can have any of the following access levels: Customer, Employee, Manager
    - Users with customer clearance should have access to all Customer Features (FR3)
    - Users with employee clearance should have access to all Customer and Employee Features (FR3, FR4)
    - Users with manager clearance should have access to all Features. (FR3, FR4, FR5)
- User Profile Features
  - Any user may modify their own password.
  - No user may modify their username
  - Any user except for the manager may delete their account.
  - Managers are the only level of user that may modify the password or username of another account or delete another account.
  - Users should be allowed to view and edit their account balance.
  - No real money is required to increase funds in the account.
- Customer Features
  - The application will allow any customers to view and order menu items
  - The application will allow any customer to create and save their own preferred beverages as “Favorites”.
    - These “Favorites” will know any addons needed.
    - Users may customize the names of these custom drinks.
  - The customer can see orders that they have placed which have not been completed.
    - The customer may cancel any orders that have not been completed.
- Employee Profile Features
  - Employees may place an order for a customer from their account when given a customer’s username.
  - Employees can see what order needs to be completed next.
    - Once an order is completed, and employee can mark the order as complete and remove it from the queue.
  - Employees should be able to add to their total hours worked and view how many hours they have worked from the last paycheck.
- Manager Profile Features
  - A manager will be able to view and edit all menu items
  - Managers will be able to see and increase stock by purchasing using money from their account.
    - For the purposes of this assignment, the manager can set the price of ingredients.
  - Managers will be able to see all employee work hours and one-click pay all at a fixed rate (>$15.00/hr)
  - Managers will be able to edit access and remove employees.
  - All income will enter the manager’s account and then be paid out for ingredients and employee pay.

### Non-functional Requirements

- The application must use a database
  
  - User account information will be stored, including the following: Username, password (encrypted), account balance, favorites, employee hours, account clearance.
  - Shop information will be stored, including the following: Inventory, menu items.

- The team will use Git for version control, with GitHub as a remote repository.

- The application will be hosted via localhost.
  
  **Future Features:** 
  
  *This section contains a list of ideas or features that are beyond the scope of the project.*

### **Glossary**

This section contains a list of important terms and their definitions.

1. *Customer* – a user that uses the application to purchase beverages.
2. *Employee* – a user that uses the application to manage orders and their own timecard.
3. *Manager* – a user that uses the application to oversee stock and financial information.
4. *User* – any person that is authorized to use the application or has logged into the application.
5. *Favorite* – a customized beverage that has been stored by a user.
