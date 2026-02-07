"""
DSWS Time Series Data Example
==============================

Este exemplo demonstra como obter séries temporais de dados do DSWS.

This example demonstrates how to retrieve time series data from DSWS.

"""

import DatastreamDSWS as DSWS
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timedelta

# Carregar variáveis de ambiente
load_dotenv()


def get_time_series_data(ds, tickers, fields, start_date, end_date, freq='D'):
    """
    Obtém dados de séries temporais do DataStream
    
    Gets time series data from DataStream
    
    Args:
        ds: DSWS connection object
        tickers: Lista de instrumentos (e.g., ['AAPL', 'MSFT'])
        fields: Lista de campos (e.g., ['P', 'MV', 'VO'])
        start_date: Data inicial (formato: 'YYYY-MM-DD')
        end_date: Data final (formato: 'YYYY-MM-DD')
        freq: Frequência dos dados ('D'=diário, 'W'=semanal, 'M'=mensal)
    
    Returns:
        DataFrame: Dados da série temporal
    """
    try:
        data = ds.get_data(
            tickers=tickers,
            fields=fields,
            start=start_date,
            end=end_date,
            freq=freq,
            kind=1  # kind=1 para séries temporais / for time series
        )
        
        return data
        
    except Exception as e:
        print(f"Erro ao obter dados / Error getting data: {e}")
        return None


def example_single_instrument():
    """
    Exemplo: Obter dados históricos de um único instrumento
    
    Example: Get historical data for a single instrument
    """
    print("\n" + "=" * 60)
    print("Exemplo 1: Dados históricos - Apple (AAPL)")
    print("Example 1: Historical data - Apple (AAPL)")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    # Últimos 30 dias
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    # Obter preço de fechamento (P) e volume (VO)
    data = get_time_series_data(
        ds,
        tickers='AAPL',
        fields=['P', 'VO'],
        start_date=start_date,
        end_date=end_date,
        freq='D'
    )
    
    if data is not None:
        print(f"\nDados de {start_date} até {end_date}:")
        print(data)
        print(f"\nEstatísticas / Statistics:")
        print(data.describe())


def example_multiple_instruments():
    """
    Exemplo: Comparar múltiplos instrumentos
    
    Example: Compare multiple instruments
    """
    print("\n" + "=" * 60)
    print("Exemplo 2: Comparação de múltiplas ações de tecnologia")
    print("Example 2: Comparison of multiple tech stocks")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    # Últimos 90 dias
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
    
    # Comparar Apple, Microsoft e Google
    data = get_time_series_data(
        ds,
        tickers=['AAPL', 'MSFT', 'GOOGL'],
        fields='P',  # Preço de fechamento
        start_date=start_date,
        end_date=end_date,
        freq='D'
    )
    
    if data is not None:
        print(f"\nPreços de fechamento - {start_date} até {end_date}:")
        print(data.head(10))
        print("\n...")
        print(data.tail(10))
        
        # Calcular retornos percentuais
        print("\n\nRetornos percentuais no período:")
        print("Percentage returns in the period:")
        if isinstance(data, pd.DataFrame) and len(data) > 0:
            first_values = data.iloc[0]
            last_values = data.iloc[-1]
            returns = ((last_values - first_values) / first_values * 100)
            print(returns)


def example_different_frequencies():
    """
    Exemplo: Dados em diferentes frequências
    
    Example: Data in different frequencies
    """
    print("\n" + "=" * 60)
    print("Exemplo 3: Dados mensais - Índice S&P 500")
    print("Example 3: Monthly data - S&P 500 Index")
    print("=" * 60)
    
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    ds = DSWS.Datastream(username=username, password=password)
    
    # Último ano em frequência mensal
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    
    data = get_time_series_data(
        ds,
        tickers='S&PCOMP',  # S&P 500 Index
        fields='P',
        start_date=start_date,
        end_date=end_date,
        freq='M'  # Mensal / Monthly
    )
    
    if data is not None:
        print(f"\nDados mensais de {start_date} até {end_date}:")
        print(data)


if __name__ == "__main__":
    print("=" * 60)
    print("DSWS - Exemplos de Séries Temporais")
    print("DSWS - Time Series Examples")
    print("=" * 60)
    
    try:
        # Executar exemplos
        example_single_instrument()
        example_multiple_instruments()
        example_different_frequencies()
        
        print("\n" + "=" * 60)
        print("✓ Todos os exemplos executados com sucesso!")
        print("✓ All examples executed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nErro / Error: {e}")
        print("\nVerifique suas credenciais no arquivo .env")
        print("Check your credentials in the .env file")
