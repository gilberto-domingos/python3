#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git
import os

def get_ticket_number():
    # Implementar lógica para obter o número do ticket (por exemplo, da ferramenta de gerenciamento de tickets que você usa)
    # Substitua "YOUR_TICKET_NUMBER" pelo número do ticket atual
    return "YOUR_TICKET_NUMBER"

def add_ticket_number_to_commit_message(repo):
    message_file = os.path.join(repo.git_dir, 'COMMIT_EDITMSG')
    with open(message_file, 'r') as f:
        message = f.read()

    ticket_number = get_ticket_number()
    new_message = f"[issue #{ticket_number}] {message}"

    with open(message_file, 'w') as f:
        f.write(new_message)

repo = git.Repo(search_parent_directories=True)
add_ticket_number_to_commit_message(repo)
