#!/usr/bin/env python3

# Import libraries
import os

# Define the message to save
message = "TESTE , SALVANDO NO ARQUIVO COMMIT_EDITMSG"

def pre_commit():
  """Saves the message to the COMMIT_EDITMSG file."""
  with open(os.path.join(".git", "COMMIT_EDITMSG"), "w") as commit_file:
    commit_file.write(message)

if __name__ == "__main__":
  pre_commit()
