# ALDA_Activity

## Description

In this project we will see the complexity and the time execution of differents sorting algorithms, in this case we used bubble sort, merge sort and shell sort. 

## Python Version

Python 3.10.5

## Running locally and testing

* Create virtual enviroment: `virtualenv env`
* To install dependencies: `pip install -r requirements.txt`

## Graficos de ejecucion respecto al tiempo

### Bubble Sort
![bubble](https://user-images.githubusercontent.com/90010884/223318473-48d1954b-62d6-4eb8-9c05-deae2ac709a6.png)

### Merge Sort
![merge](https://user-images.githubusercontent.com/90010884/223318483-cb869fa9-9d01-4eea-a66c-bc0bd1b8df51.png)

### Shell Sort
![shell](https://user-images.githubusercontent.com/90010884/223318491-e1f7f491-a309-4606-bf32-8b51eafde686.png)

## Current Coverage

To run `coverage`, make sure that you have it installed in your pc, if not run `pip install coverage`, then run the requirements.txt. After that run `coverage run -m unittest discover` and `coverage report` it show you the following table:

### Test
![image](https://user-images.githubusercontent.com/90010884/223321908-1e81b14d-f438-42da-9d99-edb75318af3b.png)

## Code Beautifer

After install Black, run de comand `black . -l 120` to beautifier you code

