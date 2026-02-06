# API Testing Project

Проект для тестирования API JSONPlaceholder и ReqRes с использованием pytest и pytest-bdd.

## 📋 Структура проекта

```
api_testing_project/
├── tests/
│   ├── test_api.py              # Тесты для JSONPlaceholder (20 тестов)
│   ├── test_reqres_api.py       # Тесты для ReqRes (10 тестов)
│   └── bdd/
│       ├── features/
│       │   ├── posts.feature           # BDD сценарии для постов
│       │   ├── users.feature           # BDD сценарии для пользователей
│       │   ├── comments.feature        # BDD сценарии для комментариев
│       │   └── reqres_users.feature    # BDD сценарии для ReqRes
│       ├── step_defs/
│       │   ├── test_posts_steps.py
│       │   ├── test_users_steps.py
│       │   ├── test_comments_steps.py
│       │   └── test_reqres_steps.py
│       └── conftest.py
├── config.py                    # Конфигурация
├── conftest.py                  # Pytest конфигурация с логированием
├── pytest.ini                   # Настройки pytest
├── requirements.txt             # Зависимости
├── run_tests.sh                 # Скрипт запуска (Linux/Mac)
├── run_tests.bat                # Скрипт запуска (Windows)
└── README.md                    # Документация
```

## 🚀 Установка

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

Будут установлены:
- requests==2.31.0
- pytest==7.4.3
- pytest-bdd==7.0.1
- pytest-html==4.1.1
- pytest-metadata==3.0.0

## 📊 Запуск тестов

### Базовые команды

```bash
# Запустить ВСЕ тесты (pytest + BDD) с HTML отчетом
pytest -v

# Запустить только pytest тесты (без BDD)
pytest tests/test_api.py tests/test_reqres_api.py -v

# Запустить только BDD тесты
pytest tests/bdd/ -v

# Запустить конкретный feature файл
pytest tests/bdd/features/posts.feature -v
pytest tests/bdd/features/reqres_users.feature -v
```

### Запуск по маркерам

```bash
# Только позитивные тесты
pytest -m positive -v

# Только негативные тесты
pytest -m negative -v

# Только граничные случаи
pytest -m edge -v

# Только smoke тесты
pytest -m smoke -v

# Тесты для конкретного API
pytest -m jsonplaceholder -v
pytest -m reqres -v
```

### Генерация отчетов

```bash
# HTML отчет
pytest --html=reports/report.html --self-contained-html -v

# HTML отчет с подробными логами
pytest --html=reports/report.html --self-contained-html -v -s

# Запуск с coverage
pip install pytest-cov
pytest --cov=tests --cov-report=html -v
```

### Использование скриптов

**Linux/Mac:**
```bash
chmod +x run_tests.sh
./run_tests.sh
```

**Windows:**
```cmd
run_tests.bat
```

## 📝 Покрытие тестов

### JSONPlaceholder API (20 тестов)

#### Позитивные сценарии (8 тестов):
1. ✅ GET all posts
2. ✅ GET single post by ID
3. ✅ POST create new post
4. ✅ PUT update post
5. ✅ PATCH partial update
6. ✅ DELETE post
7. ✅ GET with correct headers
8. ✅ GET with query parameters (filtering)

#### Негативные сценарии (6 тестов):
9. ❌ GET non-existent post (404)
10. ❌ POST with missing required fields
11. ❌ POST with invalid data types
12. ❌ GET invalid endpoint (404)
13. ❌ Unsupported HTTP method
14. ❌ PUT to non-existent resource

#### Граничные случаи (6 тестов):
15. 🔸 POST with empty payload
16. 🔸 POST with very large payload
17. 🔸 Rate limiting simulation
18. 🔸 GET with ID = 0
19. 🔸 GET with negative ID
20. 🔸 Special characters in filter

### ReqRes API (10 тестов)

#### Позитивные сценарии (6 тестов):
21. ✅ GET list of users
22. ✅ GET single user by ID
23. ✅ POST create new user
24. ✅ PUT update user
25. ✅ POST login with valid credentials
26. ✅ POST register new user

#### Негативные сценарии (4 теста):
27. ❌ GET non-existent user (404)
28. ❌ POST login without password (400)
29. ❌ POST register without email (400)
30. ❌ GET invalid endpoint (404)

### BDD Сценарии (13 сценариев в 4 feature файлах)

#### posts.feature (5 сценариев):
- Get all posts successfully
- Create a new post successfully
- Update a post successfully
- Delete a post successfully
- Get non-existent post returns 404

#### users.feature (3 сценария):
- Get all users successfully
- Get a specific user by ID
- Get user with invalid ID

#### comments.feature (3 сценария):
- Get all comments successfully
- Filter comments by post ID
- Create a new comment

#### reqres_users.feature (4 сценария):
- Get paginated users list
- Create a new user in ReqRes
- Login with valid credentials
- Login fails without password

## 📈 Логирование

Проект использует многоуровневое логирование:

### Уровни логов:
- **INFO**: Общая информация о выполнении тестов (консоль)
- **DEBUG**: Детальная информация (файлы логов)

### Файлы логов:
- `reports/test_logs.log` - Детальные логи всех тестов
- `reports/test_execution.log` - Логи выполнения тестов

### Что логируется:
- ✅ Начало и конец каждого теста
- ✅ HTTP запросы (метод, URL, payload)
- ✅ HTTP ответы (статус, headers, body)
- ✅ Assertions и их результаты
- ✅ Ошибки и предупреждения

## 🎯 Используемые API

### 1. JSONPlaceholder
- **URL**: https://jsonplaceholder.typicode.com
- **Endpoints**: /posts, /users, /comments
- **Особенности**: Mock API, всегда возвращает успешные ответы

### 2. ReqRes
- **URL**: https://reqres.in/api
- **Endpoints**: /users, /login, /register
- **Особенности**: Реальная валидация данных, коды ошибок

## 🏷️ Маркеры pytest

Тесты размечены следующими маркерами:

- `@pytest.mark.positive` - Позитивные тесты
- `@pytest.mark.negative` - Негативные тесты
- `@pytest.mark.edge` - Граничные случаи
- `@pytest.mark.smoke` - Smoke тесты
- `@pytest.mark.regression` - Регрессионные тесты
- `@pytest.mark.jsonplaceholder` - Тесты JSONPlaceholder
- `@pytest.mark.reqres` - Тесты ReqRes

## 📊 Просмотр отчетов

После запуска тестов откройте:

1. **HTML отчет**: `reports/report.html` (откройте в браузере)
2. **Логи**: `reports/test_logs.log` (текстовый редактор)

HTML отчет содержит:
- ✅ Общую статистику тестов
- ✅ Детальные результаты каждого теста
- ✅ Время выполнения
- ✅ Описание тестов
- ✅ Stack traces для failed тестов

## 🛠️ Дополнительные команды

```bash
# Запуск с watch (автоматический перезапуск при изменениях)
pip install pytest-watch
ptw

# Запуск конкретного теста по имени
pytest tests/test_api.py::TestJSONPlaceholderAPI::test_get_all_posts_success -v

# Запуск с остановкой на первой ошибке
pytest -x

# Запуск последних failed тестов
pytest --lf

# Параллельное выполнение (быстрее)
pip install pytest-xdist
pytest -n auto
```

## 📧 Автор

Проект создан для выполнения Assignment 7 по API тестированию.

## 📄 Лицензия

Образовательный проект для учебных целей.

---

**Примечание**: Убедитесь что у вас есть интернет соединение для доступа к API.
