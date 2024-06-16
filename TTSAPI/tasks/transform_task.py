import os
from celery import shared_task
import torch
from TTS.api import TTS

from TTSAPI.clients.boto import s3

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC",
          progress_bar=True).to(device)


@shared_task()
def generate_tts(text, file_path):
    try:
        tts.tts_to_file(text, file_path=file_path)

        # after generation of file upload to s3
        with open(file_path, 'rb') as data:
            file_name = file_path.split('/')[-1]
            s3.Bucket('ttsed').put_object(Key=file_name, Body=data)

        # delete file from server
        os.remove(file_path)
        return file_path
    except Exception as e:
        print(e)
        return None
