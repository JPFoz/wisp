-- MySQL Script generated by MySQL Workbench
-- Fri Jun 28 23:09:17 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema weather
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema weather
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `weather` DEFAULT CHARACTER SET utf8 ;
USE `weather` ;

-- -----------------------------------------------------
-- Table `weather`.`wind_measurement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weather`.`wind_speed_measurement` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `wind_speed` DECIMAL(4,2) NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `date_created`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `weather`.`passive_measurement` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `temperature` DECIMAL(10,2) NULL,
  `humidity` DECIMAL(10,2) NULL,
  `pressure` DECIMAL(10,2) NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `date_created`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `weather`.`wind_gust_measurement` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `wind_gust` DECIMAL(4,2) NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `date_created`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
