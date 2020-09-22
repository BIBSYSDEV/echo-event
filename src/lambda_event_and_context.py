from __future__ import unicode_literals
import logging
import json
import time

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)


class PythonObjectEncoder(json.JSONEncoder):
    """Custom JSON Encoder that allows encoding of un-serializable objects
    For object types which the json module cannot natively serialize, if the
    object type has a __repr__ method, serialize that string instead.
    Usage:
        >>> example_unserializable_object = {'example': set([1,2,3])}
        >>> print(json.dumps(example_unserializable_object,
                             cls=PythonObjectEncoder))
        {"example": "set([1, 2, 3])"}
    """

    def default(self, obj):
        if isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return json.JSONEncoder.default(self, obj)
        elif hasattr(obj, '__repr__'):
            return obj.__repr__()
        else:
            return json.JSONEncoder.default(self, obj.__repr__())


def lambda_handler(event, context):
    print('Event: ', json.dumps(event))
    print('Context: ', json.dumps(vars(context), cls=PythonObjectEncoder))
    sleep(15)
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
