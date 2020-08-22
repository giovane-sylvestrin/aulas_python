"""
Module collections -> Deque
https://docs.python.org/3/library/collections.html

Lista de alta performance
"""

from collections import deque

deq = deque('geek')  # poderia ser iniciado vazio

print(deq)

# Adicionar elementos -> append

deq.append('y')
print(deq)

deq.appendleft('y')  # adiciona no inicio da lista
print(deq)

# remover elementos
deq.pop()
print(deq)

deq.popleft()
print(deq)
