# Dockerized-Sentiment-Analysis

This Flask based web application allows the user to enter a sentence into the form and after submitting it, the app will classify the sentiment of the sentence and output wether it's positive, negative or neutral. Both the web app and the ml model are dockerized into a docker image. 

To make it work: 

Clone the project, then type this command: 
    
    docker-compose up

The application will run on the docker port 5000.

To do unit tests, type this command into a new terminal located in the same docker working directory: 

    python test_app.py

If you wish to train the model again, model.pkl should be deleted, since a new one will be made for each train. Type this command to train: 

    python model.py

The dataset used can be found here: https://www.kaggle.com/crowdflower/twitter-airline-sentiment

We chose this dataset beacuse of its volume almost 15,000 tweet examples and also because we thought it would be interesting to see if a model train on tweets can be better to compare with reviews.

Our web app is themed for movie reviews "Mugen train" from demon slayer. We want to know if every single person liked the movie. So when you enter something it will say if it is a positive, negative or neutral review.
