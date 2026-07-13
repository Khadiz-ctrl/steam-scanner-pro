from datetime import datetime


class Logger:

    FILE_NAME = "scanner.log"

    @staticmethod
    def info(message):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(Logger.FILE_NAME, "a", encoding="utf-8") as file:

            file.write(f"[{now}] INFO  {message}\n")