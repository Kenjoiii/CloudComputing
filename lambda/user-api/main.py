import json

def handler(event, context):
    print("User API invoked")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Mock User API successful"})
    }
