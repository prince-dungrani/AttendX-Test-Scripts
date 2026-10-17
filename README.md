
# AttendX-Test-Scripts

## Project Description
This repository contains sample automated test scripts
for the AttendX student attendance application.

## Files
- login_test.py: Tests valid login, wrong password,
  and empty login fields.
- attendance_test.py: Tests attendance marking,
  duplicate attendance, and an empty student ID.

## Requirements
- Python 3

## Run Tests
python -m unittest login_test.py
python -m unittest attendance_test.py

## Note
These are demonstration tests using sample logic.
Connect them to the real application before production use.
