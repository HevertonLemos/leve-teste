from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import User, Salaries
from api.serializers import UserSerializer, SalariesSerializer


# basic CRUD
class UserListViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SalariesListViewSet(generics.ListCreateAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer


class SalariesEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer


# A média dos salários
class SalaryAverageViewset(APIView):

    def get(self, request):
        queryset = Salaries.objects.all()

        total = 0
        qtd = queryset.count()

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            for item in queryset:
                total += item.salary

            average = total/qtd

            return Response({'average': average, 'total': total, 'qtd': qtd})


class SalaryAverageUserView(APIView):

    def get(self, request, pk=None):
        queryset = Salaries.objects.all()

        total = 0
        qtd = queryset.filter(cpf=str(pk)).count()

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            for item in queryset.filter(cpf=str(pk)):
                total += item.salary

            average = total/qtd

            return Response({'average': average, 'total': total, 'qtd': qtd})


# A média dos descontos discount
class AverageDiscountViewset(APIView):

    def get(self, request):
        queryset = Salaries.objects.all()

        total = 0
        qtd = queryset.count()

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            for item in queryset:
                total += item.discount

            average = total/qtd

            return Response({'average': average, 'total': total, 'qtd': qtd})


class AverageDiscountUserView(APIView):

    def get(self, request, pk=None):
        queryset = Salaries.objects.all()

        total = 0
        qtd = queryset.filter(cpf=str(pk)).count()

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            for item in queryset.filter(cpf=str(pk)):
                total += item.discount

            average = total/qtd

            return Response({'average': average, 'total': total, 'qtd': qtd})


# O maior salário
class BigestSalaryViewset(APIView):

    def get(self, request):
        queryset = Salaries.objects.all()

        salary = 0
        qtd = queryset.count()
        user = None

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            for item in queryset:
                if item.salary > salary:
                    salary = item.salary
                    user = item
            serializer = SalariesSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class BigestSalaryUserView(APIView):

    def get(self, request, pk=None):
        queryset = Salaries.objects.all()

        salary = 0
        qtd = queryset.filter(cpf=str(pk)).count()
        user = None

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            for item in queryset.filter(cpf=str(pk)):
                if item.salary > salary:
                    salary = item.salary
                    user = item
            serializer = SalariesSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)


# O menor salário
class LowestSalaryViewset(APIView):

    def get(self, request):
        queryset = Salaries.objects.all()

        salary = 0
        qtd = queryset.count()
        user = None

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            salary = queryset.first().salary
            user = queryset.filter().first()
            for item in queryset:
                if item.salary < salary:
                    salary = item.salary
                    user = item
            serializer = SalariesSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class LowestSalaryUserView(APIView):

    def get(self, request, pk=None):
        queryset = Salaries.objects.all()

        salary = 0
        qtd = queryset.filter(cpf=str(pk)).count()
        user = None

        if qtd == 0:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            salary = queryset.filter(cpf=str(pk)).first().salary
            user = queryset.filter(cpf=str(pk)).first()
            for item in queryset.filter(cpf=str(pk)):
                if item.salary < salary:
                    salary = item.salary
                    user = item
            serializer = SalariesSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
