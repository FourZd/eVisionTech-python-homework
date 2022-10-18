from rest_framework.views import APIView
from rest_framework.response import Response
from .data import obtain_data

class GetDirContent(APIView):
    """
    View to see all files and folders in the directory.
    """
    def get(self, format=None):
        data = obtain_data.get_data() # check data.py for more info
        return Response(data) # returning API with data