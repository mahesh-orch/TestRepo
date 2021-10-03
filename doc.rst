## Modification in action delete API

|st2| offers functionality to delete actions/workflows with by invoking API. Previously this API
was only de-registering actions from database. This API has now modified to delete related
action/workflow files from disk as well. When action delete command is used from CLI it asks 
users permission to delete the files on disk.

`-f` and `--force` arguments are added action delete command as auto yes flags for deleting 
related files from disk without prompting for user permission.

The updated usage and arguments for ``st2 action delete`` command are:

| usage 

    st2 action delete [-h] [-t TOKEN] [--api-key API_KEY] [-j] [-y] [-f]
                         ref-or-id
    Delete an existing action

* positional arguments:
    ``ref-or-id``           Reference or ID of the action
    
* optional arguments:
    -h, --help            show this help message and exit
    -t TOKEN, --token TOKEN
                        Access token for user authentication. Get
                        ST2_AUTH_TOKEN from the environment variables by
                        default
    --api-key API_KEY     Api Key for user authentication. Get ST2_API_KEY from
                        the environment variables by default
    -j, --json            Print output in JSON format
    -y, --yaml            Print output in YAML format
    -f, --force           Auto yes flag to delete action files from disk


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
