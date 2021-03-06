Logs Analysis Project - Udacity - Full-Stack Web Development Course

By Mohammed

Project purpose:
The purpose of this project is to write queries to answer questions from newspaper database.

The questions are:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Code Requirements:
The project code requires the following software:

- Python 3.7
- psycopg2 2.7
- PostgreSQL 11.1.10
- Vagrant
- VirtualBox 5.2.22


Project contents:
- Log.py - The Python program to run the PostgreSQL
- newsdata, to run the SQL queries and show the results.
- PostgreSQL database.
- Vagrantfile - Configuration file for the Vagrant virtual machine.
- README.md


How to Run the Project:
Download the project zip file from Github and unzip the file.
The terminal should be used to run the VM and then start navigating the database.

Project Running Requirements:
- Open the terminal
- Go to vagrant directory
- Run "Vagrant up"
- Run "Vagrant SSH"
- To connect to the database run this command "psql -d news -f newsdata.sql" then start navigating around.

To run the python code:
- Make sure of being in the right directory
- Run "python Logs.py" and the answers of the questions should be displayed.