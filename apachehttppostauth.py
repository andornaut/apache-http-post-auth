#!/usr/bin/env python
import json
import ssl
import sys
import urllib
import urllib2

IGNORE_SSL_ERRORS = False
REQUIRE_SUCCESS_STATUS_IN_JSON_RESPONSE = False
USERNAME_PARAM_NAME = 'username'
PASSWORD_PARAM_NAME = 'password'


def authenticate(url, username, password):
    data = urllib.urlencode({USERNAME_PARAM_NAME: username, PASSWORD_PARAM_NAME: password})
    request = urllib2.Request(url, data)

    ssl_context = ssl.create_default_context()
    if not IGNORE_SSL_ERRORS:
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

    try:
        response = urllib2.urlopen(request, context=ssl_context)
    except urllib2.HTTPError as e:
        if e.code == 403:
            return False
        raise

    return not REQUIRE_SUCCESS_STATUS_IN_JSON_RESPONSE or contains_success_status(response)


def contains_success_status(response):
    json_response = json.loads(response.read())
    status = str(json_response.get('status')).lower()
    return status == 'success'


if __name__ == '__main__' and len(sys.argv) == 2:
    url = sys.argv[1]
    username = sys.stdin.readline().strip()
    password = sys.stdin.readline().strip()
    if authenticate(url, username, password):
        exit(0)

exit(1)
