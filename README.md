# pythonRPA

Utilitários simples para automação de tarefas de desktop em Python usando `pyautogui` e `pygetwindow`.

## Visão Geral
Este projeto traz a classe `AppAutomator`, definida em `app_automation.py`, que facilita:
- Executar programas do sistema operacional;
- Localizar janelas através do `pygetwindow`;
- Interagir com elementos na tela usando reconhecimento de imagem;
- Enviar comandos de teclado e mouse.

Como exemplo de uso, o script `mouse.py` movimenta o cursor periodicamente para evitar que a tela de descanso seja ativada.

## Requisitos
- Python 3.8+;
- `pyautogui`;
- (Opcional) `pygetwindow` para detecção de janelas.

## Instalação
Clone o repositório e instale as dependências:

```bash
pip install pyautogui pygetwindow
```

## Executando o exemplo
Para executar a aplicação de demonstração:

```bash
python mouse.py
```

## Automacao de aplicativos
Para integrar o `AppAutomator` ao seu projeto, importe a classe e utilize seus métodos para iniciar e manipular aplicativos.

## Janela de chat com ChatGPT
O script `chat_window.py` abre uma janela de chat que envia a mensagem digitada
ao ChatGPT e executa cada linha retornada como um comando do sistema. Defina a
variável `OPENAI_API_KEY` com sua chave da OpenAI antes de rodar o programa.

```bash
python chat_window.py
```

## Licença
Consulte o arquivo `LICENSE` para detalhes de licença.
