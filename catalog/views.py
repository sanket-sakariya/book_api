from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from .decorators import require_api_key
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return require_api_key(_create_book)(request)

@require_api_key
def _create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        return require_api_key(_update_book)(request, book)

    elif request.method == 'DELETE':
        return require_api_key(_delete_book)(request, book)

@require_api_key
def _update_book(request, book):
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@require_api_key
def _delete_book(request, book):
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@require_api_key
@parser_classes([MultiPartParser])
def upload_cover(request, pk):
    book = get_object_or_404(Book, pk=pk)
    file = request.FILES.get('cover')

    if not file:
        return Response({"error": "NO_FILE", "message": "No file provided"}, status=400)

    if file.size > 2 * 1024 * 1024:
        return Response({"error": "FILE_TOO_LARGE", "message": "Max size is 2MB"}, status=413)

    if file.content_type not in ['image/jpeg', 'image/png', 'image/webp']:
        return Response({
            "error": "INVALID_FILE_TYPE",
            "message": "Only JPG, PNG, and WEBP files are allowed",
            "allowed_types": ["jpg", "png", "webp"],
            "received_type": file.content_type.split("/")[-1]
        }, status=400)

    book.cover_image = file
    book.save()
    return Response({
        "id": book.id,
        "title": book.title,
        "cover_url": request.build_absolute_uri(book.cover_image.url),
        "message": "Cover uploaded successfully"
    }, status=200)
