import json

def handler(event, context):
    print("WebSocket API invoked")
    route_key = event.get('requestContext', {}).get('routeKey')

    if route_key == "$connect":
        return {"statusCode": 200, "body": "Connected"}
    elif route_key == "$disconnect":
        return {"statusCode": 200, "body": "Disconnected"}

    # Handle the "ping" action required by the test
    body = event.get('body', '{}')
    try:
        body_json = json.loads(body)
        if body_json.get('action') == 'ping':
            return {
                "statusCode": 200,
                "body": json.dumps({"action": "pong", "timestamp": "mock-time"})
            }
    except json.JSONDecodeError:
        pass

    return {"statusCode": 200, "body": json.dumps({"message": "Mock WebSocket action..."})}
