# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/kicha3007-boop/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kicha3007-boop/python-project-50/actions)
[![Python CI](https://github.com/kicha3007-boop/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/kicha3007-boop/python-project-50/actions/workflows/pyci.yml)

`gendiff` сравнивает два конфигурационных файла (JSON или YAML, в том числе вложенные) и
показывает разницу в одном из трёх форматов: `stylish` (по умолчанию), `plain`, `json`.

## Требования

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Установка

```bash
git clone https://github.com/kicha3007-boop/python-project-50.git
cd python-project-50
make install          # зависимости для разработки
make build            # сборка пакета
make package-install  # команда gendiff в системе
```

## Использование

```bash
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

gendiff file1.json file2.yml
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
...

gendiff --format plain file1.json file2.json
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
...

gendiff --format json file1.json file2.json
```

Как библиотека:

```python
from gendiff import generate_diff

print(generate_diff('file1.json', 'file2.yml', 'plain'))
```

## Разработка

```bash
make test           # тесты
make test-coverage  # тесты с порогом покрытия из pyproject.toml
make lint           # ruff
```

## Устройство

- `gendiff/generator.py` — `generate_diff()`: прочитать файлы → распарсить → построить дерево → отформатировать.
- `gendiff/parser.py` — разбор содержимого по типу данных (`json`, `yaml`).
- `gendiff/diff_tree.py` — внутреннее представление: узлы `added`, `removed`, `changed`, `unchanged`, `nested`.
- `gendiff/formatters/` — по модулю на формат вывода, выбор по имени в `__init__.py`.

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>
