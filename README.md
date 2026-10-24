# Contact Book

A simple Python CLI application for managing and searching contacts.

این پروژه یک دفترچه مخاطبین ساده است که امکان ثبت، نمایش، جست‌وجو و حذف مخاطبین را از طریق ترمینال فراهم می‌کند.

## Features

- Add new contacts
- Display all saved contacts
- Search contacts by name
- Delete contacts by their list number
- Prevent empty names and phone numbers
- Avoid duplicate phone numbers

## Requirements

- Python 3
- No external packages required

## How to Run

Run the following command from the project directory:

```bash
python3 main.py
```

## How It Works

The application stores contact names and phone numbers in two lists. An interactive menu allows users to add, view, search, and delete contacts.

اطلاعات در این نسخه فقط هنگام اجرای برنامه در حافظه نگهداری می‌شوند. پس از خروج، مخاطبین ذخیره نمی‌مانند.

## Concepts Practiced

- Variables and strings
- Lists and list methods
- Functions
- Conditional statements
- Loops
- User input and output
- Basic input validation
- Searching through a list

## Limitations

- Contacts are not saved after the program exits.
- Each phone number can only be added once.
- Contact information is stored in memory only.

