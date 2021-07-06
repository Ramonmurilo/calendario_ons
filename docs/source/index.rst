.. calendario_ons documentation master file, created by
   sphinx-quickstart on Mon Jul  5 23:02:03 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentação calendario_ons
===========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. automodule:: calendario_ons
 :members:



Como usar
=========


Exemplo ::

   import calendario_ons

   dados_semana_operativa = calendario_ons.from_date('05-07-2021')
   print(dados_semana_operativa)

Output
   >>> {'inicio': DateTime(2021, 7, 3, 0, 0, 0, tzinfo=Timezone('UTC')), 
      'final': DateTime(2021, 7, 9, 0, 0, 0, tzinfo=Timezone('UTC')), 
      'dias-realizados-semana': 2, 
      'semana-operativa': 2, 
      'rev': 1, 
      'semana-operativa-ano': 27}




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
