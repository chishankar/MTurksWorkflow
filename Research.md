# Research of MTurk Workflow Boto API

My initial goal was to be able to have 1 ```Batch``` with 2 ```HITs``` (Human Integrated Tasks) each with seperate qualifications so that a single user can do one HIT but not the other task as shown in a work flow modeled below:

![Alt text](https://user-images.githubusercontent.com/25187819/28838989-27ab04d6-76c0-11e7-8961-66174a143e54.png "WorkFlow")

 Upon further research I found two things:
 1. It is not possible to create two ```HITS``` within the same ```batch``` with different qualifications
 2. It is not possible using ```AWS``` (Amazon Web Services) via the ```Boto API``` to restrict the user from accepting the next HIT in
    the batch.

The model is thus reduced to:

![Alt text](https://user-images.githubusercontent.com/25187819/28838988-27a86398-76c0-11e7-96d5-dbcccb523639.png "WorkFlow")

Where ```Qualificiation A``` grants the user access to completing 2 ```HITS``` within the same ```batch```. Further research shows, that limiting the user to one ```HIT``` in the same ```batch``` can be handled by the backend server in multiple different ways.
  1. The server can use a ```JavaScript``` function to request the ```USER_ID's``` of those who have completed the random first hit and
      dynamically change the link on the following ```HIT``` to NULL or to a message: "You have already completed a HIT in this batch"
  2. You can have one ```Qualification Test``` for single ```HIT``` and dyanmically change what the link redirects you too on the backend.
  
 
 
 
 
 * Sources for research can be found under the sources file in the repository
