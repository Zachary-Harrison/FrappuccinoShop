# Dans Frappuccino Paradise Shop Application

***

### Workspace Layout

***

Dan's Frappuccino Paradise Shop Web App will be stored on this repository.

This project creates a functional web-app for a frappuccino shop.  This includes
menu access, online ordering, in-house ordering, inventory control,
and payroll management.

Any documentation and resources for this project will be kept in the "docs" folder.
This includes use case diagrams, the project plan, and project requirements.  More may 
be added as the project progresses.

The code for the application and server will be kept in the "app" folder.

### Version-Control Procedures

***

Collaborators must fork the repository found at Zachary-Harrison/cs3450-group10.
The forked repository must then be cloned.  After completing any work, collaborators
should submit a pull request so that all progress is documented and issues may be discussed.
Commit messages should be clear to assist in task control.

<h3>Tool Stack Description and Setup Procedure</h3>
<hr>
Django - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Automates webserving, database handling, encryption, and more. See install instructions below in "Build Instructions".
</br>

Python3 - Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming. Most team members are familiar with Python and it is very effective for background processes. Download Python 3 here https://www.python.org/downloads/.
</br>

JavaScript - JavaScript is a scripting or programming language that allows you to implement complex features on web pages displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. This will assist in making the site aesthetically pleasing and provide
some additional functionality.

<h3>Build Instructions - Linux and MacOS</h3>
<hr>
Download Python 3 here :
https://www.python.org/downloads/

Clone the project.

> bash $ git clone https://github.com/Zachary-Harrison/cs3450-group10

Install Django via pip3

> bash $ sudo pip3 install django

Install psycopg2

For Linux servers, first run

> bash $ sudo apt install libpq-dev postgresql

then continue.

For MacOS start here

> bash $ sudo pip3 install psycopg2

> bash $ sudo pip3 install psycopg2-binary

Navigate to the project sub-folder. 

> bash $ cd app/cs3450_group10

Run the server using the following command. (3000 is port, this is changable)

> bash $ python3 manage.py runserver 3000

In a web browser, navigate to http://localhost:3000/shop_app to view the app.
3000 may be replaced with any port you wish to host the webserver on.

<h3> Unit Testing </h3>
<hr>

In order to make sure that our database and functions were working properly unit tests were put in place. These unit tests build objects and put them into the database, then call them to make sure that they are functioning as intended. When you run your tests, the default behavior of the test utility is to find all the test cases (that is, subclasses of unittest.TestCase) in any file whose name begins with test, automatically build a test suite out of those test cases, and run that suite.Test discovery is based on the unittest module’s built-in test discovery. By default, this will discover tests in any file named test*.py under the current working directory.

You can specify particular tests to run by supplying any number of “test labels” to ./manage.py test. Each test label can be a full Python dotted path to a package, module, TestCase subclass, or test method.

To read more about the documentation, follow this link https://docs.djangoproject.com/en/4.1/topics/testing/overview/

Run unit tests within the same directory as manage.py
Run unit tests with the following command:

> bash $ python3 manage.py test shop_app

By default our tests test for:
Drink model

- Drink name
- Drink price
- Drink image
  Order model
- Order name
- Order drink
  Ingredient model
- Ingredient name
- Ingredient price
- Ingredient quantity
  Account model
- Account name
- Account password
- Account user type
- Account balance

### System Testing Instructions

<hr>
<h4>Test if server is on correct port and open</h4>
<h5>Linux and MacOS

> bash $ sudo ss -tnlp || grep -m 1 -w -F '127.0.0.1:3000'

This should result in one of the lines looking like so:

> "LISTEN              0                   10                                    127.0.0.1:3000                                   0.0.0.0:*                  users:(("python3",pid=104387,fd=4))"

If this fails try:

> bash $ sudo netstat -tnlp || grep -m 1 -w -F '127.0.0.1:3000'

This should be the result:

> "tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      104387/python3"

#### Check if server is serving files

Open preferred web browser and type this into the search bar:

        "http://127.0.0.1:3000/shop_app/"

Should result in the shop page.

***

### Deliverables

- [Project Plan](docs/ProjectPlan.md)
- [Requirements Definition](docs/RequirementsDefinition.md)
- [Low Fidelity Prototype](docs/LowFidelityProtoInstructions.md)
- [High Fidelity Prototype](docs/HighFidelityProtoInstructions.md)
- [PowerPoint Presentation](docs/presentation/CS3450-Group10-Presentation.pptx)
- [4 screen capture videos](videos/)
- [Five color Burn-down chart of the entire project](docs/presentation/5color_project_burndown.png)

***

### Other Development Notes

***

- (Deployed) = Currently deployed in the working branch. Will receive updates and improvements as development and maintenance continue.
- (Possible) = In theory, not currently planned to be put into development
- (Under Development) = Is currently undergoing development
- (Scrapped) = No longer planning to be a feature
- (Deprecated) = Will not be receiving updates, feature is finished and further support will be extremely limited
