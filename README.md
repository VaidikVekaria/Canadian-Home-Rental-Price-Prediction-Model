# Canadian-Home-Rental-Price-Prediction-Model
Data Science and Machine Learning Project for predicting rental prices for different types of homes in canada.

Web-interface to get price predictions using input paramaters. 
![Capture2](https://github.com/user-attachments/assets/6dff8c04-8ae6-447d-ac39-3ecc5d213ff0)


## Preparing training data
Pre-processing, feature extraction, oneHotencoding performed on kaggle dataset. https://www.kaggle.com/datasets/sergiygavrylov/25000-canadian-rental-housing-market-june-2024/code?datasetId=5214669

## model/main.py 
Utilized GridSearch CV to find the best model on the training data and saved the model in a pickle file. 

![GridSearchCV](https://github.com/user-attachments/assets/91257427-739b-4bce-a4cc-7f11573050b2)
![Linear Regression](https://github.com/user-attachments/assets/591797b7-0dda-462e-b4e3-be5cd9acec5a)

## client/app.js
Populates the drop down menu for 'type' and 'furnishing'. Using Geocode API, 'Address' is coverted to longitude and latitude which are used as input features for our model. 
![type](https://github.com/user-attachments/assets/0878468d-fb30-4844-958f-dca3b80b474b) ![furnishing](https://github.com/user-attachments/assets/b3466cbb-17af-4fb2-af19-8288621b3c9c)


## server/server.py
Running a flask server with Get and Post Routes. Finally deploy flask application on Amazon EC2 intance using Nginx reverse proxy. 


