from TTSAPI.clients.boto import s3


def create_presigned_url(s3_path, expires_in):
    file_path = s3_path.split('/')
    response = s3.generate_presigned_url('get_object',
                                         Params={'Bucket': file_path[0],
                                                 'Key': file_path[1]},
                                         ExpiresIn=expires_in)
    return response
