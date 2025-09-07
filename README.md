# ♻️ EcoBot – ChatBot Instrutor de Reciclagem
| Equipe                               | GitHub           |
|-------------------------------------|------------------|
| Leôncio Ferreira Flores Neto        | [@leoncioferreira-ufca](https://github.com/leoncioferreira-ufca)|
| Alan Mendes Vieira                  | [@alan-mendes-ufca](https://github.com/alan-mendes-ufca)         |
| Grazielly Bibiano do Nascimento     | [@graziellybn](https://github.com/graziellybn) |
| Antônio Pereira da Luz Neto        | [@netoo-444](https://github.com/netoo-444)   |
## 📌 Descrição:

Este projeto é um chatbot educativo desenvolvido em Python com Tkinter que ensina sobre reciclagem de materiais.
Além disso, o bot possui personalidades diferentes (formal, engraçada e rude), que afetam o tom da resposta, mas não o conteúdo.
---

## 🎯 Objetivos do Projeto

- Ensinar de forma interativa como reciclar diferentes tipos de materiais.
- Incentivar a conscientização ambiental através da tecnologia.
- Demonstrar conceitos de programação aplicada a um caso real.

---

## 🛠️ Tecnologias Utilizadas

- ✅ Python 3
- ✅ Tkinter (Interface gráfica)
- ✅ Dicionário de dados
- ✅ Manipulação de arquivos `.txt`
- ✅ Programação Orientada a Objetos (POO)

---

## 📚 Modos de Resposta (Personalidades)

O EcoBot pode responder de diferentes formas, dependendo da **personalidade escolhida pelo usuário**:

### 🧑‍🎓 Formal

* Fornece respostas educadas e detalhadas.
* Ideal para contextos acadêmicos ou explicativos.
* **Exemplo:** *“Para reciclar uma garrafa PET, lave-a, retire o rótulo e leve a um ponto de coleta adequado.”*

### 😂 Engraçado

* Responde de maneira leve, com humor e gírias.
* Torna a interação mais descontraída.
* **Exemplo:** *“Dá um banho na PET, tira a roupinha (rótulo) e manda pro ponto de coleta. Simples assim!”*

### 😒 Rude

* Responde de forma direta e impaciente.
* Curtas e objetivas, sem rodeios.
* **Exemplo:** *“Lava, tira o rótulo e leva pra reciclagem. Pronto.”*

> O usuário escolhe a personalidade ao iniciar o sistema e pode trocá-la durante a execução.
> O sistema mantém um contador de uso de cada personalidade e registra em arquivo.

---

## 🗂️ Estrutura de Arquivos

```bash
📂 Ecobot/
└── 📂 classes/
    ├── __init__.py       # <-- SEU ARQUIVO COM ESSES IMPORTS
    ├── ecobot.py         # define ChatBot
    ├── personality.py    # define Personalidade
    ├── history.py        # define Historico
    ├── learning.py       # define Aprendizado
    └── statistics.py     # define Estatisticas

```

---

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/ufca-es/Eco-bot.git
   ```
2. Entre no diretório:

   ```bash
   cd Eco-bot
   ```
3. Execute o projeto:

   ```bash
   python main.py
   ```
## 📜 Licença

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
