[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/96ZOmXDB)
# Instructions 

Write the sequence of git commands to implement each of the scenarios described. 

## Scenario 1

Jane wants to control the versions of a paper that she is writing in a file named **paper.txt**. 

TODO #1: Create a folder named **sc1**, make it the working directory, and initialize a new repository. 

```
mkdir sc1
cd sc1
git init
```

Next, Jane wants to create a new file named **paper.txt** and make a few changes to it. 

TODO #2: Make a new version of the paper

```
touch paper.txt
git add paper.txt
git commit -m "creation of paper.txt"
git tag v0.1
```

Jane then makes further modifications on **paper.txt**. 

TODO #3: Make a new version of the paper

```
git add paper.txt
git commit -m "updates to paper.txt"
git tag v0.2
```

After talking to her advisor, Jane needs to revert to version 1 of her paper. 

TODO #4: Revert to version 1 of the paper (hint: use git's reset and checkout commands)

```
git reset --hard
git checkout "v0.1"
```

Jane then makes further modifications on **paper.txt**. 

TODO #5: Make a new version of the paper

```
git add paper.txt
git commit -m "updates to paper.txt"
git tag v0.2
```

## Scenario 2

Bob is working collaboratively with Sam on a project named **jinks**. Bob creates a GitHub repository with the same name and adds Sam as a collaborator. Bob's GitHub repository URL: "https://github.com/bob/jinks". 

Bob clones the repository. 

TODO #1: Git commands to clone the **jinks** repository

```
git clone https://github.com/bob/jinks
```

Bob then creates a file named **README.md** with information about the project. 

TODO #2: Git commands to add **README.md** to the repository, commit and push to remote. 

```
cd jinks
touch "README.md"
git init
git add https://github.com/bob/jinks
git commit -m "added readme file"
git push origin jinks
```

After cloning the repository, Sam creates a new branch called **sam20240219** and adds a new file named **main.py** to the branch. 

TODO #3: Git commands to create and switch to the **sam20240219** branch, followed by the addition of **main.py** into a new version. 

```
git clone https://github.com/bob/jinks
cd jinks
git branch sam20240219
git checkout sam20240219
touch main.py
```

Sam wants to incorporate the changes made to the new branch into **main**. 

TODO #4: Git commands to: 

* switch to **main**
* update the local version of **main** from the remote 
* incorporate the changes made in **sam20240219** into **main**
* remote update 

```
git checkout main
git pull
git merge sam20240219
git add .
git commit -m "update to main"
git config pull.rebase false
git pull origin jinks
git push origin jinks
```