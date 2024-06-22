
# University Student Management System
    Video Demo:  https://youtu.be/7W4WLKulTig?si=eE5dRcQEBy8YUkPG
 #### Description:

This project is a University Student Management System written in Python. It provides functionalities to manage and search for student records based on various criteria such as university enrollment, college ID, and branch ID. The system uses a CSV file (`student.csv`) to store student data and employs the `pandas` library for data manipulation and the `prettytable` library for displaying results in a tabular format.

## Project Structure

- `project.py`: The main script that implements the functionalities of the student management system.
- `test_project.py`: Contains unit tests for the functions defined in `project.py` using the `pytest` framework.
- `student.csv`: The CSV file containing student records.

## Features

1. **Check Student Enrollment**: Verify if a student is enrolled in the university using their hall ticket number.
2. **Search by College ID**: Retrieve a list of students associated with a specific college ID.
3. **Search by Branch ID**: Retrieve a list of students associated with a specific branch ID.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pandas` library
- `prettytable` library
- `pytest` library (for testing)

### Installation

1. Clone the repository or download the source code.
2. Install the required libraries using pip:
    ```bash
    pip install pandas prettytable pytest
    ```
3. Ensure `student.csv` is in the same directory as `project.py`.

### Running the Application

To start the application, execute the following command:
```bash
python project.py
```


### Running Tests
To run the tests, execute the following command:
```bash
    pytest test_project.py
```

## Detailed Functionality
`project.py`
- Data Loading and Initialization:

```python
data = pd.read_csv("student.csv")
```

Reads the student data from `student.csv`

- ### Main Function:

```python
def main():
    ...
```
Provides a menu-driven interface for the user to interact with the system.

- ### Student Verification:

```python
def stu_on_uni(id):
    ...
```
Verifies if a student is enrolled in the university using their hall ticket number.

- ### College Search:
```python
def clg_on_uni(dd):
    ...
```
Searches for students based on college ID.

- ### Branch Search:

```python
def brch_on_uni(id2):
    ...
```
Searches for students based on branch ID.


`test_project.py`
- ### Unit Tests:
Contains tests for the functions in `project.py` to ensure they work as expected.

```python
def test_stu_on_uni():
    ...

def test_clg_on_uni():
    ...

def test_brch_on_uni():
    ...
```

`student.csv`
- ### Sample Data:
```csv
stu_id,stu_name,stu_clg,stu_brch,stu_year
101,hemanth,L1,101,20
102,sai,L2,102,21
103,teja,L3,103,22
104,ravi,L4,104,20
201,sai,L1,101,20
```