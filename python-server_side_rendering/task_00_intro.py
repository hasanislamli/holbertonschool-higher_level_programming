#!/usr/bin/python3
"""
Module for generating personalized invitation files from a template.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation files based on a template and a list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries containing attendee data.

    Behavior:
        - Validates input types.
        - Handles empty template or attendees list.
        - Replaces missing values with "N/A".
        - Generates output files named output_X.txt.
    """

    # --- Input validation ---
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if (not isinstance(attendees, list) or
            not all(isinstance(a, dict) for a in attendees)):
        print("Error: attendees must be a list of dictionaries.")
        return

    # --- Empty checks ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Process each attendee ---
    for index, attendee in enumerate(attendees, start=1):
        output = template

        placeholders = [
            "name",
            "event_title",
            "event_date",
            "event_location"
        ]

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            output = output.replace("{" + key + "}", str(value))

        # --- File writing ---
        filename = f"output_{index}.txt"

        try:
            # Optional: prevent overwrite (can remove if not required)
            if os.path.exists(filename):
                print(f"{filename} already exists, overwriting.")

            with open(filename, "w", encoding="utf-8") as file:
                file.write(output)

        except Exception as error:
            print(f"Error writing file {filename}: {error}")
