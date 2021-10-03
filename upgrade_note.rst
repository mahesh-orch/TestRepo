.. _upgrade_notes:

Upgrade Notes
=============

.. _ref-upgrade-notes-v3-6:

|st2| v3.6
----------

* Action delete API has been modified to delete related files from disk along with
  de-registering actions from database. For action delete CLI command two arguments
  ``-f`` and ``--force`` have been added as auto yes flag to remove related files from disk.

.. _ref-upgrade-notes-v3-5:

|st2| v3.5
----------

* Node was upgraded from v10 to v14. Node 14 repository will be required to be
  setup, prior to upgrade of st2chatops.
* Support for Ubuntu 16.04 (Xenial) was removed.
* Redis server is installed and configured as backend for the coordination service
  by default to support workflows with multiple branches and tasks with items.
  Upgrade requires coordination service to be setup manually.
  For workflows to be executed properly, setup the coordination service
  accordingly.
