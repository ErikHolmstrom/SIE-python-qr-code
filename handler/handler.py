import json

import boto3
from pdf2image import convert_from_bytes
from pyzbar import pyzbar
import sys

# [0] List of ids for the contents in the AWS bucket to get informatio on
CONTENT_ID_LIST = sys.argv[0]

# [1] Access key id to AWS
AWS_ACCESS_KEY_ID = sys.argv[1]

# [2] Access key secret to AWS
AWS_SECRET_ACCESS_KEY = sys.argv[2]

# [3] name of the AWS region tp use (e.g. "eu-west-1")
REGION_NAME = sys.argv[3]

# [4] aws bucket name to use
BUCKET_NAME = sys.argv[4]

# Set this Path to where you have poppler installed
POPPLER_PATH = "D:/dev/poppler-20.12.1/bin"


class QrCodeContent:
    def __init__(self, qr_data_json):
        self.supplier_name = qr_data_json["nme"]
        self.supplier_registration_number = qr_data_json["cid"]
        self.invoice_number = qr_data_json["iref"]
        self.invoice_data = qr_data_json["idt"]
        self.due_date = qr_data_json["ddt"]
        self.price = qr_data_json["due"]
        self.vat = qr_data_json["vat"]
        self.currency = qr_data_json["cur"]
        self.partner = qr_data_json["pt"] # Like Bankgiro (BG)
        self.account_number = qr_data_json["acc"]


def get_session():
    return boto3.Session(
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def get_file_bytes_from_s3(content_id):
    s3 = get_session().resource("s3")
    s3_object = s3.Object(BUCKET_NAME, str(content_id))
    bytes = s3_object.get()['Body'].read()
    return bytes


def main():
    parsed_contents = []
    for content_id in CONTENT_ID_LIST:
        bytes = get_file_bytes_from_s3(content_id)
        pages = convert_from_bytes(bytes, 500, poppler_path=POPPLER_PATH)

        qr_decoded = []
        for page in pages:
            qr_decoded = pyzbar.decode(page)
            if len(qr_decoded) > 0:
                break

        if len(qr_decoded) > 0:
            qr_data_string = qr_decoded[0].data.decode("utf-8")
            qr_data_json = json.loads(qr_data_string)

            qr_code_content = QrCodeContent(qr_data_json)
            parsed_contents.append(qr_code_content)

    return parsed_contents

main()
