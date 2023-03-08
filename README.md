# AppNotes
Work for certification in python

# Application Instruction

`--help` -- show this message

`--add [OPTION]`-- append new note
* `--title TITLE` -- title of notes
* `--msg MESSAGE` -- message of notes

`--show [OPTION]`-- show list of notes
* `--all` -- show all list
* `--id ID` -- id of notes

`--find [OPTION]`-- search note. If multiple keys are specified, then the AND rule applies
* `SUBSTRING` -- search substring in title and message
* `--title SUBSTRING` -- search substring in title
* `--msg SUBSTRING` -- search substring in message

`--edit ID` -- edit note of ID
* `--title TITLE` -- title of notes
* `--msg MESSAGE` -- message of notes

`--delete ID` -- delete note of ID

`--export` -- export data from csv file

`--import PATH_TO_FILE` -- import data to csv file
