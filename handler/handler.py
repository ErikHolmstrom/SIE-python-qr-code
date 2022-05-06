#
# Use example: python3 handler.py [name_of_content] access_key_id access_key_secret eu-west-1 bucket
#

import sys
import json

# [1] List of ids for the contents in the AWS bucket to get information on
from QrCodeReader import QrCodeReader

CONTENT_ID_LIST = eval(sys.argv[1])

# [2] Access key id to AWS
AWS_ACCESS_KEY_ID = sys.argv[2]

# [3] Access key secret to AWS
AWS_SECRET_ACCESS_KEY = sys.argv[3]

# [4] name of the AWS region tp use (e.g. "eu-west-1")
REGION_NAME = sys.argv[4]

# [5] aws bucket name to use
BUCKET_NAME = sys.argv[5]

# Set this Path to where you have poppler installed
POPPLER_PATH = "D:/dev/poppler-20.12.1/bin"


print("Content ids: " + str(CONTENT_ID_LIST))
print("Access key: " + AWS_ACCESS_KEY_ID + ", " + AWS_SECRET_ACCESS_KEY)
print("Region: " + REGION_NAME)
print("Bucket: " + BUCKET_NAME)


qr_reader = QrCodeReader(
    CONTENT_ID_LIST,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    REGION_NAME,
    BUCKET_NAME,
    POPPLER_PATH
)
result = qr_reader.process()
print(json.dumps([ob.__dict__ for ob in result]))
