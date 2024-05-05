#!/usr/bin/env python3

# Import libraries
import os

def pre_commit():
  """Saves a message to the COMMIT_EDITMSG file."""
  message = "TESTE , SALVANDO NO ARQUIVO COMMIT_EDITMSG"
  with open(os.path.join(".git", "COMMIT_EDITMSG"), "w") as commit_file:
    commit_file.write(message)

if __name__ == "__main__":
  pre_commit()
