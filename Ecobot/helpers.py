import os
import json
from typing import Dict, Any

# --- Constantes e Helpers ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_response_path(filename: str) -> str:
    """Cria o caminho completo para um arquivo de resposta."""
    return os.path.join(BASE_DIR, "responses", filename)

def read_json_file(path: str) -> Dict[str, Any]:
    """Lê um arquivo JSON de forma segura, retornando {} em caso de erro."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def write_json_file(path: str, data: Dict[str, Any]):
    """Escreve dados em um arquivo JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- Lógica Principal ---

def load_personalities() -> Dict[str, Any]:
    """Carrega as personalidades a partir do arquivo questions.json."""
    questions_data = read_json_file(get_response_path("questions.json"))
    if not questions_data:
        raise FileNotFoundError("Arquivo questions.json não encontrado ou inválido.")

    # Dicionário para armazenar os dados de cada personalidade
    personalities_data = {
        'funny': {'name': 'Ecobot-funny', 'responses': {}},
        'education': {'name': 'Ecobot-education', 'responses': {}},
        'rude': {'name': 'Ecobot-rude', 'responses': {}}
    }
    keywords = {}

    # Preenche os dados de resposta e palavras-chave
    for question, details in questions_data.items():
        keywords[question] = details.get('keywords', [])
        personalities_data['funny']['responses'][question] = details.get('engracada', [])
        personalities_data['education']['responses'][question] = details.get('formal', [])
        personalities_data['rude']['responses'][question] = details.get('rude', [])

    # Adiciona as palavras-chave a cada personalidade
    for p_key in personalities_data:
        personalities_data[p_key]['keywords'] = keywords
        
    return personalities_data

def save_learning_response(question: str, answer: str):
    """Carrega as respostas aprendidas, adiciona uma nova e salva o arquivo."""
    path = get_response_path("learning_responses.json")
    data = read_json_file(path)
    data[question] = answer
    write_json_file(path, data)

# --- Execução ---
personalidades = load_personalities()
