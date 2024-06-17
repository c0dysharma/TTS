import os
from celery import shared_task
import torch
from TTS.api import TTS

from TTSAPI.clients.boto import s3
from TTSAPI.models import TransformationInfo

device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "tts_models/en/ljspeech/fast_pitch"
tts = TTS(model_name=model_name,
          progress_bar=True).to(device)


@shared_task()
def generate_tts(transformationJobId):
    bucket = 'ttsed'
    try:
        job = TransformationInfo.objects.get(pk=transformationJobId)
        job.status = TransformationInfo.Status.PROCESSING
        job.model_used = model_name
        job.save()

        tts.tts_to_file(job.text, file_path=job.output_filepath)

        # after generation of file upload to s3
        with open(job.output_filepath, 'rb') as data:
            file_name = job.output_filepath.split('/')[-1]
            s3.Bucket(bucket).put_object(Key=file_name, Body=data)

        # delete file from server
        os.remove(job.output_filepath)

        job.status = TransformationInfo.Status.COMPLETED
        job.s3_url = os.path.join(bucket, file_name)
        job.save()
        return job.output_filepath
    except Exception as e:
        print(e)

        job.status = TransformationInfo.Status.FAILED
        job.save()
        return None
