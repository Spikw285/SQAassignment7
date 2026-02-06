# conftest.py
import pytest
import logging
import os
from datetime import datetime

# Создаем директорию для отчетов если её нет
os.makedirs('reports', exist_ok=True)


# Настройка логирования
def setup_logger(name):
    """Создает и настраивает logger для тестов"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Консольный handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_format)

    # Файловый handler
    file_handler = logging.FileHandler('reports/test_execution.log')
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - [%(levelname)s] - %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


@pytest.fixture(scope='session')
def logger():
    """Session-wide logger fixture"""
    return setup_logger('APITests')


@pytest.fixture(autouse=True)
def log_test_info(request, logger):
    """Автоматически логирует информацию о каждом тесте"""
    test_name = request.node.name
    logger.info("=" * 80)
    logger.info(f"STARTING TEST: {test_name}")
    logger.info("=" * 80)

    yield

    logger.info("=" * 80)
    logger.info(f"FINISHED TEST: {test_name}")
    logger.info("=" * 80)
    logger.info("")


# Хуки для pytest-html
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Добавляет дополнительную информацию в HTML отчет"""
    outcome = yield
    report = outcome.get_result()

    # Добавляем extra информацию только для failed тестов
    if report.when == 'call':
        extra = getattr(report, 'extra', [])

        if report.failed:
            try:
                # Импортируем pytest_html только если он доступен
                import pytest_html
                # Добавляем timestamp
                extra.append(pytest_html.extras.text(
                    f"Failure Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                ))

                # Если есть логи, добавляем их
                if hasattr(item, 'test_log'):
                    extra.append(pytest_html.extras.text(
                        item.test_log,
                        name='Test Logs'
                    ))
            except ImportError:
                # pytest-html не установлен, пропускаем
                pass

        report.extra = extra


def pytest_html_report_title(report):
    """Устанавливает заголовок HTML отчета"""
    report.title = "API Testing Report"


def pytest_configure(config):
    """Добавляет метаданные в HTML отчет"""
    # Проверяем наличие _metadata атрибута (добавляется pytest-metadata)
    if hasattr(config, '_metadata'):
        config._metadata['Project'] = 'API Testing Assignment'
        config._metadata['Tester'] = 'Your Name'
        config._metadata['APIs Tested'] = 'JSONPlaceholder, ReqRes, DummyAPI'
        config._metadata['Test Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def pytest_html_results_table_header(cells):
    """Настраивает заголовки таблицы результатов"""
    cells.insert(2, '<th>Description</th>')
    cells.insert(3, '<th>Duration (s)</th>')


def pytest_html_results_table_row(report, cells):
    """Добавляет дополнительные колонки в таблицу результатов"""
    # Проверяем, что это тестовый отчет с duration (а не CollectReport)
    if hasattr(report, 'duration'):
        cells.insert(2, f'<td>{getattr(report, "description", "N/A")}</td>')
        cells.insert(3, f'<td>{report.duration:.2f}</td>')
    else:
        # Для отчетов без duration (например CollectReport)
        cells.insert(2, '<td>-</td>')
        cells.insert(3, '<td>-</td>')


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Добавляет summary в HTML отчет"""
    prefix.extend([
        "<h2>Test Summary</h2>",
        "<p>This report contains results of API testing for JSONPlaceholder, ReqRes, and DummyAPI APIs.</p>"
    ])