"""
Конфигурация проекта
"""
from ColorGenerator import ColorGenerator


class ColorMethod:
    """Описание метода генерации цветов"""
    
    def __init__(self, func, description):
        self.func = func
        self.description = description


# Доступные методы генерации цветов
METHODS = {
    'fps_oklab': ColorMethod(
        ColorGenerator.generate_fps_oklab_colors,
        'Farthest-Point Sampling в OKLab - максимальная визуальная различимость'
    ),
    'simple': ColorMethod(
        ColorGenerator.generate_colors,
        'Простое равномерное распределение по цветовому кругу'
    ),
    'even': ColorMethod(
        ColorGenerator.generate_colors_even,
        'Равномерное распределение - первая половина яркая, вторая тёмная'
    ),
    'golden': ColorMethod(
        ColorGenerator.generate_golden_colors,
        'Использование золотого угла для естественного распределения'
    ),
    'matplotlib': ColorMethod(
        ColorGenerator.generate_matplotlib_colors,
        'Готовая палитра Matplotlib tab20'
    ),
    'lab_distinct': ColorMethod(
        ColorGenerator.generate_distinct_lab_colors,
        'Максимально различимые цвета в CIE Lab пространстве'
    ),
}


class Config:
    """Настройки"""
    
    # ============================================
    # ГЛАВНЫЕ НАСТРОЙКИ - ИЗМЕНИТЕ ЗДЕСЬ
    # ============================================
    
    # Метод генерации цветов (ключ из METHODS)
    COLOR_METHOD = 'fps_oklab'
    
    # Пути
    INPUT_FILE = 'data/example.txt'
    OUTPUT_DIR = 'data'
    
    @classmethod
    def get_method(cls):
        """Получить выбранный метод"""
        if cls.COLOR_METHOD not in METHODS:
            raise ValueError(f"Неизвестный метод '{cls.COLOR_METHOD}'")
        return METHODS[cls.COLOR_METHOD]