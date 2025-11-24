import re


class SelectorExtractor:
    @staticmethod
    def extract_ids(file_path):
        """
        Извлекает все уникальные ID селекторы (с #) из файла
        и возвращает их список без символа #
        """
        ids = set()

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Находим все селекторы, начинающиеся с #
                matches = re.findall(r'#([a-zA-Z0-9_-]+)', line)
                ids.update(matches)

        return sorted(list(ids))

    @staticmethod
    def extract_classes(file_path):
        """
        Извлекает все уникальные class селекторы (с .) из файла
        и возвращает их список без символа .
        """
        classes = set()

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Находим все селекторы, начинающиеся с .
                matches = re.findall(r'\.([a-zA-Z0-9_-]+)', line)
                classes.update(matches)

        return sorted(list(classes))

    @staticmethod
    def save_ids_to_file(input_file, output_file='ids.txt'):
        """
        Извлекает ID селекторы и сохраняет их в файл (по одному на строку)
        """
        ids = SelectorExtractor.extract_ids(input_file)

        with open(output_file, 'w', encoding='utf-8') as f:
            for id_name in ids:
                f.write(id_name + '\n')

        print(f"✅ Найдено {len(ids)} уникальных ID селекторов")
        print(f"📄 Сохранено в файл: {output_file}")

        return ids

    @staticmethod
    def save_classes_to_file(input_file, output_file='classes.txt'):
        """
        Извлекает class селекторы и сохраняет их в файл (по одному на строку)
        """
        classes = SelectorExtractor.extract_classes(input_file)

        with open(output_file, 'w', encoding='utf-8') as f:
            for class_name in classes:
                f.write(class_name + '\n')

        print(f"✅ Найдено {len(classes)} уникальных class селекторов")
        print(f"📄 Сохранено в файл: {output_file}")

        return classes