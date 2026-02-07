# LSEG-DATA and DataStreamPy - Exemplos / Examples

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Biblioteca pública de códigos e exemplos usando as bibliotecas Python LSEG-DATA e DataStreamPy.

Public library of code samples and examples using both LSEG-DATA and DataStreamPy Python libraries.

## 📋 Índice / Table of Contents

- [Sobre / About](#sobre--about)
- [Instalação / Installation](#instalação--installation)
- [Configuração / Configuration](#configuração--configuration)
- [Exemplos / Examples](#exemplos--examples)
- [Uso / Usage](#uso--usage)
- [Contribuindo / Contributing](#contribuindo--contributing)

## 🎯 Sobre / About

Este repositório contém exemplos práticos e rotinas para facilitar o uso das seguintes bibliotecas:

This repository contains practical examples and routines to facilitate the use of the following libraries:

- **DataStreamPy (DSWS)**: Acesso ao DataStream Web Service da LSEG
- **LSEG Data**: Plataforma de dados da London Stock Exchange Group

### Público-Alvo / Target Audience

- Analistas financeiros / Financial analysts
- Cientistas de dados / Data scientists
- Desenvolvedores / Developers
- Pesquisadores / Researchers
- Estudantes de finanças / Finance students

## 💻 Instalação / Installation

### Pré-requisitos / Prerequisites

- Python 3.8 ou superior / Python 3.8 or higher
- pip (gerenciador de pacotes Python / Python package manager)

### Passos / Steps

1. **Clone o repositório / Clone the repository**:
```bash
git clone https://github.com/AleMelchiori/LSEG-DATA-and-DATASTREAMPY-Exemples.git
cd LSEG-DATA-and-DATASTREAMPY-Exemples
```

2. **Crie um ambiente virtual (recomendado) / Create a virtual environment (recommended)**:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências / Install dependencies**:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração / Configuration

### 1. Configurar Credenciais / Set Up Credentials

Copie o arquivo de template e configure suas credenciais:

Copy the template file and configure your credentials:

```bash
cp .env.template .env
```

Edite o arquivo `.env` com suas credenciais:

Edit the `.env` file with your credentials:

```bash
# DataStream Web Service (DSWS)
DSWS_USERNAME=seu_usuario
DSWS_PASSWORD=sua_senha

# LSEG Data Platform
LSEG_APP_KEY=sua_chave_de_aplicacao
```

### 2. Obter Credenciais / Getting Credentials

#### DataStream (DSWS)
- Solicite acesso através da sua instituição ou contate a LSEG
- Request access through your institution or contact LSEG
- [LSEG DataStream](https://www.lseg.com/en/data-analytics/financial-data/datastream-macroeconomic-analysis)

#### LSEG Data Platform
- Registre-se no portal de desenvolvedores da LSEG
- Register on the LSEG Developer Portal
- [LSEG Developer Portal](https://developers.lseg.com/)

## 📚 Exemplos / Examples

### DataStream Web Service (DSWS)

Localização / Location: `dsws_examples/`

| Exemplo / Example | Descrição / Description |
|-------------------|-------------------------|
| `01_basic_connection.py` | Conexão básica e teste / Basic connection and test |
| `02_time_series_data.py` | Séries temporais / Time series data |
| `03_advanced_queries.py` | Consultas avançadas / Advanced queries |

**Tópicos cobertos / Topics covered**:
- ✅ Conexão com DSWS / DSWS connection
- ✅ Preços históricos / Historical prices
- ✅ Dados fundamentais / Fundamental data
- ✅ Múltiplos instrumentos / Multiple instruments
- ✅ Diferentes frequências / Different frequencies
- ✅ Moedas e commodities / Currencies and commodities

### LSEG Data Platform

Localização / Location: `lseg_data_examples/`

| Exemplo / Example | Descrição / Description |
|-------------------|-------------------------|
| `01_basic_connection.py` | Conexão básica e teste / Basic connection and test |
| `02_historical_data.py` | Dados históricos / Historical data |
| `03_realtime_data.py` | Dados em tempo real / Real-time data |

**Tópicos cobertos / Topics covered**:
- ✅ Conexão com LSEG Data / LSEG Data connection
- ✅ Dados históricos / Historical data
- ✅ Dados em tempo real / Real-time data
- ✅ Dados fundamentais / Fundamental data
- ✅ Taxas de câmbio / Currency rates
- ✅ Notícias / News

## 🚀 Uso / Usage

### Executar um Exemplo / Run an Example

```bash
# Exemplo DSWS
python dsws_examples/01_basic_connection.py

# Exemplo LSEG Data
python lseg_data_examples/01_basic_connection.py
```

### Estrutura Básica / Basic Structure

**DSWS**:
```python
import DatastreamDSWS as DSWS
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('DSWS_USERNAME')
password = os.getenv('DSWS_PASSWORD')

ds = DSWS.Datastream(username=username, password=password)
data = ds.get_data(tickers='AAPL', fields='P', kind=0)
print(data)
```

**LSEG Data**:
```python
import lseg.data as ld
import os
from dotenv import load_dotenv

load_dotenv()
app_key = os.getenv('LSEG_APP_KEY')

ld.open_session(name="desktop", app_key=app_key)
data = ld.get_data(universe=['AAPL.O'], fields=['TR.PriceClose'])
print(data)
ld.close_session()
```

## 📖 Documentação Adicional / Additional Documentation

- [DataStream DSWS Python Documentation](https://product.datastream.com/dsws/1.0/)
- [LSEG Data Library for Python](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python)
- [LSEG Data Item Browser](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/documentation#data-item-browser)

## 🤝 Contribuindo / Contributing

Contribuições são bem-vindas! Por favor:

Contributions are welcome! Please:

1. Faça um fork do repositório / Fork the repository
2. Crie uma branch para sua feature / Create a feature branch
3. Faça commit das suas mudanças / Commit your changes
4. Faça push para a branch / Push to the branch
5. Abra um Pull Request / Open a Pull Request

## 📝 Licença / License

Este projeto está disponível para uso público. Consulte o arquivo LICENSE para mais detalhes.

This project is available for public use. See the LICENSE file for more details.

## 👤 Autor / Author

**Alessandro Melchiori**

## 🙏 Agradecimentos / Acknowledgments

- LSEG (London Stock Exchange Group) por fornecer as bibliotecas e APIs
- LSEG (London Stock Exchange Group) for providing the libraries and APIs
- Comunidade Python / Python community

## 📞 Suporte / Support

Para questões específicas sobre as bibliotecas:

For library-specific questions:

- **DSWS**: Contate o suporte da LSEG DataStream / Contact LSEG DataStream support
- **LSEG Data**: Visite o [LSEG Developer Community](https://community.developers.lseg.com/)

Para questões sobre os exemplos:

For questions about the examples:

- Abra uma issue neste repositório / Open an issue in this repository

---

**Nota**: Este repositório contém apenas exemplos educacionais. Sempre verifique se você possui as licenças e permissões necessárias para acessar os dados.

**Note**: This repository contains educational examples only. Always ensure you have the necessary licenses and permissions to access the data.
