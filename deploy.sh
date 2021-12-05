#!/usr/bin/env bash

# Log into ECR
aws ecr get-login-password \
--region us-east-1 | docker login --username AWS --password-stdin 192967699069.dkr.ecr.us-east-1.amazonaws.com

# Build the Docker image and push it to ECR with `latest` tag
docker build -t lightsaber-private aws/
docker tag lightsaber-private:latest 192967699069.dkr.ecr.us-east-1.amazonaws.com/lightsaber-private:latest
docker push 192967699069.dkr.ecr.us-east-1.amazonaws.com/lightsaber-private:latest

# Update lambda to use latest ECR image
aws lambda \
update-function-code \
--function-name grabDislikeCount \
--image-uri 192967699069.dkr.ecr.us-east-1.amazonaws.com/lightsaber-private:latest --region us-east-1