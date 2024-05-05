#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git
import os

def get_ticket_number():
    # Implemente aqui a lógica para obter o número do ticket
    # Por exemplo, se estiver armazenado localmente em um arquivo
    # você pode ler o número do arquivo. Aqui, estamos apenas retornando um número fixo para demonstração.
    ticket_number = "123"  # Substitua isso pela lógica real
    print("Número do ticket:", ticket_number)  # Imprime o número do ticket para verificar
    return ticket_number

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
