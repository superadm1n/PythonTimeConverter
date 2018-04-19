# PythonTimeConverter
Tool written in Python that allows the conversion of time between Military 
and Standard time. You can integrate this into an existing project or run
the module directly from the command line as a standalone application.


### Prerequisites

Python 3.x

## Tests

Code contained in unit_tests.py covers the testing of the 2 functions within
converter.py and validates that it will accept only good input and throw 
exceptions on bad data

## Usage

You may use this module directly on the command line by the following syntax
```
converter.py <ENTER>
converter.py -m2s HH:MM <ENTER> --> converts Military time to Standard time
converter.py -s2m HH:MM:AM/HH:MM:PM <ENTER> --> converts Standard time to Military time
```


## Authors

* **Kyle Kowalczyk** - *Initial work* - 
[Superadm1n](https://github.com/Superadm1n)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

