#!/bin/bash

# setup environment
export REPO_NAME="yu-python-repo"
export REGION="europe-west1"

gcloud config set artifacts/repository $REPO_NAME
gcloud config set artifacts/location $REGION

# create a artifact repo
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=python \
    --location=$REGION \
    --description="Python package repository"

# verify
gcloud artifacts repositories list