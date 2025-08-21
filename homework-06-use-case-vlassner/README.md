[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/HNe6qA3o)
# Instructions 

Victoria Lassner

Draw a use case diagram (using planuml) for the following scenario. 

A system that allows companies to hire employees to fill vacancies. A job description can be created and a link must be provided for posting on platforms such as LinkedIn and similar. Candidates apply for a job by filling out a form and sending documents such as CVs and letters of recommendation, for example. A hiring committee evaluates all candidates for a position. The system should allow the hiring committee to discard candidates who do not meet the requirements. In these cases, an email should automatically be sent to the candidate saying that they are no longer being considered. The remaining candidates are interviewed and a decision is then made. Analytical reports can be obtained for any completed hiring process.

```
@startuml
:Candidates:

:Hiring_Committee:

package jobApp {
    Hiring_Committee --> (Job Description)
    Hiring_Committee --> (Post Job online) .. (Create Social Media Link) : includes
    Hiring_Committee --> (Evaluate Candidates)
    (Evaluate Candidates) --> (Do not meet Requirements) : Discard
    (Evaluate Candidates) --> (Meet Requirments)
    (Meet Requirements) --> (Interview)
    (Interview) --> (Analytical Report)
    (Interview) --> (Decision Made)
    Hiring_Committee --> (Analytical Report)
    (Do not meet Requirements) --> (Send Rejection Email)
    (Send Rejection Email) --> Candidates

    
    Candidates --> (Fill out Form)
    Candidates --> (Send Documents)
    (Send Documents) .. (Letters of Recommendation) : include
    (Send Documents) .. (CVS) : include
}
@enduml
```