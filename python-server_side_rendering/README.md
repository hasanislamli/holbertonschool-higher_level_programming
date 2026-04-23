Python Server-Side Rendering Project

Description
This project focuses on understanding and implementing Server-Side Rendering (SSR) using Python. It introduces the concept of generating dynamic content on the server before sending it to the client.

The project begins with a simple templating program and progresses toward building web applications using Flask and Jinja2.


Learning Objectives

- Understand Server-Side Rendering (SSR)
- Learn the difference between SSR and Client-Side Rendering (CSR)
- Implement templating logic in Python
- Work with file handling (read and write)
- Handle errors and edge cases properly
- Prepare for Flask and Jinja2


Technologies Used

- Python 3
- File Handling
- String Manipulation
- Error Handling


Project Structure

python-server_side_rendering/

task_00_intro.py
template.txt
output_1.txt
output_2.txt
output_3.txt
README


Task 0: Simple Templating Program

Description

This task involves creating a Python function that generates personalized invitation files using a template and a list of attendees.


Function

generate_invitations(template, attendees)


Inputs

- template: string (invitation template)
- attendees: list of dictionaries


Output

The program generates files:

output_1.txt
output_2.txt
output_3.txt

Each file contains personalized content.


Error Handling

The function handles:

- Invalid input types
- Empty template
- Empty attendees list
- Missing values (replaced with "N/A")


Example Template

Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.


Example Data

attendees = [
{"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
{"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
{"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]


Usage

python3 main.py


Key Concepts

- Server-Side Rendering (SSR)
- Template processing
- File generation
- Data handling


Resources

- Python Official Documentation
- Flask Documentation
- Jinja2 Documentation
