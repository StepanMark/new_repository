import psycopg2

# 1. Параметры подключения (те же, что мы вводили в DBeaver)
connection_params = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "12345"
}

try:
    # 2. Устанавливаем соединение
    connection = psycopg2.connect(**connection_params)
    
    # 3. Создаем "курсор" — это объект для выполнения команд
    cursor = connection.cursor()
    
    # 4. Выполняем наш запрос (тот самый JOIN)
    query = """
        SELECT u.name
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        WHERE o.order_id IS NULL;
    """
    cursor.execute(query)
    
    # 5. Получаем результат
    results = cursor.fetchall()
    
    print("Пользователи без покупок:")
    print(results)
    for row in results:
        print(f"- {row[0]}")

except Exception as error:
    print(f"Ошибка при работе с Postgres: {error}")

finally:
    # 6. Обязательно закрываем соединение, чтобы не тратить ресурсы
    if connection:
        cursor.close()
        connection.close()
        print("\nСоединение с базой закрыто.")