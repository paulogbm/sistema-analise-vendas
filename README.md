# 📊 SalesVision BI

> Plataforma inteligente de análise de dados de vendas desenvolvida para a disciplina de Teste de Software.

---

## 📌 Sobre o Projeto

O **SalesVision BI** é uma plataforma web desenvolvida para processar e analisar dados de vendas a partir de arquivos CSV. O sistema permite que usuários realizem o upload de planilhas de vendas e obtenham automaticamente indicadores estratégicos para apoio à tomada de decisão.

A solução foi projetada para simplificar a análise de dados comerciais, fornecendo informações como receita total, produtos com melhor desempenho, produtos com menor desempenho e identificação de valores fora do padrão (outliers).

---

## 🚀 Funcionalidades

| Funcionalidade                                | Status                |
| --------------------------------------------- | --------------------- |
| Login de acesso ao sistema                    | ✅ Implementado        |
| Dashboard interativo                          | ✅ Implementado        |
| Upload de arquivos CSV                        | ✅ Implementado        |
| Processamento automático dos dados            | ✅ Implementado        |
| Cálculo da receita total                      | ✅ Implementado        |
| Identificação do produto líder                | ✅ Implementado        |
| Identificação do produto com menor desempenho | ✅ Implementado        |
| Detecção de outliers                          | ✅ Implementado        |
| Histórico de análises                         | 🚧 Em desenvolvimento |
| Banco de dados SQLite                         | 🚧 Em desenvolvimento |
| Relatórios avançados                          | 🚧 Em desenvolvimento |

---

## 👥 Perfis de Usuário

### Usuário

* Realizar login no sistema;
* Fazer upload de arquivos CSV;
* Visualizar indicadores de vendas;
* Consultar resultados das análises.

### Administrador

* Gerenciar informações do sistema;
* Acompanhar histórico de análises;
* Gerenciar usuários e configurações futuras.

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
│ SQLite Database │
│ (Em desenvolvimento)
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

### Banco de Dados

* SQLite (em desenvolvimento)

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
├── static/
│   └── css/
├── templates/
├── tests/
├── uploads/
├── app.py
├── README.md
└── requirements.txt
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

* Interface responsiva e intuitiva.
* Processamento rápido dos arquivos enviados.
* Compatibilidade com navegadores modernos.
* Código versionado utilizando GitHub.
* Arquitetura preparada para expansão futura.

---

## 🧪 Testes de Software

O projeto contempla:

* Testes Unitários
* Testes de API
* Testes End-to-End (E2E)
* Casos de teste documentados
* Evidências de execução

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

🚧 Em desenvolvimento

Versão atual: **1.0**
