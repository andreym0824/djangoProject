--
-- Create model Author
--
CREATE TABLE `books_author` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `salutation` varchar(10) NOT NULL, `first_name` varchar(30) NOT NULL, `last_name` varchar(40) NOT NULL, `email` varchar(254) NOT NULL, `headshot` varchar(100) NOT NULL);
--
-- Create model Publisher
--
CREATE TABLE `books_publisher` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(30) NOT NULL, `address` varchar(50) NOT NULL, `city` varchar(60) NOT NULL, `state_province` varchar(30) NOT NULL, `country` varchar(50) NOT NULL, `website` varchar(200) NOT NULL);
--
-- Create model Book
--
CREATE TABLE `books_book` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(100) NOT NULL, `publication_date` date NOT NULL, `publisher_id` integer NOT NULL);
CREATE TABLE `books_book_authors` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `book_id` integer NOT NULL, `author_id` integer NOT NULL);
ALTER TABLE `books_book` ADD CONSTRAINT `books_book_publisher_id_189e6c56_fk_books_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `books_publisher` (`id`);
ALTER TABLE `books_book_authors` ADD CONSTRAINT `books_book_authors_book_id_author_id_8714badb_uniq` UNIQUE (`book_id`, `author_id`);
ALTER TABLE `books_book_authors` ADD CONSTRAINT `books_book_authors_book_id_ed3433e7_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`);
ALTER TABLE `books_book_authors` ADD CONSTRAINT `books_book_authors_author_id_984f1ab8_fk_books_author_id` FOREIGN KEY (`author_id`) REFERENCES `books_author` (`id`);