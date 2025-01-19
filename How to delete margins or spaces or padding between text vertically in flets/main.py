from flet import Page, Column, Text, app


def main(page: Page):
    page.controls = [
        Column(
            controls=[Text("hello world"), Text("hello world")],
            alignment="start",  # Align items at the start (default behavior)
            vertical_alignment="center",  # Center the text vertically in each row if necessary
        )
    ]
    page.update()


app(main)
