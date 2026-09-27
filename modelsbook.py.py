class BookModel:
    @staticmethod
    def get_all_books(conn):
        """Retrieve all books from the database."""
        cursor = conn.cursor()
        cursor.execute("SELECT Book, Author, Genre, Availability FROM book_1")
        all_books = cursor.fetchall()
        cursor.close()
        return all_books

    @staticmethod
    def check_availability(conn, book_name):
        cursor = conn.cursor()
        cursor.execute("SELECT Availability FROM book_1 WHERE LOWER(Book) = LOWER(%s)", (book_name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None

    @staticmethod
    def update_availability(conn, book_name, is_available):
        cursor = conn.cursor()
        status = "Yes" if is_available else "No"
        cursor.execute("UPDATE book_1 SET Availability = %s WHERE LOWER(Book) = LOWER(%s)", (status, book_name))
        conn.commit()
        cursor.close()