from http.server import BaseHTTPRequestHandler, HTTPServer

# Hастройки доступа
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс для обработки входящих запросов"""

    @staticmethod
    def __get_html_content():
        with open('index.html', encoding='utf-8') as index:
            return index.read()

    def do_get(self):
        """ Метод для обработки входящих GET-запросов """
        page = self.__get_html_content()

        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html; charset=utf-8")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page, "utf-8"))  # Тело ответа


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