***********************
Introduction & Settings
***********************

Introduction
============

Simple Python and Docker app

Setup
=====

No local setup should be needed apart from:

- `docker <https://docs.docker.com/engine/installation/>`__
- `docker-compose <https://docs.docker.com/compose/>`__


create a .env file with the following Environment variables.

- *DEBUG=whatever*
- *SECRET_KEY=whatever*
- *PG_USERNAME=whatever*
- *PG_PASSWORD=whatever*
- *PG_NAME=whatever*
- *PG_HOST=whatever*
- *PG_PORT=5432 (default postgres port)*


The local dev setup uses **docker-compose** to spin up all necessary services.
Make sure you have it installed and can connect to the **docker daemon**.

Build the app
-------------

Run in project directory after you clone the repository:

.. code:: bash

    docker-compose build

This will download and build all the containers.

Run the app
===========

Start the dev server
------------------

Run in project directory:

.. code:: bash

    docker-compose up

This will start the django dev server. The ``docker-compose.yml``
file describes the setup of the containers.

.. note:: if the server didn't start the first time kill the process and run ``docker-compose up`` again

Run the tests
-------------

Type command below to run tests:

.. code:: bash

    docker-compose run neliti test

Run word counts
---------------

.. code:: bash

    docker-compose run neliti count 

This will start ipython with the word_frequencies function available.
Inside the shell type ( word_frequencies('test.html') )


Run commands on the server
==========================

Each docker container uses the same script as entrypoint. The ``entrypoint.sh``
script offers a range of commands to start services or run commands.
The full list of commands can be seen in the script.
The pattern to run a command is always
``docker-compose run <container-name> <entrypoint-command> <...args>``

The following are some examples:

+-------------------------------------+----------------------------------------------------------+
| Action                              | Command                                                  |
+=====================================+==========================================================+
| Run tests                           | ``docker-compose run neliti test``                       |
+-------------------------------------+----------------------------------------------------------+
| Run django commands                 | ``docker-compose run neliti manage help``                |
+-------------------------------------+----------------------------------------------------------+
| Create a django shell               | ``docker-compose run neliti manage shell``               |
+-------------------------------------+----------------------------------------------------------+
| Show ORM migrations                 | ``docker-compose run neliti manage showmigrations``      |
+-------------------------------------+----------------------------------------------------------+
| Run word counts                     | ``docker-compose run neliti count``                      |
+-------------------------------------+----------------------------------------------------------+


Containers and services
=======================

These are the two containers we have at the moment.

+-----------+-------------------------------------------------------------------------+
| Container | Description                                                             |
+===========+=========================================================================+
| neliti    | `Django <https://www.djangoproject.com/>`__                             |
+-----------+-------------------------------------------------------------------------+
| db        | `PostgreSQL <https://www.postgresql.org/>`__ database                   |
+-----------+-------------------------------------------------------------------------+

All of the container definitions for development can be found in the ``docker-compose.yml``.

.. note:: Postgresql uses Django ORM models for table configuration and migrations.
