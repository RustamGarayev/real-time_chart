import decimal
import json
from datetime import date, datetime


class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)

        if isinstance(o, (datetime, date)):
            return o.strftime('%Y-%m-%d')

        return super(JsonEncoder, self).default(o)
