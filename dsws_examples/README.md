# DSWS Examples / Exemplos DSWS

Esta pasta contém exemplos de uso da biblioteca DataStream Web Service (DSWS) em Python.

This folder contains examples of using the DataStream Web Service (DSWS) library in Python.

## Exemplos Disponíveis / Available Examples

### 01_basic_connection.py
- **Português**: Demonstra como estabelecer uma conexão básica com o DSWS e fazer uma consulta simples.
- **English**: Demonstrates how to establish a basic connection with DSWS and make a simple query.

**Uso / Usage**:
```bash
python 01_basic_connection.py
```

### 02_time_series_data.py
- **Português**: Exemplos de como obter séries temporais de dados, incluindo dados de um único instrumento, múltiplos instrumentos, e diferentes frequências (diário, semanal, mensal).
- **English**: Examples of how to retrieve time series data, including single instrument data, multiple instruments, and different frequencies (daily, weekly, monthly).

**Uso / Usage**:
```bash
python 02_time_series_data.py
```

### 03_advanced_queries.py
- **Português**: Consultas avançadas incluindo dados fundamentais, constituintes de índices, moedas e commodities.
- **English**: Advanced queries including fundamental data, index constituents, currencies and commodities.

**Uso / Usage**:
```bash
python 03_advanced_queries.py
```

## Campos Comuns / Common Fields

### Preços / Prices
- `P` - Preço / Price
- `PO` - Preço de Abertura / Open Price
- `PH` - Preço Máximo / High Price
- `PL` - Preço Mínimo / Low Price

### Volume e Valor / Volume and Value
- `VO` - Volume
- `MV` - Valor de Mercado / Market Value

### Dados Fundamentais / Fundamental Data
- `PE` - Índice P/L / Price/Earnings Ratio
- `DY` - Rendimento de Dividendos / Dividend Yield
- `EPS` - Lucro por Ação / Earnings Per Share
- `BETA` - Beta
- `NAME` - Nome da Empresa / Company Name

## Frequências / Frequencies

- `D` - Diário / Daily
- `W` - Semanal / Weekly
- `M` - Mensal / Monthly
- `Q` - Trimestral / Quarterly
- `Y` - Anual / Yearly

## Configuração / Setup

1. Certifique-se de ter o arquivo `.env` configurado com suas credenciais:
   Make sure you have the `.env` file configured with your credentials:

```
DSWS_USERNAME=your_username
DSWS_PASSWORD=your_password
```

2. Instale as dependências:
   Install dependencies:

```bash
pip install -r ../requirements.txt
```

## Documentação / Documentation

Para mais informações sobre códigos de instrumentos e campos disponíveis, consulte a documentação oficial do DataStream.

For more information about instrument codes and available fields, refer to the official DataStream documentation.
