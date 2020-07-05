# Deploy a ML model to AWS EC2

Deploying a Machine Learning model to EC2 nd accessing it as a webserice using [flask](https://palletsprojects.com/p/flask/) and [docker](https://www.docker.com/).

## Getting Started

1. Use [Iris_LogisticReg.ipynb](https://github.com/abhi094/Educational-Projects/blob/master/Deploying%20Model%20to%20AWS/Iris_LogisticReg.ipynb) to train a logistic regression model on the iris dataset and generate a pickled model file (iris_trained_model.pkl)
2. Use **app.py** to wrap the inference logic in a flask server to serve the model as a REST webservice:
3. Execute the command python **app.py** to run the flask app.
4. Go to the browser and hit the url 127.0.0.1:80 to get a message Hello World! displayed.
5. Next, run the below command in terminal to query the flask server to get a reply 2 for the model file provided in this repo:
```
curl -X POST \
0.0.0.0:80/predict \
-H 'Content-Type: application/json' \
-d '[5.9,3.0,5.1,1.8]'
```
6. Run docker build -t app-iris . to build the docker image using Dockerfile. (Pay attention to the period in the docker build command)
7. Run docker run -p 80:80 app-iris to run the docker container that got generated using the app-iris docker image.
8. Use the below command in terminal to query the flask server to get a reply 2 for the model file provided in this repo:
```
curl -X POST \
127.0.0.1:80/predict \
-H 'Content-Type: application/json' \
-d '[5.9,3.0,5.1,1.8]'
```

Ref : https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf
