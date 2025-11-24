"""
Главный скрипт для генерации CSS и HTML с цветами для селекторов
Использует FPS в OKLab для максимальной визуальной различимости цветов
"""

from SelectorExtractor import SelectorExtractor
from SelectorColorMapper import SelectorColorMapper


def print_banner():
    """Красивый баннер"""
    print("=" * 70)
    print("🎨 CSS COLOR GENERATOR")
    print("   Генератор максимально различимых цветов для CSS селекторов")
    print("   Метод: Farthest-Point Sampling в OKLab")
    print("=" * 70)
    print()


def process_selectors(input_file='example.txt'):
    """Обрабатывает файл и генерирует все необходимые файлы"""

    print_banner()

    # Шаг 1: Извлечение селекторов
    print("📋 ШАГ 1: ИЗВЛЕЧЕНИЕ СЕЛЕКТОРОВ")
    print("-" * 70)

    try:
        # Извлекаем ID селекторы
        id_selectors = SelectorExtractor.save_ids_to_file(
            input_file,
            output_file='ids.txt'
        )
        print()

        # Извлекаем class селекторы
        class_selectors = SelectorExtractor.save_classes_to_file(
            input_file,
            output_file='classes.txt'
        )
        print()

    except FileNotFoundError:
        print(f"❌ Ошибка: файл '{input_file}' не найден!")
        return
    except Exception as e:
        print(f"❌ Ошибка при извлечении селекторов: {e}")
        return

    # Проверяем, есть ли селекторы
    if not id_selectors and not class_selectors:
        print("⚠️ Селекторы не найдены в файле!")
        return

    print("=" * 70)
    print()

    # Шаг 2: Генерация CSS и HTML для ID селекторов
    if id_selectors:
        print("🎨 ШАГ 2: ГЕНЕРАЦИЯ ЦВЕТОВ ДЛЯ ID СЕЛЕКТОРОВ")
        print("-" * 70)

        try:
            # Генерируем CSS
            id_pairs = SelectorColorMapper.generate_css_for_ids(
                id_selectors,
                output_file='selectors_ids.css'
            )

            # Генерируем HTML таблицу
            SelectorColorMapper.generate_html_table(
                id_pairs,
                selector_type='id',
                output_file='selectors_ids.html'
            )

            print()
            print(f"📊 Статистика:")
            print(f"   • ID селекторов: {len(id_selectors)}")
            print(f"   • Файлы созданы: selectors_ids.css, selectors_ids.html")
            print()

        except Exception as e:
            print(f"❌ Ошибка при генерации для ID селекторов: {e}")
            print()
    else:
        print("⚠️ ID селекторы не найдены, пропускаем...")
        print()

    print("=" * 70)
    print()

    # Шаг 3: Генерация CSS и HTML для class селекторов
    if class_selectors:
        print("🎨 ШАГ 3: ГЕНЕРАЦИЯ ЦВЕТОВ ДЛЯ CLASS СЕЛЕКТОРОВ")
        print("-" * 70)

        try:
            # Генерируем CSS
            class_pairs = SelectorColorMapper.generate_css_for_classes(
                class_selectors,
                output_file='selectors_classes.css'
            )

            # Генерируем HTML таблицу
            SelectorColorMapper.generate_html_table(
                class_pairs,
                selector_type='class',
                output_file='selectors_classes.html'
            )

            print()
            print(f"📊 Статистика:")
            print(f"   • Class селекторов: {len(class_selectors)}")
            print(f"   • Файлы созданы: selectors_classes.css, selectors_classes.html")
            print()

        except Exception as e:
            print(f"❌ Ошибка при генерации для class селекторов: {e}")
            print()
    else:
        print("⚠️ Class селекторы не найдены, пропускаем...")
        print()

    print("=" * 70)
    print()

    # Итоговая статистика
    print("✅ ГОТОВО!")
    print()
    print("📁 Созданные файлы:")
    print("   Текстовые списки:")
    if id_selectors:
        print("     • ids.txt")
    if class_selectors:
        print("     • classes.txt")
    print()
    print("   CSS файлы:")
    if id_selectors:
        print("     • selectors_ids.css")
    if class_selectors:
        print("     • selectors_classes.css")
    print()
    print("   HTML таблицы:")
    if id_selectors:
        print("     • selectors_ids.html")
    if class_selectors:
        print("     • selectors_classes.html")
    print()
    print("=" * 70)
    print()
    print("💡 Совет: откройте HTML файлы в браузере, чтобы увидеть таблицу цветов!")
    print()


def demo_color_generation():
    """Демонстрация генерации цветов"""
    from ColorGenerator import ColorGenerator
    from HtmlCreator import HtmlCreator

    print_banner()
    print("🎨 ДЕМО: Генерация тестовых цветов")
    print("-" * 70)
    print()

    n = int(input("Введите количество цветов для генерации (рекомендуется ≤ 40): "))
    print()

    if n > 40:
        print("⚠️ Внимание: для n > 40 качество различимости может снизиться")
        print()

    # Генерируем цвета
    colors = ColorGenerator.generate_fps_oklab_colors(n)

    # Создаем HTML таблицу
    html_table = HtmlCreator.create_html_table(colors)

    # Сохраняем в файл
    with open('demo_colors.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="ru">\n')
        f.write('<head>\n')
        f.write('    <meta charset="UTF-8">\n')
        f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('    <title>Демо: Сгенерированные цвета</title>\n')
        f.write('    <style>\n')
        f.write('        body { font-family: Arial, sans-serif; padding: 20px; background-color: #f5f5f5; }\n')
        f.write('        h1 { text-align: center; color: #333; }\n')
        f.write('        .info { text-align: center; margin: 20px; color: #666; }\n')
        f.write('    </style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('    <h1>🌈 Демо: Максимально различимые цвета</h1>\n')
        f.write('    <div class="info">\n')
        f.write(f'        <p>Сгенерировано цветов: {n}</p>\n')
        f.write('        <p>Метод: Farthest-Point Sampling в OKLab</p>\n')
        f.write('    </div>\n')
        f.write(html_table)
        f.write('</body>\n')
        f.write('</html>')

    print()
    print("✅ Демо файл создан: demo_colors.html")
    print("💡 Откройте его в браузере, чтобы увидеть результат!")
    print()


def main():
    """Главная функция с меню выбора"""
    while True:
        print()
        print("╔" + "=" * 68 + "╗")
        print("║" + " " * 20 + "ГЛАВНОЕ МЕНЮ" + " " * 36 + "║")
        print("╚" + "=" * 68 + "╝")
        print()
        print("Выберите действие:")
        print()
        print("  1️⃣  - Обработать example.txt (полный pipeline)")
        print("  2️⃣  - Демонстрация генерации цветов")
        print("  3️⃣  - Обработать другой файл")
        print("  0️⃣  - Выход")
        print()

        choice = input("Введите номер действия: ").strip()
        print()

        if choice == '1':
            process_selectors('example.txt')

        elif choice == '2':
            demo_color_generation()

        elif choice == '3':
            filename = input("Введите имя файла: ").strip()
            if filename:
                process_selectors(filename)
            else:
                print("❌ Имя файла не может быть пустым!")

        elif choice == '0':
            print("👋 До свидания!")
            print()
            break

        else:
            print("❌ Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    # Автоматически запускаем полный pipeline для example.txt
    # Раскомментируйте следующую строку для интерактивного меню:
    # main()

    # Или используйте прямой запуск:
    process_selectors('data/example.txt')