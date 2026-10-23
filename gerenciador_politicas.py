"""Gerencia políticas de segurança usando herança e polimorfismo."""

#Classe
class Politica: #Classe base
    def __init__ (self, nome, versao, status):
        self.nome = nome
        self.versao = versao
        self.status = status

    def aplicar(self):
        print(f"Aplicando política: {self.nome} | Versão: {self.versao} | Status: {self.status}")

class PoliticaSeguranca(Politica): # Classe derivada | Segurança herdando de Politica
    def __init__ (self, nome, versao, status):
        super().__init__ (nome, versao, status)

    def aplicar(self):
        print(f"🔒 Política de Segurança: {self.nome} | Versão: {self.versao} | Status: {self.status}")

class PoliticaPrivacidade(Politica): # Classe derivada | Privacidade herdando de Politica
    def __init__ (self, nome, versao, status):
        super().__init__ (nome, versao, status)

    def aplicar(self):
        print(f"🔐 Política de Privacidade: {self.nome} | Versão: {self.versao} | Status: {self.status}")

class PoliticaAcesso(Politica): # Classe derivada | Acesso herdando de Politica
    def __init__ (self, nome, versao, status):
        super().__init__ (nome, versao, status)

    def aplicar(self):
        print(f"🚪 Política de Acesso: {self.nome} | Versão: {self.versao} | Status: {self.status}")

#Lista de políticas
politicas = [
    PoliticaSeguranca("Política de Senhas Corporativas", "v2.1", "ativa"),
    PoliticaSeguranca("Política de Gestão de Vulnerabilidades", "v1.0", "ativa"),
    PoliticaSeguranca("Política de Resposta a Incidentes", "v3.2", "em revisão"),
    PoliticaPrivacidade("Política de Dados Pessoais LGPD", "v1.3", "ativa"),
    PoliticaPrivacidade("Política de Retenção de Dados", "v2.0", "ativa"),
    PoliticaPrivacidade("Política de Consentimento", "v1.1", "desatualizada"),
    PoliticaAcesso("Política de Controle de Acesso", "v3.0", "ativa"),
    PoliticaAcesso("Política de Privilégio Mínimo", "v2.4", "ativa"),
    PoliticaAcesso("Política de Acesso Remoto VPN", "v1.5", "em revisão")
]

#Funções
def listar_politicas(lista_de_politicas):
    for politica in lista_de_politicas:
        politica.aplicar()

#Programa principal
if __name__ == "__main__":
    listar_politicas(politicas)
