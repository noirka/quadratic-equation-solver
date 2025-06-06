# Quadratic Equation Solver

Консольний застосунок для розв'язання квадратних рівнянь виду `ax² + bx + c = 0`.

## Опис

Програма знаходить дійсні корені квадратного рівняння та підтримує два режими роботи:

- **Інтерактивний режим** - введення коефіцієнтів через консоль
- **Файловий режим** - читання коефіцієнтів з файлу

Квадратне рівняння може мати 0, 1 або 2 дійсних корені залежно від дискримінанта.

## Встановлення та запуск

### Вимоги

- Python 3.6 або новіша версія

### Клонування репозиторію

```bash
git clone https://github.com/noirka/quadratic-equation-solver.git
cd quadratic-equation-solver
```

### Запуск

**Інтерактивний режим:**

```bash
python equation.py
```

**Файловий режим:**

```bash
python equation.py filename.txt
```

## Приклади використання

### Інтерактивний режим

```bash
$ python equation.py
a = 2
b = 1
c = -3
Equation is: (2.0) x^2 + (1.0) x + (-3.0) = 0
There are 2 roots
x1 = -1.5
x2 = 1.0
```

### Файловий режим

```bash
$ python equation.py test_valid.txt
Equation is: (1.0) x^2 + (0.0) x + (0.0) = 0
There are 1 roots x1 = 0.0
```

## Формат файлу для неінтерактивного режиму

Файл повинен містити три числа (коефіцієнти a, b, c) розділених одним пробілом:

```
a b c
```

**Приклад файлу:**

```
1 0 -4
```

**Вимоги до формату:**

- Три числа через один пробіл
- Десятковий роздільник - крапка (.)
- Символ нового рядка в кінці файлу (\n)
- Коефіцієнт `a` не може дорівнювати 0

## Обробка помилок

Програма обробляє наступні помилки:

- Некоректний ввід в інтерактивному режимі
- Відсутність файлу
- Неправильний формат файлу
- Коефіцієнт a = 0

## Тестові файли

У репозиторії присутні тестові файли:

- `test_valid.txt` - випадок з одним коренем
- `test_two_roots.txt` - випадок з двома коренями
- `test_zero.txt` - помилка (a = 0)
- `test_invalid.txt` - неправильний формат файлу

## Git History

### Revert коміт

Для демонстрації функціональності git revert був створений коміт з тимчасовою експериментальною функцією, який потім був відкочений.

**Revert коміт:** `05034c7`

Цей коміт показує, як можна безпечно відкочувати зміни в Git без втрати історії.

## Структура проекту

```
quadratic-equation-solver/
├── equation.py           # Основний файл програми
├── README.md            # Документація
├── test_valid.txt       # Тестовий файл (один корінь)
├── test_two_roots.txt   # Тестовий файл (два корені)
├── test_zero.txt        # Тестовий файл (помилка a=0)
└── test_invalid.txt     # Тестовий файл (неправильний формат)
```

## Автор

Остапова Вероніка Артурівна
Студент 2 курсу групи ІМ-34
