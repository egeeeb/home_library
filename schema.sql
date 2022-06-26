-- MySQL Script generated by MySQL Workbench
-- Sat Apr 23 20:25:49 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema home_library
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema home_library
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `home_library` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `home_library` ;

-- -----------------------------------------------------
-- Table `home_library`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `home_library`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `author` VARCHAR(100) NULL DEFAULT NULL,
  `publisher` VARCHAR(100) NULL DEFAULT NULL,
  `status` VARCHAR(45) NOT NULL,
  `owner` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 513
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `home_library`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `home_library`.`ratings` (
  `good_reads` FLOAT NULL DEFAULT NULL,
  `book_id` INT NOT NULL,
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`book_id`),
  UNIQUE INDEX `book_id_UNIQUE` (`book_id` ASC) VISIBLE,
  CONSTRAINT `book_id_fk`
    FOREIGN KEY (`book_id`)
    REFERENCES `home_library`.`books` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


CREATE TABLE `home_library`.`goodreads_genres` (
  `name` VARCHAR(300) NOT NULL,
  `book_id` INT NOT NULL,
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX `genre_book_id_fk_idx` (`book_id` ASC) VISIBLE,
  INDEX `genre_name_idx` (`name` ASC) VISIBLE,
  UNIQUE INDEX `genre_book_id_name_uq_idx` (`name` ASC, `book_id` ASC) VISIBLE,
  CONSTRAINT `genre_book_id_fk_idx`
    FOREIGN KEY (`book_id`)
    REFERENCES `home_library`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `home_library`.`goodreads_quotes` (
  `book_id` INT NOT NULL,
  `number_of_quotes` INT NOT NULL DEFAULT 0,
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`book_id`),
  UNIQUE INDEX `book_id_UNIQUE` (`book_id` ASC) VISIBLE,
  CONSTRAINT `book_id_FK_quotes`
    FOREIGN KEY (`book_id`)
    REFERENCES `home_library`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
