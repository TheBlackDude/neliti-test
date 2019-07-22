#!/bin/bash
set -e

show_help() {
  echo """
  Commands
  -----------------------------------------
  start_dev      : start the django dev server
  test           : run unit tests
  manage         : run django commands
  shell          : Ipython shell
  count          : Count word frequencies
  """
}

export PYTHONPATH="/code/:$PYTHONPATH"
export DJANGO_SETTINGS_MODULE=config.settings

case "$1" in
  "start_dev" )
    # run migrations first if theres any && start the dev server
    ./manage.py migrate --noinput
    ./manage.py runserver 0.0.0.0:8000
  ;;
  "test" )
    # linting first
    flake8 ./
    # run python tests and pass on any args e.g individual tests
    ./manage.py test "${@:2}"
  ;;
  "manage" )
    # run django commands
    ./manage.py "${@:2}"
  ;;
  "shell" )
    # start ipython
    ipython
  ;;
  "count" )
    # get word counts results
    ipython q2.py -i
  ;;
  * )
    show_help
  ;;
esac
