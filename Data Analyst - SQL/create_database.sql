DROP DATABASE IF EXISTS `dark_magician`;
CREATE DATABASE `dark_magician`; 
USE `dark_magician`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `deck` (
    `card_id` int(4) NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `atribute` varchar(50) NOT NULL,
    `level_rank` int(50) DEFAULT NULL,   
    `sub_type` varchar(50) NOT NULL,  
    `type` varchar(50) NOT NULL,
    `atk` int(50) DEFAULT NULL,
    `def` int(50) DEFAULT NULL,
    `link_level` int(50) DEFAULT NULL,
    `quantity` int(50) NOT NULL,
    `deck_location` varchar(50) DEFAULT 'Main',
  PRIMARY KEY (`card_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
INSERT INTO `deck` VALUES (DEFAULT,'Dark Magician', 'Dark', 7, 'Normal', 'Monster', 2500, 2100, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,'Apprentice Illusion Magician', 'Dark', 6, 'Effect', 'Monster', 2000, 1700, DEFAULT, 2, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,'Dark Magician Girl', 'Dark', 6, 'Effect', 'Monster', 2000, 1700, DEFAULT, 1, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,'Keeper of Dragon Magic', 'Dark', 4, 'Effect', 'Monster', 1800, 1300, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Magican's Rod", 'Dark', 3, 'Effect', 'Monster', 1600, 100, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Ash Blossom & Joyous Spring", 'Fire', 3, 'Effect', 'Monster', 0, 1800, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Magicians' Souls", 'Dark', 1, 'Effect', 'Monster', 0, 0, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"The Eye of Timaeus", 'Spell', DEFAULT, 'Normal', 'Spell', DEFAULT, DEFAULT, DEFAULT, 1, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Dark Magic Attack", 'Spell', DEFAULT, 'Normal', 'Spell', DEFAULT, DEFAULT, DEFAULT, 1, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Harpie's Feather Duster", 'Spell', DEFAULT, 'Normal', 'Spell', DEFAULT, DEFAULT, DEFAULT, 1, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Polymerization", 'Spell', DEFAULT, 'Normal', 'Spell', DEFAULT, DEFAULT, DEFAULT, 1, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Soul Servant", 'Spell', DEFAULT, 'Quick-Play', 'Spell', DEFAULT, DEFAULT, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Called By The Grave", 'Spell', DEFAULT, 'Quick-Play', 'Spell', DEFAULT, DEFAULT, DEFAULT, 1, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Dark Magical Circle", 'Spell', DEFAULT, 'Continuous', 'Spell', DEFAULT, DEFAULT, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Magician's Salvation", 'Spell', DEFAULT, 'Field', 'Spell', DEFAULT, DEFAULT, DEFAULT, 2, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Ice Dragon's Prison", 'Trap', DEFAULT, 'Normal', 'Trap', DEFAULT, DEFAULT, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Enternal Soul", 'Trap', DEFAULT, 'continuous', 'Trap', DEFAULT, DEFAULT, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Solemn Strike", 'Trap', DEFAULT, 'counter', 'Trap', DEFAULT, DEFAULT, DEFAULT, 3, DEFAULT);
INSERT INTO `deck` VALUES (DEFAULT,"Dark Magician the Dragon Knight", 'Dark', 8, 'Effect Fusion', 'Monster', 3000, 2500, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Amulet Dragon", 'Dark', 8, 'Effect Fusion', 'Monster', 2900, 2500, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Dark Paladin", 'Dark', 8, 'Effect Fusion', 'Monster', 2900, 2400, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"The Dark Magicians", 'Dark', 8, 'Effect Fusion', 'Monster', 2800, 2300, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Dark Magician Girl the Dragon Knight", 'Dark', 7, 'Effect Fusion', 'Monster', 2600, 1700, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Red-Eyes Flare Metal Dragon", 'Dark', 7, 'Effect XYZ', 'Monster', 2800, 2400, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Number 11: Big-Eye", 'Dark', 7, 'Effect XYZ', 'Monster', 2600, 2000, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Ebon Illusion Magician", 'Dark', 7, 'Effect XYZ', 'Monster', 2500, 2100, DEFAULT, 2, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Ebon High Magician", 'Dark', 7, 'Effect XYZ', 'Monster', 2300, 2800, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Norito the Moral Leader", 'Light', 6, 'Effect XYZ', 'Monster', 2700, 2000, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Photon Strike Bounzer", 'Light', 6, 'Effect XYZ', 'Monster', 2700, 2000, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"The Phantom Knights of Break Sword", 'Dark', 3, 'Effect XYZ', 'Monster', 2000, 1000, DEFAULT, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Knightmare Unicorn", 'Dark', DEFAULT, 'Effect Link', 'Monster', 2200, DEFAULT, 3, 1, 'Extra');
INSERT INTO `deck` VALUES (DEFAULT,"Knightmare Phoenix", 'Fire', DEFAULT, 'Effect Link', 'Monster', 1900, DEFAULT, 2, 1, 'Extra');