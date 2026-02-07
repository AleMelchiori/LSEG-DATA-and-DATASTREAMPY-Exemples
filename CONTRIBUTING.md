# Guia de Contribuição / Contributing Guide

Obrigado por considerar contribuir para este projeto!

Thank you for considering contributing to this project!

## 🤝 Como Contribuir / How to Contribute

### Reportar Bugs / Report Bugs

Se você encontrou um bug, por favor:

If you found a bug, please:

1. Verifique se já não existe uma issue aberta sobre o problema
   Check if there isn't already an open issue about it
2. Abra uma nova issue com:
   Open a new issue with:
   - Descrição clara do problema / Clear description of the problem
   - Passos para reproduzir / Steps to reproduce
   - Comportamento esperado vs atual / Expected vs actual behavior
   - Versão do Python e bibliotecas / Python and library versions

### Sugerir Melhorias / Suggest Improvements

Para sugerir novos exemplos ou melhorias:

To suggest new examples or improvements:

1. Abra uma issue com tag "enhancement"
2. Descreva o que você gostaria de ver / Describe what you'd like to see
3. Explique o caso de uso / Explain the use case

### Adicionar Novos Exemplos / Add New Examples

#### Passo 1: Fork e Clone

```bash
# Fork no GitHub
# Fork on GitHub

# Clone seu fork / Clone your fork
git clone https://github.com/SEU_USUARIO/LSEG-DATA-and-DATASTREAMPY-Exemples.git
cd LSEG-DATA-and-DATASTREAMPY-Exemples
```

#### Passo 2: Criar Branch

```bash
git checkout -b feature/meu-novo-exemplo
# ou / or
git checkout -b bugfix/correcao-exemplo
```

#### Passo 3: Adicionar Seu Exemplo

**Estrutura de um Exemplo**:

```python
"""
Título do Exemplo
=================

Descrição em português do que o exemplo faz.

Description in English of what the example does.

Requisitos / Requirements:
- Biblioteca necessária / Required library
- Credenciais / Credentials

"""

import necessarias_bibliotecas
import os
from dotenv import load_dotenv

load_dotenv()


def funcao_principal():
    """
    Docstring em português
    
    Docstring in English
    """
    # Seu código aqui
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("Título do Exemplo")
    print("Example Title")
    print("=" * 60)
    
    try:
        funcao_principal()
        
        print("\n✓ Exemplo executado com sucesso!")
        print("✓ Example executed successfully!")
        
    except Exception as e:
        print(f"\nErro / Error: {e}")
```

#### Passo 4: Seguir Padrões / Follow Standards

**Nomenclatura de Arquivos / File Naming**:
- Use numeração sequencial: `01_`, `02_`, etc.
- Use nomes descritivos em inglês
- Use snake_case: `example_name.py`

**Comentários / Comments**:
- Sempre inclua descrições em português E inglês
- Always include descriptions in Portuguese AND English
- Use docstrings para funções
- Use docstrings for functions

**Código / Code**:
- Siga PEP 8
- Use variáveis e funções com nomes descritivos
- Use descriptive names for variables and functions
- Inclua tratamento de erros
- Include error handling

#### Passo 5: Testar

```bash
# Teste seu exemplo
python seu_exemplo.py

# Verifique imports
python -c "import seu_modulo; print('OK')"
```

#### Passo 6: Commit

```bash
git add .
git commit -m "Adiciona exemplo de [descrição]"
# ou / or
git commit -m "Adds example of [description]"
```

**Padrões de Mensagem de Commit / Commit Message Standards**:
- Em inglês / In English
- Use verbos no imperativo: "Add", "Fix", "Update"
- Seja descritivo mas conciso / Be descriptive but concise

Exemplos / Examples:
- ✅ "Add DSWS multi-currency example"
- ✅ "Fix connection error in basic example"
- ✅ "Update README with new instructions"
- ❌ "Update" (muito vago / too vague)
- ❌ "Fixed stuff" (não descritivo / not descriptive)

#### Passo 7: Push e Pull Request

```bash
git push origin feature/meu-novo-exemplo
```

Depois, no GitHub:

Then, on GitHub:

1. Abra um Pull Request / Open a Pull Request
2. Descreva suas mudanças / Describe your changes
3. Referencie issues relacionadas / Reference related issues
4. Aguarde review / Wait for review

## 📋 Checklist para Pull Request

Antes de submeter, verifique se:

Before submitting, check if:

- [ ] O código está funcionando / Code is working
- [ ] Comentários estão em PT e EN / Comments are in PT and EN
- [ ] Seguiu padrões de nomenclatura / Followed naming standards
- [ ] Adicionou documentação necessária / Added necessary documentation
- [ ] Testou com credenciais reais / Tested with real credentials
- [ ] Não commitou credenciais / Didn't commit credentials
- [ ] Seguiu PEP 8 / Followed PEP 8

## 🎨 Padrões de Código / Code Standards

### Python Style

Seguimos PEP 8 com algumas preferências:

We follow PEP 8 with some preferences:

- Indentação: 4 espaços / Indentation: 4 spaces
- Linha máxima: 100 caracteres / Max line length: 100 characters
- Strings: aspas simples quando possível / Single quotes when possible

### Estrutura de Diretórios / Directory Structure

```
LSEG-DATA-and-DATASTREAMPY-Exemples/
├── dsws_examples/
│   ├── 01_basic_connection.py
│   ├── 02_time_series_data.py
│   └── README.md
├── lseg_data_examples/
│   ├── 01_basic_connection.py
│   ├── 02_historical_data.py
│   └── README.md
├── .env.template
├── .gitignore
├── README.md
├── requirements.txt
└── SETUP_GUIDE.md
```

## 🚫 O Que NÃO Fazer / What NOT to Do

- ❌ Não faça commit de arquivos `.env` com credenciais
  Don't commit `.env` files with credentials
- ❌ Não adicione dependências desnecessárias
  Don't add unnecessary dependencies
- ❌ Não remova ou modifique exemplos existentes sem discussão
  Don't remove or modify existing examples without discussion
- ❌ Não use dados proprietários ou confidenciais nos exemplos
  Don't use proprietary or confidential data in examples

## ✅ O Que Fazer / What to Do

- ✅ Adicione novos exemplos práticos
  Add new practical examples
- ✅ Melhore documentação
  Improve documentation
- ✅ Corrija bugs
  Fix bugs
- ✅ Adicione casos de uso reais
  Add real use cases
- ✅ Melhore tratamento de erros
  Improve error handling

## 🔍 Review Process

1. **Automático / Automated**:
   - Verificação de sintaxe / Syntax check
   - PEP 8 compliance

2. **Manual**:
   - Code review por mantenedor / by maintainer
   - Teste de funcionalidade / Functionality test
   - Verificação de documentação / Documentation check

## 💬 Comunicação / Communication

- **Issues**: Para bugs e sugestões / For bugs and suggestions
- **Pull Requests**: Para contribuições de código / For code contributions
- **Discussions**: Para perguntas gerais / For general questions

## 📄 Licença / License

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto (MIT).

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT).

## 🙏 Agradecimentos / Acknowledgments

Todos os contribuidores serão reconhecidos no README principal.

All contributors will be acknowledged in the main README.

---

**Obrigado por contribuir! / Thank you for contributing!** 🎉
