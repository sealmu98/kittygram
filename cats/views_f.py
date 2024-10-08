from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    # В случае POST-запроса добавим список записей в БД
    if request.method == 'POST':
        # Создаём объект сериализатора
        # и передаём в него данные из POST-запроса
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            # Если полученные данные валидны —
            # сохраняем данные в базу через save().
            serializer.save()
            # Возвращаем JSON со всеми данными нового объекта
            # и статус-код 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные не прошли валидацию —
        # возвращаем информацию об ошибках и соответствующий статус-код:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # В случае GET-запроса возвращаем список всех котиков
    # Получаем все объекты модели
    cats = Cat.objects.all()
    # Передаём queryset в конструктор сериализатора
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def cat_detail(request, pk):
    # Получаем объект Cat по pk
    cat = Cat.objects.get(pk=pk)

    # В случае PUT или PATCH-запроса обновляем объект Cat
    if request.method == 'PUT' or request.method == 'PATCH':
        # Создаём объект сериализатора с данными из запроса
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            # Если полученные данные валидны — сохраняем изменения
            serializer.save()
            # Возвращаем JSON со всеми данными обновлённого объекта
            # и статус-код 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Если данные не прошли валидацию —
        # возвращаем информацию об ошибках и соответствующий статус-код:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # В случае DELETE-запроса удаляем объект Cat
    elif request.method == 'DELETE':
        cat.delete()
        # Возвращаем пустой ответ с статус-кодом 204
        return Response(status=status.HTTP_204_NO_CONTENT)

    # В случае GET-запроса возвращаем данные объекта Cat
    serializer = CatSerializer(cat)
    return Response(serializer.data)
