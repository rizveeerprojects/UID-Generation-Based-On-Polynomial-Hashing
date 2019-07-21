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

1. You will need two csv formatted (',' separated) files respectively for Training and Testing Database. Both of them must be in proper csv formatted having specific column names. Please see the example image:

![file format](https://raw.githubusercontent.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/master/Images/file_format.png)

2. Our projects main code is [implementation.py](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/implementation.py). Run this code through terminal or any python supported IDE.

3. First we will take input of how many numbers we will use to mod string mapped integers and then take the numbers which will be used to mod.

![mod input](https://raw.githubusercontent.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/master/Images/mod_input.png)

4. Then we will take the training and testing file's path. It is advised to keep the files in the same directory and provide just file name. Don't give any extra trailing or starting spaces in any input.

![file_name](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/file_name.png)

5. Then give how many columns are in the file and how many of them are string and will be hased. After that provide the column names. First those which will be hased and following that those which will not be hashed. We are saying that all of the columns of csv files will be used to generate UID, either their type will be string(which will be hashed) or integer(which will not be hashed). 

![col num hash col](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/col_num_hash_col.png)
![col description](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/col_description.png)

6. Then we will provide weights to the attributes. First those columns which have string data types and after that those column which will have integer data type.
![weight](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/weight_provide.png)

7. Then we will take input of conflict measure ratio (CM) and min_attribute_conflict. CM denotes the minimum threshold to denote there exists conflict for a testing instance and min_attribute_conflict denotes the minimum number of attributes to be conflicted to report a tuple as conflicted tuple for the current training instance. 
![cm](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/cm_min_attr.png)

8. Then we will provide deviation amount for each integer columns aka attributes. 
![deviation](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/deviation.png)

9. Then our code will start to calculate conflict amount of each testing instacne from testing csv file. This code is implemented as multithreaded aka collection parallel program. We have defined there will be at most 10 threads. But users can change this variable by updating the following parameter in the code. Performance in run time will improve more and more if we use multicore computer.

![threads](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/thread.png)

10. The Result of the code will be saved into **ResultFile.txt** with each testing instance along with possible conflicted training instances. 
![result](https://github.com/rizveeerprojects/UID-Generation-Based-On-Polynomial-Hashing/blob/master/Images/result.png)



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

