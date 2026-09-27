CREATE DATABASE IF NOT EXISTS project1;
USE project1;

DROP TABLE IF EXISTS borrower_list;
DROP TABLE IF EXISTS memberships;
DROP TABLE IF EXISTS book_1;

CREATE TABLE book_1 (
    Book VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Publisher VARCHAR(100),
    Availability VARCHAR(10)
);

CREATE TABLE borrower_list (
    Name VARCHAR(100),
    Book VARCHAR(100),
    Date_of_borrowing DATE,
    Date_of_return DATE,
    Compensation VARCHAR(50),
    Membership VARCHAR(20),
    Payment_mode VARCHAR(20)
);

INSERT INTO book_1 (Book, Author, Genre, Publisher, Availability) VALUES
('Harry Potter', 'J.K. Rowling', 'Fantasy', 'Bloomsbury', 'No'),
('1984', 'George Orwell', 'Dystopian', 'Secker & Warburg', 'No'),
('To Kill a Mockingbird', 'Harper Lee', 'Classic', 'J.B. Lippincott', 'Yes'),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 'Allen & Unwin', 'No'),
('The Alchemist', 'Paulo Coelho', 'Fiction', 'HarperOne', 'No'),
('Pride and Prejudice', 'Jane Austen', 'Romance', 'T. Egerton', 'Yes'),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 'Scribner', 'Yes'),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 'Little, Brown', 'Yes'),
('Moby Dick', 'Herman Melville', 'Adventure', 'Harper & Brothers', 'No'),
('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 'Allen & Unwin', 'Yes'),
('Brave New World', 'Aldous Huxley', 'Dystopian', 'Chatto & Windus', 'Yes'),
('Crime and Punishment', 'Fyodor Dostoevsky', 'Psychological Fiction', 'The Russian Messenger', 'Yes'),
('War and Peace', 'Leo Tolstoy', 'Historical Fiction', 'The Russian Messenger', 'Yes'),
('Jane Eyre', 'Charlotte Bronte', 'Romance', 'Smith, Elder & Co.', 'Yes'),
('Wuthering Heights', 'Emily Bronte', 'Gothic Fiction', 'Thomas Cautley Newby', 'Yes'),
('Fahrenheit 451', 'Ray Bradbury', 'Dystopian', 'Ballantine Books', 'Yes'),
('The Picture of Dorian Gray', 'Oscar Wilde', 'Gothic Fiction', 'Lippincott', 'Yes'),
('Dracula', 'Bram Stoker', 'Horror', 'Archibald Constable', 'Yes'),
('Frankenstein', 'Mary Shelley', 'Sci-Fi', 'Lackington, Hughes', 'Yes'),
('The Odyssey', 'Homer', 'Epic Poetry', 'Penguin Classics', 'Yes'),
('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'Non-Fiction', 'Harper', 'Yes'),
('Atomic Habits', 'James Clear', 'Self-Help', 'Avery', 'Yes'),
('Thinking, Fast and Slow', 'Daniel Kahneman', 'Psychology', 'Farrar, Straus and Giroux', 'Yes'),
('The Da Vinci Code', 'Dan Brown', 'Thriller', 'Doubleday', 'Yes'),
('Angels & Demons', 'Dan Brown', 'Mystery', 'Pocket Books', 'Yes'),
('Dune', 'Frank Herbert', 'Sci-Fi', 'Chilton Books', 'Yes'),
('Foundation', 'Isaac Asimov', 'Sci-Fi', 'Gnome Press', 'Yes'),
('Neuromancer', 'William Gibson', 'Cyberpunk', 'Ace Books', 'Yes'),
('The Shining', 'Stephen King', 'Horror', 'Doubleday', 'Yes'),
('IT', 'Stephen King', 'Horror', 'Viking', 'Yes'),
('A Game of Thrones', 'George R.R. Martin', 'Fantasy', 'Bantam Spectra', 'Yes'),
('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 'Alfred A. Knopf', 'Yes'),
('Life of Pi', 'Yann Martel', 'Adventure', 'Knopf Canada', 'Yes'),
('The Kite Runner', 'Khaled Hosseini', 'Drama', 'Riverhead Books', 'Yes'),
('A Thousand Splendid Suns', 'Khaled Hosseini', 'Drama', 'Riverhead Books', 'Yes'),
('Animal Farm', 'George Orwell', 'Satire', 'Secker & Warburg', 'Yes'),
('The Book Thief', 'Markus Zusak', 'Historical Fiction', 'Picador', 'Yes'),
('Slaughterhouse-Five', 'Kurt Vonnegut', 'Sci-Fi', 'Delacorte', 'Yes'),
('Catch-22', 'Joseph Heller', 'Satire', 'Simon & Schuster', 'Yes'),
('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Magical Realism', 'Harper & Row', 'Yes'),
('The Metamorphosis', 'Franz Kafka', 'Absurdist Fiction', 'Kurt Wolff Verlag', 'Yes'),
('The Stranger', 'Albert Camus', 'Philosophical', 'Gallimard', 'Yes'),
('Beloved', 'Toni Morrison', 'Historical Fiction', 'Alfred A. Knopf', 'Yes'),
('The God of Small Things', 'Arundhati Roy', 'Fiction', 'IndiaInk', 'Yes'),
('Midnight''s Children', 'Salman Rushdie', 'Magical Realism', 'Jonathan Cape', 'Yes'),
('Norwegian Wood', 'Haruki Murakami', 'Romance', 'Kodansha', 'Yes'),
('Kafka on the Shore', 'Haruki Murakami', 'Magical Realism', 'Shinchosha', 'Yes'),
('The Silent Patient', 'Alex Michaelides', 'Psychological Thriller', 'Celadon Books', 'Yes'),
('Educated', 'Tara Westover', 'Memoir', 'Random House', 'Yes'),
('Steve Jobs', 'Walter Isaacson', 'Biography', 'Simon & Schuster', 'Yes');

INSERT INTO borrower_list (Name, Book, Date_of_borrowing, Date_of_return, Compensation, Membership, Payment_mode) VALUES
('Rohan Mehta', '1984', '2025-05-03', '2025-05-17', 'None', 'Platinum', 'None'),
('Rahul Desai', 'The Great Gatsby', '2025-05-05', '2025-05-20', 'Late Fee', 'Silver', 'Net Banking'),
('Sneha Kapoor', 'Moby Dick', '2025-05-11', '2025-05-25', 'None', 'Gold', 'UPI'),
('Aarav Shah', 'The Hobbit', '2025-06-01', '2025-06-15', 'Late Fee', 'Silver', 'Cash'),
('Divya Patel', 'Pride and Prejudice', '2025-06-05', '2025-06-19', 'None', 'Platinum', 'Card'),
('Mathew', 'The Great Gatsby', '2025-06-14', '2025-06-28', 'None', 'Silver', 'None');

CREATE TABLE memberships (
    Name VARCHAR(100),
    MembershipType VARCHAR(20),
    Price INT,
    PurchaseDate DATE
);

INSERT INTO memberships (Name, MembershipType, Price, PurchaseDate) VALUES
('Amit Sharma', 'Silver', 100, '2025-06-01'),
('Riya Mehta', 'Gold', 200, '2025-06-05'),
('Kabir Joshi', 'Platinum', 300, '2025-06-10');