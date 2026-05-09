import os
import csv
from datetime import datetime


class CsvWriter:
    def __init__(self, output_dir='./output'):
        self.output_dir = output_dir
        self.ensure_dir(output_dir)

    def ensure_dir(self, dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

    def write(self, data, filename=None):
        timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        output_filename = filename or f'test_data_{timestamp}.csv'
        file_path = os.path.join(self.output_dir, output_filename)

        if data:
            headers = data[0].keys()
            
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
        
        return file_path

    def write_in_chunks(self, generator, total_records, chunk_size=10000, nationalities=None):
        timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        total_chunks = (total_records + chunk_size - 1) // chunk_size
        files = []

        print(f"\n开始生成 {total_records:,} 条数据，分 {total_chunks} 批处理...")

        for chunk in range(total_chunks):
            start = chunk * chunk_size
            end = min(start + chunk_size, total_records)
            current_chunk_size = end - start

            print(f"正在生成第 {chunk + 1}/{total_chunks} 批 ({start + 1}-{end})...")

            chunk_data = []
            for _ in range(current_chunk_size):
                chunk_data.append(generator.generate_row(nationalities))

            filename = f'test_data_{timestamp}_{chunk + 1}.csv'
            file_path = self.write(chunk_data, filename)
            files.append(file_path)

            print(f"第 {chunk + 1} 批完成，已写入 {file_path}")

        return files