#!/usr/bin/env bash
set -e

DOCKER_COMPOSE=`which docker-compose || echo "docker compose"`
COMPOSE="$DOCKER_COMPOSE -f docker-compose.yml"


case $1 in
  -h|--help|help)
    echo "katapult.sh commands:"
    echo "  runserver: run the development stack"
    echo "  loaduser: loaddata to user Model"
    echo "  migrate: run migrate to DB"
    echo "  run: Just run de server"
    ;;
  runserver)
    function cleanup {
      $COMPOSE down
    }
    trap cleanup EXIT
    $COMPOSE up -d --build --remove-orphans
    $COMPOSE exec web python manage.py migrate
    $COMPOSE exec web python manage.py loaddata fixtures/user_admin.json
    $COMPOSE logs -f web
    ;;
    loaduser)
    shift
    $COMPOSE exec web python manage.py loaddata fixtures/user_admin.json
    ;;
    migrate)
    shift
    $COMPOSE exec web python manage.py migrate
    ;;
    run)
    function cleanup {
      $COMPOSE down
    }
    trap cleanup EXIT
    $COMPOSE up -d --build --remove-orphans
    $COMPOSE logs -f web
    ;;
esac
