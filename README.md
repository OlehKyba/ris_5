# РІС. Практична робота №5.

## Завдання
* Налаштувати реплікацію Master-Slave та Master-Master на будь якій базі даних.
* Створити тестове застосування, що зможе викоритовувати репліку (писати в одну ноду, зчитувати з іншої).
* Описати процес налаштування, проблеми з якими зіштовхнулися та яким чином їх подолали.


## Описання практичної роботи
1. У файлі [docker-compose.yml](./docker-compose.yml) були налаштовані контейнери
для асинхронної Master-Slave реплікація для `PostgreSQL` та Master-Master реплікація 
для `MariaDB`.
2. У файлі [test_bl.py](./ris_5/test/test_bl.py) були написані тести для перевірки коректності
роботи реплікацій. Алгоритм тестів простий: вони завантажують файл [dataset.csv](./data/dataset.csv)
у базу даних та виконують два запита для агрегації даних: `count_dataset_items` та `count_dataset_by_sex`,
що описані у файлі [bl.py](./ris_5/bl.py).
3. Тести проходять у випадку отримання правильних значень агрегацій, що можливо лише при наявності
всіх даних у репліках.
   

## Як запустити проєкт?
1. Виконати команду для збору `docker image` з кодом `python`:
```bash
make build
```
2. Запустити БД:
```bash
make run
```
3. Запустити тести:
```bash
make test
```

## Висновки
На цій практичній роботі я налаштував Master-Slave та Master-Master реплікації на `PostgreSQL` та
`MariaDB` за допомогою технології `Docker` та `docker-compose`. Також я написав автоматичні тести, 
що перевіряють коректність роботи реплікацій за допомогою мови програмування `python`. Під час виконання
практичної роботи не зіштовхнувся з серйозниим проблемами завдяки чудово описаній документації docker image
баз даних: [PostgreSQL](https://github.com/bitnami/bitnami-docker-postgresql#readme) та 
[MariaDB](https://github.com/bitnami/bitnami-docker-mariadb-galera#readme).