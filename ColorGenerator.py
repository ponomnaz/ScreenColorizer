import colorsys
import math
import random
import matplotlib.pyplot as plt
import numpy as np


class ColorGenerator:
    @staticmethod
    def generate_colors_even(n):
        """
        Генерирует чётное количество цветов:
        первая половина - яркие (value=1.0),
        вторая половина - тёмные (value=0.5)
        """
        if n % 2 != 0:
            raise ValueError("Количество цветов должно быть чётным")

        half = n // 2
        colors = []

        for i in range(n):
            hue = i * 360 / n
            saturation = 1.0
            if i < half:
                value = 1.0
            else:
                value = 0.5

            r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation, value)
            colors.append((int(r * 255), int(g * 255), int(b * 255)))

        return colors

    @staticmethod
    def generate_colors(n):
        """
        Генерирует любое количество равноудалённых цветов
        с одинаковой яркостью (value=1.0)
        """
        colors = []

        for i in range(n):
            hue = i * 360 / n
            saturation = 1.0
            value = 1.0

            r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation, value)
            colors.append((int(r * 255), int(g * 255), int(b * 255)))

        return colors

    @staticmethod
    def generate_golden_colors(n):
        if n % 2 != 0:
            raise ValueError("Количество цветов должно быть чётным")

        half = n // 2
        golden_angle = 360 * (1 + math.sqrt(5)) / 2
        colors = []

        for i in range(n):
            hue = (i * golden_angle) % 360
            saturation = 1.0
            value = 1.0 if i < half else 0.5
            r, g, b = colorsys.hsv_to_rgb(hue / 360, saturation, value)
            colors.append((int(r * 255), int(g * 255), int(b * 255)))

        return colors

    @staticmethod
    def generate_matplotlib_colors(n):
        if n % 2 != 0:
            raise ValueError("Количество цветов должно быть чётным")

        cmap = plt.get_cmap('tab20')
        indices = np.linspace(0, 1, n)
        colors_rgba = cmap(indices)

        colors = []
        half = n // 2
        for i, (r, g, b, a) in enumerate(colors_rgba):
            if i >= half:
                r, g, b = [c * 0.5 for c in (r, g, b)]
            colors.append((int(r * 255), int(g * 255), int(b * 255)))

        return colors

    @staticmethod
    def rgb_to_lab(r, g, b):
        """Конвертация RGB -> Lab (CIE Lab)"""
        r, g, b = [x / 255.0 for x in (r, g, b)]
        r = ((r + 0.055) / 1.055) ** 2.4 if r > 0.04045 else r / 12.92
        g = ((g + 0.055) / 1.055) ** 2.4 if g > 0.04045 else g / 12.92
        b = ((b + 0.055) / 1.055) ** 2.4 if b > 0.04045 else b / 12.92
        x = r * 0.4124 + g * 0.3576 + b * 0.1805
        y = r * 0.2126 + g * 0.7152 + b * 0.0722
        z = r * 0.0193 + g * 0.1192 + b * 0.9505
        x, y, z = [v / ref for v, ref in zip((x, y, z), (0.95047, 1.0, 1.08883))]
        x = x ** (1 / 3) if x > 0.008856 else 7.787 * x + 16 / 116
        y = y ** (1 / 3) if y > 0.008856 else 7.787 * y + 16 / 116
        z = z ** (1 / 3) if z > 0.008856 else 7.787 * z + 16 / 116
        return (116 * y - 16, 500 * (x - y), 200 * (y - z))

    @staticmethod
    def delta_e(lab1, lab2):
        """Расстояние между цветами в Lab (CIE76)"""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(lab1, lab2)))

    @staticmethod
    def generate_distinct_lab_colors(n, skip=16):
        """Генерация максимально различимых цветов в Lab пространстве"""
        if n % 2 != 0:
            raise ValueError("Количество цветов должно быть чётным")

        colors = [[0, 0, 0]]
        for _ in range(n - 1):
            max_dist = -math.inf
            best_color = None
            for r in range(0, 256, skip):
                for g in range(0, 256, skip):
                    for b in range(0, 256, skip):
                        candidate = [r, g, b]
                        lab_cand = ColorGenerator.rgb_to_lab(*candidate)
                        min_dist = min(ColorGenerator.delta_e(lab_cand, ColorGenerator.rgb_to_lab(*c)) for c in colors)
                        if min_dist > max_dist:
                            max_dist = min_dist
                            best_color = candidate
            if best_color:
                colors.append(best_color)

        half = n // 2
        for i in range(half, n):
            colors[i] = [int(c * 0.5) for c in colors[i]]

        return [tuple(c) for c in colors]

    @staticmethod
    def rgb_to_oklab(r, g, b):
        """Конвертация RGB -> OKLab (перцептивно равномерное цветовое пространство)"""

        def rgb_to_linear(v):
            v = v / 255.0
            if v > 0.04045:
                return ((v + 0.055) / 1.055) ** 2.4
            else:
                return v / 12.92

        lin_r = rgb_to_linear(r)
        lin_g = rgb_to_linear(g)
        lin_b = rgb_to_linear(b)

        M1 = np.array([
            [0.4122214708, 0.5363325363, 0.0514459929],
            [0.2119034982, 0.6806995451, 0.1073969566],
            [0.0883024619, 0.2817188376, 0.6299787005]
        ])

        lms = M1 @ np.array([lin_r, lin_g, lin_b])
        lms_prime = np.cbrt(lms)

        M2 = np.array([
            [0.2104542553, 0.7936177850, -0.0040720468],
            [1.9779984951, -2.4285922050, 0.4505937099],
            [0.0259040371, 0.7827717662, -0.8086757667]
        ])

        oklab = M2 @ lms_prime
        return oklab  # [L, a, b]

    @staticmethod
    def oklab_to_rgb(L, a, b):
        """Конвертация OKLab -> RGB"""

        def linear_to_rgb(v):
            if v > 0.0031308:
                return 1.055 * (v ** (1 / 2.4)) - 0.055
            else:
                return 12.92 * v

        M2 = np.array([
            [0.2104542553, 0.7936177850, -0.0040720468],
            [1.9779984951, -2.4285922050, 0.4505937099],
            [0.0259040371, 0.7827717662, -0.8086757667]
        ])
        M2_inv = np.linalg.inv(M2)

        lms_prime = M2_inv @ np.array([L, a, b])
        lms = lms_prime ** 3

        M1 = np.array([
            [0.4122214708, 0.5363325363, 0.0514459929],
            [0.2119034982, 0.6806995451, 0.1073969566],
            [0.0883024619, 0.2817188376, 0.6299787005]
        ])
        M1_inv = np.linalg.inv(M1)

        lin_rgb = M1_inv @ lms
        r = linear_to_rgb(lin_rgb[0]) * 255
        g = linear_to_rgb(lin_rgb[1]) * 255
        b = linear_to_rgb(lin_rgb[2]) * 255

        # Clip to 0-255
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        return int(round(r)), int(round(g)), int(round(b))

    @staticmethod
    def generate_fps_oklab_colors(n, num_samples=10000):
        """
        🌈 GOLD STANDARD: Farthest-Point Sampling в OKLab

        Генерирует n максимально различимых цветов с помощью Farthest-Point Sampling
        в перцептивно равномерном OKLab пространстве.

        Параметры:
        - n: количество цветов (рекомендуется ≤ 40)
        - num_samples: количество сэмплов для поиска (больше = лучше, но медленнее)

        Возвращает: список кортежей (r, g, b)
        """
        if n > 40:
            print("⚠️ Предупреждение: для n > 40 рекомендуется увеличить num_samples")

        print(f"🎨 Генерация {n} цветов методом FPS в OKLab...")
        print(f"📊 Сэмплирование {num_samples} точек...")

        # Генерируем случайные RGB точки
        rgb_points = []
        oklab_points = []

        for _ in range(num_samples):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            # Пропускаем слишком тёмные цвета (для лучшей различимости)
            if r + g + b < 60:
                continue

            rgb_points.append((r, g, b))
            oklab_points.append(ColorGenerator.rgb_to_oklab(r, g, b))

        print(f"✅ Сэмплировано {len(rgb_points)} валидных точек")

        # Выбираем первую точку - ищем самый насыщенный цвет
        max_saturation = -1
        first_index = 0
        for i, (r, g, b) in enumerate(rgb_points):
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if s * v > max_saturation:
                max_saturation = s * v
                first_index = i

        selected_indices = [first_index]
        selected_oklab = [oklab_points[first_index]]

        print(f"🎯 FPS: выбор максимально удалённых цветов...")

        # Farthest-Point Sampling
        for iteration in range(1, n):
            max_min_dist = -float('inf')
            best_index = -1

            for i in range(len(oklab_points)):
                if i in selected_indices:
                    continue

                # Находим минимальное расстояние до уже выбранных цветов
                min_dist = min(
                    math.sqrt(sum((x - y) ** 2 for x, y in zip(oklab_points[i], s)))
                    for s in selected_oklab
                )

                # Выбираем точку с максимальным минимальным расстоянием
                if min_dist > max_min_dist:
                    max_min_dist = min_dist
                    best_index = i

            if best_index != -1:
                selected_indices.append(best_index)
                selected_oklab.append(oklab_points[best_index])

                if (iteration + 1) % 5 == 0:
                    print(f"  → {iteration + 1}/{n} цветов выбрано")

        # Конвертируем обратно в RGB
        colors = [rgb_points[i] for i in selected_indices]

        print(f"✨ Готово! Сгенерировано {len(colors)} максимально различимых цветов")

        return colors