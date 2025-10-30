# ♻️ EcoBot – ChatBot Instrutor de Reciclagem
| Equipe                               | GitHub           |
|-------------------------------------|------------------|
| Leôncio Ferreira Flores Neto        | [@LeoncioFerreira](https://github.com/LeoncioFerreira)|
| Alan Mendes Vieira                  | [@alan-mendes-ufca](https://github.com/alan-mendes-ufca)|
| Grazielly Bibiano do Nascimento     | [@graziellybn](https://github.com/graziellybn) |
| Antônio Pereira da Luz Neto        | [@netoo-444](https://github.com/netoo-444)   |
## 📌 Descrição:

Este projeto é um chatbot educativo desenvolvido em Python com Streamlit que ensina sobre reciclagem de materiais.
Além disso, o bot possui personalidades diferentes (formal, engraçada e rude), que afetam o tom da resposta, mas não o conteúdo.
---

## 🎯 Objetivos do Projeto

- Ensinar de forma interativa como reciclar diferentes tipos de materiais.
- Incentivar a conscientização ambiental através da tecnologia.
- Demonstrar conceitos de programação aplicada a um caso real.

---

## 🛠️ Tecnologias Utilizadas

- ✅ Python 3
- ✅ Streamlit (Interface gráfica)
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
├── Ecobot
│   ├── chatbot_data
│   │   ├── history.txt
│   │   ├── learning_responses.json
│   │   ├── questions.json
│   │   └── relatorio.txt
│   ├── classes
│   │   ├── chatbot_analytics.py
│   │   ├── chatbot_frequent_questions.py
│   │   ├── chatbot_learning.py
│   │   ├── chatbot_memory.py
│   │   ├── chatbot.py
│   │   ├── chatbot_reply.py
│   │   ├── chatbot_report.py
│   │   └── __init__.py
│   ├── helpers.py
│   ├── main.py
│   ├── requirements.txt
│   └── test
│       └── test_reply.py
└── README.md
```

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   1.1 git clone https://github.com/ufca-es/Eco-bot.git
   1.2 cd ecobot/Ecobot
   exemplo: cd "/home/pc/Desktop/teste_final/Eco-bot/Ecobot"
   ```
2. Criar ambiente virtual (recomendado)

   ```bash
   2.1python3 -m venv venv

   2.2 source venv/bin/activate   # Linux/Mac
   2.2 venv\Scripts\activate      # Windows (PowerShell)
   ```
 
3. Instalar dependências
 ```bash
    3.1 pip install -r requirements.txt
   ```
4. Executar a versão com Streamlit (interface gráfica)
 ```bash
    4.1 streamlit run app.py
   ```
# Tasks atribuídas

Leôncio → Task 05 → Configuração do repositório no GitHub (estrutura básica, README inicial ) e interface

Alan + Leôncio → Task 09 (respostas aleatórias para mesma pergunta)

Alan → Task 08 (mudança de personalidade durante a execução)

Neto → Task 10 (persistência de aprendizado)

Grazy → Task 11 (ler histórico anterior ao iniciar o programa) + Task 12 (salvar histórico da sessão)

Alan → Task 13 (coletar estatísticas: total de interações, pergunta mais feita, uso de personalidades) + Task 16 (organização final das classes/módulos)

Neto → Task 14 (gerar relatório legível – relatorio.txt)

Grazy → Task 15 (exibir sugestões de perguntas frequentes)

* As demais tasks todos contribuíram.
  ## ✍️Guias De Uso / Funcionalidades - Prompt

* **Após executar o "python main.py", irá aparecer as personalidade e qual o usuário pode escolher.**

<img width="433" height="147" alt="image" src="https://github.com/user-attachments/assets/ee05c6bf-b5d9-4dbb-8a54-50975f999fda" />

* **Após a sua escolha de personalidade, o EcoBot mostrará as 5 interações anteriores, junto com as perguntas mais frequentes.**

<img width="998" height="395" alt="image" src="https://github.com/user-attachments/assets/d750c91c-7967-4c02-bb3e-3e02274e27bf" />

* **Exemplos de uso da personalidade "engracada" após digitar "Olá"**

<img width="996" height="272" alt="image" src="https://github.com/user-attachments/assets/d14d97ef-48a3-417b-9338-ce759bea3206" />

* **Caso o usuário queira mudar a personalidade durante a execução do bot, ele deve digitar algo relacionado a "Mudar personalidade", e logo após aparecerá a escolha inical de personalidade do EcoBot, segue o exemplo:**

<img width="447" height="187" alt="image" src="https://github.com/user-attachments/assets/53f97014-276f-40ae-903b-f382b6a4c746" />

* **Após o usuário terminar suas internações, e escrevera palavra "sair" (ou palavras relacionadas a se despedir) o ChatBot irá gerar um resumo das interações do usuário com o ChatBot**

* Você pode acessar esse relatório que ficará salvo dentro da pasta responses em um arquivo .txt

<img width="761" height="158" alt="image" src="https://github.com/user-attachments/assets/8255840d-88f9-40ad-8bfc-97a5997f33c6" /> 

* **Relatório Gerado:**

<img width="263" height="177" alt="image" src="https://github.com/user-attachments/assets/cb9f72e1-f6bf-43b4-afca-31e18694775a" />

***


## ✍️Guias De Uso / Funcionalidades - Interface

* **No canto superior esquerdo, o usuário pode estar alterando a personalidade do bot para engraçada,formal ou rude. (Segue objeto citado circundado de vermelho na imagem)**
<img width="1436" height="600" alt="fotopersonc" src="https://github.com/user-attachments/assets/f3ec0db9-7023-480e-8bbf-ea98abe95658" />

* **Ao lado esquerdo o EcoBot mostrará as 5 interações anteriores.**

<img width="1417" height="600" alt="interações" src="https://github.com/user-attachments/assets/105c2142-a3fe-49e7-a2f5-0465bad1377f" />

* **Na parte de conversa com o bot, o usuário deve colocar sua pergunta na lacuna escrita "Digite sua pergunta" (circundado de vermelho na foto abaixo)**

* **Logo após a interação aparecerá um bloco com o nome "Pergunta: "sua pergunta" " (circundado de verde na foto abaixo)**

* **Depois, aparecerá a resposta do EcoBot. (circundado de amarelo na foto abaixo)**


<img width="1295" height="749" alt="conversas" src="https://github.com/user-attachments/assets/1069652e-1f67-433d-8d9b-d972b0dc2f5a" />



* **Ao clicar na lacuna escrita com "💡 Ver sugestões de perguntas" o bot baixará uma aba com as perguntas frequentes realizadas pelo usuário, o usuário pode clicar na pergunta frequente e o bot o responderá** (circundado de azul na foto abaixo)


<img width="1428" height="600" alt="sugestao" src="https://github.com/user-attachments/assets/c484c489-44b5-4571-b723-d8fec856de3c" />


* **No canto inferior esquerdo, haverá um ícone de uma lixeira que serve para limpar a conversa após o usuário clicar nela.(seguue na foto abaixo)**


<img width="1419" height="771" alt="limparconversa" src="https://github.com/user-attachments/assets/033aeed9-e21d-413e-af2a-7e1e73cdf3b5" />


* **Após limpar a conversa, será limpa a interação no chat com o bot(segue na foto)**


<img width="1275" height="759" alt="conversa limpa" src="https://github.com/user-attachments/assets/b901bb8e-c3e2-468b-8b7a-b871f89063e8" />


* **No canto inferior esquerdo, acima do ícone da lixeira, há um ícone de um Disket seguido com a frase "Salvar conversa"**



<img width="1416" height="787" alt="salvar conversa" src="https://github.com/user-attachments/assets/e6798589-222d-4399-9b0a-c9d1beb26771" />

* **Após o usuário clicar em salvar, aparecer a interação do usuário na parte de Downloads (destacado em verde na foto abaixo)**

<img width="1058" height="813" alt="conversasalva" src="https://github.com/user-attachments/assets/6599d2fc-6d40-407f-bd54-72488e8b94b9" />

* **o .txt gerado:**

<img width="546" height="107" alt="image" src="https://github.com/user-attachments/assets/abe64109-1c02-4160-9b2a-e7b7376f3789" />

* **Caso o usuário pergunte algo que o bot não saiba, ele entrará no modo aprendizado. No qual o usuário pode digitar uma resposta e ensiná-lo, ou não. Ao clicar em "ensinar" o bot aprende uma resposta para aquela pergunta (circulado em azul na foto abaixo) E ao clicar em "Esquecer" o bot desconsidera o aprendizado.(Circulado de verde na foto abaixo)**

<img width="941" height="540" alt="aprendizado" src="https://github.com/user-attachments/assets/a67c7012-8963-4983-bf6a-f4c7a8e5cf47" />

## 📜 Licença

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
