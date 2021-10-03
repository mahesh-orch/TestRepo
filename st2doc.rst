Secrets Masking
---------------

|st2| offers functionality for masking secrets in API responses and log messages. This is enabled
by default.

To disable it, set the ``api.mask_secrets`` and ``log.mask_secrets`` config options in
``/etc/st2/st2.conf``:

.. sourcecode:: ini

    [api]
    mask_secrets = True

    ...

    [log]
    mask_secrets = False

Masking Secrets in API Responses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When secret masking is enabled for API responses, |st2| will mask values for secret parameters in
all the API responses which operate on the following system entities:

* Action Executions
* Live Actions
* Datastore (key-value) Items

|st2| will determine if a particular action parameter is a secret based on the parameter definition
in the action metadata file.

Any action parameter that has the ``secret: true`` attribute will be treated as a secret for
masking purposes.

Masking can be disabled on a per-API request basis, by passing the ``?show_secrets=True`` query
parameter to all of the supported API endpoints. This is only available to users with the admin
role.

This example shows the secret parameter ``cmd`` being masked in the response of the
``/v1/executions/`` API endpoint.

.. sourcecode:: bash

  curl -X GET 'http://127.0.0.1:9101/v1/executions/?limit=1'
  [
      {
          "status": "requested",
          "start_timestamp": "2017-04-07T13:01:50.953242Z",
          "log": [
              {
                  "status": "requested",
                  "timestamp": "2017-04-07T13:01:50.970000Z"
              }
          ],
          "parameters": {
              "cmd": "********"
          },
          ...
          "id": "58e78dbe0640fd765ca74896"
      }
  ]

This shows the same request, when a user with admin role disables masking on a per-request basis:

.. sourcecode:: bash

  curl -X GET 'http://127.0.0.1:9101/v1/executions/?limit=1&show_secrets=True'
  [
      {
          "status": "requested",
          "start_timestamp": "2017-04-07T13:01:50.953242Z",
          "log": [
              {
                  "status": "requested",
                  "timestamp": "2017-04-07T13:01:50.970000Z"
              }
          ],
          "parameters": {
              "cmd": "date"
          },
          ...
          "id": "58e78dbe0640fd765ca74896"
      }
  ]

Masking Secrets in Log Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
