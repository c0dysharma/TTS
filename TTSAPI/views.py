from os import path
from urllib import response
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from TTSAPI.models import TransformationInfo
from TTSAPI.tasks import transform_task as transform


class TTSView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        # print(response)
        # print(TTS().list_models().list_datasets())
        body = request.data
        text = body['text']

        file_name = str(uuid.uuid4())+'.wav'
        output_filepath = path.join('./', file_name)

        obj = TransformationInfo.objects.create(
            text=text,
            output_filepath=output_filepath)

        transform.generate_tts.delay(obj.id)
        return Response('Working')
