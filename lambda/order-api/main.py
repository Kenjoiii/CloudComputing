import json

def handler(event, context):
    print("Order API invoked")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Mock Order API successful"})
    }
