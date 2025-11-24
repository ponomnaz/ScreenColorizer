from ColorGenerator import ColorGenerator


class SelectorColorMapper:
    """Класс для создания CSS и HTML с цветами для селекторов"""

    @staticmethod
    def generate_css_for_ids(selectors, output_file='selectors_ids.css'):
        """Генерирует CSS файл с цветами для ID селекторов"""
        n = len(selectors)

        if n == 0:
            print("⚠️ Нет селекторов для обработки")
            return []

        colors = ColorGenerator.generate_fps_oklab_colors(n)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('/* ========================================== */\n')
            f.write('/* Автоматически сгенерированные цвета       */\n')
            f.write('/* для ID селекторов                         */\n')
            f.write('/* ========================================== */\n')
            f.write('/* Метод: Farthest-Point Sampling в OKLab    */\n')
            f.write('/* Обеспечивает максимальную визуальную      */\n')
            f.write('/* различимость цветов                       */\n')
            f.write('/* ========================================== */\n\n')

            for selector, (r, g, b) in zip(selectors, colors):
                f.write(f'#{selector} {{\n')
                f.write(f'    background-color: rgb({r}, {g}, {b});\n')
                f.write(f'}}\n\n')

        print(f"✅ CSS файл сохранён: {output_file}")
        return list(zip(selectors, colors))

    @staticmethod
    def generate_css_for_classes(selectors, output_file='selectors_classes.css'):
        """Генерирует CSS файл с цветами для class селекторов"""
        n = len(selectors)

        if n == 0:
            print("⚠️ Нет селекторов для обработки")
            return []

        colors = ColorGenerator.generate_fps_oklab_colors(n)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('/* ========================================== */\n')
            f.write('/* Автоматически сгенерированные цвета       */\n')
            f.write('/* для class селекторов                      */\n')
            f.write('/* ========================================== */\n')
            f.write('/* Метод: Farthest-Point Sampling в OKLab    */\n')
            f.write('/* Обеспечивает максимальную визуальную      */\n')
            f.write('/* различимость цветов                       */\n')
            f.write('/* ========================================== */\n\n')

            for selector, (r, g, b) in zip(selectors, colors):
                f.write(f'.{selector} {{\n')
                f.write(f'    background-color: rgb({r}, {g}, {b});\n')
                f.write(f'}}\n\n')

        print(f"✅ CSS файл сохранён: {output_file}")
        return list(zip(selectors, colors))

    @staticmethod
    def generate_html_table(selector_color_pairs, selector_type='id', output_file='selectors_table.html'):
        """
        Генерирует HTML таблицу с селекторами и их цветами в виде сетки
        selector_type: 'id' или 'class'
        """
        if not selector_color_pairs:
            print("⚠️ Нет данных для генерации HTML таблицы")
            return

        prefix = '#' if selector_type == 'id' else '.'

        html = '<!DOCTYPE html>\n'
        html += '<html lang="ru">\n'
        html += '<head>\n'
        html += '    <meta charset="UTF-8">\n'
        html += '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        html += f'    <title>Таблица цветов для {selector_type} селекторов</title>\n'
        html += '    <style>\n'
        html += '        * {\n'
        html += '            margin: 0;\n'
        html += '            padding: 0;\n'
        html += '            box-sizing: border-box;\n'
        html += '        }\n'
        html += '        body {\n'
        html += '            font-family: "Segoe UI", Arial, sans-serif;\n'
        html += '            padding: 20px;\n'
        html += '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\n'
        html += '            min-height: 100vh;\n'
        html += '        }\n'
        html += '        .container {\n'
        html += '            max-width: 1600px;\n'
        html += '            margin: 0 auto;\n'
        html += '            background-color: white;\n'
        html += '            border-radius: 15px;\n'
        html += '            box-shadow: 0 10px 40px rgba(0,0,0,0.2);\n'
        html += '            overflow: hidden;\n'
        html += '        }\n'
        html += '        h1 {\n'
        html += '            text-align: center;\n'
        html += '            padding: 25px;\n'
        html += '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\n'
        html += '            color: white;\n'
        html += '            margin: 0;\n'
        html += '            font-size: 1.8em;\n'
        html += '            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);\n'
        html += '        }\n'
        html += '        .grid-wrapper {\n'
        html += '            padding: 20px;\n'
        html += '        }\n'
        html += '        .color-grid {\n'
        html += '            display: grid;\n'
        html += '            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));\n'
        html += '            gap: 15px;\n'
        html += '            padding: 10px;\n'
        html += '        }\n'
        html += '        .color-card {\n'
        html += '            border: 2px solid #e0e0e0;\n'
        html += '            border-radius: 10px;\n'
        html += '            overflow: hidden;\n'
        html += '            box-shadow: 0 2px 8px rgba(0,0,0,0.1);\n'
        html += '            transition: transform 0.2s, box-shadow 0.2s;\n'
        html += '            cursor: pointer;\n'
        html += '        }\n'
        html += '        .color-card:hover {\n'
        html += '            transform: translateY(-5px);\n'
        html += '            box-shadow: 0 8px 20px rgba(0,0,0,0.2);\n'
        html += '        }\n'
        html += '        .color-sample {\n'
        html += '            height: 120px;\n'
        html += '            display: flex;\n'
        html += '            align-items: center;\n'
        html += '            justify-content: center;\n'
        html += '            color: white;\n'
        html += '            font-family: monospace;\n'
        html += '            font-size: 11px;\n'
        html += '            font-weight: 600;\n'
        html += '            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);\n'
        html += '            padding: 10px;\n'
        html += '            word-break: break-all;\n'
        html += '        }\n'
        html += '        .selector-name {\n'
        html += '            padding: 12px;\n'
        html += '            background-color: #f8f9fa;\n'
        html += '            text-align: center;\n'
        html += '            font-family: monospace;\n'
        html += '            font-size: 13px;\n'
        html += '            font-weight: 600;\n'
        html += '            color: #333;\n'
        html += '            border-top: 2px solid #e0e0e0;\n'
        html += '            word-break: break-word;\n'
        html += '        }\n'
        html += '        .info {\n'
        html += '            text-align: center;\n'
        html += '            padding: 20px;\n'
        html += '            background-color: #f8f9fa;\n'
        html += '            border-top: 2px solid #e0e0e0;\n'
        html += '        }\n'
        html += '        .info p {\n'
        html += '            margin: 8px 0;\n'
        html += '            color: #555;\n'
        html += '            font-size: 14px;\n'
        html += '        }\n'
        html += '        .info strong {\n'
        html += '            color: #764ba2;\n'
        html += '        }\n'
        html += '        .badge {\n'
        html += '            display: inline-block;\n'
        html += '            padding: 4px 12px;\n'
        html += '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\n'
        html += '            color: white;\n'
        html += '            border-radius: 20px;\n'
        html += '            font-weight: 600;\n'
        html += '            margin: 0 5px;\n'
        html += '        }\n'
        html += '    </style>\n'
        html += '</head>\n'
        html += '<body>\n'
        html += '    <div class="container">\n'
        html += f'        <h1>🎨 Таблица цветов для {selector_type.upper()} селекторов</h1>\n'
        html += '        <div class="grid-wrapper">\n'
        html += '            <div class="color-grid">\n'

        # Создаем карточки для каждого селектора
        for selector, (r, g, b) in selector_color_pairs:
            color_str = f'rgb({r}, {g}, {b})'
            html += '                <div class="color-card">\n'
            html += f'                    <div class="color-sample" style="background-color: {color_str};">{color_str}</div>\n'
            html += f'                    <div class="selector-name">{prefix}{selector}</div>\n'
            html += '                </div>\n'

        html += '            </div>\n'
        html += '        </div>\n'
        html += '        <div class="info">\n'
        html += f'            <p><strong>Всего селекторов:</strong> <span class="badge">{len(selector_color_pairs)}</span></p>\n'
        html += f'            <p><strong>Метод генерации:</strong> Farthest-Point Sampling в OKLab</p>\n'
        html += f'            <p>Обеспечивает <strong>максимальную визуальную различимость</strong> цветов</p>\n'
        html += '        </div>\n'
        html += '    </div>\n'
        html += '</body>\n'
        html += '</html>'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✅ HTML таблица сохранена: {output_file}")