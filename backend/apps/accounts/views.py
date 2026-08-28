import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


CATEGORY_RESPONSES = {
	"cardiologia": {
		"label": "Cardiologia",
		"keywords": ("cardiologia", "coração", "coracao", "pressão", "pressao", "infarto", "arritmia", "colesterol"),
		"response": "Cardiologia estuda o coração e a circulação. Dúvidas comuns envolvem pressão arterial, colesterol e ritmo cardíaco. Para uma orientação individual, procure um profissional de saúde e leve seus exames e medicamentos em uso.",
	},
	"neurologia": {
		"label": "Neurologia",
		"keywords": ("neurologia", "cabeça", "cabeca", "enxaqueca", "memória", "memoria", "convulsão", "convulsao", "nervo", "tontura"),
		"response": "Neurologia aborda o cérebro, a medula e os nervos. Sintomas como dor de cabeça recorrente, alterações de memória ou tontura merecem avaliação clínica, especialmente quando são novos ou persistentes.",
	},
	"ortopedia": {
		"label": "Ortopedia",
		"keywords": ("ortopedia", "osso", "ossos", "joelho", "coluna", "fratura", "articulação", "articulacao", "músculo", "musculo", "dor nas costas"),
		"response": "Ortopedia cuida de ossos, músculos, articulações e movimento. Dor persistente, perda de força, inchaço ou limitação para se movimentar devem ser avaliados por um profissional.",
	},
}

URGENT_KEYWORDS = ("falta de ar", "dor no peito", "desmaio", "convulsão", "convulsao", "sangramento intenso", "fraqueza súbita", "fraqueza subita")


def _find_category(message):
	for category, content in CATEGORY_RESPONSES.items():
		if any(keyword in message for keyword in content["keywords"]):
			return category
	return None


@csrf_exempt
def encyclopedia_chat(request):
	if request.method != "POST":
		return JsonResponse({"error": "Envie uma pergunta usando POST."}, status=405)

	message = str(request.POST.get("message", "")).strip().lower()
	if not message:
		return JsonResponse({"error": "Digite uma pergunta para começar."}, status=400)
	if len(message) > 500:
		return JsonResponse({"error": "Sua pergunta deve ter até 500 caracteres."}, status=400)

	if any(keyword in message for keyword in URGENT_KEYWORDS):
		response = "Os sinais que você descreveu podem exigir atendimento imediato. Procure um pronto atendimento ou ligue para o SAMU (192). Não espere uma resposta do autoatendimento."
		category = "Atenção imediata"
	else:
		category = _find_category(message)
		if category:
			response = CATEGORY_RESPONSES[category]["response"]
			category = CATEGORY_RESPONSES[category]["label"]
		else:
			response = "Posso explicar temas de Cardiologia, Neurologia e Ortopedia. Conte sua dúvida de forma geral, sem compartilhar dados pessoais, ou escolha uma categoria abaixo."
			category = "Enciclopédia"

	return JsonResponse({"category": category, "response": response})
