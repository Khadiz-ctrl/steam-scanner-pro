from app.scanner.service import ScannerService


def main():

    scanner = ScannerService()

    scanner.run()


if __name__ == "__main__":
    main()