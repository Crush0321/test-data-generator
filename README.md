# 测试数据生成工具 (Test Data Generator)

一个用Python编写的高性能测试数据生成工具，支持生成上万条CSV格式的测试数据。

## 功能特性

- 高性能生成：10,000条数据仅需0.1秒，平均速度90,000+条/秒
- 支持大数据量：可轻松生成百万级数据，支持分批次写入避免内存溢出
- 丰富的数据类型：支持中文姓名、手机号、邮箱、国籍等200+国家数据
- 灵活配置：通过配置文件自定义生成规则和字段
- 标准CSV输出：生成的CSV文件可直接用于测试导入

## 支持的字段

| 字段名 | 说明 | 示例 |
|--------|------|------|
| identityType | 身份类型(1-4随机) | 2 |
| identityNo | 唯一标识 | test782343510001 |
| name | 中文姓名 | 张三 |
| sex | 性别(1男/2女) | 1 |
| loginType | 登录类型(1-3随机) | 3 |
| mobile | 中国大陆手机号 | 13812345678 |
| email | 随机邮箱地址 | 张三123@qq.com |
| smsCode | 验证码(30%概率为空) | 123456 |
| password | 密码(默认123456) | 123456 |
| rePassword | 确认密码 | 123456 |
| companyCn | 中文公司名称 | 张三科技有限公司 |
| companyEn | 英文公司名称(默认空) | |
| openid | OpenID(20%概率为空) | openid_a1b2c3d4e5f6g |
| nationality | 国籍代码 | CHN |
| nationalityCn | 国籍中文名 | 中国 |
| nationalityEn | 国籍英文名 | China |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置生成参数

编辑 `config.py` 文件：

```python
TOTAL_RECORDS = 10000    # 生成总条数
CHUNK_SIZE = 10000       # 每批写入大小（大数据量时建议50000）
OUTPUT_DIR = './output'  # 输出目录
```

### 3. 运行生成

```bash
python main.py
```

## 使用示例

### 生成10万条数据

```python
# config.py
TOTAL_RECORDS = 100000
CHUNK_SIZE = 50000
```

### 自定义字段规则

在 `config.py` 的 `FIELD_RULES` 中配置：

```python
FIELD_RULES = {
    'identityType': {'type': 'enum', 'values': [1, 2, 3, 4]},
    'name': {'type': 'chinese_name'},
    'mobile': {'type': 'mobile'},
    'email': {'type': 'email'},
    # ... 更多字段
}
```

## 项目结构

```
test-data-generator/
├── main.py              # 主入口文件
├── config.py            # 配置文件
├── requirements.txt     # 依赖声明
├── README.md            # 项目说明
├── .gitignore           # Git忽略文件
└── src/
    ├── __init__.py
    ├── generator.py     # 核心数据生成器
    ├── nationalities.py # 国籍数据(200+国家)
    └── csv_writer.py    # CSV文件写入器
```

## 性能测试

| 数据量 | 耗时 | 平均速度 |
|--------|------|----------|
| 1万条 | 0.11秒 | 92,434条/秒 |
| 10万条 | ~1秒 | ~90,000条/秒 |
| 100万条 | ~10秒 | ~90,000条/秒 |

## 输出示例

```csv
identityType,identityNo,name,sex,loginType,mobile,email,smsCode,password,rePassword,companyCn,companyEn,openid,nationality,nationalityCn,nationalityEn
2,test782343510001,陈二,1,3,13419601142,周六345@126.com,,123456,123456,吴明科技有限公司,,,GNB,几内亚比绍,Guinea-Bissau
1,test782343510002,卫三,1,3,13273763218,赵六414@163.com,,123456,123456,李四信息技术,,,ZAF,南非,South Africa
```

## 许可证

MIT License