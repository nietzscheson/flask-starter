#!/bin/sh

set -e

# Run the application
flask db upgrade
flask run --host 0.0.0.0
