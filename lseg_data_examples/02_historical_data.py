"""
LSEG Data - Historical Data Example
====================================

Este exemplo demonstra como obter dados históricos usando a LSEG Data Platform.

This example demonstrates how to retrieve historical data using LSEG Data Platform.

"""

import lseg.data as ld
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timedelta

load_dotenv()


def setup_session():
    """Configura a sessão LSEG / Sets up LSEG session"""
    app_key = os.getenv('LSEG_APP_KEY')
    ld.open_session(name="desktop", app_key=app_key)


def get_historical_prices(instruments, start_date, end_date, fields=None):
    """
    Obtém preços históricos para instrumentos
    
    Gets historical prices for instruments
    
    Args:
        instruments: Lista de RICs (e.g., ['AAPL.O', 'MSFT.O'])
        start_date: Data inicial (formato: 'YYYY-MM-DD')
        end_date: Data final (formato: 'YYYY-MM-DD')
        fields: Campos a serem retornados (default: preço de fechamento e volume)
    
    Returns:
        DataFrame: Dados históricos
    """
    if fields is None:
        fields = ['TR.PriceClose', 'TR.Volume']
    
    try:
        data = ld.get_history(
            universe=instruments,
            fields=fields,
            start=start_date,
            end=end_date
        )
        
        return data
        
    except Exception as e:
        print(f"Erro ao obter dados / Error getting data: {e}")
        return None


def example_single_stock_history():
    """
    Exemplo: Histórico de uma única ação
    
    Example: Single stock history
    """
    print("\n" + "=" * 60)
    print("Exemplo 1: Histórico de 30 dias - Apple (AAPL.O)")
    print("Example 1: 30-day history - Apple (AAPL.O)")
    print("=" * 60)
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    data = get_historical_prices(
        instruments=['AAPL.O'],
        start_date=start_date.strftime('%Y-%m-%d'),
        end_date=end_date.strftime('%Y-%m-%d')
    )
    
    if data is not None:
        print(f"\nDados históricos:")
        print(data)
        
        if isinstance(data, pd.DataFrame) and not data.empty:
            print(f"\nEstatísticas / Statistics:")
            print(data.describe())


def example_multiple_stocks():
    """
    Exemplo: Comparar múltiplas ações
    
    Example: Compare multiple stocks
    """
    print("\n" + "=" * 60)
    print("Exemplo 2: Comparação de ações de tecnologia")
    print("Example 2: Technology stocks comparison")
    print("=" * 60)
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    
    # RICs das principais empresas de tecnologia
    tech_stocks = ['AAPL.O', 'MSFT.O', 'GOOGL.O']
    
    data = get_historical_prices(
        instruments=tech_stocks,
        start_date=start_date.strftime('%Y-%m-%d'),
        end_date=end_date.strftime('%Y-%m-%d'),
        fields=['TR.PriceClose']
    )
    
    if data is not None:
        print(f"\nPreços de fechamento - últimos 90 dias:")
        print(data.head(15))
        print("\n...")
        print(data.tail(15))


def example_with_multiple_fields():
    """
    Exemplo: Obter múltiplos campos de dados
    
    Example: Get multiple data fields
    """
    print("\n" + "=" * 60)
    print("Exemplo 3: Múltiplos campos de dados")
    print("Example 3: Multiple data fields")
    print("=" * 60)
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Múltiplos campos
    fields = [
        'TR.PriceOpen',
        'TR.PriceHigh',
        'TR.PriceLow',
        'TR.PriceClose',
        'TR.Volume'
    ]
    
    data = get_historical_prices(
        instruments=['AAPL.O'],
        start_date=start_date.strftime('%Y-%m-%d'),
        end_date=end_date.strftime('%Y-%m-%d'),
        fields=fields
    )
    
    if data is not None:
        print(f"\nDados OHLCV - últimos 7 dias:")
        print("OHLCV Data - last 7 days:")
        print(data)


def example_with_fundamental_data():
    """
    Exemplo: Dados fundamentais históricos
    
    Example: Historical fundamental data
    """
    print("\n" + "=" * 60)
    print("Exemplo 4: Dados fundamentais")
    print("Example 4: Fundamental data")
    print("=" * 60)
    
    try:
        # Dados fundamentais atuais
        data = ld.get_data(
            universe=['AAPL.O', 'MSFT.O', 'GOOGL.O'],
            fields=[
                'TR.CompanyName',
                'TR.PriceClose',
                'TR.CompanyMarketCap',
                'TR.PERatio',
                'TR.DividendYield'
            ]
        )
        
        if data is not None:
            print("\nDados fundamentais atuais:")
            print("Current fundamental data:")
            print(data)
            
    except Exception as e:
        print(f"Erro / Error: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("LSEG Data - Exemplos de Dados Históricos")
    print("LSEG Data - Historical Data Examples")
    print("=" * 60)
    
    try:
        # Configurar sessão
        setup_session()
        
        # Executar exemplos
        example_single_stock_history()
        example_multiple_stocks()
        example_with_multiple_fields()
        example_with_fundamental_data()
        
        print("\n" + "=" * 60)
        print("✓ Todos os exemplos executados com sucesso!")
        print("✓ All examples executed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nErro / Error: {e}")
        print("\nVerifique suas credenciais no arquivo .env")
        print("Check your credentials in the .env file")
        
    finally:
        try:
            ld.close_session()
            print("\n✓ Sessão encerrada / Session closed")
        except:
            pass
