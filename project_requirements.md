# Requirements for Django Email Classifier Application



## Objectives
This Django Email Classifier is a simple web application that classifies emails as either newsletters or regular emails.

## Core Business Requirements (User story)
#### 1. As an email admin, I should be able to login to the Application's Admin page.
#### 2. As an email admin, I should be able to upload email export files specifically in .csv format.
#### 3. As an email admin, I should be able to classify the emails in bulk whether each on is a *newsletter* or a *regular email*.
#### 4. As am email admin, I should be able to view the classification results easily

## Extended Busienss Requirements (May or not be implemented depending on the time constraints)


## Technical Requirements
### Tech Stack:
- Python
- Django
- Any csv reader modules
- Any logistic regression modules (Scikit-Learn, Keras, spaCy, Tensorflow)
- Django's Unit Testing Module (unittest)
- SQLite

## Project Roadmap
#### 1. Initialize Django Project
#### 2. Create Django superuser and check the admin page
#### 3. Create essential models for the project
#### 4. Register models to the admin
#### 5. Implement admin interface for uploading csv file
#### 6. Implement a service for reading data from different sources
  - Only fully implement csv parsing of email
  - Leave the rest as blank slate (use pass)
#### 7. Implement a service for classifying email data 
  - mock classification - for testing and initial implementations
  - logic-based classification
  - using machine learning model
#### 8. Implement a service the machine learning classification
  - Only fully implement one,
  - leave the rest as blank slate (use pass)
#### 7. Implement admin interface for triggering classification (the classification at this point would still be a dummy)
#### 8. Add model to monitor classification progress
#### 9. (Optional) Make the classification asynchronous, meaning the interface should not hang up when triggering the event
#### 10. (Optional - for asynchronous) There should be progress monitoring of the status
#### 11. Implmenet admin interface for displaying classification results
