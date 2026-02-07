"""
LSEG Data - Real-Time Data Streaming Example
============================================

Este exemplo demonstra como obter dados em tempo real (streaming) usando LSEG Data Platform.

This example demonstrates how to get real-time streaming data using LSEG Data Platform.

"""

import lseg.data as ld
import os
from dotenv import load_dotenv
import time

load_dotenv()


def setup_session():
    """Configura a sessão LSEG / Sets up LSEG session"""
    app_key = os.getenv('LSEG_APP_KEY')
    ld.open_session(name="desktop", app_key=app_key)


def example_real_time_snapshot():
    """
    Exemplo: Snapshot de dados em tempo real
    
    Example: Real-time data snapshot
    """
    print("\n" + "=" * 60)
    print("Exemplo 1: Snapshot de dados em tempo real")
    print("Example 1: Real-time data snapshot")
    print("=" * 60)
    
    try:
        # Obter snapshot de preços atuais
        data = ld.get_data(
            universe=['AAPL.O', 'MSFT.O', 'GOOGL.O'],
            fields=[
                'TR.PriceClose',
                'TR.PriceClose.date',
                'TR.Volume',
                'TR.CompanyMarketCap'
            ]
        )
        
        print("\nDados em tempo real / Real-time data:")
        print(data)
        
    except Exception as e:
        print(f"Erro / Error: {e}")


def example_streaming_prices():
    """
    Exemplo: Stream de preços (simulado com polling)
    
    Example: Price streaming (simulated with polling)
    
    Nota: O streaming real requer configuração avançada e conexão específica.
    Note: Real streaming requires advanced configuration and specific connection.
    """
    print("\n" + "=" * 60)
    print("Exemplo 2: Monitoramento de preços (polling)")
    print("Example 2: Price monitoring (polling)")
    print("=" * 60)
    
    instruments = ['AAPL.O', 'MSFT.O']
    
    print(f"\nMonitorando preços de {instruments}")
    print(f"Monitoring prices for {instruments}")
    print("(Ctrl+C para parar / to stop)")
    print()
    
    try:
        for i in range(5):  # 5 iterações para demonstração
            data = ld.get_data(
                universe=instruments,
                fields=['TR.PriceClose', 'TR.PriceClose.date']
            )
            
            print(f"\nAtualização {i+1} / Update {i+1}:")
            print(data)
            
            if i < 4:  # Não esperar na última iteração
                time.sleep(10)  # Aguardar 10 segundos
                
    except KeyboardInterrupt:
        print("\n\nMonitoramento interrompido pelo usuário")
        print("Monitoring stopped by user")
    except Exception as e:
        print(f"Erro / Error: {e}")


def example_intraday_data():
    """
    Exemplo: Dados intraday (dentro do dia)
    
    Example: Intraday data
    """
    print("\n" + "=" * 60)
    print("Exemplo 3: Dados intraday")
    print("Example 3: Intraday data")
    print("=" * 60)
    
    try:
        # Obter dados intraday recentes
        data = ld.get_data(
            universe=['AAPL.O'],
            fields=[
                'TR.PriceOpen',
                'TR.PriceHigh',
                'TR.PriceLow',
                'TR.PriceClose',
                'TR.Volume'
            ]
        )
        
        print("\nDados intraday / Intraday data:")
        print(data)
        
    except Exception as e:
        print(f"Erro / Error: {e}")


def example_currency_rates():
    """
    Exemplo: Taxas de câmbio em tempo real
    
    Example: Real-time currency rates
    """
    print("\n" + "=" * 60)
    print("Exemplo 4: Taxas de câmbio em tempo real")
    print("Example 4: Real-time currency rates")
    print("=" * 60)
    
    try:
        # Pares de moedas comuns
        currencies = ['EUR=', 'GBP=', 'JPY=']  # USD pairs
        
        data = ld.get_data(
            universe=currencies,
            fields=['TR.PriceClose', 'TR.PriceClose.date']
        )
        
        print("\nTaxas de câmbio / Currency rates:")
        print(data)
        
    except Exception as e:
        print(f"Erro / Error: {e}")


def example_news_headlines():
    """
    Exemplo: Manchetes de notícias recentes
    
    Example: Recent news headlines
    """
    print("\n" + "=" * 60)
    print("Exemplo 5: Manchetes de notícias")
    print("Example 5: News headlines")
    print("=" * 60)
    
    try:
        # Obter notícias recentes
        data = ld.get_data(
            universe=['AAPL.O'],
            fields=[
                'TR.HeadlineType',
                'TR.Headline',
                'TR.HeadlineDate'
            ]
        )
        
        print("\nManchetes recentes / Recent headlines:")
        print(data)
        
    except Exception as e:
        print(f"Nota: Campo de notícias pode requerer permissões específicas")
        print(f"Note: News fields may require specific permissions")
        print(f"Erro / Error: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("LSEG Data - Exemplos de Dados em Tempo Real")
    print("LSEG Data - Real-Time Data Examples")
    print("=" * 60)
    
    try:
        # Configurar sessão
        setup_session()
        
        # Executar exemplos
        example_real_time_snapshot()
        example_streaming_prices()
        example_intraday_data()
        example_currency_rates()
        example_news_headlines()
        
        print("\n" + "=" * 60)
        print("✓ Exemplos executados!")
        print("✓ Examples executed!")
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
