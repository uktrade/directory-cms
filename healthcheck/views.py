from directory_healthcheck.views import BaseHealthCheckAPIView
from health_check.db.backends import DatabaseBackend
from rest_framework.response import Response
from rest_framework.views import APIView


from config.signature import SignatureCheckPermission


class DatabaseAPIView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return DatabaseBackend()


class PingAPIView(APIView):

    permission_classes = (SignatureCheckPermission, )
    http_method_names = ("get", )

    def get(self, request, *args, **kwargs):
        return Response(status=200)
