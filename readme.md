# Бэкенд для задачи N - 10

На проекте используется чистая архитектура.
Вместо usecases использую services.
Структура соответстует принципам REST.
Взаимодействие построено на JWT.

в директории /ml/ хранится модуль ML.

## Запуск
1. Склонировать проект командой: git clone
2. Запустить контейнер из консоли командой: docker-compose -f docker-compose up -d --build 
3. Перейти в контейнер: docker exec -it hackathon_app_1 bash
4. Обновить данные: python create_tables.py

