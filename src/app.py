import json


def handler(event, context):
    print("Hei fra oppgradert versjon 3")
    print(json.dumps(event))
    # print(dir(context))
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
