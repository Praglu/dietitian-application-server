#!/usr/bin/env sh

set -o errexit
set -o nounset

pyclean () {
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_check () {
  echo flake8...
  flake8 .

  echo xenon...
  xenon --max-absolute B --max-modules B --max-average B server -i 'test*,migrations' -e

  echo bandit...
  bandit -ii -ll -r .
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_check
