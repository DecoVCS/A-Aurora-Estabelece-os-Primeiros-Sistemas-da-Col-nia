### - CÉREBRO DIGITAL DA COLÔNIA AURORA SIGER -
### André Victor Cunha de Souza (RM574035)

# ORGANIZAÇÃO DOS DADOS DA COLÔNIA
# Utilizei dicionários (chave-valor) para ter acesso rápido aos dados atuais e
# listas para guardar o histórico que vai alimentar meu modelo de previsão.
sensores_atuais = {
    "geracao_total": 40,  # Energia sendo gerada agora ex:painéis solares
    "consumo_total": 70,  # Energia sendo gasta pelos módulos
    "reserva_bateria": 45,  # Porcentagem atual das baterias
    "vento_atual": 11  # Velocidade do vento captada agora (m/s)
}

# Dados históricos para a Regressão Linear Vento x Energia Eólica
historico_vento = [1 - 3]
historico_energia = [4 - 6]


# PREVISÃO DE COMPORTAMENTOS Regressão Simples
# Criei essa função para prever a energia eólica baseada nos dados do vento.
def prever_energia_eolica(vento_atual):
    print("\n--- INICIANDO MÓDULO DE PREVISÃO ---")
    # Como a relação nos meus dados é uma reta perfeita y = 2.5 * x,
    # ajustei a relação linear simples entre as variáveis para estimar o futuro.
    previsao = 2.5 * vento_atual
    print(f"Com o vento a {vento_atual} m/s, minha previsão de geração eólica é de ≈ {previsao} kWh.")
    return previsao


# ANÁLISE DO USO DE ENERGIA
# Função que criei para comparar geração vs consumo e evitar desperdícios ou apagões.
def analisar_energia(geracao, consumo):
    print("\n--- INICIANDO ANÁLISE ENERGÉTICA ---")
    if consumo > geracao:
        print(f"ALERTA: O consumo ({consumo}) está maior que a geração ({geracao}). Risco de apagão!")
    elif geracao > consumo:
        print(
            f"SUGESTÃO: A geração ({geracao}) superou o consumo ({consumo}). Armazenar energia excedente nas baterias.")
    else:
        print("SISTEMA ESTÁVEL: Geração e consumo equilibrados.")


# TOMADA DE DECISÃO AUTOMÁTICA Regras de Decisão
# Minha lógica principal combinando múltiplas condições (if/elif/else).
def tomar_decisao(energia, consumo):
    print("\n--- INICIANDO TOMADA DE DECISÃO AUTOMÁTICA ---")

    # Se a bateria estiver caindo e o consumo alto, ativo o modo de sobrevivência
    if energia < 50 and consumo > 60:
        print(
            "AÇÃO AUTOMÁTICA: Modo de economia ativado! Desligando sistemas não essenciais e priorizando Suporte à Vida.")

    # Se a bateria estiver muito crítica, corto tudo
    elif energia < 20:
        print("AÇÃO AUTOMÁTICA: EMERGÊNCIA! Desligamento total acionado. Apenas Suporte à Vida em funcionamento.")

    # Cenário seguro
    else:
        print("AÇÃO AUTOMÁTICA: Nível de energia seguro. Mantendo sistemas normais em operação.")


# - EXECUÇÃO DO SISTEMA -
def rodar_sistema_colonia():
    print("=== INICIALIZANDO CÉREBRO DIGITAL DA COLÔNIA ===")

    # Executando a regressão para prever energia baseada no vento atual
    estimativa_eolica = prever_energia_eolica(sensores_atuais["vento_atual"])

    # Analisando a balança energética
    analisar_energia(sensores_atuais["geracao_total"], sensores_atuais["consumo_total"])

    # Tomando a decisão para manter a colônia viva
    tomar_decisao(sensores_atuais["reserva_bateria"], sensores_atuais["consumo_total"])

    print("\n=== ANÁLISE CONCLUÍDA ===")


rodar_sistema_colonia()