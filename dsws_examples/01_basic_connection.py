"""
DSWS Basic Connection Example
==============================

Este exemplo demonstra como estabelecer uma conexão básica com o DataStream Web Service (DSWS).

This example demonstrates how to establish a basic connection with DataStream Web Service (DSWS).

Requisitos / Requirements:
- DatastreamDSWS library instalada / installed
- Credenciais DSWS válidas / Valid DSWS credentials

"""

import DatastreamDSWS as DSWS
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente / Load environment variables
load_dotenv()

def connect_to_dsws():
    """
    Conecta ao DataStream Web Service usando credenciais do arquivo .env
    
    Connects to DataStream Web Service using credentials from .env file
    
    Returns:
        DSWS object: Objeto de conexão com DSWS / DSWS connection object
    """
    username = os.getenv('DSWS_USERNAME')
    password = os.getenv('DSWS_PASSWORD')
    
    if not username or not password:
        raise ValueError(
            "Credenciais DSWS não encontradas. "
            "Configure DSWS_USERNAME e DSWS_PASSWORD no arquivo .env\n"
            "DSWS credentials not found. "
            "Set DSWS_USERNAME and DSWS_PASSWORD in .env file"
        )
    
    # Criar objeto DataStream
    ds = DSWS.Datastream(username=username, password=password)
    
    print("✓ Conexão com DSWS estabelecida com sucesso!")
    print("✓ Successfully connected to DSWS!")
    
    return ds


def test_connection(ds):
    """
    Testa a conexão fazendo uma consulta simples
    
    Tests the connection by making a simple query
    
    Args:
        ds: DSWS connection object
    """
    try:
        # Consulta simples: preço de fechamento da Apple
        # Simple query: Apple closing price
        data = ds.get_data(tickers='AAPL', fields='P', kind=0)
        
        print("\nTeste de conexão - Dados da Apple (AAPL):")
        print("Connection test - Apple (AAPL) data:")
        print(data)
        
        return True
    except Exception as e:
        print(f"\nErro ao testar conexão / Error testing connection: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("DSWS - Exemplo de Conexão Básica")
    print("DSWS - Basic Connection Example")
    print("=" * 60)
    print()
    
    try:
        # Conectar ao DSWS
        ds = connect_to_dsws()
        
        # Testar conexão
        test_connection(ds)
        
    except Exception as e:
        print(f"\nErro / Error: {e}")
        print("\nVerifique suas credenciais no arquivo .env")
        print("Check your credentials in the .env file")
