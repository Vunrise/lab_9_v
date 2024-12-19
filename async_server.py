import asyncio


# Функция обработки клиентских подключений
async def handle_echo(reader, writer):
    # Чтение данных от клиента
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Получено сообщение от {addr}: {message}")

    # Отправка данных обратно клиенту (эхо)
    writer.write(data)
    await writer.drain()
    print(f"Сообщение отправлено обратно клиенту {addr}")

    # Закрытие соединения
    writer.close()
    await writer.wait_closed()
    print(f"Соединение с {addr} закрыто")


# Основная корутина для запуска сервера
async def main():
    HOST = '127.0.0.1'  # Локальный хост
    PORT = 8888         # Порт для прослушивания
    server = await asyncio.start_server(handle_echo, HOST, PORT)

    addr = server.sockets[0].getsockname()
    print(f"Сервер запущен и слушает {addr}")

    async with server:
        await server.serve_forever()

# Запуск сервера
if __name__ == "__main__":
    asyncio.run(main())
