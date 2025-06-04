from os import system
# Importando os módulos necessários ==================================================================================================  

''' Ciencia dos Materiais '''
from CienciaMateriais.Difusao import Difusao
from CienciaMateriais.PropriedadesEletricasMagneticas import PropriedadesEletricasMagneticas
from CienciaMateriais.PropriedadesMecanicas import PropriedadesMecanicas
from CienciaMateriais.PropriedadesTermicas import PropriedadesTermicas
from CienciaMateriais.TransformadorDeFase import TransformadorDeFase

''' Sistemas FluidoMecanicos '''
from SistemasFluidoMecanicos.BombasTurbinas import BombasTurbinas
from SistemasFluidoMecanicos.DinamicaFluidos import DinamicaFluidos
from SistemasFluidoMecanicos.EstaticaFluidos import EstaticaFluidos
from SistemasFluidoMecanicos.PropriedadesFluidos import PropriedadesFluidos
from SistemasFluidoMecanicos.TransferenciaCalor import TransferenciaCalor

''' Tabela de Materiais '''
from TabelaMateriais.Cadastro import Consulta_e_Cadastro

''' Cores '''
from Estilo.Cores import cores

# Reaproveitamento de Código =================================================================================================================

def Titulo(texto):
    system('cls')
    print('='*75)
    print(f'                  {texto}')
    print('='*75)

def Invalida():
    system('cls')
    print('{}OPÇÃO INVÁLIDA!!\nCertifique-se de digitar uma opção válida\n{}'.format(cores['amarelo'], cores['normal']))

def VoltarMenu():
    system('cls')
    input('{}\nPressione ENTER para voltar ao menu anterior...{}'.format(cores['ciano'], cores['normal']))

if __name__ == "__main__":

    while True: # Loop do menu principal ================================================================================================

        
        Titulo("Menu de Principal")

        opcao = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
            "A) Ciencia dos Materiais\n" +
            "B) Sistemas FLuido-Mecânicos\n" +
            "C) Exibir Tabela de Propriedade dos materiais\n" +
            "D) Fechar o programa\n\n" +
            "Sua opção: ").lower()
        
        match opcao:
            case "a": # Abrir Menu de Ciencia dos Materiais =========================================================================
                
                while True:

                    Titulo("Menu de Ciencia dos Materiais")
                    opcao1 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                   "A) Difusão\n" +
                                   "B) Propriedades Elétricas\n" +
                                   "C) Propriedades Mecânicas\n" +
                                   "D) Propriedades Térmicas\n" +
                                   "E) Tranformador de Fase\n" +
                                   "F) Voltar ao menu principal\n\n" +
                                   "Sua opção: ").lower()
                    
                    match opcao1:
                        case "a": # Abrir Menu de Difusão ==========================================================================================
                            difusao = Difusao()

                            while True:  
                                Titulo("Difusão")
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                            "A) Calcular Fluxo de Difusão (Fick Primeira lei)\n" +
                                            "B) Obter Coeficiente de Difusão\n" +
                                            "C) Calcular Distância de difusão aproximada\n" +   
                                            "D) Voltar ao menu anterior\n\n" +
                                            "Sua opção: ").lower()
                                match opcao2:
                                    case "a": # Calcular Fluxo de Difusão (Fick Primeira lei) ==========================================================
                                        
                                        Titulo("Calcular Fluxo de Difusão")

                                        coeficiente_difusao = float(input("Coeficiente de difusão (m²/s): "))
                                        gradiente_concentracao = float(input("Gradiente de concentração (kg/m³)/m: "))

                                        if coeficiente_difusao < 0 or gradiente_concentracao < 0:
                                            print("{}Coeficiente de difusão ou gradiente de concentração inválido. Não pode ser negativo.{}".format(cores['vermelho'], cores['normal']))
                                            input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                                            continue
                                        # Calcular o fluxo de difusão usando a primeira lei de Fick
                                        fluxo = difusao.calcular_fluxo_difusao_fick_primeira_lei(coeficiente_difusao, gradiente_concentracao)
                                        print(f"Fluxo de Difusão: {cores["verde"]}{fluxo:.2e} kg/(m².s){cores["normal"]}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Obter Coeficiente de Difusão ==========================================================================================
                                        
                                        Titulo("Obter Coeficiente de Difusão")
                                        coeficiente = difusao.obter_coeficiente_difusao()
                                        print(f"Coeficiente de Difusão: {cores['verde']}{coeficiente}{cores["normal"]}")
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Distância de difusão aproximada ==========================================================================================
                                        
                                        Titulo("Calcular Distância de Difusão Aproximada")
                                        coeficiente_difusao = float(input("Coeficiente de difusão (m²/s): "))
                                        tempo = float(input("Tempo de difusão (s): "))
                                        distancia = difusao.calcular_distancia_difusao_aproximada(coeficiente_difusao, tempo)
                                        if distancia is not None:
                                            print(f"Distância de Difusão Aproximada: {cores['verde']}{distancia:.2e} m{cores["normal"]}")
                                        else:
                                            print("Coeficiente de difusão ou tempo inválido. Não pode ser negativo.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Voltar ao menu anterior ==========================================================================================
                                        
                                        break

                                    case _: 
                                        Invalida()       

                        case "b": # Abrir Menu de Propriedades Elétricas ==========================================================================================
                            
                            PropEletroMag = PropriedadesEletricasMagneticas()

                            while True:
                                Titulo("Propriedades Elétricas e Magnéticas")
                                
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                            "A) Resistividade Eletrica\n" +
                                            "B) Condutividade Eletrica\n" +
                                            "C) Obter Permeabilidade Magnética\n" +
                                            "D) Força Magnética em Condultor\n" +
                                            "E) Voltar ao menu anterior\n\n" +
                                            "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Resistividade Elétrica ==========================================================================================
                                        
                                        Titulo("Calcular Resistividade Elétrica")
                                        resistencia = float(input("Resistência (Ω): "))
                                        area = float(input("Área (m²): "))
                                        comprimento = float(input("Comprimento (m): "))
                                        resistividade = PropEletroMag.calcular_resistividade_eletrica(resistencia, area, comprimento)
                                        print(f"Resistividade Elétrica: {cores['verde']}{resistividade:.2e} Ω.m{cores['normal']}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Calcular Condutividade Elétrica ==========================================================================================
                                        
                                        Titulo("Calcular Condutividade Elétrica")
                                        resistividade = float(input("Resistividade (Ω.m): "))
                                        condutividade = PropEletroMag.calcular_condutividade_eletrica(resistividade)
                                        if condutividade is not None:
                                            print(f"Condutividade Elétrica: {cores['verde']}{condutividade:.2e} S/m{cores['normal']}")
                                        else:
                                            print("Resistividade inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Obter Permeabilidade Magnética ==========================================================================================
                                        
                                        Titulo("Obter Permeabilidade Magnética")
                                        permeabilidade = PropEletroMag.obter_permeabilidade_magnetica()
                                        print(f"Permeabilidade Magnética: {cores['verde']}{permeabilidade}{cores['normal']}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Força Magnética em Condutor ==========================================================================================
                                        
                                        Titulo("Calcular Força Magnética em Condutor")
                                        corrente = float(input("Corrente (A): "))
                                        comprimento = float(input("Comprimento (m): "))
                                        campo_magnetico = float(input("Campo Magnético (T): "))
                                        angulo = float(input("Ângulo (radianos): "))
                                        forca = PropEletroMag.calcular_forca_magnetica_em_condutor(corrente, comprimento, campo_magnetico, angulo)
                                        print(f"Força Magnética: {cores['verde']}{forca:.2f} N{cores['normal']}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Voltar ao menu anterior ==========================================================================================
                                        break

                                    case _:
                                        Invalida()

                        case "c": # Abrir Menu de Propriedades Mecânicas ==========================================================================================
                            PropMecanicas = PropriedadesMecanicas()
                            
                            while True:
                                Titulo("Propriedades Mecânicas")
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                            "A) Tensão Normal (Tração ou Compressão)\n" +
                                            "B) Tensão de Cisalhamento\n" +
                                            "C) Deformação Normal (Alongamento ou Contração)\n" +
                                            "D) Deformação de Cisalhamento (Tangente do Ângulo de deformação)\n" +
                                            "E) Módulo de Young (Elasticidade)\n" +
                                            "f) Módulo de Cisalhamento (Rigidez)\n" +
                                            "G) Coeficiente de Poisson\n" +
                                            "H) Resistência à Tração\n" +
                                            "I) Limite de Escoamento\n" +
                                            "J) Ductilidade (Alongamento)\n" +
                                            "K) Ductilidade (Redução de Área)\n" +
                                            "L) Dureza\n" +
                                            "M) Voltar ao menu anterior\n\n" +
                                            "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Tensão Normal ==========================================================================================
                                        
                                        Titulo("Calcular Tensão Normal")
                                        forca = float(input("Força (N): "))
                                        area = float(input("Área (m²): "))
                                        tensao = PropMecanicas.calcular_tensao_normal(forca, area)
                                        if tensao is not None:
                                            print(f"Tensão Normal: {cores['verde']}{tensao:.2e} Pa{cores['normal']}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Calcular Tensão de Cisalhamento ==========================================================================================
                                        
                                        Titulo("Calcular Tensão de Cisalhamento")
                                        forca = float(input("Força (N): "))
                                        area = float(input("Área (m²): "))
                                        tensao_cisalhamento = PropMecanicas.calcular_tensao_cisalhamento(forca, area)
                                        if tensao_cisalhamento is not None:
                                            print(f"Tensão de Cisalhamento: {cores['verde']}{tensao_cisalhamento:.2e} Pa{cores['normal']}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Deformação Normal ==========================================================================================
                                        
                                        Titulo("Calcular Deformação Normal")
                                        delta_l = float(input("Variação de comprimento (m): "))
                                        l0 = float(input("Comprimento inicial (m): "))
                                        deformacao = PropMecanicas.calcular_deformacao_normal(delta_l, l0)
                                        if deformacao is not None:
                                            print(f"Deformação Normal: {cores['verde']}{deformacao:.4f}{cores['normal']}")
                                        else:
                                            print("Comprimento inicial inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Deformação de Cisalhamento ==========================================================================================
                                        
                                        Titulo("Calcular Deformação de Cisalhamento")
                                        deslocamento = float(input("Deslocamento lateral (m): "))
                                        l0 = float(input("Comprimento inicial (m): "))
                                        deformacao_cisalhamento = PropMecanicas.calcular_deformacao_cisalhamento(deslocamento, l0)
                                        if deformacao_cisalhamento is not None:
                                            print(f"Deformação de Cisalhamento: {cores['verde']}{deformacao_cisalhamento:.4f}{cores['normal']}")
                                        else:
                                            print("Comprimento inicial inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Calcular Módulo de Young ==========================================================================================
                                        
                                        Titulo("Calcular Módulo de Young")
                                        tensao = float(input("Tensão (Pa): "))
                                        deformacao = float(input("Deformação: "))
                                        modulo_young = PropMecanicas.calcular_modulo_young(tensao, deformacao)
                                        if modulo_young is not None:
                                            print(f"Módulo de Young: {cores['verde']}{modulo_young:.2e} Pa{cores['normal']}")
                                        else:
                                            print("Deformação inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "f": # Calcular Módulo de Cisalhamento ==========================================================================================
                                        
                                        Titulo("Calcular Módulo de Cisalhamento")
                                        tensao_cisalhamento = float(input("Tensão de cisalhamento (Pa): "))
                                        deformacao_cisalhamento = float(input("Deformação de cisalhamento: "))
                                        modulo_cisalhamento = PropMecanicas.calcular_modulo_cisalhamento(tensao_cisalhamento, deformacao_cisalhamento)
                                        if modulo_cisalhamento is not None:
                                            print(f"Módulo de Cisalhamento: {cores['verde']}{modulo_cisalhamento:.2e} Pa{cores['normal']}")
                                        else:
                                            print("Deformação de cisalhamento inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "g": # Calcular Coeficiente de Poisson ==========================================================================================
                                        
                                        Titulo("Calcular Coeficiente de Poisson")
                                        tensao_normal = float(input("Tensão normal (Pa): "))
                                        deformacao_lateral = float(input("Deformação lateral: "))
                                        deformacao_normal = float(input("Deformação normal: "))
                                        coeficiente_poisson = PropMecanicas.calcular_coeficiente_poisson(tensao_normal, deformacao_lateral, deformacao_normal)
                                        if coeficiente_poisson is not None:
                                            print(f"Coeficiente de Poisson: {cores['verde']}{coeficiente_poisson:.4f}{cores['normal']}")
                                        else:
                                            print("Deformação normal inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "h": # Calcular Resistência à Tração ==========================================================================================
                                        
                                        Titulo("Calcular Resistência à Tração")
                                        forca = float(input("Força (N): "))
                                        area = float(input("Área (m²): "))
                                        resistencia_tracao = PropMecanicas.obter_resistencia_tracao(forca, area)
                                        if resistencia_tracao is not None:
                                            print(f"Resistência à Tração: {cores['verde']}{resistencia_tracao:.2e} Pa{cores['normal']}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "i": # Calcular Limite de Escoamento ==========================================================================================
                                        
                                        Titulo("Calcular Limite de Escoamento")
                                        forca = float(input("Força (N): "))
                                        area = float(input("Área (m²): "))
                                        limite_escoamento = PropMecanicas.obter_limite_escoamento(forca, area)
                                        if limite_escoamento is not None:
                                            print(f"Limite de Escoamento: {cores['verde']}{limite_escoamento:.2e} Pa{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "j": # Calcular Ductilidade (Alongamento) ==========================================================================================
                                        
                                        Titulo("Calcular Ductilidade (Alongamento)")
                                        delta_l = float(input("Variação de comprimento (m): "))
                                        l0 = float(input("Comprimento inicial (m): "))
                                        ductilidade = PropMecanicas.calcular_ductilidade_alongamento(delta_l, l0)
                                        if ductilidade is not None:
                                            print(f"Ductilidade (Alongamento): {cores['verde']}{ductilidade:.4f}{cores["normal"]}")
                                        else:
                                            print("Comprimento inicial inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "k": # Calcular Ductilidade (Redução de Área) ==========================================================================================
                                        
                                        Titulo("Calcular Ductilidade (Redução de Área)")
                                        area_inicial = float(input("Área inicial (m²): "))
                                        area_final = float(input("Área final (m²): "))
                                        ductilidade_reducao_area = PropMecanicas.calcular_ductilidade_reducao_area(area_inicial, area_final)
                                        if ductilidade_reducao_area is not None:
                                            print(f"Ductilidade (Redução de Área): {cores['verde']}{ductilidade_reducao_area:.4f}{cores["normal"]}")
                                        else:
                                            print("Área inicial inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "l": # Calcular Dureza ==========================================================================================
                                        
                                        Titulo("Obter Dureza")
                                        dureza = PropMecanicas.obter_dureza()
                                        print(f"Dureza: {cores['verde']}{dureza}{cores["normal"]}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "m": # Voltar ao menu anterior ==========================================================================================
                                        
                                        break

                                    case _:
                                        Invalida()

                        case "d": # Abrir Menu de Propriedades Térmicas ==========================================================================================
                            PropTermicas = PropriedadesTermicas()

                            while True:
                                Titulo("Propriedades Térmicas")

                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                                "A) Calor Específico\n" +
                                                "B) Capacidade Calorífica\n" +
                                                "C) Condutividade Térmica\n" +
                                                "D) Expansão Térmica Linear\n" +
                                                "E) Comprimento Final após Expansão Térmica\n" +
                                                "F) Voltar ao menu anterior\n\n" +
                                                "Sua opção: ").lower()

                                match opcao2:
                                    case "a": # Calcular Calor Específico ==========================================================================================
                                        
                                        Titulo("Calcular Calor Específico")
                                        calor = float(input("Calor (J): "))
                                        massa = float(input("Massa (kg): "))
                                        delta_t = float(input("Variação de temperatura (K ou °C): "))
                                        calor_especifico = PropTermicas.calcular_calor_especifico(calor, massa, delta_t)
                                        if calor_especifico is not None:
                                            print(f"Calor Específico: {cores['verde']}{calor_especifico:.2f} J/(kg.K){cores["normal"]}")
                                        else:
                                            print("Massa inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Calcular Capacidade Calorífica ==========================================================================================
                                        
                                        Titulo("Calcular Capacidade Calorífica")
                                        calor = float(input("Calor (J): "))
                                        massa = float(input("Massa (kg): "))
                                        delta_t = float(input("Variação de temperatura (K ou °C): "))
                                        capacidade_calorifica = PropTermicas.calcular_capacidade_calorifica(calor, massa, delta_t)
                                        if capacidade_calorifica is not None:
                                            print(f"Capacidade Calorífica: {cores['verde']}{capacidade_calorifica:.2f} J/K{cores["normal"]}")
                                        else:
                                            print("Massa inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Condutividade Térmica ==========================================================================================
                                        
                                        Titulo("Obter Condutividade Térmica")
                                        condutividade = PropTermicas.obter_condutividade_termica()
                                        print(f"Condutividade Térmica: {cores['verde']}{condutividade}{cores["normal"]}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Expansão Térmica Linear ==========================================================================================
                                        
                                        Titulo("Calcular Expansão Térmica Linear")
                                        coeficiente_expansao = float(input("Coeficiente de expansão térmica linear (1/K ou 1/°C): "))
                                        comprimento_inicial = float(input("Comprimento inicial (m): "))
                                        delta_temperatura = float(input("Variação da temperatura (K ou °C): "))
                                        delta_l = PropTermicas.calcular_expansao_termica_linear(coeficiente_expansao, comprimento_inicial, delta_temperatura)
                                        
                                        if delta_l is not None:
                                            print(f"Variação no Comprimento devido à Expansão Térmica: {cores['verde']}{delta_l:.6f} m{cores["normal"]}")
                                        else:
                                            print("Comprimento inicial inválido. Não pode ser zero.")
                                        
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Calcular Comprimento Final após Expansão Térmica ==========================================================================================
                                        
                                        Titulo("Calcular Comprimento Final após Expansão Térmica")
                                        comprimento_inicial = float(input("Comprimento inicial (m): "))
                                        delta_l = float(input("Variação no comprimento (m): "))
                                        comprimento_final = PropTermicas.calcular_comprimento_final_expansao_linear(comprimento_inicial, delta_l)
                                        if comprimento_final is not None:
                                            print(f"Comprimento Final após Expansão Térmica: {cores['verde']}{comprimento_final:.6f} m{cores["normal"]}")
                                        else:
                                            print("Comprimento inicial inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "f": # Voltar ao menu anterior ==========================================================================================
                                        
                                        break

                                    case _:
                                        Invalida()

                        case "e": # Abrir Menu de Tranformador de Fase ==========================================================================================
                            transformacao_fase = TransformadorDeFase()
                            
                            while True:
                                Titulo("Transformador de Fase")

                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                            "A) Calcular Fração de Fases (Regra da Alavanca)\n" +
                                            "B) Obter Temperatura de Transformação de Fase\n" +
                                            "C) Obter Microestrutura Prevista\n" +
                                            "D) Voltar ao menu anterior\n\n" +
                                            "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Fração de Fases (Regra da Alavanca) ==========================================================================================
                                        
                                        Titulo("Calcular Fração de Fases (Regra da Alavanca)")
                                        composicao_liga = float(input("Composição da liga (em %): "))
                                        composicao_fase_alfa = float(input("Composição da fase alfa (em %): "))
                                        composicao_fase_beta = float(input("Composição da fase beta (em %): "))
                                        fracao_alfa, fracao_beta = transformacao_fase.calcular_fracao_fase_regra_da_alavanca(composicao_liga, composicao_fase_alfa, composicao_fase_beta)
                                        if fracao_alfa is not None and fracao_beta is not None:
                                            print(f"Fração da Fase Alfa: {cores['verde']}{fracao_alfa:.2f}{cores["normal"]}")
                                            print(f"Fração da Fase Beta: {cores['verde']}{fracao_beta:.2f}{cores["normal"]}")
                                        else:
                                            print("A composição das fases alfa e beta é a mesma.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Obter Temperatura de Transformação de Fase ==========================================================================================
                                        
                                        Titulo("Obter Temperatura de Transformação de Fase")
                                        temperatura = transformacao_fase.obter_temperatura_transformacao_fase()
                                        print(f"Temperatura de Transformação de Fase: {cores['verde']}{temperatura}{cores["normal"]}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Obter Microestrutura Prevista ==========================================================================================
                                        
                                        Titulo("Obter Microestrutura Prevista")
                                        microestrutura = transformacao_fase.obter_microestrutura_prevista()
                                        print(f"Microestrutura Prevista: {cores['verde']}{microestrutura}{cores["normal"]}")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Voltar ao menu anterior ==========================================================================================
                                        
                                        break

                                    case _:
                                        Invalida()
                        case 'f': # Voltar ao menu anterior ==========================================================================================
                            break

                        case _:
                            Invalida()

            case "b": # Abrir Menu de Sistemas Fluido Mecânicos =========================================================================
                
                while True:
                    Titulo("Menu de Sistemas Fluido Mecânicos")
                    opcao1 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                   "A) Bombas e Turbinas\n" +
                                   "B) Dinâmica dos Flúidos\n" +
                                   "C) Estática dos FLúidos\n" +
                                   "D) Propriedades dos Flúidos\n" +
                                   "E) Tranferencia de Calor\n" +
                                   "f) Voltar ao menu principal\n\n" +
                                   "Sua opção: ").lower()
                    
                    match opcao1:
                        case "a": # Abrir Menu de Bombas e Turbinas ==========================================================================================
                            bombasTurbinas = BombasTurbinas()
                            
                            while True:
                                Titulo("Bombas e Turbinas")
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                                "A) Altura Manométrica da Bomba\n" +
                                                "B) Potência Hidráulica da Bomba\n" +
                                                "C) Eficiencia da Bomba\n" +
                                                "D) Potência Hidráulica da Turbina\n" +
                                                "E) Altura Líquida da Turbina\n" +
                                                "F) Eficiência da Turbina\n" +
                                                "G) Voltar ao menu anterior\n\n" +
                                                "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Altura Manométrica da Bomba ========================================================================================== 
                                        Titulo("Calcular Altura Manométrica da Bomba")
                                        pd = float(input("Pressão de descarga (Pa): "))
                                        ps = float(input("Pressão de sucção (Pa): "))
                                        vd = float(input("Velocidade de descarga (m/s): "))
                                        vs = float(input("Velocidade de sucção (m/s): "))
                                        hd = float(input("Altura de descarga (m): "))
                                        hs = float(input("Altura de sucção (m): "))
                                        rho = float(input("Densidade do fluido (kg/m³): "))
                                        hm = bombasTurbinas.calcular_altura_manometrica_bomba(pd, ps, vd, vs, hd, hs, rho)
                                        if hm is not None:
                                            print(f"Altura Manométrica da Bomba: {cores['verde']}{hm:.2f} m{cores["normal"]}")
                                        else:
                                            print("Densidade inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Calcular Potência Hidráulica da Bomba ==========================================================================================
                                        Titulo("Calcular Potência Hidráulica da Bomba")
                                        rho = float(input("Densidade do fluido (kg/m³): "))
                                        Q = float(input("Vazão volumétrica (m³/s): "))
                                        hm = float(input("Altura manométrica (m): "))
                                        Ph = bombasTurbinas.calcular_potencia_hidraulica_bomba(rho, Q, hm)
                                        if Ph is not None:
                                            print(f"Potência Hidráulica da Bomba: {cores['verde']}{Ph:.2f} W{cores["normal"]}")
                                        else:
                                            print("Altura manométrica inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Eficiência da Bomba ==========================================================================================
                                        Titulo("Calcular Eficiência da Bomba")
                                    
                                        potencia_fornecida = float(input("Potência hidráulica fornecida ao fluido (em Watts): "))
                                        potencia_entrada = float(input("Potência hidráulica da bomba (W): "))

                                        if potencia_entrada == 0:
                                            print("Potência hidráulica inválida. Não pode ser zero.")
                                            continue
                                        eficiencia = bombasTurbinas.calcular_eficiencia_bomba(potencia_fornecida, potencia_entrada)
                                        if eficiencia is not None:
                                            print(f"Eficiência da Bomba: {cores['verde']}{eficiencia:.2f}{cores["normal"]}")
                                        else:
                                            print("Potência fornecida inválida. Não pode ser zero.")
                                    
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Potência Hidráulica da Turbina ==========================================================================================
                                        Titulo("Calcular Potência Hidráulica da Turbina")
                                        rho = float(input("Densidade do fluido (kg/m³): "))
                                        Q = float(input("Vazão volumétrica (m³/s): "))
                                        h = float(input("Altura líquida (m): "))
                                        eficiencia_turbina = float(input("Eficiência da turbina (0 a 1): "))
                                        potencia = bombasTurbinas.calcular_potencia_hidraulica_turbina(rho, Q, h, eficiencia_turbina)
                                        if potencia is not None:
                                            print(f"Potência Hidráulica da Turbina: {cores['verde']}{potencia:.2f} W{cores["normal"]}")
                                        else:
                                            print("Altura líquida inválida. Não pode ser zero.")
                                        
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Calcular Altura Líquida da Turbina ==========================================================================================
                                        Titulo("Calcular Altura Líquida da Turbina")
                                        altura_bruta = float(input("Altura bruta (m): "))
                                        perdas_carga_turbina = float(input("Perdas de carga na turbina (m): "))
                                        altura_liquida = bombasTurbinas.calcular_altura_liquida_turbina(altura_bruta, perdas_carga_turbina)
                                        if altura_liquida is not None:
                                            print(f"Altura Líquida da Turbina: {cores['verde']}{altura_liquida:.2f} m{cores["normal"]}")
                                        else:
                                            print("Altura bruta inválida. Não pode ser zero.")
                                        
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "f": # Calcular Eficiência da Turbina ==========================================================================================
                                        Titulo("Calcular Eficiência da Turbina")
                                        
                                        potencia_gerada = float(input("Potência gerada pela turbina (W): "))
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        vazao_volumetrica = float(input("Vazão volumétrica (m³/s): "))
                                        altura_liquida = float(input("Altura líquida (m): "))
                                        eficiencia = bombasTurbinas.calcular_eficiencia_turbina_experimental(potencia_gerada, densidade, vazao_volumetrica, altura_liquida)
                                        if eficiencia is not None:
                                            print(f"Eficiência da Turbina: {cores['verde']}{eficiencia:.2f}{cores["normal"]}")
                                        else:
                                            print("Potência hidráulica disponível inválida. Não pode ser zero.")
                                    
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))                                        
                                        
                                    case "g": # Voltar ao menu anterior ==========================================================================================
                                        break

                                    case _:
                                        Invalida()
                        
                        case "b": # Abrir Menu de Dinâmica dos Flúidos ==========================================================================================
                            dinamicaFluidos = DinamicaFluidos()
                            
                            while True:
                                Titulo("Dinâmica dos Flúidos")
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                                "A) Vazão Volumétrica\n" +
                                                "B) Vazão Mássica\n" +
                                                "C) Equação da Continuidade Incompressível\n" +
                                                "D) Equação da Continuidade Compressível\n" +
                                                "E) Equação de Bernoulli\n" +
                                                "F) Perda de Carga Distribuída\n" +
                                                "G) Perda de Carga Local\n" +
                                                "H) Número de Reynolds (viscosidade dinâmica)\n" +
                                                "I) Número de Reynolds )Viscosidade cinemática)\n" +
                                                "J) Voltar ao menu anterior\n\n" +
                                                "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Vazão Volumétrica ==========================================================================================
                                        Titulo("Calcular Vazão Volumétrica")
                                        area = float(input("Área da seção (m²): "))
                                        velocidade = float(input("Velocidade do fluido (m/s): "))
                                        vazao_volumetrica = dinamicaFluidos.calcular_vazao_volumetrica(area, velocidade)
                                        if vazao_volumetrica is not None:
                                            print(f"Vazão Volumétrica: {cores['verde']}{vazao_volumetrica:.2f} m³/s{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                                    
                                    case "b": # Calcular Vazão Mássica ==========================================================================================
                                        Titulo("Calcular Vazão Mássica")
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        vazao_volumetrica = float(input("Vazão volumétrica (m³/s): "))
                                        vazao_massica = dinamicaFluidos.calcular_vazao_massica(densidade, vazao_volumetrica)
                                        if vazao_massica is not None:
                                            print(f"Vazão Mássica: {cores['verde']}{vazao_massica:.2f} kg/s{cores["normal"]}")
                                        else:
                                            print("Densidade inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Equação da Continuidade Incompressível ==========================================================================================
                                        Titulo("Calcular Equação da Continuidade Incompressível")
                                        area1 = float(input("Área da seção 1 (m²): "))
                                        velocidade1 = float(input("Velocidade na seção 1 (m/s): "))
                                        area2 = float(input("Área da seção 2 (m²): "))
                                        velocidade2 = dinamicaFluidos.aplicar_equacao_continuidade_incompressivel(area1, velocidade1, area2)
                                        if velocidade2 is not None:
                                            print(f"Velocidade na seção 2: {cores['verde']}{velocidade2:.2f} m/s{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                                    
                                    case "d": # Calcular Equação da Continuidade Compressível ==========================================================================================
                                        Titulo("Calcular Equação da Continuidade Compressível")
                                        area1 = float(input("Área da seção 1 (m²): "))
                                        velocidade1 = float(input("Velocidade na seção 1 (m/s): "))
                                        area2 = float(input("Área da seção 2 (m²): "))
                                        densidade1 = float(input("Densidade na seção 1 (kg/m³): "))
                                        densidade2 = float(input("Densidade na seção 2 (kg/m³): "))
                                        velocidade2 = dinamicaFluidos.aplicar_equacao_continuidade_compressivel(area1, velocidade1, area2, densidade1, densidade2)
                                        if velocidade2 is not None:
                                            print(f"Velocidade na seção 2: {cores['verde']}{velocidade2:.2f} m/s{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                                    
                                    case "e": # Calcular Equação de Bernoulli ==========================================================================================
                                        Titulo("Calcular Equação de Bernoulli")
                                        mensagem = "Função para calcular um termo desconhecido da Equação de Bernoulli \n(requer implementação específica para isolar a variável desejada)."
                                        print("{}{} Está opção ainda não está implementada.{}".format(cores["amarelo"], mensagem, cores['normal']))
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "f": # Calcular Perda de Carga Distribuída ==========================================================================================
                                        Titulo("Calcular Perda de Carga Distribuída")
                                        comprimento = float(input("Comprimento do tubo (m): "))
                                        diametro = float(input("Diâmetro do tubo (m): "))
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        fator_atrito = float(input("Fator de atrito (adimensional): "))
                                        velocidade = float(input("Velocidade do fluido (m/s): "))
                                        perda_carga = dinamicaFluidos.calcular_perda_carga_distribuida(comprimento, diametro, fator_atrito, densidade, velocidade)
                                        if perda_carga is not None:
                                            print(f"Perda de Carga Distribuída: {cores['verde']}{perda_carga:.2f} Pa{cores["normal"]}")
                                        else:
                                            print("Diâmetro inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "g": # Calcular Perda de Carga Local ==========================================================================================
                                        Titulo("Calcular Perda de Carga Local")
                                        coeficiente_perda = float(input("Coeficiente de perda de carga local (adimensional): "))
                                        velocidade = float(input("Velocidade do fluido (m/s): "))
                                        perda_carga_local = dinamicaFluidos.calcular_perda_carga_localizada(coeficiente_perda, velocidade)
                                        if perda_carga_local is not None:
                                            print(f"Perda de Carga Local: {cores['verde']}{perda_carga_local:.2f} Pa{cores["normal"]}")
                                        else:
                                            print("Coeficiente de perda de carga local inválido. Não pode ser zero.")
                                        
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "h": # Calcular Número de Reynolds (viscosidade dinâmica) ==========================================================================================
                                        Titulo("Calcular Número de Reynolds (viscosidade dinâmica)")
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        velocidade = float(input("Velocidade do fluido (m/s): "))
                                        diametro = float(input("Diâmetro do tubo (m): "))
                                        viscosidade_dinamica = float(input("Viscosidade dinâmica do fluido (Pa.s): "))
                                        numero_reynolds = dinamicaFluidos.calcular_numero_reynolds(densidade, velocidade, diametro, viscosidade_dinamica)
                                        if numero_reynolds is not None:
                                            print(f"Número de Reynolds: {cores['verde']}{numero_reynolds:.2f}{cores["normal"]}")
                                        else:
                                            print("Viscosidade dinâmica inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "i": # Calcular Número de Reynolds (viscosidade cinemática) ==========================================================================================
                                        Titulo("Calcular Número de Reynolds (viscosidade cinemática)")
                                        velocidade = float(input("Velocidade do fluido (m/s): "))
                                        diametro = float(input("Diâmetro do tubo (m): "))
                                        viscosidade_cinematica = float(input("Viscosidade cinemática do fluido (m²/s): "))
                                        numero_reynolds = dinamicaFluidos.calcular_numero_reynolds_alternativo(velocidade, diametro, viscosidade_cinematica)
                                        if numero_reynolds is not None:
                                            print(f"Número de Reynolds: {cores['verde']}{numero_reynolds:.2f}{cores["normal"]}")
                                        else:
                                            print("Viscosidade cinemática inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                                    
                                    case "j": 
                                        break
                                    
                                    case _:
                                        Invalida()

                        case "c": # Abrir Menu de Estática dos Flúidos ==========================================================================================
                            estFluidos = EstaticaFluidos()
                            
                            while True:
                                Titulo("Estática dos Flúidos")
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                                "A) Variação de Pressão com Profundidade\n" +
                                                "B) Força Hidrostática Plana\n" +
                                                "C) Centro de Pressão em Superficie Plana\n" +
                                                "D) Força Hidrostática em Superfície Curva Horizontal\n" +
                                                "E) Força Hidrostática em Superfície Curva Vertical\n" +
                                                "F) Voltar ao menu anterior\n\n" +
                                                "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a":
                                        Titulo("Variação de Pressão com Profundidade")
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        delta_profundidade = float(input("Diferença na Profundidade (z1 - z2) (m): "))
                                        variacao_pressao = estFluidos.calcular_variacao_pressao_profundidade(densidade, delta_profundidade)
                                        if variacao_pressao is not None:
                                            print(f"Variação de Pressão: {cores['verde']}{variacao_pressao:.2f} Pa{cores["normal"]}")
                                        else:
                                            print("Densidade inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "b": # Calcular Força Hidrostática Plana ==========================================================================================
                                        Titulo("Calcular Força Hidrostática Plana")
                                        pressao_centroide = float(input("Pressão no centroide da área (Pa): "))
                                        area = float(input("Área da superfície (m²): "))
                                        forca_hidrostatica = estFluidos.calcular_forca_hidrostatica_plana(pressao_centroide, area)
                                        if forca_hidrostatica is not None:
                                            print(f"Força Hidrostática Plana: {cores['verde']}{forca_hidrostatica:.2f} N{cores["normal"]}")
                                        else:
                                            print("Pressão no centroide inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Centro de Pressão em Superficie Plana ==========================================================================================
                                        Titulo("Calcular Centro de Pressão em Superficie Plana")
                                        y_centroide = float(input("Coordenada y do centroide da área (m): "))
                                        momento_inercia_xcg = float(input("Momento de inércia da área em relação ao eixo x que passa pelo centroide (m⁴): "))
                                        area = float(input("Área da superfície (m²): "))
                                        centro_pressao = estFluidos.calcular_centro_pressao_superficie_plana(y_centroide, momento_inercia_xcg, area)
                                        if centro_pressao is not None:
                                            print(f"Centro de Pressão: {cores['verde']}{centro_pressao:.2f} m{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Força Hidrostática em Superfície Curva Horizontal ==========================================================================================
                                        Titulo("Calcular Força Hidrostática em Superfície Curva Horizontal")
                                        pressao_centroide_projecao_vertical = float(input("Pressão no centroide da projeção vertical da área (Pa): "))
                                        area_projecao_vertical = float(input("Área da projeção vertical da superfície (m²): "))
                                        forca_hidrostatica = estFluidos.calcular_forca_hidrostatica_curva_horizontal(pressao_centroide_projecao_vertical, area_projecao_vertical)
                                        if forca_hidrostatica is not None:
                                            print(f"Força Hidrostática em Superfície Curva Horizontal: {cores['verde']}{forca_hidrostatica:.2f} N{cores["normal"]}")
                                        else:
                                            print("Pressão no centroide inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Calcular Força Hidrostática em Superfície Curva Vertical ==========================================================================================
                                        Titulo("Calcular Força Hidrostática em Superfície Curva Vertical")
                                        peso_volume_fluido_acima = float(input("Peso do volume de fluido diretamente acima da superfície curva (N): "))
                                        forca_hidrostatica = estFluidos.calcular_forca_hidrostatica_curva_vertical(peso_volume_fluido_acima)
                                        if forca_hidrostatica is not None:
                                            print(f"Força Hidrostática em Superfície Curva Vertical: {cores['verde']}{forca_hidrostatica:.2f} N{cores["normal"]}")
                                        else:
                                            print("Peso do volume de fluido inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "f": # Voltar ao menu anterior ==========================================================================================  
                                        break

                                    case _:
                                        Invalida()
                        
                        case "d": # Abrir Menu de Propriedades Térmicas ==========================================================================================
                            Titulo("Propriedades Flúidos")
                            propriedades = PropriedadesFluidos()
                            while True:
                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                                "A) Densidade\n" +
                                                "B) Peso Específico\n" +
                                                "C) Viscosidade Cinemática\n" +
                                                "D) Compressibilidade\n" +
                                                "E) Tensão Superficial\n" +
                                                "F) Voltar ao menu anterior\n\n" +
                                                "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Densidade ==========================================================================================
                                        Titulo("Calcular Densidade")
                                        massa = float(input("Massa (kg): "))
                                        volume = float(input("Volume (m³): "))
                                        densidade = propriedades.calcular_densidade(massa, volume)
                                        if densidade is not None:
                                            print(f"Densidade: {cores['verde']}{densidade:.2f} kg/m³{cores["normal"]}")
                                        else:
                                            print("Volume inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                                    
                                    case "b": # Calcular Peso Específico ==========================================================================================
                                        Titulo("Calcular Peso Específico")
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        peso_especifico = propriedades.calcular_peso_especifico(densidade)
                                        if peso_especifico is not None:
                                            print(f"Peso Específico: {cores['verde']}{peso_especifico:.2f} N/m³{cores["normal"]}")
                                        else:
                                            print("Densidade inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Viscosidade Cinemática ==========================================================================================
                                        Titulo("Calcular Viscosidade Cinemática")
                                        viscosidade_dinamica = float(input("Viscosidade dinâmica (Pa.s): "))
                                        densidade = float(input("Densidade do fluido (kg/m³): "))
                                        viscosidade_cinematica = propriedades.calcular_viscosidade_cinematica(viscosidade_dinamica, densidade)
                                        if viscosidade_cinematica is not None:
                                            print(f"Viscosidade Cinemática: {cores['verde']}{viscosidade_cinematica:.2f} m²/s{cores["normal"]}")
                                        else:
                                            print("Densidade inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Compressibilidade ==========================================================================================
                                        Titulo("Calcular Compressibilidade")
                                        compressibilidade_info = propriedades.obter_compressibilidade()
                                        print(cores['amarelo'] + compressibilidade_info + cores['normal'])

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Calcular Tensão Superficial ==========================================================================================
                                        Titulo("Calcular Tensão Superficial")
                                        forca = float(input("Força atuando na superfície (N): "))
                                        comprimento = float(input("Comprimento da linha onde a força atua (m): "))
                                        tensao_superficial = propriedades.calcular_tensao_superficial(forca, comprimento)
                                        if tensao_superficial is not None:
                                            print(f"Tensão Superficial: {cores['verde']}{tensao_superficial:.2f} N/m{cores["normal"]}")
                                        else:
                                            print("Comprimento inválido. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "f": # Voltar ao menu anterior ==========================================================================================
                                        break

                                    case _:
                                        Invalida()

                        case "e": # Abrir Menu de Tranferência de Calor ==========================================================================================
                            Titulo("Transferência de Calor")
                            transferenciaCalor = TransferenciaCalor()
                            while True:

                                opcao2 = input("\nSelecione qual a opção do menu você deseja seguir:\n\n" +
                                                "A) Condução de Calor\n" +
                                                "B) Convecção de Calor\n" +
                                                "C) Radiação de Calor\n" +
                                                "D) Trocador de Calor Logarítmica\n" +
                                                "E) Voltar ao menu anterior\n\n" +
                                                "Sua opção: ").lower()
                                
                                match opcao2:
                                    case "a": # Calcular Condução de Calor ==========================================================================================
                                        Titulo("Calcular Condução de Calor")
                                        k = float(input("Condutividade térmica (W/(m.K)): "))
                                        area = float(input("Área da seção (m²): "))
                                        dT = float(input("Diferença de temperatura (K): "))
                                        espessura = float(input("Espessura do material (m): "))
                                        condução = transferenciaCalor.calcular_conducao_calor(k, area, dT, espessura)
                                        if condução is not None:
                                            print(f"Condução de Calor: {cores['verde']}{condução:.2f} W{cores["normal"]}")
                                        else:
                                            print("Espessura inválida. Não pode ser zero.")
                                        
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))
                        
                                    case "b": # Calcular Convecção de Calor ==========================================================================================
                                        Titulo("Calcular Convecção de Calor")
                                        h = float(input("Coeficiente de convecção (W/(m².K)): "))
                                        area = float(input("Área da superfície (m²): "))
                                        temperatura_superficie = float(input("Temperatura da superfície (K): "))
                                        temperatura_fluido = float(input("Temperatura do fluido (K): "))
                                        convecção = transferenciaCalor.calcular_conveccao_calor(h, area, temperatura_superficie, temperatura_fluido)
                                        if convecção is not None:
                                            print(f"Convecção de Calor: {cores['verde']}{convecção:.2f} W{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "c": # Calcular Radiação de Calor ==========================================================================================
                                        Titulo("Calcular Radiação de Calor")
                                        emissividade = float(input("Emissividade da superfície (0 a 1): "))
                                        area = float(input("Área da superfície (m²): "))
                                        temperatura_superficie = float(input("Temperatura da superfície (K): "))
                                        temperatura_ambiente = float(input("Temperatura do ambiente (K): "))
                                        radiação = transferenciaCalor.calcular_radiacao_calor(emissividade, area, temperatura_superficie, temperatura_ambiente)
                                        if radiação is not None:
                                            print(f"Radiação de Calor: {cores['verde']}{radiação:.2f} W{cores["normal"]}")
                                        else:
                                            print("Área inválida. Não pode ser zero.")
                                        
                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "d": # Calcular Trocador de Calor ==========================================================================================
                                        Titulo("Calcular Trocador de Calor Logarítmica")
                                        temperatura_entrada_quente = float(input("Temperatura de entrada do fluido quente (K ou °C): "))
                                        temperatura_saida_quente = float(input("Temperatura de saída do fluido quente (K ou °C): "))
                                        temperatura_entrada_frio = float(input("Temperatura de entrada do fluido frio (K ou °C): "))
                                        temperatura_saida_frio = float(input("Temperatura de saída do fluido frio (K ou °C): "))
                                        trocador_calor = transferenciaCalor.calcular_trocador_calor_logaritmica(temperatura_entrada_quente, temperatura_saida_quente, temperatura_entrada_frio, temperatura_saida_frio)
                                        if trocador_calor is not None:
                                            print(f"Diferença de Temperatura Média Logarítmica: {cores['verde']}{trocador_calor:.2f} K ou °C{cores["normal"]}")
                                        else:
                                            print("Diferença de temperatura inválida. Não pode ser zero.")

                                        input('{}Pressione ENTER para voltar ao menu anterior...{}'.format(cores['amarelo'], cores['normal']))

                                    case "e": # Voltar ao menu anterior ==========================================================================================  
                                        break

                                    case _:
                                        Invalida()
                        
                        case "f": # Voltar ao menu de SIstemas Fluido Mecânicos ==========================================================================================
                            break

                        case _:
                            Invalida()
                            

            case "c": # Abrir menu de Tabela dos Materiais =============================================================================
                tabela_handler = Consulta_e_Cadastro()
                while True:
                    
                    Titulo("Tabela de Materiais")
                    acao = input(
                        "\nO que deseja fazer?\n"
                        "A) Consultar materiais\n"
                        "B) Cadastrar novo material\n"
                        "C) Deletar material\n"
                        "D) Voltar ao menu principal\n\n"
                        "Sua opção: ").lower()
                    
                    match acao: 
                        case "a":
                            system('cls')
                            tabela_handler.consultar_material()
                            VoltarMenu()
                        case "b":
                            system('cls')
                            tabela_handler.cadastrar_novo_material()
                            VoltarMenu()
                        case "c":
                            system('cls')
                            tabela_handler.deletar_material()
                            VoltarMenu()
                        case "d":
                            break
                        case _:
                            Invalida()
            
            case "d": # fechar o Programa ================================================================================================
                
                print(f"{cores['verde']}Programa finalizado. Até logo!{cores['normal']}")
                break

            case _: # Tratativa de opção inválida =================================================================================
                Invalida()