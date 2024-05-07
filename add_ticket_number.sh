#!/bin/bash

# Capture the commit message
commit_message=$(cat .git/COMMIT_EDITMSG)

# Extract ticket number from current branch name
ticket_number=$(git rev-parse --abbrev-ref HEAD | grep -oE '[0-9]+')

# Add ticket number to commit message
new_commit_message="$commit_message #$ticket_number"

# Save the new commit message
echo "$new_commit_message" > .git/COMMIT_EDITMSG

# Exits without errors
exit 0