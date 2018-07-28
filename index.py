from __future__ import print_function

import base64
import json

print('Loading function')


def lambda_handler(event, context):
    print('========event========')
    print(json.dumps(event, indent=4, sort_keys=True))

    records = event['Records']

    for record in records:
        print(record)
        print(record['eventID'])

    print('Successfully processed {} records.'.format(len(records)))

    output = records
    return {'records': output}
