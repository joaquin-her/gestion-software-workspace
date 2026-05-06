#!/bin/bash

# Script to set Jira environment variables
# Source this script with: source setup_jira_env.sh

export JIRA_API_TOKEN="your_api_token_here"
export JIRA_EMAIL="your-mail@fi.uba.ar"
export JIRA_BASE_URL="https://grupo15gestion.atlassian.net"

echo "Jira environment variables set:"
echo "JIRA_EMAIL: $JIRA_EMAIL"
echo "JIRA_BASE_URL: $JIRA_BASE_URL"
echo "JIRA_API_TOKEN: [REDACTED]"
