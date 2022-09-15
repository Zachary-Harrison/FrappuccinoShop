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
