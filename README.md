To install the docker image, you need docker desktop. https://www.docker.com/products/docker-desktop/
Once docker desktop is installed, clone the repo to a local folder:
```
git clone https://github.com/vikasgrover2/vg-llm.git
cd vg-llm
```

Next, build the base notebook image which will grab the official jupyter/basenotebook image
```
cd base-notebook
docker build . -t jupyter/base-notebook:v1
```

With the base notebook built, we will extend that image and add all the dependencies needed to run langchain code examples. These dependencies are all mentioned in requirements.txt.
```
cd ..
docker build . -t jupyter/notebook_with_llm:v1
```

You will need to update the .env file with your OPEN API Key, Activeloop Deeplake API key,Google API KEY and Google CSE ID. You can get the API Keys from:
- https://platform.openai.com/api-keys
- https://app.activeloop.ai/
- https://console.cloud.google.com/apis/credentials
- https://programmablesearchengine.google.com/controlpanel/create

  More instructions regarding GOOGLE API and CSE ID are available at: https://python.langchain.com/docs/integrations/tools/google_search

The extended image is what is used to finally start the docker containter using docker compose. If you change the name of the image, make sure to update docker-compose.yml.
```
docker compose up -d
```

Once the container starts up, jupyter server will be available at http://127.0.0.1:8888/lab. To get the token, login to the container, and list server
```
docker exec -it llm bash
jupyter server list
```
Token will be displayed after '?token='

Use the token to log into the jupyter notebooks. If all the libraries in requirements were installed successfully, all code should run.
