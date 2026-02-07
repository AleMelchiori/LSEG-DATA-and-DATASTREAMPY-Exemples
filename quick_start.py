#!/usr/bin/env python3
"""
Quick Start Script
==================

Script de início rápido para verificar instalação e configuração.

Quick start script to verify installation and configuration.

"""

import sys
import os


def print_header():
    """Imprime cabeçalho / Print header"""
    print("=" * 70)
    print("LSEG-DATA and DataStreamPy - Quick Start")
    print("Verificação de Instalação / Installation Check")
    print("=" * 70)
    print()


def check_python_version():
    """Verifica versão do Python / Check Python version"""
    print("🔍 Verificando versão do Python / Checking Python version...")
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("   ❌ Python 3.8+ é necessário / Python 3.8+ is required")
        return False
    else:
        print("   ✅ Versão do Python OK / Python version OK")
        return True


def check_dependencies():
    """Verifica dependências / Check dependencies"""
    print("\n🔍 Verificando dependências / Checking dependencies...")
    
    required = {
        'DatastreamDSWS': 'DatastreamDSWS',
        'lseg.data': 'lseg-data',
        'pandas': 'pandas',
        'numpy': 'numpy',
        'dotenv': 'python-dotenv'
    }
    
    missing = []
    
    for module, package in required.items():
        try:
            __import__(module)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} (faltando / missing)")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Dependências faltando / Missing dependencies: {', '.join(missing)}")
        print("\n💡 Execute / Run: pip install -r requirements.txt")
        return False
    
    return True


def check_env_file():
    """Verifica arquivo .env / Check .env file"""
    print("\n🔍 Verificando arquivo .env / Checking .env file...")
    
    if not os.path.exists('.env'):
        print("   ❌ Arquivo .env não encontrado / .env file not found")
        print("\n💡 Execute / Run: cp .env.template .env")
        print("   Depois edite o arquivo .env com suas credenciais")
        print("   Then edit the .env file with your credentials")
        return False
    
    print("   ✅ Arquivo .env encontrado / .env file found")
    
    # Verificar conteúdo / Check content
    with open('.env', 'r') as f:
        content = f.read()
        
        has_dsws = 'DSWS_USERNAME' in content and 'DSWS_PASSWORD' in content
        has_lseg = 'LSEG_APP_KEY' in content
        
        if has_dsws and 'your_username' not in content:
            print("   ✅ Credenciais DSWS configuradas / DSWS credentials configured")
        else:
            print("   ⚠️  Credenciais DSWS não configuradas / DSWS credentials not configured")
            
        if has_lseg and 'your_app_key' not in content:
            print("   ✅ Credenciais LSEG configuradas / LSEG credentials configured")
        else:
            print("   ⚠️  Credenciais LSEG não configuradas / LSEG credentials not configured")
    
    return True


def check_examples():
    """Verifica exemplos / Check examples"""
    print("\n🔍 Verificando estrutura de exemplos / Checking examples structure...")
    
    dsws_ok = os.path.exists('dsws_examples') and os.path.isdir('dsws_examples')
    lseg_ok = os.path.exists('lseg_data_examples') and os.path.isdir('lseg_data_examples')
    
    if dsws_ok:
        dsws_count = len([f for f in os.listdir('dsws_examples') if f.endswith('.py')])
        print(f"   ✅ dsws_examples/ ({dsws_count} exemplos / examples)")
    else:
        print("   ❌ dsws_examples/ não encontrado / not found")
        
    if lseg_ok:
        lseg_count = len([f for f in os.listdir('lseg_data_examples') if f.endswith('.py')])
        print(f"   ✅ lseg_data_examples/ ({lseg_count} exemplos / examples)")
    else:
        print("   ❌ lseg_data_examples/ não encontrado / not found")
    
    return dsws_ok and lseg_ok


def print_next_steps():
    """Imprime próximos passos / Print next steps"""
    print("\n" + "=" * 70)
    print("📚 Próximos Passos / Next Steps")
    print("=" * 70)
    print()
    print("1. Configure suas credenciais no arquivo .env")
    print("   Configure your credentials in the .env file")
    print()
    print("2. Execute um exemplo DSWS:")
    print("   Run a DSWS example:")
    print("   python dsws_examples/01_basic_connection.py")
    print()
    print("3. Execute um exemplo LSEG Data:")
    print("   Run an LSEG Data example:")
    print("   python lseg_data_examples/01_basic_connection.py")
    print()
    print("4. Leia o guia de instalação completo:")
    print("   Read the complete setup guide:")
    print("   SETUP_GUIDE.md")
    print()
    print("=" * 70)


def main():
    """Função principal / Main function"""
    print_header()
    
    checks = [
        ("Python Version", check_python_version()),
        ("Dependencies", check_dependencies()),
        ("Environment File", check_env_file()),
        ("Examples Structure", check_examples())
    ]
    
    print("\n" + "=" * 70)
    print("📊 Resumo / Summary")
    print("=" * 70)
    
    all_ok = True
    for name, result in checks:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
        if not result:
            all_ok = False
    
    print("=" * 70)
    
    if all_ok:
        print("\n🎉 Tudo pronto! / All set!")
        print("Você está pronto para usar os exemplos!")
        print("You are ready to use the examples!")
    else:
        print("\n⚠️  Alguns itens precisam de atenção")
        print("Some items need attention")
        print("Siga as instruções acima para corrigir")
        print("Follow the instructions above to fix")
    
    print_next_steps()


if __name__ == "__main__":
    main()
