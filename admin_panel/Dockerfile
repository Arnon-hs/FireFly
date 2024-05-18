# Установка базового образа
FROM python:3.9-slim

# Установка переменной окружения PYTHONUNBUFFERED для предотвращения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Создание и переход в рабочую директорию в контейнере
WORKDIR /app

# Копирование зависимостей проекта и установка их
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта
COPY . /app

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
