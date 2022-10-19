#!/usr/bin/env sh

set -o errexit
set -o nounset

# Initializing global variables and functions:
: "${DJANGO_ENV:=development}"

# Fail CI if `DJANGO_ENV` is not set to `development`:
if [ "$DJANGO_ENV" != 'development' ]; then
  echo 'DJANGO_ENV is not set to development. Running tests is not safe.'
  exit 1
fi

pyclean () {
  # Cleaning cache:
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_test () {
  pytest "$@"
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_test "$@"
