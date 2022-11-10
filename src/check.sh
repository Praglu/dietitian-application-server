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
  xenon --max-absolute A --max-modules A --max-average A server -i 'test*,migrations' -e 'server/apps/account/admin.py,server/apps/chl/updater.py,server/apps/task/management/commands/process_completed_tasks.py,server/services/email.py,server/apps/chl/importer.py,server/apps/chl/adapters/escort.py,server/apps/chl/adapters/task.py,server/apps/chl/adapters/location.py,server/apps/common/exceptions.py,server/settings/middlewares/escort_internal_network.py'

  echo security...
  safety check --bare  -i 39642

  echo bandit...
  bandit -ii -ll -r .
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_check
