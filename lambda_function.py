import logging
import json
import os
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(inputPayload, context):
    slack_link = os.environ['SLACK_URL']
    try:
        url = inputPayload['issue']['html_url']
    except Exception as e:
        logger.error(e)
        # return a 500 error code
        res = json.dumps({'statusCode': 500, 'body': f'Error: {e}'})
        return res
    reply = {'text': f"Issue Created: {url}"}
    res = requests.post(slack_link, json=reply)
    return res