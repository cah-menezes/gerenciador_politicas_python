# 🏛️ Gerenciador de Políticas de Segurança

Script Python que modela políticas de segurança corporativa usando herança e polimorfismo — útil para catalogação e gestão de políticas em contextos de GRC.

## O que o script faz

- Modela uma classe base `Politica` com atributos e comportamento genérico
- Cria três tipos de política herdando da base: Segurança, Privacidade e Acesso
- Cada tipo tem seu próprio comportamento ao ser aplicado
- Percorre uma lista de políticas chamando `aplicar()` em cada uma

## Como executar

```
python gerenciador_politicas.py
```