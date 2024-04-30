# comands 
python3 -m venv python_study
source python_study/bin/activate
pip install django

django-admin startproject core .
django-admin --version
find . -type d -name 'venv' -o -name '.venv'
cd ~ && find . -type d -name 'venv' -o -name '.venv'


python instalar ect ...

Para começar a trabalhar com a linguagem de programação Python no Ubuntu 22.04, você precisa seguir algumas etapas básicas para configurar seu ambiente de desenvolvimento. Aqui estão os passos principais:

Verifique se o Python está instalado: No Ubuntu 22.04, o Python geralmente já está instalado por padrão. Você pode verificar digitando python3 --version no terminal. Isso deve exibir a versão do Python instalada. Certifique-se de ter o Python 3.x instalado, pois o Python 2.x não é mais mantido.

Instale o gerenciador de pacotes pip: O pip é o gerenciador de pacotes padrão para Python, que facilita a instalação de bibliotecas e pacotes Python. Para instalar o pip, você pode executar o seguinte comando no terminal:

Copy code
sudo apt install python3-pip
Ambiente virtual (opcional, mas recomendado): É uma boa prática criar ambientes virtuais para projetos Python. Isso ajuda a isolar as dependências de diferentes projetos e a evitar conflitos. Você pode criar um ambiente virtual usando o módulo venv, que geralmente já está incluído na instalação padrão do Python 3:

Copy code
python3 -m venv nome_do_seu_ambiente_virtual
Ative o ambiente virtual: Depois de criar um ambiente virtual, você precisa ativá-lo antes de começar a trabalhar no seu projeto. Você pode fazer isso executando o seguinte comando no terminal:

bash
Copy code
source nome_do_seu_ambiente_virtual/bin/activate
Instale pacotes e bibliotecas: Com o ambiente virtual ativado, você pode instalar pacotes e bibliotecas Python específicos para o seu projeto usando o pip. Por exemplo:

Copy code
pip install nome_do_pacote
Com esses passos, você deve ter um ambiente de desenvolvimento Python funcional no Ubuntu 22.04. Lembre-se de sempre verificar a documentação oficial e os requisitos específicos de seus projetos para garantir uma configuração adequada.
