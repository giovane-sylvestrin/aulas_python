"""
PEP8
easter egg comando: import this

Boas práticas:
[1] Usar Casual Case para nome de classes


class Calculator:
    pass


class CalculdoraCientifica:
    pass


[2] Usar nomes em minusculo, separados por "_", para funções e variáveis


def soma():
    pass


def leitura_arq():
    pass


temp = 25


[3] Usar 4 espaços para identação (NÃO USAR TAB - pode ter configuraão diferente) !!!!!!!!!!!


if 'a' in 'banana':
    print('tem')


[4] Linhas em branco
-Separar funções e classes com duas linhas em branco
-Métodos dentro de uma classe devem ser separados com uma linha em branco


[5] Imports
-Devem sempre ser feitas em linhas separadas

# Import Errado (importe de pacotes completos)

import sys, os

# Import Certo

import sys
import os

# Não há problemas (importe de itens)

from types import StringType, ListType

# Caso muitos imports fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocaldos no topo dos arquivos, logo depois de quaisquer comentários ou docstrings e
# antes de constantes e variáveis globais

[6] Espaços em expressões e instruções

# Não faça

funcao( algo[ 1 ], {outro: 2 } )
algo (1)

# Faça

funcao(algo[1], {outro: 2})
algo(1)


[7] Termine sempre uma instrução com uma nova linha
"""
import this
