def handler(event, context):
    print("Notification Worker invoked")
    for record in event.get('Records', []):
        print(f"Processing message: {record.get('body')}")
    return {"statusCode": 200}
