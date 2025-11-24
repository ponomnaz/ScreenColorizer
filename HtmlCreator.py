class HtmlCreator:
    @staticmethod
    def create_html_table(colors):
        # Создаём HTML-таблицу
        html = '<table border="1" style="border-collapse: collapse;">\n'
        html += '  <tr>\n'
        
        for rgb in colors:
            r, g, b = rgb
            color_str = f"rgb({r}, {g}, {b})"
            html += f'    <td style="background-color: {color_str}; width: 100px; height: 50px; text-align: center; color: #fff;">{color_str}</td>\n'
        
        html += '  </tr>\n'
        html += '</table>'
        
        return html
        