# ♻️ EcoBot – ChatBot Instrutor de Reciclagem

| Equipe                               | GitHub           |
|-------------------------------------|------------------|
| Leôncio Ferreira Flores Neto        | [@leoncioferreira-ufca](https://github.com/leoncioferreira-ufca)|
| Alan Mendes Vieira                  | [@alan-mendes-ufca](https://github.com/alan-mendes-ufca)         |
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


# Estrutura de Diretórios do EcoBot

```bash
Eco-bot/
│
├── classes/ # Núcleo do chatbot
│ ├── chatbot.py # Classe principal e lógica do chatbot
│ ├── chatbot_analytics.py # Coleta e análise de métricas
│ ├── chatbot_frequent_questions.py # Perguntas frequentes pré-definidas
│ ├── chatbot_memory.py # Gerenciamento de memória e histórico
│ └── chatbot_report.py # Geração de relatórios automáticos
│
├── chatbot_data/ # Armazenamento de dados e histórico
│ ├── history.txt # Histórico de interações
│ ├── learning_responses.json # Respostas aprendidas dinamicamente
│ ├── questions.json # Banco de perguntas e respostas
│ └── relatorio.txt # Saída de relatórios gerados
│
├── helpers.py # Funções auxiliares reutilizáveis
├── main.py # Ponto de entrada do projeto
├── requirements.txt # Dependências do projeto (pip install -r requirements.txt)
└── README.md # Documentação do projeto
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
