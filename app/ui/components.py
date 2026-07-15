from rich.panel import Panel

from app.ui.theme import Theme, console


class Components:

    @staticmethod
    def title(text):

        console.print()

        console.print(
            Panel.fit(
                text,
                style=Theme.TITLE
            )
        )

    @staticmethod
    def section(text):

        console.rule(
            f"[{Theme.HEADER}]{text}[/{Theme.HEADER}]"
        )

    @staticmethod
    def field(label, value):

        console.print(
            f"[{Theme.LABEL}]{label:<20}[/{Theme.LABEL}] "
            f"[{Theme.VALUE}]{value}[/{Theme.VALUE}]"
        )

    @staticmethod
    def success(text):

        console.print(
            text,
            style=Theme.SUCCESS
        )

    @staticmethod
    def warning(text):

        console.print(
            text,
            style=Theme.WARNING
        )

    @staticmethod
    def error(text):

        console.print(
            text,
            style=Theme.ERROR
        )

    @staticmethod
    def separator():

        console.rule()