from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProgrmmingCard
from.serialzer import ProgrammingCardSerializer


@api_view(['GET'])
def GetCards(request):
    # Simulating a database query
    allObj = ProgrmmingCard.objects.all()
    serializer = ProgrammingCardSerializer(allObj, many=True)
    cards = [
        {
            "id": 1,
            "name": "Card 1",
            "description": "This is a sample card."
        },
        {
            "id": 2,
            "name": "Card 2",
            "description": "Another sample card."
        }
    ]

    # Returning the cards as a JSON response
    return Response(cards)

@api_view(["post"])
def CreateCard(request):
    name = request.data.get("name")
    description = request.data.get("description")
    print(
        f"Name: {name}, Description: {description}"
    )
    card = ProgrmmingCard(name=name, description=description)
    card.save()
    return Response("Done")





