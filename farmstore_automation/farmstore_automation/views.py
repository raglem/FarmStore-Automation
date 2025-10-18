from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from farmstore_automation.test import run_order_test

class TestOrderAPIView(APIView):
    # GET endpoint to run order test
    def get(self, request, format=None):
        # Run the order test and forward the result
        data = run_order_test()
        return Response(data, status=HTTP_200_OK)