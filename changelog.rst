* Modified action delete api. Action delete api removes related action/workflow files on disk along with de-registering them from database. Prompts on CLI for user permission before removing disk files.

  ``-f`` and ``--force`` arguments added for action delete CLI command as auto yes flag and will delete related files on disk without prompting for user permission. #5304

  Contributed by @mahesh-orch.
