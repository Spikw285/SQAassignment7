#!/bin/bash

echo "======================================"
echo "API Testing - Test Runner"
echo "======================================"
echo ""
echo "Выберите опцию:"
echo "1. Запустить все тесты"
echo "2. Только pytest тесты"
echo "3. Только BDD тесты"
echo "4. JSONPlaceholder тесты"
echo "5. ReqRes тесты"
echo "6. Генерировать HTML отчет"
echo "7. Запустить smoke тесты"
echo "8. Запустить позитивные тесты"
echo "9. Запустить негативные тесты"
echo ""
read -p "Введите номер (1-9): " choice

case $choice in
    1)
        echo "Запуск всех тестов..."
        pytest -v
        ;;
    2)
        echo "Запуск pytest тестов..."
        pytest tests/test_api.py tests/test_reqres_api.py -v
        ;;
    3)
        echo "Запуск BDD тестов..."
        pytest tests/bdd/ -v
        ;;
    4)
        echo "Запуск JSONPlaceholder тестов..."
        pytest -m jsonplaceholder -v
        ;;
    5)
        echo "Запуск ReqRes тестов..."
        pytest -m reqres -v
        ;;
    6)
        echo "Генерация HTML отчета..."
        pytest --html=reports/report.html --self-contained-html -v
        echo "Отчет сохранен в reports/report.html"
        ;;
    7)
        echo "Запуск smoke тестов..."
        pytest -m smoke -v
        ;;
    8)
        echo "Запуск позитивных тестов..."
        pytest -m positive -v
        ;;
    9)
        echo "Запуск негативных тестов..."
        pytest -m negative -v
        ;;
    *)
        echo "Неверный выбор"
        ;;
esac

echo ""
echo "======================================"
echo "Проверьте логи в директории reports/"
echo "======================================"
