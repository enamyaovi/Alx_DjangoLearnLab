BEGIN;
--
-- Create model Book
--
CREATE TABLE "bookshelf_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "author" varchar(100) NOT NULL, "publication_year" integer NOT NULL);
COMMIT;
BEGIN;
--
-- Create model Author
--
CREATE TABLE "relationship_app_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model Book
--
CREATE TABLE "relationship_app_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "author_id" bigint NOT NULL REFERENCES "relationship_app_author" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Library
--
CREATE TABLE "relationship_app_library" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL);
CREATE TABLE "relationship_app_library_books" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "library_id" bigint NOT NULL REFERENCES "relationship_app_library" ("id") DEFERRABLE INITIALLY DEFERRED, "book_id" bigint NOT NULL REFERENCES "relationship_app_book" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Librarian
--
CREATE TABLE "relationship_app_librarian" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "library_id" bigint NOT NULL UNIQUE REFERENCES "relationship_app_library" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "relationship_app_book_author_id_4973e502" ON "relationship_app_book" ("author_id");
CREATE UNIQUE INDEX "relationship_app_library_books_library_id_book_id_8fffb898_uniq" ON "relationship_app_library_books" ("library_id", "book_id");
CREATE INDEX "relationship_app_library_books_library_id_0bbe1a77" ON "relationship_app_library_books" ("library_id");
CREATE INDEX "relationship_app_library_books_book_id_ad2f6e74" ON "relationship_app_library_books" ("book_id");
COMMIT;
