#!/usr/bin/env python3
"""Generate readme badges for Princeton Research Computing."""
# /// script
# requires-python = ">=3.13"
# ///

import base64


def get_right_side_text() -> str:
    print(
        "Input the year(s) that you worked on the project. Here's some examples:\n\n"
        '"2025"           - if RSE(s) worked on the project for a year or less then put\n'
        "                   the year that they finished.\n"
        '"2025-2025"      - if RSE(s) worked on the project for more than a year\n'
        "                   continuously then put the starting and ending year with a dash\n"
        "                   between them.\n"
        '"2025-Current"   - if RSE(s) are currently working on a project then put the\n'
        '                   starting year and the word "Current" with a dash between.\n'
        '"2022,2024,2026" - if RSE(s) worked on the same project at different times then\n'
        '                   put a list of years. "-Current" can be added to the end if\n'
        "                   it's actively being worked on by an RSE.\n"
    )

    # Get user input and convert to lowercase
    right_text = str(input("Input Years: ")).lower()

    # Strip any spaces
    right_text = right_text.replace(" ", "")

    # Verify it only has allowed characters
    verification = right_text.replace("current", "")
    for allowed in "0123456789-,":
        verification = verification.replace(allowed, "")
    if len(verification) != 0:
        msg = f'The input string "{right_text}" may only contain numbers, dashes, commas, or the the word "current"'
        raise ValueError(msg)

    # Capitalize "Current" correctly
    if "current" in right_text:
        right_text = right_text.replace("current", "Current")

    # Replace "-" with "--"
    right_text = right_text.replace("-", "--")

    return right_text


def main() -> None:
    # ===== Parameters =====
    left_text = "Princeton RC".replace(" ", "_").replace("-", "--")

    left_color = "#5A575B".replace("#", "%23")
    right_color = "#F58025".replace("#", "%23")

    icon_path = "PU_mark.svg"

    base_link = "https://img.shields.io/badge/"
    badge_name = "Princeton RC Badge"
    icon_prefix_svg = ".svg?logo=data:image/svg+xml;base64,"
    clickable_link = (
        "https://researchcomputing.princeton.edu/"
    )
    # ===== End of Parameters =====

    # Get the right side text
    right_text = get_right_side_text()

    # ===== Generate Badge =====
    # Encode icon in base64
    with open(icon_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode()
        icon_string = f"{icon_prefix_svg}{base64_string}"

    # Generate the badges
    badge_link = f"{base_link}{left_text}-{right_text}-{right_color}{icon_string}&labelColor={left_color}"

    badge = f"[![{badge_name}]({badge_link})]({clickable_link})"
    # ===== End Generate Badge =====

    print("\nHere's your badge:\n")
    print(badge)


if __name__ == "__main__":
    main()
