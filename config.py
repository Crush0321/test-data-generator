TOTAL_RECORDS = 10000
CHUNK_SIZE = 10000
OUTPUT_DIR = './output'

FIELD_RULES = {
    'identityType': {'type': 'enum', 'values': [1, 2, 3, 4]},
    'identityNo': {'type': 'pattern', 'pattern': 'test{timestamp}{counter}'},
    'name': {'type': 'chinese_name'},
    'sex': {'type': 'enum', 'values': [1, 2]},
    'loginType': {'type': 'enum', 'values': [1, 2, 3]},
    'mobile': {'type': 'mobile'},
    'email': {'type': 'email'},
    'smsCode': {'type': 'sms_code', 'nullable': True},
    'password': {'type': 'fixed', 'value': '123456'},
    'rePassword': {'type': 'fixed', 'value': '123456'},
    'companyCn': {'type': 'company_cn'},
    'companyEn': {'type': 'fixed', 'value': ''},
    'openid': {'type': 'openid', 'nullable': True},
    'nationality': {'type': 'nationality', 'format': 'code'},
    'nationalityCn': {'type': 'nationality', 'format': 'cn'},
    'nationalityEn': {'type': 'nationality', 'format': 'en'}
}

HEADERS = [
    'identityType', 'identityNo', 'name', 'sex', 'loginType', 'mobile',
    'email', 'smsCode', 'password', 'rePassword', 'companyCn', 'companyEn',
    'openid', 'nationality', 'nationalityCn', 'nationalityEn'
]