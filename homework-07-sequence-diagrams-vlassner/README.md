[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/st6fJh7_)
# Instructions 

Victoria Lassner

Draw UML sequence diagrams for the scenarios described below. 

# Scenario 1

Citizens can log onto a website to report the location and severity of potholes found in the city. The system prompts authenticated users to enter information using an online form. The information that they enter is saved in a database.

Create a UML sequence diagram with the participants: **Citizen**, **Web Server** and **Database**. The diagram must have an **alternative flow** showing paths for **successful** and **failed** authentication, based on the result of a database query for a citizen user with a given "id" and the subsequent password verification. In case of successful authentication, the web server must redirect citizens to "/potholes/new" (an input form). Citizens can then enter the information (location and severity) of a pothole found via the online form. As a result of the form submission, a new pothole entry is inserted into the database. The web server then sends a confirmation message to the citizen. Alternatively, if the citizen cannot be authenticated, an “authentication failure” message is sent back to the citizen.

```
@startuml
skin rose

participant Citizen 
entity "Web Server"
database Database

Citizen -> "Web Server": Login
"Web Server"-> Database: query for customer ID and Password

alt success
 Database -> "Web Server": "Successful authentication"
 "Web Server" -> Citizen: Redirect to /potholes/new
 Citizen -> "Web Server": Enter location and severity
  "Web Server" -> Database: Save new pot hole info
 "Web Server" -> Citizen: Confirmation message
else failure
  Database -> "Web Server": "Failed authentication"
 "Web Server" -> Citizen: Send authentication failure message 
end
@enduml
```
2 points

# Scenario 2

Users of the free app "mujhe sab pata hai" (I know everything) can ask questions that must start with: 

* what should I do to ... or 
* what should I do if ...

The app's backend uses NLP (Natural Language Processing) to standardize question text and then queries a curated database of answers to the most popular questions. Questions that cannot be found in the database are answered with "Hmmm... Let me think about it. Ask me again in 24 hours." The question is then saved in the database. The system's editors periodically query the database for unanswered questions. After some research, they come up with an answer with a dash of humor and sarcasm. The response is then stored in the database. Whenever a message is sent back to the customer, the app also sends an advertisement and this is how the developers earn their revenue. The app pledges to answer all questions in 24h, as long as they do not violate the app's usage policy that prohibits questions with criminal or offensive intentions.

Create a first UML sequence diagram with participants: **user**, **frontend**, **backend**, **database**, and **ad server**. The **frontend** displays an input form where the user can enter their question. The question is then sent to the **backend**. The diagram should have an **alternative flow** showing paths for when an answer to the question is found in the database or not. If the question is new, it is  saved in the database. Before the **frontend** displays the answer to the question, it exchanges messages with the **ad server** requesting that a new ad be generated. The ad is then displayed with the answer. 

``` 
@startuml
skin rose

participant User 
entity frontend
entity backend
entity "Ad Server"
database Database

frontend -> User: displays an input form
User -> frontend: Asks a question
frontend -> backend: sends input
backend -> Database: query for question

alt success
 Database-> backend: question is found & sends answer
 backend -> "Ad Server": pulls ad for question
 backend -> frontend: sends answer
 "Ad Server" -> frontend: sends ad
 frontend -> User: displays ad and answer
  
else failure
  Database-> backend: question is not found
  backend -> Database: saves question
  backend -> frontend: sends failure message 
  frontend -> "Ad Server": requests for new ad to be made
  frontend -> User: displays "Hmmm... Let me think about it. Ask me again in 24 hours."
end
@enduml
```
2 points

Create a second UML sequence diagram with the participants: **editor**, **frontend**, **backend**, and **database**. The **frontend** asks the **backend** for an unanswered question, prioritizing the oldest ones. After querying the database, the **backend** returns an unanswered question to the **frontend**, which in turn displays an input form where the editor can enter the "official" answer to the question. The response is then sent to the **backend** to be saved in the database.

```
@startuml
skin rose

participant Editor 
entity "frontend"
entity "backend"
database Database

frontend -> backend: asks for unanswered questions
backend -> Database: Query for oldest question
Database -> backend: sends oldest question
backend -> frontend:  returns unanswered question
frontend -> Editor: Displays input form for question
Editor -> frontend: Inputs answer
frontend -> backend: sends response
backend -> Database: saves response
@enduml
```
1 point

