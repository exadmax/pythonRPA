# pythonRPA

Este repositório contém utilidades simples de automação usando
``pyautogui``. Além da aplicação de exemplo ``mouse.py`` foi adicionada a
classe :class:`AppAutomator` em ``app_automation.py`` que permite:

* Executar programas do sistema operacional;
* Localizar janelas através do ``pygetwindow``;
* Interagir com elementos na tela por reconhecimento de imagem;
* Enviar comandos de teclado e mouse.

O uso destas funcionalidades depende do suporte de ``pyautogui`` e
``pygetwindow`` ao sistema operacional em execução.
