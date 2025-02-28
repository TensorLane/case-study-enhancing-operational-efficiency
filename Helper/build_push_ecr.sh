## THE FOLLOWING COMMAND IS FROM THE OFFICIAL ECR PUSH COMMAND 
## FIRST LOGIN WITH YOUR AWS CRED IN CLI
## CREATE ECR REPO MANUALLY IN THE CONSOLE
## JUST SEE THE PUSH COMMAND ON THE CONSOLE. THE IMAGE NAME NEED SO BE SET AS LATEST 
## LAUNCH DOCKER AND RUN THIS SCRIPT

%%sh

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 955028845085.dkr.ecr.us-east-1.amazonaws.com

# template is the repo name and sklearn is the image name / tag name
docker build -t repo-name .

# tag the image so it can be pushed to repo
docker tag repo-name:latest 955028845085.dkr.ecr.us-east-1.amazonaws.com/repo-name:latest

# push the image to ECR
docker push 955028845085.dkr.ecr.us-east-1.amazonaws.com/repo-name:latest