from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note


@api_view(['GET']) # 'GET' decorator
def getRoutes(request):  # function based view 
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'Get',
            'body': None,
            'description': 'Return an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'Get',
            'body': None,
            'description': 'Return a single note object'
        },
        {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in PUT request'
        },
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETe',
            'body': None,
            'description': 'Deletes an existing note'
        }
    ]
    return Response(routes)  # save false means we can turn any kinds of data into json data


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()

    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )

    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(note, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(reqest, pk):
   note = Note.objects.get(id=pk)
   note.delete()
   
   return Response('Note was deleted')