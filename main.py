import time
from src.generator import DataGenerator
from src.csv_writer import CsvWriter
from src.nationalities import NATIONALITIES
from config import TOTAL_RECORDS, CHUNK_SIZE, OUTPUT_DIR


def main():
    print('=== 测试数据生成工具 ===')
    print(f'配置信息:')
    print(f'  - 生成记录数: {TOTAL_RECORDS:,} 条')
    print(f'  - 每批大小: {CHUNK_SIZE:,} 条')
    print(f'  - 输出目录: {OUTPUT_DIR}')

    start_time = time.time()

    generator = DataGenerator()
    writer = CsvWriter(OUTPUT_DIR)

    files = writer.write_in_chunks(generator, TOTAL_RECORDS, CHUNK_SIZE, NATIONALITIES)

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print(f'\n=== 生成完成 ===')
    print(f'生成文件: {", ".join(files)}')
    print(f'耗时: {duration} 秒')
    print(f'平均速度: {int(TOTAL_RECORDS / (end_time - start_time))} 条/秒')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'生成失败: {e}')
        import traceback
        traceback.print_exc()
        exit(1)