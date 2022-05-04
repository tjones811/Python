-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema burgers
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `burgers` ;

-- -----------------------------------------------------
-- Schema burgers
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `burgers` DEFAULT CHARACTER SET utf8 ;
USE `burgers` ;

-- -----------------------------------------------------
-- Table `burgers`.`restaurants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `burgers`.`restaurants` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `burgers`.`burgers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `burgers`.`burgers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `bun` VARCHAR(255) NULL DEFAULT NULL,
  `meat` VARCHAR(255) NULL DEFAULT NULL,
  `calories` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `restaurant_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_burgers_restaurants_idx` (`restaurant_id` ASC) VISIBLE,
  CONSTRAINT `fk_burgers_restaurants`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `burgers`.`restaurants` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
