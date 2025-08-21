# Instructions

Create a virtual environment and install the following packages: 

```
pip3 install pycodestyle autopep8
```

To check if **src/example1.py** complies to PEP8 run: 

```
python3 -m pycodestyle src/example1.py
```

Manually correct the errors/warnings and re-check your code until it clears PEP8. 

Alternatively, you can automatically make your code comply to PEP by running: 

```
python3 -m autopep8 --in-place src/example1.py
```