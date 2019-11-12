#Trabalho de Sistemas seguros
### Assinatura digital
##### Ariel Souza e Gabriel Souza


Para rodar o projeto basta:
* Ter python >3.7 instalado: https://www.python.org/downloads/
* ter pip instalado: https://pip.pypa.io/en/stable/installing/
* rodar ```$ pip3 install -r requirements.txt``` na pasta raiz do projeto
* rodar na pasta raiz do projeto ```$ python3 generate_keys.py``` para que assim os dois pares de chaves sejam gerados
* adcionar uma variavel de ambiente ```$ export KEY=a``` ou ```$ export KEY=b``` que dirá qual par de chaves ele deve usar, A ou B
* rodar a aplicação com ```python3 main.py```

* Questão 1: O arquivo generate_keys.py gera dois pares de chaves

* Questão 2: Dentro de ambas as aplicações criadas (key_a.py e key_b.py) existe um assinador com a sua respectiva chave

* Questão 3: Quando é criada uma assinatura com uma das chaves de A ambas as chaves (publica e privada de A) podem ser utilizadas para verificar.

* Questão 4: Quando se tenta autenticar com qualquer uma das chaves B, a verificação falha

