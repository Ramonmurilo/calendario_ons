"""

Módulo para gerar calendário operativo segundo o critério adotado pelo ONS

OBJETIVO: utilizar para o cálculo de ENA por semana operativa

"""

import pendulum

def from_date(data_string=None, hoje=False):
    """Gera dados do calendário operativo diário, segundo o critério adotado pelo ONS.

    Com base numa data de entrada é calculado os dados necessários para os processos de modelagem segundo o ONS.

    Args:
        data_string (str): (DD-MM-YYYY) data base na qual se deseja ter as informações.
        hoje (bool): Habilita o uso da data no momento da execução.
    |
    Returns:
        dict: Dados de calendário necessários para os processos de modelagem do ONS.
            
                | 'chave' : valor
                | 'inicio': primeiro dia da semana operativa (DateTime)
                | 'final' : último dia da semana operativo (DateTime)
                | 'dias-realizados-semana': quantos dias da semana operativa são de realizado (int)
                | 'semana-operativa': valor da semana operativa do mes (int)
                | 'rev'   : numeração da revisão da semana (int)
                | 'semana-operativa-ano': número da semana operativa do ano (int)

    """
    
    data_requerida = pendulum.today('America/Sao_Paulo') if hoje else pendulum.from_format(data_string, 'DD-MM-YYYY')
    
    
    if data_requerida.day_of_week == pendulum.SATURDAY:

        inic_semana_operativa = data_requerida
        final_semana_operativa = data_requerida.add(days=6)
        semana_operativa_do_mes = final_semana_operativa.week_of_month
        semana_operativa_do_ano = final_semana_operativa.week_of_year
        dias_realizados = 0

    else:

        # pega o primeiro dia da semana operativa
        # O "+1" corrige o início da semana de domingo para sábado 
        inic_semana_operativa = data_requerida.subtract(days=(data_requerida.day_of_week+1))

        # Calcula qual será o último dia da semana operativa
        # O 5 ao invés de 6(dias da semana sem contar o atual) corrige o início da semana operativa para o sábado
        final_semana_operativa = data_requerida.add(days=(5 - data_requerida.day_of_week))

        # Numeral que representa a semana operativa do mês
        semana_operativa_do_mes = final_semana_operativa.week_of_month

        # Numeral que representa a semana operativa do ano
        semana_operativa_do_ano = final_semana_operativa.week_of_year
        
        dias_realizados = data_requerida.day_of_week+1

    resultado = {'inicio': inic_semana_operativa,
                'final': final_semana_operativa,
                 'dias-realizados-semana': dias_realizados,
                'semana-operativa': semana_operativa_do_mes,
                'rev': semana_operativa_do_mes-1,
                'semana-operativa-ano': semana_operativa_do_ano
                }
    
    
    return resultado

