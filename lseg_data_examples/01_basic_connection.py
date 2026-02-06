"""
LSEG Data - Basic Connection Example
======================================

Este exemplo demonstra como estabelecer uma conexão básica com a LSEG Data Platform.

This example demonstrates how to establish a basic connection with LSEG Data Platform.

Requisitos / Requirements:
- lseg-data library instalada / installed
- App Key válido da LSEG / Valid LSEG App Key

"""

import lseg.data as ld
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


def connect_to_lseg():
    """
    Conecta à LSEG Data Platform usando App Key do arquivo .env
    
    Connects to LSEG Data Platform using App Key from .env file
    
    Returns:
        session: Sessão aberta com LSEG / Open LSEG session
    """
    app_key = os.getenv('LSEG_APP_KEY')
    
    if not app_key:
        raise ValueError(
            "App Key não encontrado. "
            "Configure LSEG_APP_KEY no arquivo .env\n"
            "App Key not found. "
            "Set LSEG_APP_KEY in .env file"
        )
    
    # Abrir sessão com LSEG Data Platform
    try:
        ld.open_session(
            name="desktop",
            app_key=app_key
        )
        
        print("✓ Conexão com LSEG Data Platform estabelecida com sucesso!")
        print("✓ Successfully connected to LSEG Data Platform!")
        
        return True
        
    except Exception as e:
        print(f"Erro ao conectar / Connection error: {e}")
        return False


def test_connection():
    """
    Testa a conexão fazendo uma consulta simples
    
    Tests the connection by making a simple query
    """
    try:
        # Consulta simples: dados da Apple
        # Simple query: Apple data
        data = ld.get_data(
            universe=['AAPL.O'],
            fields=['TR.PriceClose', 'TR.Volume']
        )
        
        print("\nTeste de conexão - Dados da Apple (AAPL.O):")
        print("Connection test - Apple (AAPL.O) data:")
        print(data)
        
        return True
        
    except Exception as e:
        print(f"\nErro ao testar conexão / Error testing connection: {e}")
        return False


def close_connection():
    """
    Fecha a sessão com LSEG Data Platform
    
    Closes the LSEG Data Platform session
    """
    try:
        ld.close_session()
        print("\n✓ Sessão encerrada / Session closed")
    except Exception as e:
        print(f"\nAviso ao fechar sessão / Warning closing session: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("LSEG Data - Exemplo de Conexão Básica")
    print("LSEG Data - Basic Connection Example")
    print("=" * 60)
    print()
    
    try:
        # Conectar à LSEG
        if connect_to_lseg():
            # Testar conexão
            test_connection()
        
    except Exception as e:
        print(f"\nErro / Error: {e}")
        print("\nVerifique suas credenciais no arquivo .env")
        print("Check your credentials in the .env file")
        
    finally:
        # Sempre fechar a sessão
        close_connection()
