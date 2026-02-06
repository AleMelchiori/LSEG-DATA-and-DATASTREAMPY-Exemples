"""
DSWS Advanced Queries Example
==============================

Este exemplo demonstra consultas avançadas no DSWS incluindo múltiplos campos,
filtros e análises.

This example demonstrates advanced DSWS queries including multiple fields,
filters and analysis.

"""

import DatastreamDSWS as DSWS
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timedelta

load_dotenv()


def get_fundamental_data(ds, tickers, fields):
    """
    Obtém dados fundamentais de empresas
    
    Gets fundamental company data
    
    Common fields / Campos comuns:
    - P: Price / Preço
    - MV: Market Value / Valor de Mercado
    - PE: Price/Earnings Ratio / Índice P/L
    - DY: Dividend Yield / Rendimento de Dividendos
    - EPS: Earnings Per Share / Lucro por Ação
    - BETA: Beta
    
    Args:
        ds: DSWS connection object
        tickers: Lista ou string com tickers
        fields: Lista ou string com campos
    
    Returns:
        DataFrame: Dados fundamentais
    """
    try:
        data = ds.get_data(
            tickers=tickers,
            fields=fields,
            kind=0  # kind=0 para snapshot / for snapshot data
        )
        return data
    except Exception as e:
        print(f"Erro / Error: {e}")
        return None


def example_fundamental_analysis():
    """
    Exemplo: Análise fundamental de empresas
    
    Example: Fundamental analysis of companies
    """
    print("\n" + "=" * 60)
    print("Exemplo 1: Análise Fundamental - Top Tech Stocks")
    print("Example 1: Fundamental Analysis - Top Tech Stocks")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
    
    # Múltiplos campos fundamentais
    fields = ['NAME', 'P', 'MV', 'PE', 'DY', 'EPS']
    
    data = get_fundamental_data(ds, tickers, fields)
    
    if data is not None:
        print("\nDados Fundamentais / Fundamental Data:")
        print(data)
        print("\n")
        print("Legenda / Legend:")
        print("NAME: Nome da empresa / Company name")
        print("P: Preço / Price")
        print("MV: Valor de mercado / Market Value")
        print("PE: Índice P/L / Price/Earnings Ratio")
        print("DY: Rendimento de dividendos / Dividend Yield")
        print("EPS: Lucro por ação / Earnings Per Share")


def example_index_constituents():
    """
    Exemplo: Obter constituintes de um índice
    
    Example: Get index constituents
    """
    print("\n" + "=" * 60)
    print("Exemplo 2: Constituintes do Dow Jones")
    print("Example 2: Dow Jones Constituents")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    # Alguns constituintes do Dow Jones
    dow_tickers = ['AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'GS', 'HD', 'IBM', 'INTC']
    
    fields = ['NAME', 'P', 'MV', 'BETA']
    
    data = get_fundamental_data(ds, dow_tickers, fields)
    
    if data is not None:
        print("\nDados dos Constituintes / Constituent Data:")
        print(data)


def example_currency_data():
    """
    Exemplo: Obter dados de moedas
    
    Example: Get currency data
    """
    print("\n" + "=" * 60)
    print("Exemplo 3: Taxas de Câmbio")
    print("Example 3: Currency Exchange Rates")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    # Últimos 30 dias
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    # Pares de moedas comuns
    currencies = ['USDEUR', 'USDGBP', 'USDJPY', 'USDBRL']
    
    try:
        data = ds.get_data(
            tickers=currencies,
            fields='P',
            start=start_date,
            end=end_date,
            freq='D',
            kind=1
        )
        
        if data is not None:
            print(f"\nTaxas de câmbio - {start_date} até {end_date}:")
            print(data.head(10))
            print("\n...")
            print(data.tail(10))
            
            # Variação percentual
            if isinstance(data, pd.DataFrame) and len(data) > 0:
                print("\n\nVariação percentual no período:")
                print("Percentage change in the period:")
                first_values = data.iloc[0]
                last_values = data.iloc[-1]
                change = ((last_values - first_values) / first_values * 100)
                print(change)
                
    except Exception as e:
        print(f"Erro ao obter dados de moedas / Error getting currency data: {e}")


def example_commodity_data():
    """
    Exemplo: Dados de commodities
    
    Example: Commodity data
    """
    print("\n" + "=" * 60)
    print("Exemplo 4: Preços de Commodities")
    print("Example 4: Commodity Prices")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    # Últimos 90 dias
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
    
    # Commodities comuns (códigos podem variar)
    commodities = ['LMAHDY', 'LMCADY', 'NYMEX']  # Exemplo de códigos
    
    try:
        data = ds.get_data(
            tickers=commodities,
            fields='P',
            start=start_date,
            end=end_date,
            freq='W',  # Semanal
            kind=1
        )
        
        if data is not None:
            print(f"\nPreços semanais de commodities - {start_date} até {end_date}:")
            print(data.head(10))
            
    except Exception as e:
        print(f"Nota: Alguns códigos de commodities podem não estar disponíveis")
        print(f"Note: Some commodity codes may not be available")
        print(f"Erro / Error: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("DSWS - Exemplos de Consultas Avançadas")
    print("DSWS - Advanced Queries Examples")
    print("=" * 60)
    
    try:
        example_fundamental_analysis()
        example_index_constituents()
        example_currency_data()
        example_commodity_data()
        
        print("\n" + "=" * 60)
        print("✓ Exemplos executados!")
        print("✓ Examples executed!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nErro / Error: {e}")
        print("\nVerifique suas credenciais no arquivo .env")
        print("Check your credentials in the .env file")
