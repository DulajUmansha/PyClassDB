# PyClassDB

Convert your MySQL database table into Python classes effortlessly, making MySQL and Python integration a breeze. This tool simplifies the process of connecting MySQL databases with Python applications, allowing developers to seamlessly work with their data.

![Screenshot 2023-11-14 135511](https://github.com/DulajUmansha/PyClassDB/assets/89386135/ea3d75e3-f5bf-4f78-bdc5-d05f93ddd974)

## Features

- **Automatic Conversion**: Quickly convert MySQL tables into Python classes with just a few simple steps.
- **Effortless Integration**: Streamline the connection between MySQL databases and Python applications.
- **Pyside6 Compatibility**: Built with Pyside6 support to enhance the user interface and overall user experience.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version 3.10)
- Pyside6

### Installation

1. Install PySide6:
   
```bash
pip install PySide6
```
   
2.Clone the repository:

   ```bash
   git clone https://github.com/DulajUmansha/PyClassDB.git
   ```

## How to use

1. Here is the sample MySql tables:
   
![Screenshot 2023-11-15 094200](https://github.com/DulajUmansha/PyClassDB/assets/89386135/5bb3727b-ec00-4176-8aba-884776ffa577)

2. Open ``` pyclassdb.py ``` and run:

https://github.com/DulajUmansha/PyClassDB/assets/89386135/332d31fb-60f7-4502-95d3-462696a0c48a

3. Finally, you can see created python class file are in the output folder. 

![Screenshot 2023-11-15 095145](https://github.com/DulajUmansha/PyClassDB/assets/89386135/23253ce4-bca9-4bcb-995f-fcdc729fc248)

## Example

1. connect to the MySql Database:
   ```python
   from database.database import Database
   
   db = Database()
   db.connect()
   ```

2. Retrive data from table:
   ```python
   from database.city import city

   tbl_city = city()
   data = tbl_city.retriveData() # ex: SELECT * FROM city;
   ```
   ```python
   from database.city import city

   tbl_city = city()
   tbl_city.set_conditionData('Name','Malvinas Argentinas') # ex: SELECT * FROM city WHERE name = 'Malvinas Argentinas';
   data = tbl_city.retriveData()
   ```
   ```python
   from database.city import city

   tbl_city = city()
   tbl_city.set_columnFilter(['Name']) # ex: SELECT Name FROM city; 
   data = tbl_city.retriveData()
   data_list = []
   for datum in data:
       data_list = data_list + [value for key, value in datum.items()]
   ```
3. Insert Data:
   ```python
   from database.city import city

   tbl_city = city()
   tbl_city.set_Name("ABC-city")
   tbl_city.set_CountryCode("AFG")
   tbl_city.insertData() # ex: INSERT INTO `city` (Name,CountryCode) VALUES ('ABC-city','AFG');
   ```
