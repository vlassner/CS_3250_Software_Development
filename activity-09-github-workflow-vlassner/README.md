# Instructions 

A GitHub Workflow is an automated process that runs one or more pre-configured jobs. 
Workflows are defined by a YAML file checked in to your repository under .github/workflows/. Once a workflow is trigged by an event or at a scheduled time, one of more scripts can be set to execute automatically. There are many different ways to configure workflow events. In this activity you will configure a GitHub workflow that is going to automatically run all tests whenever a push is made to the main branch. 

Take a look at [.github/workflows/my_workflow.yml](.github/workflows/my_workflow.yml): 

```
name: Run tests on push to main 

env:
  PYTHONPATH: src

on: 
  push:
    branches: [ main ]

jobs: 
  test: 
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          python -m unittest discover -s tests -p '*_test.py'
```

Finish the TO-DOs in [tests/square_test.py](tests/square_test.py). Commit and push it to main when you are done. Next, go to the **Actions** tab on GitHub. Verify that the tests failed! Modify [src/square.py](src/square.py), commit and push it to main, and verify that the tests now pass. 
