import json
from rest_framework.generics import GenericAPIView,ValidationError
from bank.serializer import BankSerializer, BankListSerializer
import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from .models import Bank


class Bankdetails(GenericAPIView):

    serializer_class = BankSerializer

    def get_queryset(self):
        return Bank.objects.all()

    def post(self,request):
        branch = str.upper(request.POST.get('branch'))
        ifsc = str.upper(request.POST.get('ifsc'))
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            path = "https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv"
            data = pd.read_csv(path)
            try:
                detail = data[(data.ifsc == ifsc) & (data.branch == branch)]
                return Response(detail, status=status.HTTP_200_OK)
            except ValidationError as e:
                return  Response(str(e),status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)

class Banklistdetails(GenericAPIView):

    serializer_class = BankListSerializer

    def get_queryset(self):
        return Bank.objects.all()

    def post(self,request):
        name = str.upper(request.POST.get('bank_name'))
        city = str.upper(request.POST.get('city'))
        serializer = BankListSerializer(data=request.data)
        if serializer.is_valid():
            path = "https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv"
            data = pd.read_csv(path)
            try:
                detail = data[(data.city == city) & (data.bank_name == name)]
                data=[]
                i=0
                for j in detail:
                    data.append(
                        {
                            "ifsc":detail.ifsc[i],
                            "bank_id":detail.bank_id[i],
                            "branch":detail.branch[i],
                            "address":detail.address[i],
                            "city":detail.city[i],
                            "district":detail.district[i],
                            "state":detail.state[i],
                            "bank_name":detail.bank_name[i],
                         }
                    )
                    i +=1
                return Response(data, status=status.HTTP_200_OK)
            except ValidationError as e:
                return  Response(str(e),status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)
