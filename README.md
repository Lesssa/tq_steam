# e.livshits
# Задание 2
Чтобы запустить тесты, необходимо выполнить файлы test_about.py и test_topselling.py. Чтобы подтянуть зависимости, которые написаны в файле requirements.txt, необходимо в командной строке в директории проекта, где лежит файл с зависимостями, запустить команду:
`pip install -r requirements.txt`

Есть некоторые проблемы:
1. Есть хардкод, который стоило бы убрать, но я не успела
2. В местах, где используется time.sleep, я пыталась сделать иначе, но скрипт не работал, как надо.
3. Иногда тесты завершаются ошибкой, потому что, например, несмотря на ожидание элементы не находятся
4. Во втором кейсе может открываться страница не Вархаммера, а Стардью, потому что содержимое отловить не удалось, хот попытки были.
5. Стоило добавить обработку баннера про куки, он иногда прерывает выполнение кейса.