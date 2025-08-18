from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events


class EventsApi(APIView):
	def get(self, request):
		events = Events.objects.all()
		events_list = []
		for e in events:
			events_doc = {
				'id': e.id,
				'title': e.title,
				'description': e.description,
				'date': e.date,
				'lieu': e.lieu,
				'nbPlace': e.nbPlace,
				'prix': e.prix
			}
			events_list.append(events_doc)
		return Response(events_list)

	def post(self, request):
		print(request.data)

		new_events = Events(title=request.data['title'],
							description=request.data['description'],
							date=request.data['date'],
							lieu=request.data['lieu'],
							nbPlace=request.data['nbPlace'],
							prix=request.data['prix'])
		new_events.save()

		return Response("Api de test pour les events")
	