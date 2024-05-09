@echo off
setlocal EnableDelayedExpansion

:: Gerar um número aleatório entre 10000 e 99999
set /a "numero=%random% %% (99999 - 10000 + 1) + 10000"

:: Enviar o número para a saída padrão
echo %numero%