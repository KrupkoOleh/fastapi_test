# Test Task FastAPI

Тестовий проєкт для роботою з публікаціями, у яких є коментарі та теми. 
Проєкт написаний на Python використовуючи бібліотеку FastAPI.  
**У проєкті є такі функції**:
- Отримання списку/отримання одного/створення/оновлення/видалення поста
- Отримання списку/отримання одного/створення/оновлення/видалення коментаря
- Отримання списку/отримання одного/створення/оновлення/видалення теми  

**З додаткової функціональності**:
- Сортування/Пагінація/Авторизація фіксованого користувача

## Зміст

- [Встановлення](#встановлення)
- [Стек технологій](#стек-технологій)
- [База даних](#база-даних)
- [Контакти](#контакти)

## Встановлення

1. **Клонування репозиторію:**
   ```bash
   git clone https://github.com/KrupkoOleh/fastapi_test.git
   
2. **Створення .env**:
   ```bash
   # Дублювання файлу під новим ім'ям
   # Linux / macOS:
   cp .env_example .env
   # Windows:
   Copy-Item .env_example .env
   # Заповнити потрібні змінні у файлі .env
   DB_HOST=
   DB_PORT=
   DB_USER=
   DB_PASS=
   DB_NAME=

3. **Створення та активація віртуального середовища**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux / macOS:
   source venv/bin/activate

4. **Встановлення залежностей**:
   ```bash
   pip install -r requirements.txt
   pip install "fastapi[standard]"

5. **Створіть та застосуйте міграції бази даних за допомогою Alembic**:
   ```bash
   alembic revision --autogenerate -m "initial migration"
   alembic upgrade head
6. **Встановлення адреси бази даних**:
   ```bash
   # У файлі alembic.ini задати адресу бази даних PostgreSQL
   sqlalchemy.url = postgresql://user:password@localhost:5432/yourdatabase
   
7. **Запуск проєкту**:
   ```bash
   fastapi dev main.py


## Стек технологій
1. **Мова програмування**: Python (версія 3.12)
2. **Фреймворк**: FastAPI
3. **Валідація**: Pydantic для вхідних/вихідних моделей
4. **ORM**: SQLAlchemy
5. **База даних**: PostgreSQL
6. **Модульна перевірка коду**: flake8
7. **Міграції баз даних**: Alembic

## База даних

![Зображення бази даних](https://i.postimg.cc/JngVfYRY/photo-2025-06-01-14-48-57.jpg)

## Контакти
Якщо є питання або пропозиції, пишіть: 
- [Telegram](https://t.me/Oliviezka)
- [Gmail](mailto:oleg.krupko.2003@gmail.com) 
- [Linkedin](https://www.linkedin.com/in/krupkooleh/)