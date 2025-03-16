# Проект по автоматизации https://qa-scooter.praktikum-services.ru/

**Java 11**

**junit 4.13.2**

**allure-maven 2.10.0**

**rest-assured 4.4.0**



# Инструкция по запуску тестов и генерации отчетов Allure

1. **Очистка и запуск тестов**
   Выполните следующую команду в терминале:
   ```bash
   mvn clean test

2. **Перейдите в директорию с результатами Allure:**
    ```bash
    cd target/allure-results


3. **Выполните команду для запуска сервера Allure:**
    ```bash
    mvn allure:serve
