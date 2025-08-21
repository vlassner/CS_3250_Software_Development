# Unittest

[unittest](https://docs.python.org/3/library/unittest.html) is the unit testing framework that comes with Python (no need to install an external package). In this activity you will write a test case to verify the correctness of the **Fraction** class (located under **src**). 

**fraction_test.py** needs to find the location of the **fraction** module, which is in a different folder. Set the location of the **fraction** module using: 

``` 
export PYTHONPATH=src 
```

# Coverage

[Coverage](https://coverage.readthedocs.io/en/7.3.2/) is a code coverage analysis tool. Used together with **unittest** it can check whether your test suite is fully testing all parts of your code. 

Install **coverage** in a virtual environment using: 

```
pip3 install coverage
```

To have **coverage** monitor the execution of the fraction test case, do the following: 

```
python3 -m coverage run tests/fraction_test.py
```

To see **coverage**'s report run: 

```
python3 -m coverage report
```