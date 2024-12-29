# Multiplue DateBases
This repository hosts a Python program using PyQt to establish multiple database connections. It's a basic implementation showcasing how to use PyQt's `QSqlDatabase` class to connect to SQLite databases. The program also uses PyQt to create a simple GUI window.

## Installation
To install PyQt, use pip:
```shell
pip install pyqt5
```
For the SQLite database, it's included in the standard library of Python.

## Usage
Run the Python file `multiplue_datebases.py` to start the application. The function `createConnection` takes a database name as an argument and tries to establish a connection to it.

```python
window.createConnection("test_db.sqlite")
```
If the connection cannot be established, it will print an error message. If the connection is successful, it will return True.

## Contributing
Please feel free to fork this repository and submit pull requests. We're always open to improvements and extensions.

## License
This project is licensed under the terms of the MIT license.