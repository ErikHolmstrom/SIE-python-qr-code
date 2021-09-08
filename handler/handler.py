# from pdf2image import convert_from_path
# from qrtools import qrtools
# import zbar
#
# def get_local_test_file():
#
#     url = 'D:/dev/qr-code-test-files/Faktura1.pdf'
#     poppler = "D:/dev/poppler-20.12.1/bin"
#
#     pages = convert_from_path(url, 500, poppler_path=poppler)
#     return pages
#
# def get_file_from_s3():
#     return None
#     #bucketname = event['Records']
#     # for record in event['Records']:
#     #     try:
#     #         download_bucket_name = record['s3']['bucket']['name']
#     #
#     #     except:
#     # #Something here
#
#
# pages = get_local_test_file()
# qr_data = None
# qr = qrtools.QR()
#
# for page in pages:
#    qr.decode(page)
#
#     # qr = qrtools.QR(page)
#     # qr_data = qr.data
#
# print(qr_data)


from pdf2image import convert_from_path
from pyzbar import pyzbar


def get_local_test_file():

    url = 'D:/dev/qr-code-test-files/Faktura1.pdf'
    poppler = "D:/dev/poppler-20.12.1/bin"

    pages = convert_from_path(url, 500, poppler_path=poppler)
    return pages

def get_file_from_s3():
    return None
    #bucketname = event['Records']
    # for record in event['Records']:
    #     try:
    #         download_bucket_name = record['s3']['bucket']['name']
    #
    #     except:
    # #Something here




pages = get_local_test_file()
qr_data = None

for page in pages:
    qr_data = pyzbar.decode(page)

print(qr_data)


