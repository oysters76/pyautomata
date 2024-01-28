# Py-Automata Algorithms (Automata Theory algorithms implemented via Python3)

This repo I started to implement methods in automata theory that I found to be interesting. 

## 1. Deterministic Finite Automata (DFA) Minimization 

min.py contains an implementation of the minimization of DFA via the table-filling method, aka Myhill-Nerode Theorem. 

Given an input DFA system <Q, q0, E, F, D> the algorithm minimizes it if possible, by 
grouping together redundant states.

```python
Before min:  {
              'A0': 'B', 
              'A1': 'C', 
              'B0': 'A', 
              'B1': 'D', 
              'C0': 'E', 
              'C1': 'F', 
              'D0': 'E', 
              'D1': 'F', 
              'E0': 'E', 
              'E1': 'F', 
              'F0': 'F', 
              'F1': 'F'
              }

After min:  {
            'AB0': 'AB', 
            'AB1': 'CDE', 
            'CDE0': 'CDE', 
            'CDE1': 'F'
            }

```