import json

import boto3
from pdf2image import convert_from_bytes
from pyzbar import pyzbar

from QrCodeContent import QrCodeContent


class QrCodeReader:
    """
     CONTENT_ID_LIST: List of ids for the contents in the AWS bucket to get information on
     AWS_ACCESS_KEY_ID: Access key id to AWS
     AWS_SECRET_ACCESS_KEY: Access key secret to AWS
     REGION_NAME: name of the AWS region tp use (e.g. "eu-west-1")
     BUCKET_NAME: aws bucket name to fetch the files to process from
     POPPLER_PATH: Set this Path to where you have poppler installed
    """
    def __init__(self, content_id_list, aws_access_key_id, aws_secret_access_key, region_name, bucket_name, poppler_path):
        self.CONTENT_ID_LIST = content_id_list
        self.AWS_ACCESS_KEY_ID = aws_access_key_id
        self.AWS_SECRET_ACCESS_KEY = aws_secret_access_key
        self.REGION_NAME = region_name
        self.BUCKET_NAME = bucket_name
        self.POPPLER_PATH = poppler_path

    def __get_session(self):
        return boto3.Session(
            region_name=self.REGION_NAME,
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY)

    def __get_file_bytes_from_s3(self, content_id):
        s3 = self.__get_session().resource("s3")
        s3_object = s3.Object(self.BUCKET_NAME, str(content_id))
        read_bytes = s3_object.get()['Body'].read()
        return read_bytes

    def process(self):
        parsed_contents = []
        for content_id in self.CONTENT_ID_LIST:
            read_bytes = self.get_file_bytes_from_s3(content_id)
            pages = convert_from_bytes(read_bytes, 500, poppler_path=self.POPPLER_PATH)

            qr_decoded = []
            for page in pages:
                qr_decoded = pyzbar.decode(page)
                # Break if a qr code was found
                if len(qr_decoded) > 0:
                    break

            # read the data if successfully decoded a qr code
            if len(qr_decoded) > 0:
                qr_data_string = qr_decoded[0].data.decode("utf-8")
                qr_data_json = json.loads(qr_data_string)

                qr_code_content = QrCodeContent(qr_data_json)
                parsed_contents.append(qr_code_content)

        return parsed_contents
