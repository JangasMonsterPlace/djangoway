# Base and Django imports
# Third party imports
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework import pagination, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
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