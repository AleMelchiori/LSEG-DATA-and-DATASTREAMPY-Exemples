# Guia de Instalação / Installation Guide

Este guia fornece instruções detalhadas para configurar e usar os exemplos deste repositório.

This guide provides detailed instructions for setting up and using the examples in this repository.

## 📋 Requisitos do Sistema / System Requirements

- **Python**: 3.8 ou superior / 3.8 or higher
- **Sistema Operacional / Operating System**: Windows, macOS, ou Linux
- **Memória / Memory**: Mínimo 4GB RAM / Minimum 4GB RAM
- **Espaço em Disco / Disk Space**: 500MB para bibliotecas / 500MB for libraries

## 🔧 Instalação Passo a Passo / Step-by-Step Installation

### Passo 1: Verificar Python / Step 1: Check Python

Verifique se você tem Python instalado:

Check if you have Python installed:

```bash
python --version
# ou / or
python3 --version
```

Se Python não estiver instalado, baixe em: https://www.python.org/downloads/

If Python is not installed, download from: https://www.python.org/downloads/

### Passo 2: Clonar o Repositório / Step 2: Clone Repository

```bash
git clone https://github.com/AleMelchiori/LSEG-DATA-and-DATASTREAMPY-Exemples.git
cd LSEG-DATA-and-DATASTREAMPY-Exemples
```

### Passo 3: Criar Ambiente Virtual / Step 3: Create Virtual Environment

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

Você verá `(venv)` no início da linha de comando quando o ambiente estiver ativo.

You will see `(venv)` at the beginning of the command line when the environment is active.

### Passo 4: Instalar Dependências / Step 4: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 5: Configurar Credenciais / Step 5: Configure Credentials

1. Copie o arquivo template:
   Copy the template file:

```bash
cp .env.template .env
```

2. Edite o arquivo `.env`:
   Edit the `.env` file:

```bash
# Use seu editor preferido / Use your preferred editor
# Windows:
notepad .env

# macOS/Linux:
nano .env
# ou / or
vim .env
```

3. Preencha suas credenciais:
   Fill in your credentials:

```
DSWS_USERNAME=seu_usuario_aqui
DSWS_PASSWORD=sua_senha_aqui
LSEG_APP_KEY=sua_chave_aqui
```

### Passo 6: Testar Instalação / Step 6: Test Installation

**Testar DSWS**:
```bash
python dsws_examples/01_basic_connection.py
```

**Testar LSEG Data**:
```bash
python lseg_data_examples/01_basic_connection.py
```

## 🔑 Obtendo Credenciais / Getting Credentials

### DataStream Web Service (DSWS)

1. **Via Instituição / Through Institution**:
   - Muitas universidades e instituições financeiras têm acesso ao DataStream
   - Many universities and financial institutions have DataStream access
   - Contate sua biblioteca ou departamento de TI
   - Contact your library or IT department

2. **Solicitação Direta / Direct Request**:
   - Visite: https://www.lseg.com/en/data-analytics/financial-data/datastream-macroeconomic-analysis
   - Entre em contato com a equipe de vendas da LSEG
   - Contact the LSEG sales team

### LSEG Data Platform

1. **Criar Conta de Desenvolvedor / Create Developer Account**:
   - Visite: https://developers.lseg.com/
   - Clique em "Register" / "Sign Up"
   - Preencha o formulário de registro
   - Fill out the registration form

2. **Obter App Key**:
   - Faça login no Developer Portal
   - Login to the Developer Portal
   - Navegue para "My Apps"
   - Navigate to "My Apps"
   - Crie uma nova aplicação
   - Create a new application
   - Copie o App Key gerado
   - Copy the generated App Key

## 🐛 Solução de Problemas / Troubleshooting

### Erro: "Module not found"

**Solução / Solution**:
```bash
# Certifique-se de estar no ambiente virtual
# Make sure you're in the virtual environment
pip install -r requirements.txt
```

### Erro: "Authentication failed"

**Causas Possíveis / Possible Causes**:
- Credenciais incorretas / Incorrect credentials
- Arquivo `.env` não encontrado / `.env` file not found
- Permissões de acesso expiradas / Expired access permissions

**Solução / Solution**:
1. Verifique as credenciais no arquivo `.env`
2. Certifique-se de que o arquivo `.env` está no diretório raiz
3. Verifique se suas credenciais ainda são válidas

### Erro de Conexão / Connection Error

**Solução / Solution**:
- Verifique sua conexão com a internet / Check your internet connection
- Verifique se há firewall bloqueando a conexão / Check if firewall is blocking
- Tente novamente em alguns minutos / Try again in a few minutes

### Erro: "Permission denied" no Linux/macOS

**Solução / Solution**:
```bash
chmod +x dsws_examples/*.py
chmod +x lseg_data_examples/*.py
```

## 📦 Dependências Principais / Main Dependencies

| Biblioteca / Library | Versão / Version | Propósito / Purpose |
|---------------------|------------------|---------------------|
| DatastreamDSWS | ≥1.0.0 | Acesso ao DSWS / DSWS access |
| lseg-data | ≥1.0.0 | Plataforma LSEG / LSEG Platform |
| pandas | ≥1.5.0 | Manipulação de dados / Data manipulation |
| numpy | ≥1.23.0 | Computação numérica / Numerical computing |
| matplotlib | ≥3.5.0 | Visualização / Visualization |
| python-dotenv | ≥0.19.0 | Variáveis de ambiente / Environment variables |

## 🔄 Atualizando Dependências / Updating Dependencies

Para atualizar todas as dependências:

To update all dependencies:

```bash
pip install --upgrade -r requirements.txt
```

## 🧪 Testando os Exemplos / Testing Examples

### Teste Rápido / Quick Test

```bash
# DSWS
python -c "import DatastreamDSWS; print('DSWS OK')"

# LSEG Data
python -c "import lseg.data; print('LSEG Data OK')"
```

### Executar Todos os Exemplos DSWS / Run All DSWS Examples

```bash
python dsws_examples/01_basic_connection.py
python dsws_examples/02_time_series_data.py
python dsws_examples/03_advanced_queries.py
```

### Executar Todos os Exemplos LSEG / Run All LSEG Examples

```bash
python lseg_data_examples/01_basic_connection.py
python lseg_data_examples/02_historical_data.py
python lseg_data_examples/03_realtime_data.py
```

## 📞 Suporte Adicional / Additional Support

- **Issues do GitHub**: https://github.com/AleMelchiori/LSEG-DATA-and-DATASTREAMPY-Exemples/issues
- **LSEG Developer Community**: https://community.developers.lseg.com/
- **DataStream Support**: Através da sua instituição / Through your institution

## 🎓 Próximos Passos / Next Steps

1. Explore os exemplos em `dsws_examples/` e `lseg_data_examples/`
2. Leia os READMEs em cada pasta de exemplos
3. Adapte os exemplos para suas necessidades
4. Consulte a documentação oficial das bibliotecas

---

**Dica**: Mantenha sempre suas credenciais seguras e nunca as compartilhe ou faça commit no Git!

**Tip**: Always keep your credentials secure and never share them or commit them to Git!
