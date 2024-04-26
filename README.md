# fastapi-backend

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![python: 3.12](https://img.shields.io/badge/python-3.12-yellowgreen)](https://www.python.org/downloads/release/python-3122/)
[![type checker: mypy](https://img.shields.io/badge/type%20checker-mypy-1f5082)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

В данном репозитории расположен код серверной части проекта Ugly Gallery, написанный на библиотеке FastAPI.

В репозитории присутствует [pre-commit](https://pre-commit.com/) для проверки качества кода перед добавлением его в
репозиторий. Чтобы установить, выполните:
```shell
poetry install
pre-commit install
```

## Гайд по запуску кода

1.  ```shell
    git clone https://github.com/UglyGallery/main-backend.git
    cd main-backend
    poetry install
    pre-commit install
    ```
2. Создадим файл с переменными среды:
    ```shell
    cp .env.example .env
    ```
3. Запустим Докер:
   ```shell
   docker compose up -d
   ```
4. Активируем Poetry virtual environment:
   ```shell
   poetry env use 3.12
   ```
5. Запустим `main` файл:
   ```shell
   python main.py
   ```

## Про расположение main файла

По хорошему, он бы должен находится в папке `src/`. Но это ломает импорты, если проект не добавлен нужным образом
в `PYTHONPATH`... Пусть пока временно будет так, потом поправим. TODO!
