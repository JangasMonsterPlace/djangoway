# Base and Django imports
# Third party imports
from importlib.resources import path
import requests
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework.decorators import api_view
from rest_framework import pagination, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser

import pandas as pd
import humps

# Local imports
from .models import CSV
from .serializers import GenericCSVSerializer 
from utils.Paginator import CustomPagination


class CSVViewset(viewsets.ModelViewSet):
    queryset = CSV.objects.all()
    serializer_class = GenericCSVSerializer
    pagination_class = CustomPagination
    parser_classes = [MultiPartParser ]

    def create(self, request):
        """
        Request header needs to be set to 'multipart/form-data' and it is only accepting form data
        """
        # Extract the file from the request
        file = request.data['file']
        df = pd.DataFrame(file)
        # Preprocess the file
        preprocessed_data = {}
        preprocessed_data['origin'] = request.data['origin']
        preprocessed_data['average_rating'] = df[request.data['rating']].mean()
        preprocessed_data['average_length'] = df[request.data['average_length']].mean()


        # Save preprocessed data to CSV model
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Save the file to gcp

        # Return the preprocessed data
        return Response(status=status.HTTP_201_CREATED)


def make_groupquery_string(groups):
    """
    This function takes a list of groups and returns a string that can be used in a query
    """
    query_string = ''
    for group in groups:
        query_string += f"group={group}&" 
    return query_string[:-1]


@api_view(['GET'])
def get_csv_list(request):
    r = requests.get('https://us-central1-easy-as-pie-hackathon.cloudfunctions.net/get_sources')
    data = r.json()
    res = humps.camelize(data)
    return Response(status=status.HTTP_200_OK, data=res)

@api_view(['GET'])
def get_date_range(request):
    query_params = request.query_params
    groups= make_groupquery_string(query_params.getlist('group'))
    r = requests.get(f'https://us-central1-easy-as-pie-hackathon.cloudfunctions.net/get_source_date_range?{groups}&source_type=csv')
    data = r.json()
    res = humps.camelize(data)
    return Response(status=status.HTTP_200_OK, data=res)


@api_view(['GET'])
def get_job_summary(request):
    query_params = request.query_params
    groups= make_groupquery_string(query_params.getlist('group'))
    min_date = query_params.get('min_date')
    max_date = query_params.get('max_date')
    r = requests.get(f'https://us-central1-easy-as-pie-hackathon.cloudfunctions.net/get_review_count?{groups}&source_type=csv&min_date={min_date}&max_date={max_date}')
    data = r.json()
    res = humps.camelize(data)
    return Response(status=status.HTTP_200_OK, data=res)
