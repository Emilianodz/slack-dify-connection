# slack_integration/views.py
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .slack_client import send_message
from .dify_client import query_dify
import os

BOT_USER_ID = os.getenv("SLACK_BOT_USER_ID")

def home(request):
    return HttpResponse("¡Servidor Django está funcionando!")

@csrf_exempt
def slack_events(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("Evento recibido:", data)
        
        # Detectar y responder a la verificación de URL de Slack
        if data.get("type") == "url_verification":
            return JsonResponse({"challenge": data.get("challenge")})

        # Continuar con el procesamiento normal de eventos
        if data.get("type") == "event_callback":
            event = data.get("event", {})
            
            if event.get("type") == "app_mention":
                if "bot_id" in event:
                    print("Mensaje enviado por el bot, ignorado.")
                    return JsonResponse({"status": "Ignorado mensaje del bot"})
                
                channel = event.get("channel")
                user_message = event.get("text")

                # Procesar el comando con Dify y utilizar la respuesta directamente
                answer_text = query_dify(user_message)
                
                # Envía la respuesta al canal de Slack
                send_message(channel=channel, text=answer_text)
                
                return JsonResponse({"status": "Mensaje procesado"})
        
        return JsonResponse({"message": "Evento recibido correctamente"})
    return JsonResponse({"error": "Método no permitido"}, status=405)
