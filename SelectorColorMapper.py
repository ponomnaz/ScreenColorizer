"""
Генерация CSS и HTML с цветами
"""


class SelectorColorMapper:
    
    @staticmethod
    def generate_css(selectors, output_file, selector_type, method):
        """Генерирует CSS файл"""
        n = len(selectors)
        colors = method.func(n)
        
        prefix = '#' if selector_type == 'id' else '.'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f'/* Метод: {method.description} */\n\n')
            
            for selector, (r, g, b) in zip(selectors, colors):
                f.write(f'{prefix}{selector} {{\n')
                f.write(f'    background-color: rgb({r}, {g}, {b});\n')
                f.write(f'}}\n\n')
        
        return list(zip(selectors, colors))

    @staticmethod
    def generate_html(pairs, output_file, selector_type, method):
        """Генерирует HTML таблицу"""
        prefix = '#' if selector_type == 'id' else '.'
        
        html = '<!DOCTYPE html>\n'
        html += '<html lang="ru">\n'
        html += '<head>\n'
        html += '    <meta charset="UTF-8">\n'
        html += f'    <title>Цвета {selector_type}</title>\n'
        html += '    <style>\n'
        html += '        body { font-family: Arial; padding: 20px; background: #f5f5f5; }\n'
        html += '        h1 { text-align: center; color: #333; }\n'
        html += '        .method { text-align: center; color: #666; margin: 20px; }\n'
        html += '        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px; }\n'
        html += '        .card { border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background: white; }\n'
        html += '        .color { height: 100px; display: flex; align-items: center; justify-content: center; color: white; font-size: 11px; }\n'
        html += '        .name { padding: 10px; text-align: center; font-family: monospace; font-size: 13px; }\n'
        html += '    </style>\n'
        html += '</head>\n'
        html += '<body>\n'
        html += f'    <h1>🎨 {selector_type.upper()} селекторы</h1>\n'
        html += f'    <div class="method">{method.description}</div>\n'
        html += '    <div class="grid">\n'
        
        for selector, (r, g, b) in pairs:
            color_str = f'rgb({r}, {g}, {b})'
            html += '        <div class="card">\n'
            html += f'            <div class="color" style="background-color: {color_str};">{color_str}</div>\n'
            html += f'            <div class="name">{prefix}{selector}</div>\n'
            html += '        </div>\n'
        
        html += '    </div>\n'
        html += '</body>\n'
        html += '</html>'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)