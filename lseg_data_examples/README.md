# LSEG Data Examples / Exemplos LSEG Data

Esta pasta contém exemplos de uso da biblioteca LSEG Data Platform em Python.

This folder contains examples of using the LSEG Data Platform library in Python.

## Exemplos Disponíveis / Available Examples

### 01_basic_connection.py
- **Português**: Demonstra como estabelecer uma conexão básica com a LSEG Data Platform e fazer uma consulta simples.
- **English**: Demonstrates how to establish a basic connection with LSEG Data Platform and make a simple query.

**Uso / Usage**:
```bash
python 01_basic_connection.py
```

### 02_historical_data.py
- **Português**: Exemplos de como obter dados históricos, incluindo preços, volumes, e dados fundamentais.
- **English**: Examples of how to retrieve historical data, including prices, volumes, and fundamental data.

**Uso / Usage**:
```bash
python 02_historical_data.py
```

### 03_realtime_data.py
- **Português**: Exemplos de dados em tempo real, incluindo snapshots, monitoramento de preços, e taxas de câmbio.
- **English**: Real-time data examples, including snapshots, price monitoring, and currency rates.

**Uso / Usage**:
```bash
python 03_realtime_data.py
```

## Códigos de Instrumentos / Instrument Codes

### Ações / Stocks
Os códigos de ações (RICs) geralmente seguem o formato: `SYMBOL.EXCHANGE`

Stock codes (RICs) generally follow the format: `SYMBOL.EXCHANGE`

Exemplos / Examples:
- `AAPL.O` - Apple (NYSE)
- `MSFT.O` - Microsoft (NASDAQ)
- `GOOGL.O` - Google (NASDAQ)
- `PETR4.SA` - Petrobras PN (B3 - Brasil)

### Moedas / Currencies
Pares de moedas usam o formato: `CCY1CCY2=`

Currency pairs use the format: `CCY1CCY2=`

Exemplos / Examples:
- `EUR=` - Euro/USD
- `GBP=` - British Pound/USD
- `JPY=` - Japanese Yen/USD

## Campos Comuns / Common Fields

### Preços / Prices
- `TR.PriceClose` - Preço de Fechamento / Closing Price
- `TR.PriceOpen` - Preço de Abertura / Opening Price
- `TR.PriceHigh` - Preço Máximo / High Price
- `TR.PriceLow` - Preço Mínimo / Low Price

### Volume e Capitalização / Volume and Capitalization
- `TR.Volume` - Volume
- `TR.CompanyMarketCap` - Capitalização de Mercado / Market Capitalization

### Dados Fundamentais / Fundamental Data
- `TR.CompanyName` - Nome da Empresa / Company Name
- `TR.PERatio` - Índice P/L / Price/Earnings Ratio
- `TR.DividendYield` - Rendimento de Dividendos / Dividend Yield
- `TR.Revenue` - Receita / Revenue
- `TR.NetIncome` - Lucro Líquido / Net Income

### Datas / Dates
- `TR.PriceClose.date` - Data do Preço / Price Date

## Configuração / Setup

1. Certifique-se de ter o arquivo `.env` configurado com seu App Key:
   Make sure you have the `.env` file configured with your App Key:

```
LSEG_APP_KEY=your_app_key_here
```

2. Instale as dependências:
   Install dependencies:

```bash
pip install -r ../requirements.txt
```

## Sessões / Sessions

A biblioteca LSEG Data requer abertura e fechamento de sessão:

The LSEG Data library requires opening and closing a session:

```python
import lseg.data as ld

# Abrir sessão / Open session
ld.open_session(name="desktop", app_key=app_key)

# Fazer consultas / Make queries
data = ld.get_data(...)

# Fechar sessão / Close session
ld.close_session()
```

## Documentação / Documentation

Para mais informações sobre RICs e campos disponíveis, consulte:

For more information about RICs and available fields, refer to:

- [LSEG Data Library for Python Documentation](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python)
- [Data Item Browser](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/documentation#data-item-browser)
