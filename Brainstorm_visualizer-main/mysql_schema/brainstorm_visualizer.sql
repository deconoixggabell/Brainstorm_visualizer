-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema brainstorm_visualizer
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `brainstorm_visualizer` ;

-- -----------------------------------------------------
-- Schema brainstorm_visualizer
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `brainstorm_visualizer` DEFAULT CHARACTER SET utf8 ;
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
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `brainstorm_visualizer`.`ideas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `brainstorm_visualizer`.`ideas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `main_idea` VARCHAR(255) NULL,
  `cat_i` VARCHAR(255) NULL,
  `sub_c_i` VARCHAR(255) NULL,
  `sub_c_ii` VARCHAR(255) NULL,
  `sub_c_iii` VARCHAR(255) NULL,
  `cat_ii` VARCHAR(255) NULL,
  `sub_c_iv` VARCHAR(255) NULL,
  `sub_c_v` VARCHAR(255) NULL,
  `sub_c_vi` VARCHAR(255) NULL,
  `cat_iii` VARCHAR(255) NULL,
  `sub_c_vii` VARCHAR(255) NULL,
  `sub_c_viii` VARCHAR(255) NULL,
  `sub_c_ix` VARCHAR(255) NULL,
  `cat_iv` VARCHAR(255) NULL,
  `sub_c_x` VARCHAR(255) NULL,
  `sub_c_xi` VARCHAR(255) NULL,
  `sub_c_xii` VARCHAR(255) NULL,
  `cat_v` VARCHAR(255) NULL,
  `sub_c_xiii` VARCHAR(255) NULL,
  `sub_c_xiv` VARCHAR(255) NULL,
  `sub_c_xv` VARCHAR(255) NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ideas_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_ideas_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `brainstorm_visualizer`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
