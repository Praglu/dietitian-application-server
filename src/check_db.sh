#!/usr/bin/env sh

set -o errexit
set -o nounset

pyclean () {
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_check_db () {
  echo migrations check...
  python manage.py makemigrations --dry-run --check
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_check_db
