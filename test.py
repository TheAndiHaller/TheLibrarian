from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Input, Static
from textual.screen import ModalScreen

from database.queries import *

class BooksApp(App):
    CSS = """
        ModalScreen {
            align: center middle;
            background: rgba(0,0,0,0.75);
        }
        #details_modal {
            background: #202020;
            color: white;
            padding: 2;
            border: round white;
            width: 60%;
        }
        """
    def compose(self) -> ComposeResult:
        yield Header()

        yield Input(placeholder="Search Title", id="book_input")
        yield Static("", id="output")

        self.table = DataTable(cursor_type="row")
        yield self.table

        yield Static("", id="details")
        yield Footer()
    
    def on_mount(self):
        self.table.add_columns("ID", "Title", "Author", "Status")
        self.book_list = get_all_books()
        for book in self.book_list:
            self.table.add_row(book.get("eid"), book.get("title"), book.get("author"), book.get("status"), key=book.get("eid"))


    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Called when the user presses Enter in the input box."""
        title = event.value.strip()
        output = self.query_one("#output", Static)
        if title:
            output.update(f"You entered: [bold yellow]{title}[/]")
        else:
            output.update("[red]No title entered[/]")

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Triggered when user presses Enter on a row."""
        row_key = event.row_key  # index or key (if you used add_row(key=...))
        """
        row_data = self.table.get_row(row_key)
        id, title, author, status = row_data

        book_details = self.book_list[int(row_key.value)-1].get("description")

        details = self.query_one("#details", Static)
        details.update(
            f"[bold yellow]{title}[/]\nby {author}\nStatus: [green]{status}[/]\nDetails: [white]{book_details}[/]"
            #f"{row_data}"
        )
        """
        book = self.book_list[int(row_key.value)-1]
        self.push_screen(BookDetailsScreen(book))
        # Optional: log to console
        #self.log(f"Row selected: {row_key} -> {row_data}")

class BookDetailsScreen(ModalScreen):
    def __init__(self, book):
        super().__init__()
        self.book = book

    def compose(self) -> ComposeResult:
        yield Static(
            f"[b]{self.book['title']}[/b]\n"
            f"Author: {self.book['author']}\n"
            f"Pages: {self.book.get('pages', '?')}\n\n"
            f"{self.book.get('description', 'No description')}",
            id="details_modal"
        )

    def on_key(self, event):
        if event.key == "escape":
            self.app.pop_screen()  # close modal

if __name__ == "__main__":
    BooksApp().run()

