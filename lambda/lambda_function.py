import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from CICD Github Actions workflow from VSCode')
    }