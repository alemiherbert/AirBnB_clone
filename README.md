# AirBnB Clone
AirBnB clone is a simple clone of AirBnB, implemented in python for the ALX Software Engineering Program

## • Requirements
The project was built using python 3.10.12 running on Ubuntu 22.04 LTS on WSL.

The code was checked for PEP8 compliance using pycodestyle v2.8.

Development was primarily done using Vim v8.2.1847 and GNU Nano v6.2

## • Installation
Clone the repository from GitHub
```(bash)
[~]$ git clone git@github.com:alemiherbert/AirBnB_clone.git
```
`cd` into the project directory and run the console
```(bash)
[~]$ cd AirBnB_clone
[AirBnB_clone]$ ./console.py
```
## — Usage
The console works in both interactive and non-interactive mode. Below are the available commands.

| Command     | What it does |
|:--- |:--- |
|`create`| Creates a new instance of `BaseModel` and saves it the JSON file.|
|`show`| Prints the string representation of the an instance based on the class name |
|`destroy`| Deletes an instance based on the class name and id |
|`all`| Prints all string representations of all instances based or not on the class name |
|`update`|Updates an instance based on the class name and id.

## — Testing
The unittests for the AirBnB clone are located in the __tests__ folder. To run all tests, run this command
```(bash)
[AirBnB_clone]$ python3 unittest -m discover tests
```
Of course, you can test a file at a time
```(bash)
[AirBnB_clone]$ python3 unittest -m tests/test_console.py
```
## — Authors
Alemi Herbert <> <alemiherbert@gmail.com>