from http.server import BaseHTTPRequestHandler, HTTPServer



# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __det_html_content(self):
        # Открываем файл с html-кодом
        with open('index.html', 'r', encoding="utf8") as file:
            html_code = file.read()

        return html_code

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        content = self.__det_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")