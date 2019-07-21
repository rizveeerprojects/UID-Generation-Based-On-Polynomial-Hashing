# UID-Generation-Based-On-Polynomial-Hashing
This project is a UID Generation System based on polynomial hashing.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.x
```

### Installing

```
Install Python 3.x 
```
```
Create a directory. Clone this repository there or download as zip and then unzip it in the directory.
```

## How To Run The Code

1. You will need two csv formatted (',' separated) files respectively for Training and Testing Database. Both of them must be in proper csv formatted have specific column names. Please see the example image:

![file format](https://raw.githubusercontent.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/master/Images/file_format.png)

2. Our projects main code is [implementation.py](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/implementation.py). Run this code through terminal or any python supported IDE.

3. First we will take input of how many numbers we will use to mod string mapped integers and then take the numbers which will be used to mod.

![mod input](https://raw.githubusercontent.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/master/Images/mod_input.png)

4. Then we will take the training and testing file's path. It is advised to keep the files in the same directory and provide just file name. Don't give extra any trailing or starting spaces in any input.

![file_name](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/file_name.png)

5. Then give how many columns are in the file and how many of them are string and will be hased. After that provide the column names. First those which will be hased and following that those which will not be hashed. 

![col num hash col](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/col_num_hash_col.png)
![col description](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/col_description.png)

## Built With

* [Python 3.x] (https://docs.python.org/3/) 
* Linux 16.04 Operating System
* [Google Spreadsheet CSV Formatted File] (https://www.google.com/sheets/about/)


## Authors
* **Amin Ahsan Ali**
* **Mainul Islam Zaber**
* **Redwan Ahmed Rizvee** 
* **Nahian Ashraf**
* **Riddho Ridwanul Haque**
* **Muntasir Wahed**


## Acknowledgments

* BRAC
* Data and Design Lab

