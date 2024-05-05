#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git
import os

def get_ticket_number():
    # Implemente a lógica para obter o número do ticket
    ticket_number = "YOUR_TICKET_NUMBER"  # Substitua "YOUR_TICKET_NUMBER" pela lógica real
    print("Número do ticket:", ticket_number)  # Adicione esta linha para imprimir o número do ticket
    return ticket_number

def add_ticket_number_to_commit_message(repo):
    message_file = os.path.join(repo.git_dir, 'COMMIT_EDITMSG')
    with open(message_file, 'r') as f:
        message = f.read()

    ticket_number = get_ticket_number()
    new_message = f"[issue #{ticket_number}] {message}"

    with open(message_file, 'w') as f:
        f.write(new_message)
    print("Commit message with ticket number:", new_message)  # Adiciona esta linha para imprimir a nova mensagem de commit

repo = git.Repo(search_parent_directories=True)
add_ticket_number_to_commit_message(repo)
