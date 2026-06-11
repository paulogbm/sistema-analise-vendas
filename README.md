# 📊 SalesVision BI

> Plataforma inteligente de análise de dados de vendas desenvolvida para a disciplina de Teste de Software.

---

## 📌 Sobre o Projeto

O **SalesVision BI** é uma plataforma web desenvolvida para processar e analisar dados de vendas a partir de arquivos CSV. O sistema permite que usuários realizem o upload de planilhas de vendas e obtenham automaticamente indicadores estratégicos para apoio à tomada de decisão.

A solução foi projetada para simplificar a análise de dados comerciais, fornecendo informações como receita total, produtos com melhor desempenho, produtos com menor desempenho e identificação de valores fora do padrão (outliers).

---

## 🚀 Funcionalidades

| Funcionalidade                                | Status      |
| --------------------------------------------- | ----------- |
| Login de acesso ao sistema                    | ✅ Concluído |
| Dashboard interativo                          | ✅ Concluído |
| Upload de arquivos CSV                        | ✅ Concluído |
| Processamento automático dos dados            | ✅ Concluído |
| Cálculo da receita total                      | ✅ Concluído |
| Identificação do produto líder                | ✅ Concluído |
| Identificação do produto com menor desempenho | ✅ Concluído |
| Detecção de outliers                          | ✅ Concluído |
| Interface responsiva                          | ✅ Concluído |
| Integração com GitHub                         | ✅ Concluído |
| Testes Unitários                              | ✅ Concluído |
| Testes de API                                 | ✅ Concluído |
| Testes E2E                                    | ✅ Concluído |

---

## 👥 Perfis de Usuário

### Usuário

* Realizar login no sistema;
* Fazer upload de arquivos CSV;
* Visualizar indicadores de vendas;
* Consultar resultados das análises.

### Administrador

* Gerenciar informações do sistema;
* Acompanhar análises realizadas;
* Gerenciar futuras configurações da plataforma.

---

## 🏗️ Arquitetura do Sistema

```text
┌─────────────────┐
│     Frontend    │
│ HTML • CSS      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Flask       │
│     Backend     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Pandas      │
│ Processamento   │
│ de Dados CSV    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Arquivos    │
│ CSV Analisados  │
└─────────────────┘
```

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python
* Flask
* Pandas

### Frontend

* HTML5
* CSS3

### Ferramentas

* Git
* GitHub
* Visual Studio Code

---

## 📂 Estrutura do Projeto

```text
Sistema-Dados-de-Vendas
│
├── models/
├── services/
│   └── analise.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── resultado.html
├── tests/
│   ├── test_analise.py
│   ├── test_api.py
│   └── test_upload.py
├── uploads/
├── app.py
├── requirements.txt
└── README.md
```

---

## 📋 Requisitos Funcionais

* RF01 – Permitir login de usuários.
* RF02 – Permitir upload de arquivos CSV.
* RF03 – Processar automaticamente os dados enviados.
* RF04 – Exibir indicadores de vendas no dashboard.
* RF05 – Identificar produtos líderes e com menor desempenho.
* RF06 – Detectar valores fora do padrão (outliers).

---

## 📋 Requisitos Não Funcionais

* Interface amigável e intuitiva.
* Compatibilidade com navegadores modernos.
* Processamento rápido de arquivos CSV.
* Código versionado utilizando GitHub.
* Estrutura modular para manutenção e evolução do sistema.

---

## 🧪 Testes de Software

O projeto contempla:

### Testes Unitários

* Validação da função de análise de vendas.
* Verificação dos cálculos de receita total.
* Identificação correta dos produtos líderes e de menor desempenho.

### Testes de API

* Teste do endpoint de upload.
* Validação das respostas do servidor.

### Testes E2E

* Fluxo completo de login.
* Upload de arquivo CSV.
* Exibição dos resultados no dashboard.

---

## 📈 Exemplo de Métricas Geradas

O sistema é capaz de apresentar:

* Receita Total de Vendas
* Produto Mais Vendido
* Produto com Menor Desempenho
* Quantidade de Outliers Detectados

---

## 👨‍💻 Integrantes

| Nome             | Papel          |
| ---------------- | -------------- |
| Débora Valeriano | Desenvolvedora |
| Paulo Gustavo    | Desenvolvedor  |
| Ana Carolina     | Desenvolvedora |

---

## 🏫 Instituição

Desenvolvido como projeto acadêmico para a disciplina de **Teste de Software**.

**Universidade Católica de Brasília (UCB)**

---

## 📌 Status do Projeto

✅ Projeto Concluído

Versão Final: **1.0**

---

## 🔗 Repositório

Sistema de Análise de Dados de Vendas desenvolvido utilizando Python, Flask e Pandas, aplicando conceitos de Engenharia de Software, Desenvolvimento Web e Teste de Software.
