import random
import time
import hashlib

CHINESE_NAMES = [
    '张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十',
    '刘一', '陈二', '杨三', '黄四', '赵五', '周六', '吴七', '郑八',
    '王九', '冯十', '陈一', '褚二', '卫三', '蒋四', '沈五', '韩六',
    '杨七', '朱八', '秦九', '尤十', '许一', '何二', '吕三', '施四',
    '张五', '孔六', '曹七', '严八', '华九', '金十', '魏一', '陶二'
]

FIRST_NAMES = [
    '张', '李', '王', '赵', '刘', '陈', '杨', '黄', '周', '吴',
    '徐', '孙', '马', '朱', '胡', '郭', '何', '林', '罗', '高'
]

LAST_NAMES = [
    '伟', '强', '敏', '静', '磊', '芳', '军', '洋', '娜', '亮',
    '明', '燕', '涛', '杰', '丽', '勇', '艳', '涛', '涛', '超'
]

DOMAINS = ['qq.com', '163.com', 'gmail.com', '126.com', 'sina.com', 'hotmail.com']


class DataGenerator:
    def __init__(self):
        self.counter = 0

    def set_counter(self, value):
        self.counter = value

    def random_int(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def random_item(self, arr):
        return random.choice(arr)

    def generate_identity_type(self):
        return 5

    def generate_identity_no(self):
        timestamp = str(int(time.time()))[-8:]
        return f"test{timestamp}{str(self.counter).zfill(4)}"

    def generate_name(self):
        if random.random() > 0.5:
            return self.random_item(CHINESE_NAMES)
        return self.random_item(FIRST_NAMES) + self.random_item(LAST_NAMES)

    def generate_sex(self):
        return self.random_int(0, 1)

    def generate_login_type(self):
        return self.random_int(1, 2)

    def generate_mobile(self):
        prefixes = ['131', '132', '133', '134', '135', '136', '137', '138', '139',
                    '150', '151', '152', '158', '159', '186', '187', '188', '170']
        prefix = self.random_item(prefixes)
        suffix = str(random.randint(0, 99999999)).zfill(8)
        return f"{prefix}{suffix}"

    def generate_email(self):
        name = self.generate_name()
        domain = self.random_item(DOMAINS)
        return f"{name}{random.randint(100, 999)}@{domain}"

    def generate_sms_code(self):
        if random.random() > 0.3:
            return ''
        return str(random.randint(0, 999999)).zfill(6)

    def generate_password(self):
        return '123456'

    def generate_company_cn(self):
        companies = ['测试公司', '科技有限公司', '信息技术', '软件开发', 
                     '数据服务', '互联网', '云计算', '人工智能']
        return f"{self.generate_name()}{self.random_item(companies)}"

    def generate_company_en(self):
        return ''

    def generate_openid(self):
        if random.random() > 0.2:
            return ''
        return f"openid_{hashlib.md5(str(time.time()).encode()).hexdigest()[:13]}"

    def generate_nationality(self, nationalities):
        return self.random_item(nationalities)

    def generate_row(self, nationalities):
        self.counter += 1
        nationality = self.generate_nationality(nationalities)
        
        return {
            'identityType': self.generate_identity_type(),
            'identityNo': self.generate_identity_no(),
            'name': self.generate_name(),
            'sex': self.generate_sex(),
            'loginType': self.generate_login_type(),
            'mobile': self.generate_mobile(),
            'email': self.generate_email(),
            'smsCode': self.generate_sms_code(),
            'password': self.generate_password(),
            'rePassword': self.generate_password(),
            'companyCn': self.generate_company_cn(),
            'companyEn': self.generate_company_en(),
            'openid': self.generate_openid(),
            'nationality': nationality['code'],
            'nationalityCn': nationality['cn'],
            'nationalityEn': nationality['en']
        }