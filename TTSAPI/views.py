from os import path
import uuid
from TTS.api import TTS

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from TTSAPI.models import TransformationInfo
from TTSAPI.serializers.transformationInfo_serializer import TransformationInfoSerializer
from TTSAPI.tasks import transform_task as transform

from TTSAPI.clients.boto import s3
from TTSAPI.utils.s3 import create_presigned_url


class TTSView(APIView):
    def post(self, request):
        body = request.data
        text = body['text']

        file_name = str(uuid.uuid4())+'.wav'
        output_filepath = path.join('./', file_name)

        obj = TransformationInfo.objects.create(
            text=text,
            output_filepath=output_filepath)

        transform.generate_tts.delay(obj.id)
        return Response(TransformationInfoSerializer(obj).data)

    def get(self, request):
        models = TTS().list_models().list_models()
        return Response(models)


class TTSJobView(APIView):
    def get(self, request, pk):
        job = get_object_or_404(TransformationInfo, pk=pk)
        return Response(TransformationInfoSerializer(job).data)


class TTSDownloadView(APIView):
    def get(self, request, pk):
        job = get_object_or_404(TransformationInfo, pk=pk)
        s3_url = job.s3_url

        # stream the s3 file here
        pre_signed_url = create_presigned_url(s3_url, 60)

        return Response(pre_signed_url)
