import json


def handler(event, context):
    print(json.dumps(event))
    print(context)
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
