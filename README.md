# harbourflowlogistics_groupwork
HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
Python version tested: python 3.14.7

Team members and concrete contributions
---------------------------------------
Name: Erik Benjegård
Contribution: 
1. Completed Meny and task 5
2. Peer review 

Name: Ziwei Luo 
Contribution: 
1. Completed task 2, task 3, task 4, task 9
2. Peer review 
3. Drafted README architecture notes 

Name:
Contribution:
1. Completed task 6 and task 7


Design notes
------------
ARCHITECTURE NOTES

1. Main function boundaries:
main() only prints the menu, reads the choice, validates it is an
integer between 1 and 8, and dispatches to a task function. No
business logic is in main().

2. Input validation:
Menu-level validation rejects non-integers and out-of-range options.
Field-level validation happens inside each task function:
validate_ref() checks format, calculate_quote() rejects non-positive
inputs, and get_number() wraps int(input()) in try/except ValueError
for reuse across weekly_report().

3. Shared calculations:
Business rates are defined as module-level constants
(BASE_CHARGE_SEK, WEIGHT_RATE_SEK_PER_KG, DISTANCE_RATE_SEK_PER_KM,
STANDARD/EXPRESS/PRIORITY_MULTIPLIER). calculate_quote() and
compare_scenarios() both reuse them.

4. Known limitations:
- compare_scenarios() reads distance and weight inside the function,
  so it cannot be tested without user input.
- The pricing formula is duplicated in calculate_quote() and
  compare_scenarios(); a shared helper would remove the duplication.
- validate_ref() returns "" for all invalid cases, so the caller
  cannot tell the user which rule failed.

-----------------
Write "None known" or describe each known limitation.
