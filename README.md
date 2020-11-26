# NMT-API - API for Neural Machine Translation
API for NMT using HuggingFace's Transformers repo and pretrained models.

## Instructions for usage:

 * Clone the repo and `cd` to it:
``` 
git clone https://github.com/piEsposito/nmt-api.git
cd nmt-api

```

 * Set the token on `.env` file

 * Build the image from Dockerfile:
 
 ```
 docker build . -t nmt-api:v1
 ```
 
 * Run the API server
 
 ```
 docker run -p 8000:8000 nmt-api:v1
 ```
