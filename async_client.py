import asyncio


# Функция для подключения клиента и обмена сообщениями
async def tcp_echo_client():
    HOST = '127.0.0.1'
    PORT = 8888
    reader, writer = await asyncio.open_connection(HOST, PORT)

    message = "Hello"
    print(f"Отправлено сообщение: {message}")
    writer.write(message.encode())
    await writer.drain()

    # Чтение ответа от сервера
    data = await reader.read(100)
    print(f"Получено сообщение от сервера: {data.decode()}")

    # Закрытие соединения
    print("Закрытие соединения")
    writer.close()
    await writer.wait_closed()

# Запуск клиента
if __name__ == "__main__":
    asyncio.run(tcp_echo_client())
