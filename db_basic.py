import psycopg2
from datetime import datetime

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
    
    # 4. Выполняем наш запрос 
    query = """
        INSERT INTO weather_stats (city, temperature, recorded_at) VALUES (%s, %s, %s);
    """
    muh_time = datetime.now()
    eben_time = datetime.now()
    new_cities = (('Muhosransk', 99, muh_time),
                  ('Ebenevsk', 0, eben_time))
    for record in new_cities:        
        cursor.execute(query, record)
    connection.commit()

    new_query = ("""
        SELECT * FROM weather_stats;
""")
    cursor.execute(new_query)
    connection.commit()
    
    # 5. Получаем результат
    results = cursor.fetchall()
    
    print(results)
    for row in results:
        print(f"- {row}")

except Exception as error:
    print(f"Ошибка при работе с Postgres: {error}")

finally:
    # 6. Обязательно закрываем соединение, чтобы не тратить ресурсы
    if connection:
        cursor.close()
        connection.close()
        print("\nСоединение с базой закрыто.")