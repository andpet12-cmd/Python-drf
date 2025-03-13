from rest_framework.response import Response
from rest_framework.views import APIView


class FirstView(APIView):
    def get(self, *args, **kwargs):
        print(self.request.query_params.dict())
        return Response({'message': 'hello from get'})

    def post(self, *args, **kwargs):
        print(self.request.query_params.dict())
        print(self.request.data)
        return Response({'message': 'hello from post'})

    def put(self, *args, **kwargs):
        return Response({'message': 'hello from put'})

    def patch(self, *args, **kwargs):
        return Response({'message': 'hello from patch'})

    def delete(self, *args, **kwargs):
        return Response({'message': 'hello from delete'})

class SecondView(APIView):
        def get(self, *args, **kwargs):
            print(kwargs)
            return Response(kwargs['age'])
