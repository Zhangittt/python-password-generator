# PassGen — генератор паролей

## Описание
Консольная программа на Python для генерации случайных паролей и оценки их надёжности. Помогает быстро создавать стойкие пароли вместо придуманных вручную.

## Возможности
| Функция | Описание |
|---|---|
| `generate_password` | Пароль из букв и цифр заданной длины |
| `generate_with_symbols` | Пароль с буквами, цифрами и спецсимволами |
| `generate_many` | Несколько паролей сразу |
| `check_strength` | Оценка надёжности пароля |
| `validate_length` | Проверка введённой длины (4–64) |
| `filter_by_strength` | Фильтр паролей по надёжности |
| `search_passwords` | Поиск паролей по подстроке |

## Технологии
- Python 3 (стандартная библиотека: `random`, `string`)
- pytest — тестирование
- Git, GitHub

## Структура проекта
```
python-password-generator/
├── src/
│   └── main.py          # исходный код программы
├── tests/
│   └── test_main.py     # тесты pytest
├── README.md            # документация
├── requirements.txt     # зависимости
└── .gitignore           # исключения Git
```

## Требования
- Python 3.10 или новее
- pip

## Установка
1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение.
3. Установите зависимости.

```bash
git clone https://github.com/Zhangittt/python-password-generator.git
cd python-password-generator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
```bash
python src/main.py
```

## Использование
```
Генератор паролей PassGen — добро пожаловать!
1 - Сгенерировать пароль
2 - Пароль со спецсимволами
3 - Несколько паролей и поиск
Выберите пункт: 2
Длина пароля (4-64): 16
Пароль: k#8Lq!zP2@mV9x&R | Надёжность: Сильный
```

Запуск тестов:
```bash
pytest
```

## Зависимости
Программа использует только стандартную библиотеку Python. Для запуска тестов нужен pytest — см. [requirements.txt](requirements.txt).

## Автор
Ансарулы Жан, группа П-25-75б