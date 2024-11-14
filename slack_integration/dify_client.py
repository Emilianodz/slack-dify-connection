# slack_integration/dify_client.py
import requests
import os

dify_url = os.getenv("DIFY_URL")
dify_token = os.getenv("DIFY_API_TOKEN")

def query_dify(prompt):
    headers = {
        "Authorization": f"Bearer {dify_token}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": {},
        "query": prompt,
        "user": "abc-123"
    }
    
    try:
        response = requests.post(dify_url, headers=headers, json=data)
        response.raise_for_status()
        
        # Extraer y devolver solo el campo "answer" de la respuesta
        response_data = response.json()
        print("Respuesta completa de Dify:", response_data)
        
        return response_data.get("answer", "Sin respuesta")
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar Dify: {e}")
        return "Error al procesar la solicitud con Dify"
