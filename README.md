# apache-http-post-auth
Authenticate users in Apache by posting to an HTTP endpoint

## Apache 2.4 configuration
```
DefineExternalAuth apachehttppostauth pipe '/usr/local/bin/apachehttppostauth.py https://example.com/api/authenticate/'

<Location />
        AuthType Basic
        AuthName "basic"
        AuthBasicProvider external
        AuthExternal apachehttppostauth
        Require valid-user
</Location>
```

## Settings
There are a few customizable settings:
```
IGNORE_SSL_ERRORS = False
REQUIRE_SUCCESS_STATUS_IN_JSON_RESPONSE = False
USERNAME_PARAM_NAME = 'username'
PASSWORD_PARAM_NAME = 'password'
```

