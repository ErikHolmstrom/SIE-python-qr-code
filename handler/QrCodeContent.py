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