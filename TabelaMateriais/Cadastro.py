import os
import json
from typing import Optional, List, Dict

class Consulta_e_Cadastro:
    def __init__(self):
        # Define o diretório onde os arquivos dos materiais serão armazenados
        self.diretorio_tabela = os.path.join(os.path.dirname(__file__), "TabelaPropriedades")
        # Cria o diretório caso ele não exista
        if not os.path.exists(self.diretorio_tabela):
            os.makedirs(self.diretorio_tabela)

    def carregar_material(self, nome_arquivo: str) -> Optional[Dict]:
        """
            Carrega os dados de um material de um arquivo JSON.
            Retorna um dicionário com os dados ou None em caso de erro.
        """
        caminho_arquivo = os.path.join(self.diretorio_tabela, nome_arquivo)
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"Erro: Arquivo {nome_arquivo} contém JSON inválido.")
            return None

    def listar_materiais(self) -> List[str]:
        """
        Lista todos os arquivos JSON no diretório de materiais, retornando os nomes em minúsculo.
        """
        arquivos = os.listdir(self.diretorio_tabela)
        return [arquivo.lower() for arquivo in arquivos if arquivo.endswith('.json')]

    def exibir_propriedades_material(self, nome_material: str):
        """
        Exibe as propriedades de um material selecionado pelo usuário.
        """
        dados_material = self.carregar_material(nome_material)
        if dados_material and 'propriedades' in dados_material:
            os.system('cls')
            print(f"\nPropriedades de {dados_material['nome_material']}:")
            for propriedade, valor in dados_material['propriedades'].items():
                print(f"- {propriedade}: {valor}")
        else:
            print("Material não encontrado ou erro ao carregar.")

    def consultar_material(self):
        """
        Mostra a lista de materiais e permite ao usuário consultar as propriedades de um material específico,
        ou apenas visualizar a lista e voltar ao menu anterior.
        """
        materiais = self.listar_materiais()
        if materiais:
            os.system('cls')
            print("\nMateriais cadastrados:")
            for idx, mat in enumerate(materiais, 1):
                print(f"{idx}) {mat}")
            while True:
                escolha = input("\nDigite o número do material para ver as propriedades, ou 'c' para voltar: ")
                if escolha.lower() == 'c':
                    return
                try:
                    escolha = int(escolha)
                    if 1 <= escolha <= len(materiais):
                        nome_material_para_consultar = materiais[escolha - 1]
                        self.exibir_propriedades_material(nome_material_para_consultar)
                        input("\nPressione Enter para voltar à lista...")
                        os.system('cls')
                        # Após mostrar as propriedades, volta para a lista
                        print("\nMateriais cadastrados:")
                        for idx, mat in enumerate(materiais, 1):
                            print(f"{idx}) {mat}")
                    else:
                        print("Opção inválida. Por favor, escolha um número da lista.")
                except ValueError:
                    print("Por favor, digite um número válido ou 'c' para cancelar.")
        else:
            print("Nenhum material cadastrado.")

    def Selecao_de_Material(self):
        """
        Permite ao usuário selecionar um material para consulta ou cadastrar um novo material.
        """
        materiais = self.listar_materiais()
        if materiais:
            os.system('cls')
            print("Lista de Materiais:")
            for idx, material in enumerate(materiais, 1):
                print(f"{idx}) {material}")

            try:
                escolha = input("\nDigite o número do material para consultar ou 'n' para cadastrar novo: ")
                if escolha.lower() == 'n':
                    self.cadastrar_novo_material()
                    return
                escolha = int(escolha)
                if 1 <= escolha <= len(materiais):
                    nome_material_para_consultar = materiais[escolha - 1]
                    self.exibir_propriedades_material(nome_material_para_consultar)
                else:
                    print("Opção inválida. Por favor, escolha um número da lista.")
                    return  # <-- Adicionado para evitar cadastro indevido
            except ValueError:
                print("Por favor, digite um número válido.")
                return  # <-- Adicionado para evitar cadastro indevido
        else:
            print("Nenhum material encontrado.")
            cadastrar = input("Deseja cadastrar um novo material? (s/n): ").lower()
            if cadastrar == 's':
                self.cadastrar_novo_material()

    def cadastrar_novo_material(self):
        """
        Permite cadastrar um novo material, preenchendo todas as propriedades baseadas em um material de referência.
        Garante que não haja duplicidade de nomes (case insensitive).
        """
        materiais = self.listar_materiais()
        if not materiais:
            print("Não há materiais de referência para cadastro.")
            return

        # Usa o primeiro material como referência para as propriedades
        referencia = self.carregar_material(materiais[0])
        propriedades_referencia = referencia['propriedades']

        nome_material = input("Digite o nome do novo material: ").strip().lower()
        nome_arquivo = nome_material.replace(" ", "_") + ".json"

        # Verifica se já existe um material com esse nome (ignorando maiúsculas/minúsculas)
        if nome_arquivo.lower() in [m.lower() for m in materiais]:
            print("Já existe um material com esse nome.")
            return

        propriedades_novas = {}
        print("Preencha as propriedades do novo material:")
        for prop in propriedades_referencia:
            valor = input(f"{prop}: ").strip()
            propriedades_novas[prop] = valor

        novo_material = {
            "nome_material": nome_material,
            "propriedades": propriedades_novas
        }

        caminho_arquivo = os.path.join(self.diretorio_tabela, nome_arquivo)
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(novo_material, f, ensure_ascii=False, indent=4)
        print(f"Material '{nome_material}' cadastrado com sucesso!")

    def deletar_material(self):
        """
        Permite ao usuário deletar um material da lista, removendo o arquivo correspondente.
        Solicita confirmação antes de deletar.
        """
        materiais = self.listar_materiais()
        if not materiais:
            print("Nenhum material para deletar.")
            return

        print("Materiais disponíveis para deletar:")
        for idx, material in enumerate(materiais, 1):
            print(f"{idx}) {material}")

        try:
            escolha = input("\nDigite o número do material que deseja deletar ou 'c' para cancelar: ")
            if escolha.lower() == 'c':
                print("Operação cancelada.")
                return
            escolha = int(escolha)
            if 1 <= escolha <= len(materiais):
                nome_arquivo = materiais[escolha - 1]
                confirm = input(f"Tem certeza que deseja deletar '{nome_arquivo}'? (s/n): ").lower()
                if confirm == 's':
                    caminho_arquivo = os.path.join(self.diretorio_tabela, nome_arquivo)
                    try:
                        os.remove(caminho_arquivo)
                        print(f"Material '{nome_arquivo}' deletado com sucesso!")
                    except FileNotFoundError:
                        print("Arquivo já não existe.")
                else:
                    print("Operação cancelada.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número válido.")


if __name__ == "__main__":
    # Permite testar o módulo diretamente pelo terminal
    tabela_handler = Consulta_e_Cadastro()

    # Lista os materiais disponíveis
    materiais = tabela_handler.listar_materiais()
    if materiais:
        print("Lista de Materiais:")
        for idx, material in enumerate(materiais, 1):
            print(f"{idx}) {material}")

        try:
            escolha = input("\nDigite o número do material para consultar ou 'n' para cadastrar novo: ")
            if escolha.lower() == 'n':
                tabela_handler.cadastrar_novo_material()
            else:
                escolha = int(escolha)
                if 1 <= escolha <= len(materiais):
                    nome_material_para_consultar = materiais[escolha - 1]
                    tabela_handler.exibir_propriedades_material(nome_material_para_consultar)
                else:
                    print("Opção inválida. Por favor, escolha um número da lista.")
        except ValueError:
            print("Por favor, digite um número válido.")
    else:
        print("Nenhum material encontrado.")
        cadastrar = input("Deseja cadastrar um novo material? (s/n): ").lower()
        if cadastrar == 's':
            tabela_handler.cadastrar_novo_material()