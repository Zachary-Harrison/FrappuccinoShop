<h2>Dan's Frappuccino Paradise Shop Application </h2>
<hr>
This project creates a functional web-app for a frappuccino shop.  This includes
menu access, online ordering, in-house ordering, inventory control,
and payroll management.
<h3>Workspace Layout</h3>
<hr>
Dan's Frappuccino Paradise Shop Web App will be stored on this repository.

Any documentation and resources for this project will be kept in the "docs" folder.
This includes use case diagrams, the project plan, and project requirements.  More may 
be added as the project progresses.

The code for the application and server will be kept in the "app" folder.
<br>
<h3>Version-Control Procedures</h3>
<hr>
Collaborators must fork the repository found at Zachary-Harrison/cs3450-group10.
The forked repository must then be cloned.  After completing any work, collaborators
should submit a pull request so that all progress is documented and issues may be discussed.
Commit messages should be clear to assist in task control.
<h3>Tool Stack Description and Setup Procedure</h3>
<hr>
Django - Simple server, database, and encryption capabilities

Python - Most team members are familiar with Python and it is very effective for background processes.

JavaScript - This will assist in making the site aesthetically pleasing and provide
some additional functionality.
<h3>Build Instructions</h3>
<hr>
Clone the project in gitbash.

> bash $ git clone https://github.com/Zachary-Harrison/cs3450-group10

Install Django via pip3

> bash $ sudo pip3 install django

Navigate to the project sub-folder. 

> bash $ cd app/cs3450_group10

Run the server using the following command.

> bash $ python3 manage.py runserver 3000

In a web browser, navigate to http://localhost:3000/shop_app to view the app.


<h3>Unit Testing Instructions</h3>
    <hr>
<h4>Testing making a new order:</h4>
Navigate to testing folder and run make_test_order.py

> bash $ python3 make_test_order.py

This should result in a order generated and will return "True" after reading the database and seeing the order in the order queue. Will return true or false and then delete the order from the queue.
(Additional instruction may be involved when development cycle happens)

<h4>Testing making a new manager:</h4>
Navigate to testing folder and run make_test_manager.py

> bash $ python3 make_test_manager.py

This will return "True" after reading the database and seeing a new test manager added. Will delete the test manager after returning true or false so database is still accurate.
(Additional instruction may be involved when development cycle happens)

<h4>Testing making a new user:</h4>
Navigate to testing folder and run make_test_user.py

> bash $ python3 make_test_user.py

This will return "True" after reading the database and seeing a new test user added. Will delete the test user after returning true or false so database is still accurate.
(Additional instruction may be involved when development cycle happens)

<h4>Testing payroll:</h4>
Navigate to testing folder and run test_payroll.py

> bash $ python3 test_payroll.py

This will test payroll functionality in several steps including deducting payroll from manager account, zeroing the hours of employees, and making sure that all payrolls are properly saved as to be recalled on in case of failure. 
(Additional instruction may be involved when development cycle happens)

    

<h3>System Testing Instructions</h3>
<hr>
<h4>Test if server is on correct port and open</h4>
<h5>Linux

> bash $ sudo ss -tnlp || grep -m 1 -w -F '127.0.0.1:3000'

This should result in one of the lines looking like so:

> "LISTEN              0                   10                                    127.0.0.1:3000                                   0.0.0.0:*                  users:(("python3",pid=104387,fd=4))"

If this fails try:

> bash $ sudo netstat -tnlp || grep -m 1 -w -F '127.0.0.1:3000'

This should be the result:

> "tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      104387/python3"

<h4>Check if server is serving files</h4>

Open prefered web browser and type this into the search bar:

        "http://127.0.0.1:3000/shop_app/"

Should result in the shop page.
<hr>




<h3>Other Development Notes</h3>
<hr>
