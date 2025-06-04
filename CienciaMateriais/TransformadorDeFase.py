class TransformadorDeFase:
    def calcular_fracao_fase_regra_da_alavanca(self, composicao_liga: float, composicao_fase_alfa: float,
                                               composicao_fase_beta: float) -> tuple[float | None, float | None]:
        """Calcula as frações de duas fases em um diagrama de fases binário usando a regra da alavanca.

        Assume um ponto dentro de uma região bifásica.

        Entrada:
            composicao_liga (float): Composição geral da liga (em % peso ou fração atômica).
            composicao_fase_alfa (float): Composição da fase alfa na temperatura de interesse (na mesma unidade de composicao_liga).
            composicao_fase_beta (float): Composição da fase beta na temperatura de interesse (na mesma unidade de composicao_liga).

        Saída:
            tuple[float | None, float | None]: Uma tupla contendo a fração da fase alfa e a fração da fase beta (entre 0 e 1).
                                             Retorna (None, None) se a composição das fases for a mesma.
        """
        if composicao_fase_beta == composicao_fase_alfa:
            return None, None

        fracao_beta = (composicao_liga - composicao_fase_alfa) / (composicao_fase_beta - composicao_fase_alfa)
        fracao_alfa = (composicao_fase_beta - composicao_liga) / (composicao_fase_beta - composicao_fase_alfa)

        return fracao_alfa, fracao_beta

    def obter_temperatura_transformacao_fase(self):
        """Função placeholder para obter a temperatura de transformação de fase.

        As temperaturas de transformação de fase (eutética, eutetóide, etc.) dependem do sistema de ligas
        e são obtidas a partir de diagramas de fases específicos.
        Esta função pode ser expandida para solicitar o sistema de ligas e consultar um banco de dados de diagramas de fases.

        Saída:
            str: Uma mensagem indicando como obter a temperatura de transformação de fase.
        """
        return "As temperaturas de transformação de fase dependem do sistema de ligas e são obtidas de diagramas de fases."

    def obter_microestrutura_prevista(self):
        """Função placeholder para obter a microestrutura prevista após uma transformação de fase.

        A microestrutura resultante depende da composição da liga, da temperatura e da taxa de resfriamento.
        A previsão precisa requer o conhecimento do diagrama de fases e da história térmica do material.
        Esta função pode ser expandida para solicitar essas informações e usar regras de transformação de fases.

        Saída:
            str: Uma mensagem indicando como prever a microestrutura.
        """
        return "A microestrutura resultante de uma transformação de fase depende da composição, " \
        "temperatura e taxa de resfriamento, e é prevista com base no diagrama de fases e cinética de transformação."

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    transformacao_fase = TransformadorDeFase()

    # Calcular fração de fases usando a regra da alavanca
    composicao_liga = 30  # % peso de B
    composicao_alfa = 10  # % peso de B
    composicao_beta = 70  # % peso de B
    fracao_alfa, fracao_beta = transformacao_fase.calcular_fracao_fase_regra_da_alavanca(composicao_liga, composicao_alfa, composicao_beta)

    if fracao_alfa is not None and fracao_beta is not None:
        print(f"Fração da Fase Alfa: {fracao_alfa:.2f}")
        print(f"Fração da Fase Beta: {fracao_beta:.2f}")
    else:
        print("A composição das fases alfa e beta é a mesma.")

    # Obter temperatura de transformação de fase
    temperatura = transformacao_fase.obter_temperatura_transformacao_fase()
    print(f"Temperatura de Transformação de Fase: {temperatura}")

    # Obter microestrutura prevista
    microestrutura = transformacao_fase.obter_microestrutura_prevista()
    print(f"Microestrutura Prevista: {microestrutura}")