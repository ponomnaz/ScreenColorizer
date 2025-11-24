"""
Точка входа
Настройки в config.py
"""
from SelectorProcessor import SelectorProcessor
from TreeBuilder import TreeBuilder

if __name__ == "__main__":
   #SelectorProcessor().process()
    input_file = 'data/example.txt'  # Путь к входному файлу
    output_dir_tree = 'data/tree.txt'
    output_dir_all = 'data/all_paths.txt'
    TreeBuilder.build_tree_from_file(input_file, output_dir_tree)
    TreeBuilder.extract_all_paths(input_file, output_dir_all)