-- Sample data for testing and development
-- Run this after creating the schema to populate with sample records

-- Insert sample authors
INSERT INTO authors (first_name, last_name, birth_year, nationality) VALUES
('George', 'Orwell', 1903, 'British'),
('Jane', 'Austen', 1775, 'British'),
('F. Scott', 'Fitzgerald', 1896, 'American'),
('Harper', 'Lee', 1926, 'American'),
('J.K.', 'Rowling', 1965, 'British'),
('Gabriel', 'García Márquez', 1927, 'Colombian'),
('Toni', 'Morrison', 1931, 'American'),
('Haruki', 'Murakami', 1949, 'Japanese');

-- Insert sample books
INSERT INTO books (title, author_id, isbn, publication_year, genre, pages) VALUES
('1984', 1, '9780451524935', 1949, 'Dystopian Fiction', 328),
('Animal Farm', 1, '9780451526342', 1945, 'Political Satire', 112),
('Pride and Prejudice', 2, '9780141439518', 1813, 'Romance', 432),
('Emma', 2, '9780141439587', 1815, 'Romance', 474),
('The Great Gatsby', 3, '9780743273565', 1925, 'Literary Fiction', 180),
('To Kill a Mockingbird', 4, '9780061120084', 1960, 'Southern Gothic', 324),
('Harry Potter and the Philosopher\'s Stone', 5, '9780747532699', 1997, 'Fantasy', 223),
('Harry Potter and the Chamber of Secrets', 5, '9780747538493', 1998, 'Fantasy', 251),
('One Hundred Years of Solitude', 6, '9780060883287', 1967, 'Magical Realism', 417),
('Beloved', 7, '9781400033416', 1987, 'Historical Fiction', 324),
('Norwegian Wood', 8, '9780375704024', 1987, 'Literary Fiction', 296),
('Kafka on the Shore', 8, '9781400079278', 2002, 'Magical Realism', 505);
