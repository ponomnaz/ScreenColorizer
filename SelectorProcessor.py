"""
Основной процессор
"""
import os
from SelectorExtractor import SelectorExtractor
from SelectorColorMapper import SelectorColorMapper
from config import Config


class SelectorProcessor:
    """Обработка селекторов"""
    
    def __init__(self):
        self.config = Config
        self.method = self.config.get_method()
        self._create_dirs()
        
    def _create_dirs(self):
        """Создать директории для выходных файлов"""
        dirs = ['txt', 'css', 'html']
        for d in dirs:
            os.makedirs(os.path.join(self.config.OUTPUT_DIR, d), exist_ok=True)
    
    def _get_output_path(self, filename):
        """Получить путь для выходного файла по расширению"""
        ext = filename.split('.')[-1]
        return os.path.join(self.config.OUTPUT_DIR, ext, filename)
    
    def process(self):
        """Главный метод обработки"""
        input_file = self.config.INPUT_FILE
        
        print("=" * 70)
        print(f"🎨 ГЕНЕРАТОР ЦВЕТОВ")
        print("=" * 70)
        print(f"📂 Файл: {input_file}")
        print(f"🎯 Метод: {self.config.COLOR_METHOD}")
        print("=" * 70)
        print()
        
        # Извлечение селекторов
        print("📋 Извлечение селекторов...")
        ids = SelectorExtractor.extract_ids(input_file)
        classes = SelectorExtractor.extract_classes(input_file)
        
        if not ids and not classes:
            print("⚠️ Селекторы не найдены!")
            return
        
        # Сохранение списков
        if ids:
            path = self._get_output_path('ids.txt')
            self._save_list(ids, path)
            print(f"✅ ID селекторов: {len(ids)} → {path}")
        
        if classes:
            path = self._get_output_path('classes.txt')
            self._save_list(classes, path)
            print(f"✅ Class селекторов: {len(classes)} → {path}")
        
        print()
        
        # Генерация CSS и HTML для ID
        if ids:
            print(f"🎨 Генерация для ID ({len(ids)} шт.)...")
            
            css_path = self._get_output_path('selectors_ids.css')
            html_path = self._get_output_path('selectors_ids.html')
            
            pairs = SelectorColorMapper.generate_css(
                ids, css_path, 'id', self.method
            )
            SelectorColorMapper.generate_html(
                pairs, html_path, 'id', self.method
            )
            
            print(f"   CSS:  {css_path}")
            print(f"   HTML: {html_path}")
            print()
        
        # Генерация CSS и HTML для classes
        if classes:
            print(f"🎨 Генерация для classes ({len(classes)} шт.)...")
            
            css_path = self._get_output_path('selectors_classes.css')
            html_path = self._get_output_path('selectors_classes.html')
            
            pairs = SelectorColorMapper.generate_css(
                classes, css_path, 'class', self.method
            )
            SelectorColorMapper.generate_html(
                pairs, html_path, 'class', self.method
            )
            
            print(f"   CSS:  {css_path}")
            print(f"   HTML: {html_path}")
            print()
        
        print("=" * 70)
        print("✅ Готово!")
        print("=" * 70)
    
    def _save_list(self, items, path):
        """Сохранить список в файл"""
        with open(path, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(item + '\n')