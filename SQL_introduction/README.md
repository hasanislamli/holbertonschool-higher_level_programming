MySQL Basics - List Databases

Project Overview
This project is part of learning MySQL basics. The goal is to understand how to connect to a MySQL server and execute simple SQL commands.

File
0-list_databases.sql

Task Description
Write a SQL script that lists all databases of a MySQL server.

Requirements

* The script must list all databases
* It should work when executed with MySQL CLI
* No programming language is used, only SQL
* The command used must be valid MySQL syntax

Usage Example
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

Expected Output
information_schema
mysql
performance_schema
sys

Concepts Covered

* MySQL server connection
* SQL command execution
* Database listing

Learning Objective
The purpose of this task is to understand how to interact with a MySQL server and retrieve database information using basic SQL commands.

