# Sprint_7
API учебного сервиса Яндекс Самокат. Его документация: qa-scooter.praktikum-services.ru/docs/

## Запуск тестов

Для запуска всех тестов с подробным выводом используйте команду:

```bash
pytest -v  --alluredir=allure_results 
```

Для установки необходимых библиотек используете команду: 

```bash
pip3 install -r requirements.txt
```

Для запуска allure отчета: 

```bash
allure serve allure_results
```