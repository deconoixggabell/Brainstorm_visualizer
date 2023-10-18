-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema brainstorm_visualizer
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `brainstorm_visualizer` ;

-- -----------------------------------------------------
-- Schema brainstorm_visualizer
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `brainstorm_visualizer` DEFAULT CHARACTER SET utf8mb3 ;
USE `brainstorm_visualizer` ;

-- -----------------------------------------------------
-- Table `brainstorm_visualizer`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `brainstorm_visualizer`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `brainstorm_visualizer`.`ideas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `brainstorm_visualizer`.`ideas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `main_idea` VARCHAR(255) NULL DEFAULT NULL,
  `cat_1` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_1_1` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_1_2` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_1_3` VARCHAR(255) NULL DEFAULT NULL,
  `cat_2` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_2_1` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_2_2` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_2_3` VARCHAR(255) NULL DEFAULT NULL,
  `cat_3` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_3_1` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_3_2` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_3_3` VARCHAR(255) NULL DEFAULT NULL,
  `cat_4` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_4_1` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_4_2` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_4_3` VARCHAR(255) NULL DEFAULT NULL,
  `cat_5` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_5_1` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_5_2` VARCHAR(255) NULL DEFAULT NULL,
  `sub_c_5_3` VARCHAR(255) NULL DEFAULT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ideas_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_ideas_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `brainstorm_visualizer`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
