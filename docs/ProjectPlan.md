# Project Plan

### Project Overview

This project aims to build a system for simulating a Frappuccino shop.

The system allows customers to visit and purchase a Frappuccino. The system includes an economy where customers can add money to their account to use to purchase drinks, workers are paid by the hour, and the manager can purchase ingredients for the shop. Money from customer purchases should be transferred to the manager, who can then distribute wages to workers. The system will run as a website.

### Team Organization

Project Manager: Zachary Harrison

Git Repository Host: Zachary Harrison

Designers and Developers: Keldon Boehmer, Zachary Harrison, Jensen Judkins, Noah Knight 

### Software Development Process

The development will be broken up into five phases.  Each phase will be a little like a Sprint in an Agile method and a little like an iteration in a Spiral process.  Specifically, each phase will be like a Sprint, in that work to be done will be organized into small tasks, placed into a “backlog”, and prioritized. Then, using on time-box scheduling, the team will decide which tasks the phase (Sprint) will address. The team will use a Scrum Board to keep track of tasks in the backlog, those that will be part of the current Sprint, those in progress, and those that are done.

Each phase will also be a little like an iteration in a Spiral process, in that each phase will include some risk analysis and that any development activity (requirements capture, analysis, design, implementation, etc.) can be done during any phase. Early phases will focus on understanding (requirements capture and analysis) and subsequent phases will focus on design and implementation.  Each phase will include a retrospective.

| Phase | Iteration                                            |
| ----- | ---------------------------------------------------- |
| 1.    | Phase 1 - Requirements Capture                       |
| 2.    | Phase 2 - Analysis, Architectural, UI, and DB Design |
| 3.    | Phase 3 - Implementation, and Unit Testing           |
| 4.    | Phase 4 - More Implementation and Testing            |

We will use Unified Modeling Language (UML) to document user goals, structural concepts, component interactions, and behaviors.

### Communication policies, procedures, and tools

- Discord – Primary location for coordination as a team. Text chat to communicate what we are working on and have finished as well as assist one another with any questions/problems. Voice calls will be used for meetings. 
- GitHub – Used for version control, and for each member to upload their completed work for team review.

### Risk Analysis

- Database Structure
    - Likelihood – Low
    - Severity – Very High
    - Consequences –  Menu items and/or prices improperly displayed. Money cannot be accurately added or removed to the accounts of any employee, customer, or manager.
    - Work-Around – None. System cannot properly function as a frappuccino shop should the frappuccino menu not work or the monetary aspect fail to function. 
- Login
    - Likelihood – Low
    - Severity – Med-High
    - Consequences – Customers cannot use their balance to pay for drinks or save a drink to their account, employees cannot fulfill orders or track their time worked, manager cannot pay employees or order ingredients.
    - Work-Around – Customers do not need to be logged in to order drinks. None for employees or manager.
- UI
    - Likelihood –  Low
    - Severity – Very High
    - Consequences – Inability to interact with users in a clear and efficient way.
    - Work-Around – None. System loses value and functionality if users are not able to
    interact with it.

### Configuration Management

See the README.md in the Git repository.
