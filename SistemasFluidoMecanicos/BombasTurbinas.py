class BombasTurbinas:
    def calcular_altura_manometrica_bomba(self, pressao_descarga: float, pressao_succao: float,
                                           velocidade_descarga: float, velocidade_succao: float,
                                           altura_descarga: float, altura_succao: float,
                                           densidade: float, gravidade: float = 9.81) -> float:
        """Calcula a altura manométrica de uma bomba.

        Entrada:
            pressao_descarga (float): Pressão na saída da bomba (em Pa).
            pressao_succao (float): Pressão na entrada da bomba (em Pa).
            velocidade_descarga (float): Velocidade do fluido na saída (em m/s).
            velocidade_succao (float): Velocidade do fluido na entrada (em m/s).
            altura_descarga (float): Altura da saída da bomba em relação a um referencial (em m).
            altura_succao (float): Altura da entrada da bomba em relação ao mesmo referencial (em m).
            densidade (float): Densidade do fluido (em kg/m³).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Altura manométrica da bomba (em m de coluna de fluido).
        """
        termos_pressao = (pressao_descarga - pressao_succao) / (densidade * gravidade)
        termos_velocidade = (velocidade_descarga**2 - velocidade_succao**2) / (2 * gravidade)
        termos_altura = altura_descarga - altura_succao
        return termos_pressao + termos_velocidade + termos_altura

    def calcular_potencia_hidraulica_bomba(self, densidade: float, vazao_volumetrica: float,
                                            altura_manometrica: float, gravidade: float = 9.81) -> float:
        """Calcula a potência hidráulica fornecida pela bomba ao fluido.

        Entrada:
            densidade (float): Densidade do fluido (em kg/m³).
            vazao_volumetrica (float): Vazão volumétrica do fluido (em m³/s).
            altura_manometrica (float): Altura manométrica da bomba (em m).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Potência hidráulica (em Watts).
        """
        return densidade * gravidade * vazao_volumetrica * altura_manometrica

    def calcular_eficiencia_bomba(self, potencia_hidraulica: float, potencia_entrada: float) -> float:
        """Calcula a eficiência da bomba.

        Entrada:
            potencia_hidraulica (float): Potência hidráulica fornecida ao fluido (em Watts).
            potencia_entrada (float): Potência fornecida à bomba (em Watts).

        Saída:
            float: Eficiência da bomba (adimensional, entre 0 e 1 ou em porcentagem se multiplicado por 100). Retorna None se potencia_entrada for zero.
        """
        if potencia_entrada == 0:
            return None
        return potencia_hidraulica / potencia_entrada

    def calcular_potencia_gerada_turbina(self, densidade: float, vazao_volumetrica: float,
                                         altura_liquida: float, eficiencia_turbina: float,
                                         gravidade: float = 9.81) -> float:
        """Calcula a potência gerada por uma turbina hidráulica.

        Entrada:
            densidade (float): Densidade do fluido (em kg/m³).
            vazao_volumetrica (float): Vazão volumétrica do fluido através da turbina (em m³/s).
            altura_liquida (float): Altura líquida disponível para a turbina (em m).
            eficiencia_turbina (float): Eficiência da turbina (adimensional, entre 0 e 1).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Potência gerada pela turbina (em Watts).
        """
        return eficiencia_turbina * densidade * gravidade * vazao_volumetrica * altura_liquida

    def calcular_altura_liquida_turbina(self, altura_bruta: float, perdas_carga_turbina: float) -> float:
        """Calcula a altura líquida disponível para a turbina.

        Entrada:
            altura_bruta (float): Altura total disponível (em m).
            perdas_carga_turbina (float): Perdas de carga no sistema da turbina (em m).

        Saída:
            float: Altura líquida disponível para a turbina (em m).
        """
        return altura_bruta - perdas_carga_turbina

    def calcular_eficiencia_turbina_experimental(self, potencia_gerada: float, densidade: float,
                                                  vazao_volumetrica: float, altura_liquida: float,
                                                  gravidade: float = 9.81) -> float:
        """Calcula a eficiência da turbina a partir de dados experimentais.

        Entrada:
            potencia_gerada (float): Potência gerada pela turbina (em Watts).
            densidade (float): Densidade do fluido (em kg/m³).
            vazao_volumetrica (float): Vazão volumétrica do fluido (em m³/s).
            altura_liquida (float): Altura líquida disponível para a turbina (em m).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Eficiência da turbina (adimensional, entre 0 e 1). Retorna None se o denominador for zero.
        """
        potencia_hidraulica_disponivel = densidade * gravidade * vazao_volumetrica * altura_liquida
        if potencia_hidraulica_disponivel == 0:
            return None
        return potencia_gerada / potencia_hidraulica_disponivel

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    bombas_turbinas = BombasTurbinas()

    # Cálculo de altura manométrica da bomba
    pd = 500000  # Pa
    ps = 100000  # Pa
    vd = 5  # m/s
    vs = 2  # m/s
    hd = 2  # m
    hs = 0  # m
    rho = 1000  # kg/m³
    hm = bombas_turbinas.calcular_altura_manometrica_bomba(pd, ps, vd, vs, hd, hs, rho)
    print(f"Altura Manométrica da Bomba: {hm:.2f} m")

    # Cálculo de potência hidráulica da bomba
    Q = 0.1  # m³/s
    Ph = bombas_turbinas.calcular_potencia_hidraulica_bomba(rho, Q, hm)
    print(f"Potência Hidráulica da Bomba: {Ph:.2f} W")

    # Cálculo de eficiência da bomba
    Pe = 50000  # W
    eficiencia_bomba = bombas_turbinas.calcular_eficiencia_bomba(Ph, Pe)
    print(f"Eficiência da Bomba: {eficiencia_bomba:.2f}")

    # Cálculo de potência gerada pela turbina
    Ht = 50  # m
    eta_t = 0.85
    Pt = bombas_turbinas.calcular_potencia_gerada_turbina(rho, Q, Ht, eta_t)
    print(f"Potência Gerada pela Turbina: {Pt:.2f} W")

    # Cálculo de altura líquida da turbina
    Hb = 55  # m
    hl_t = 5  # m
    Hliq = bombas_turbinas.calcular_altura_liquida_turbina(Hb, hl_t)
    print(f"Altura Líquida da Turbina: {Hliq:.2f} m")