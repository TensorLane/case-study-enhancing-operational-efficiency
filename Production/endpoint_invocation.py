import boto3
import json
import pandas as pd

df_production_w4 = pd.read_csv('df_4.csv')

X = df_production_w4.sample(8)
X = X.drop(['date', 'Load_Type'], axis='columns')

features = X.to_dict(orient='records')
payload=json.dumps({'features':features}).encode()

aws_access_key_id = 'your aws access key id'
aws_secret_access_key = 'your aws secret access key'

# Create a new session with SageMaker
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Create a SageMaker Runtime client
sagemaker_runtime = session.client('sagemaker-runtime', region_name='us-east-1')

# Invoke the endpoint
response = sagemaker_runtime.invoke_endpoint(EndpointName='load-classifier-endpoint',ContentType='application/json', Body=payload)
result = json.loads(response['Body'].read().decode())
print("Prediction result:", result)


''' 
-- USE THIS FUNCTION TO INVOKE ENDPOINT WITH AWS LAMBDA
-- ATTACH SAGEMAKER ACCESS POLICY TO LAMBDA FUNCTION ROLES 

import boto3
import json
def lambda_handler(event, context):
    client = boto3.client('sagemaker-runtime')
    # Specify your SageMaker endpoint name
    endpoint_name = 'california-housing-xgbregressor-endpoint'
    # Format the input data as required by your model
    payload = json.dumps(event)
    response = client.invoke_endpoint(EndpointName=endpoint_name,
                            ContentType='application/json', Body=payload)
    result = json.loads(response['Body'].read().decode())
 
    return result

-- JSON FORMAT FOR LAMBDA FUNCTION TEST :
{
  "features": [
    {
      "MedInc": 7,
      "HouseAge": 16,
      "AveRooms": 5.7612903225806456,
      "AveBedrms": 1.0580645161290323,
      "Population": 548,
      "AveOccup": 3.535483870967742,
      "Latitude": 37.79,
      "Longitude": -120.83
    },
    {
      "MedInc": 7,
      "HouseAge": 33,
      "AveRooms": 4.2091690544412605,
      "AveBedrms": 1.0601719197707737,
      "Population": 1318,
      "AveOccup": 3.7765042979942693,
      "Latitude": 37.61,
      "Longitude": -121.02
    }
  ]
}
'''
