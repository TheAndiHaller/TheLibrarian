from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable

class BooksApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        table = DataTable()
        table.add_columns("Title", "Author", "Status")
        table.add_rows([
            ("Snow Crash", "Neal Stephenson", "Read"),
            ("Dune", "Frank Herbert", "Unread"),
        ])
        yield table
        yield Footer()

if __name__ == "__main__":
    BooksApp().run()
