# Dan's Frappuccino Paradise

Starbucks is crazy complicated. There's so many different types of coffee that it makes it very difficult to even understand what you're purchasing. So, we're going to open Dan's Frappuccino Paradise! 

- <u>Customers</u>
  - order a Frappuccino based on the options we give them. 
  - pay with money from their **account** with (essentially) unlimited money.
    - encrypt the account
    - they need a unique username and password
- <u>Employee</u> 
  - take order
  - take money from customers
  - have a button that allows them to "clock in". "Hey, I worked 3 hours"
- <u>Frappuccino Baristas</u> 
  - make the beverage and ring up the order.
  - have a button that allows them to "clock in". "Hey, I worked 3 hours"
- <u>Manager </u> 
  - Collect money
  - Stock inventory - each customer is going to use up resources. Manager keeps track of that
  - Pay workers
  - TGIF button (eagle-shits button). On friday, they hit the button and all the employees get paid. 

We're going to want to make a website for this

- This website will have different views for
  - <u>Customer View</u>:
    - <u>Login</u> and <u>Sign-up</u> screen
      - unique usernames
      - require the user to create a good password
      - encrypt the passwords
    - Order drink from <u>Drink Menu</u>:
      - ability to custom-make drink
      - subtract inventory on order
      - Cancel order button?
        - re-add inventory to drink
    - ability to add money to account
    - maintain an order history
      - "order again" button
      - "my favorite drink" idea
    - restrict access to cashier/barista and manager view
    - pay money for drink
      - money goes straight to manager
  - <u>Cashier/Barista View</u>:
    - create order based on customer's request
    - take money away from customer account
    - "order fulfilled" button
    - time clock/button
    - allow customer view, restrict access to manager view
  - <u>Manager View</u>:
    - pay employees button
      - add money to employee accounts
      - take money away from business account
    - give access to cashier views?
    - see how much of each ingredient there is remaining in the store
    - ability to edit <u>Drink Menu</u>:
      - edit price
      - add/remove drinks
    - ability to fire/hire employees

In this class, money is kind of fake. 
