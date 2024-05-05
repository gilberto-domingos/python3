#!/usr/bin/env python

import os
import subprocess
import re
import random
import string

def generate_random_ticket_number():
    # Gerar um número aleatório de 5 dígitos
    return ''.join(random.choices(string.digits, k=5))

def main():
    # Get the staged files list (files marked for commit)
    staged_files = subprocess.check_output(["git", "diff", "--cached", "--name-only"]).decode("utf-8").splitlines()

    # Check if any staged files contain a ticket number pattern
    ticket_pattern = r"(ticket|issue|#)\s*\d+"  # Regular expression for common ticket number formats
    has_ticket_number = any(line for line in staged_files if re.search(ticket_pattern, line, re.IGNORECASE))

    # If no ticket number is found, generate a random ticket number
    if not has_ticket_number:
        random_ticket_number = generate_random_ticket_number()
        print(f"No ticket number found in staged files. Adding a random ticket number: {random_ticket_number}")

        # Adicione o número do ticket aleatório à mensagem de commit
        commit_message = f"Commit with random ticket number: #{random_ticket_number}"
    else:
        # Encontre o número do ticket no padrão e adicione à mensagem de commit
        ticket_numbers = [re.search(ticket_pattern, line, re.IGNORECASE).group() for line in staged_files if re.search(ticket_pattern, line, re.IGNORECASE)]
        commit_message = f"Commit with ticket number: {' '.join(ticket_numbers)}"

    # Verificar se a variável de ambiente COMMIT_EDITMSG está definida antes de acessá-la
    commit_editmsg_path = os.environ.get('COMMIT_EDITMSG')
    if commit_editmsg_path:
        # Escreva a mensagem de commit atualizada no arquivo COMMIT_EDITMSG
        with open(commit_editmsg_path, 'w') as f:
            f.write(commit_message)

        # Continuar com o commit usando o comando git commit --no-verify para evitar loops infinitos de pré-commit
        subprocess.call(["git", "commit", "--no-verify", "-F", commit_editmsg_path])
    else:
        print("Error: COMMIT_EDITMSG environment variable is not defined.")

if __name__ == "__main__":
    main()
