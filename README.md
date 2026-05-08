# -Auditoria-de-Or-amentos-Corporativos-Python-
# 🏢 Auditoria de Orçamentos Corporativos (Python)

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()

## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Programação de Computadores. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.

A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.

## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.

## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.

## ⚙️ Como Executar

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/gui995/-Auditoria-de-Or-amentos-Corporativos-Python-.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd -Auditoria-de-Or-amentos-Corporativos-Python-
   ```
3. Execute o script principal:
   ```bash
   python orcamento_empresa.py
   ```

## 🧠 Lógica e Estrutura do Código

A parte que mais exigiu atenção foi pensar em como descer nos dicionários sem saber quantos níveis existiam. A solução foi criar uma função separada chamada `_percorrer` que chama ela mesma sempre que encontra um novo dicionário, e só para quando chega em um número — que é o orçamento de fato. Separei ela da função principal justamente pra que o decorator não ficasse disparando log a cada nível que a recursão descia, o que poluiria demais a saída.

O `@auditor` foi pensado pra ser independente da função que ele envolve, por isso usei `*args` e `**kwargs` dentro do `wrapper` — assim ele consegue repassar qualquer argumento sem precisar conhecer a assinatura da função decorada. Dentro dele usei `time.perf_counter()` no lugar de `time.time()` porque ele tem precisão maior pra medir intervalos curtos, o que faz mais sentido pra esse tipo de monitoramento.

* **Dados:** A estrutura `EMPRESA` foi montada como um dicionário aninhado simulando a hierarquia real de uma empresa — Matriz e Filiais como primeiro nível, depois os departamentos, sub-departamentos e equipes. Os valores numéricos ficam sempre nas pontas (folhas), que é onde a recursão para de descer e soma o valor.

## 👤 Autor

* **Guilherme Henrique**
* GitHub: [gui995](https://github.com/gui995)

---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
