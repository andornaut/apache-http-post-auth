# apache-http-post-auth
Authenticate users in Apache by posting to an HTTP endpoint. 

You can configure the Apache [authnz external](https://github.com/phokz/mod-auth-external/tree/master/mod_authnz_external) authentication provider to pipe HTTP Basic Authentication credentials to [apachehttppostauth.py](./apachehttppostauth.py), which then POSTs them to an HTTP endpoint. If the endpoint responds with anything other than a 200 (OK) status code, then the authentication request is rejected.

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
IGNORE_UNEXPECTED_STATUS_CODES = False
REQUIRE_JSON_SUCCESS_STATUS_IN_RESPONSE = False
USERNAME_PARAM_NAME = 'username'
PASSWORD_PARAM_NAME = 'password
```
