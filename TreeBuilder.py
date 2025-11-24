"""
Построение дерева из путей селекторов
"""
import os


class TreeBuilder:
    
    @staticmethod
    def build_tree_from_file(input_file, output_file):
        """Строит дерево из файла с путями"""
        
        # Читаем файл
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Собираем все уникальные пути
        all_paths = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Разделяем строку на тип элемента и пути
            parts = line.split(' ', 1)
            if len(parts) > 1:
                paths_str = parts[1]
                
                # Разделяем по ';' и берём самый длинный путь (он полный)
                paths = [p.strip() for p in paths_str.split(';') if p.strip()]
                
                if paths:
                    # Берём самый длинный путь (он содержит полную иерархию)
                    longest = max(paths, key=lambda x: len(x.split()))
                    all_paths.append(longest)
        
        # Строим дерево
        tree = {}
        
        for path in all_paths:
            # Разбиваем путь на компоненты
            components = [c.strip() for c in path.split() if c.strip()]
            
            if components:
                TreeBuilder._add_to_tree(tree, components)
        
        # Создаём директорию если нужно
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Записываем дерево в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            TreeBuilder._write_tree(tree, f)
        
        print(f"✅ Дерево сохранено: {output_file}")
        
        # Статистика
        TreeBuilder._print_stats(tree)
        
        return tree
    
    @staticmethod
    def _add_to_tree(tree, components):
        """Добавляет путь в дерево"""
        current = tree
        
        for comp in components:
            if comp not in current:
                current[comp] = {}
            current = current[comp]
    
    @staticmethod
    def _write_tree(node, file, prefix='', is_root=True):
        """Рекурсивно записывает дерево в файл"""
        
        if not node:
            return
        
        items = sorted(node.items())
        
        for i, (key, children) in enumerate(items):
            is_last = (i == len(items) - 1)
            
            # Определяем символы для отрисовки
            if is_root:
                connector = ''
                extension = ''
            else:
                connector = '└── ' if is_last else '├── '
                extension = '    ' if is_last else '│   '
            
            # Пишем текущий узел
            file.write(prefix + connector + key + '\n')
            
            # Рекурсивно пишем детей
            if children:
                new_prefix = prefix + extension
                TreeBuilder._write_tree(children, file, new_prefix, False)
    
    @staticmethod
    def _print_stats(tree):
        """Выводит статистику"""
        def count_nodes(node):
            count = len(node)
            for child in node.values():
                count += count_nodes(child)
            return count
        
        total = count_nodes(tree)
        roots = len(tree)
        
        print(f"📊 Узлов в дереве: {total}")
        print(f"📊 Корневых элементов: {roots}")
    
    @staticmethod
    def extract_all_paths(input_file, output_file):
        """
        Извлекает все уникальные пути из файла
        Пример: #roombox #header #logo;#header #logo;#logo
        Результат: 
            #roombox #header #logo
            #header #logo
            #logo
        """
        
        # Читаем файл
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Собираем все уникальные пути
        unique_paths = set()
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Разделяем строку на тип элемента и пути
            parts = line.split(' ', 1)
            if len(parts) > 1:
                paths_str = parts[1]
                
                # Разделяем по ';' и добавляем каждый путь
                for path in paths_str.split(';'):
                    path = path.strip()
                    if path:
                        unique_paths.add(path)
        
        # Сортируем пути
        sorted_paths = sorted(unique_paths)
        
        # Создаём директорию если нужно
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Записываем в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            for path in sorted_paths:
                f.write(path + '\n')
        
        print(f"✅ Все пути сохранены: {output_file}")
        print(f"📊 Уникальных путей: {len(sorted_paths)}")
        
        return sorted_paths