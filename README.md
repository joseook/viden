# 👁️ Viden - Assistente de Desenvolvimento Multimodal

Viden é um assistente de desenvolvimento inteligente que utiliza a tela do usuário e áudio em tempo real para resolver dúvidas de programação de forma multimodal. Ele identifica linguagens, erros no console e estrutura de arquivos sem que você precise copiar e colar nada.

---

## ✨ Funcionalidades

- **Live Stream Multimodal**: Captura contínua de frames da tela e áudio.
- **Contexto Dinâmico**: Identificação automática de código e erros diretamente do seu ambiente de desenvolvimento.
- **Resposta via Voz (TTS)**: Feedback sonoro para manter seu foco total no código.
- **Controle Total**: Atalho global (`Ctrl+Shift+V`) para ativar ou silenciar o assistente instantaneamente.
- **Alta Performance**: Latência ultra-baixa com processamento otimizado.

---

## 🚀 Como Começar

### Pré-requisitos
- Python 3.10+
- Chave de API do Google Gemini
- Chave de API da OpenAI (para TTS)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/joseook/viden.git
   cd viden
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto (use o `.env.example` como base):
   ```env
   GOOGLE_API_KEY=sua_chave_aqui
   OPENAI_API_KEY=sua_chave_aqui
   ```

4. Execute o assistente:
   ```bash
   python src/main.py
   ```

---

## 🛠️ Estrutura do Projeto

- `src/`: Código fonte principal.
  - `capture/`: Módulos de captura de tela (`mss`) e áudio (`PyAudio`).
  - `ai/`: Integração com o Google Gemini (Modelo Multimodal).
  - `speech/`: Conversão de texto para fala (OpenAI TTS).
  - `ui/`: Gerenciamento de interface e atalhos de teclado.
- `requirements.txt`: Lista de dependências do Python.

---

## 🤝 Como Contribuir

O Viden é um projeto **Open Source** e adoraríamos ter sua contribuição! Seja corrigindo bugs, sugerindo novas funcionalidades ou melhorando a documentação.

### Passos para contribuir:

1. **Faça um Fork** do projeto.
2. **Crie uma Branch** para sua feature (`git checkout -b feature/NovaFuncionalidade`).
3. **Commit suas mudanças** (`git commit -m 'Adiciona nova funcionalidade'`).
4. **Push para a Branch** (`git push origin feature/NovaFuncionalidade`).
5. **Abra um Pull Request**.

### Exemplo de contribuição de código:
Se você quiser adicionar um novo provedor de TTS, basta criar uma nova classe em `src/speech/` que siga a interface padrão e enviar seu PR!

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com ❤️ para a comunidade de desenvolvedores.
