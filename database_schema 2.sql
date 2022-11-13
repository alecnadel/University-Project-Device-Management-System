-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dev_mgmt_sys
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `devices`
--

DROP TABLE IF EXISTS `devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `devices` (
  `Device_Name` varchar(100) NOT NULL,
  `Device_Type` text,
  `OS_Type` text,
  `OS_Version` text,
  `Ram` text,
  `CPU` text,
  `Bits` text,
  `Screen_Resolution` text,
  `Grade` text,
  `UUID` text,
  `Available` tinyint DEFAULT '1',
  `Activity` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`Device_Name`),
  UNIQUE KEY `Device_Name_UNIQUE` (`Device_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devices`
--

LOCK TABLES `devices` WRITE;
/*!40000 ALTER TABLE `devices` DISABLE KEYS */;
INSERT INTO `devices` VALUES ('1Link','Dell Laptop','Windows','','','','','','','',1,1),('Akuma','Samsung Tab A','Android','5.0.2','2 GB','Quad-Core 1.2GHz','?','768 x 1024 (132ppi)','Low','None',0,1),('Balrog','Galaxy S7 Edge','Android','6.0.1','4 GB','Octa-Core 4x2.3 GHz & 4x1.6 GHz','?','1440 x 2560 (534ppi)','High','None',1,1),('Barret','iPhone 4','IOS','7.1.2','500MB','Single-Core 1GHz','32','640 x 960 (330ppi)','Obsolete','40b7c83097b9a803b38b193f97124f21682653a4',1,1),('Basch','iPhone 5','IOS','10.0.1','1GB','Dual-Core 1.3GHz','32','640 x 1136 (326ppi)','Low','086deb3ff832fe09fc492d835f8f539d853a70d5',1,1),('Batman','Vive','VR','','','','','','','',1,1),('Bison','Galaxy S5','Android','4.4.2','2 GB','Quad-Core 2.5GHz','?','1080 x 1920 (432ppi)','Medium','None',1,1),('Blanka','Nexus 7','Android','5.0.2','1 GB','Quad-Core 1.2GHz','?','800 x 1280 (216ppi)','Low','None',1,1),('Cid','iPhone 6+','IOS','11.2','1 GB DDR3','Dual-Core 1.4GHz','64','1080 x 1920 (401ppi)','Medium','9cda2720c72ff3e26e82e49ea796c8a4f9246f8e',1,1),('Dr Robotnik','iPad 4','IOS','10.1','1GB','Dual-Core 1.4GHz','32','1536 x 2048 (264ppi)','Medium','3e751193bdbf92b35a440f225318b5498de96c9e',1,1),('E-Honda','Galaxy Tab 1','Android','4.0.4','1 GB','Dual-Core 1GHz','?','800 x 1280 (149ppi)','Low','None',1,1),('Espio','iPad Mini 2 (retina)','IOS','11.2','1GB','Dual-Core 1.3GHz','64','1536 x 2048 (324 ppi)','Low','7ecfbae1544a8d56ccdacd6dc27ed9038196b2f5',1,1),('Fox McCloud','iPad Air (retina)','IOS','10.3.2','1 GB DDR3','Dual-Core 1.3GHz','64','1536 x 2048 (264ppi)','Medium','7c7a369fd078c67f1cc123685ad887d3e32a6552',1,1),('Fran','iPhone 6S','IOS','11.2.2','2 GB DDR 4','Dual-Core 1.85 GHz','64','1334 x 750 (326 ppi)','High','49c2e825d69a758ff9379dd1ba0b9c24913f645e',1,1),('Glados','LG G Pad','Android','4.4.2','2 GB','Quad-Core 1.7GHz','?','1200 x 1920 (273ppi)','Medium','None',1,1),('Gordon Freeman','iPod 5','IOS','9.3.5','500MB','Dual-Core 1GHz','32','640 x 1136 (326ppi)','Obsolete','8df683d2213df8bffdb6f8157e38c8b41809fb69',1,1),('Guile','HTC One mini 2','Android','4.4.2','1 GB','Quad-Core 1.2GHz','?','720 x 1280 (326ppi)','Low','None',1,1),('Gun Jack','W8 Surface','Windows','?','2 GB','Quad-Core 1.3GHz','','768 x 1366 (148ppi)','Low - Mid','',1,1),('Guy Brush','iPod 5','IOS','9','500MB','Dual-Core 1GHz','32','640 x 1136 (326ppi)','Obsolete','',1,1),('Iggy','iPod 5','IOS','8.4.1','500MB','Dual-Core 1GHz','32','640 x 1136 (326ppi)','Obsolete','ba9ff54ef1d18b27feb179271c49f90a6d813531',1,1),('IpadPro','iPad Pro','IOS','11.1','4 GB','Hexa-core 2.39 GHz','64','2224 x 1668','High','193ea81981bbc3ea8535688ea1c8b5f6eaa4514e',1,1),('John Marston','iPod 5','IOS','8.3.0','500MB','Dual-Core 1GHz','32','640 x 1136 (326ppi)','Obsolete','53ddbab0034331cab54858dd980906cbb457367f',1,1),('Karen','iPhone 5s','IOS','11.1.1','1GB','Dual-Core 1.3GHz','64','640 x 1136 (326ppi)','Low','11c7581c85ca118915b345a2da4fb558bce0cdb7',1,1),('Ken','Nexus 10','Android','4.4.4','2 GB','Dual-Core 1.7GHz','?','1600 x 2560 (299ppi)','Low','None',1,1),('King','Kindle Fire HD','Android','?','1 GB','Dual-Core 1.5GHz','?','1200 x 1920 (254ppi)','Low','None',1,1),('Knuckles','iPad Mini 2 (retina)','IOS','10 Beta 2','1GB','Dual-Core 1.3GHz','64','1536 x 2048 (324 ppi)','Low','82b93d029411bbede53c16523c7f6c58054e526b',1,1),('Kratos','iPad Air 2','IOS','9.3.4','2 GB','Octa-core 1.5 GHz','64','2048 x 1536 (264ppi)','High','0b7886a9d846ea7cd50f80c1eefbeba3ead44b21',1,1),('Kuma','W8 Nokia','Windows','8.1','500 MB','Dual-Core 1GHz','','480 x 800 (233ppi)','Low','',1,1),('Lara Croft','iPhone 7+','IOS','10.3.2','3 GB','Quad-core 2.34 GHz','64','1920 x 1080 (401ppi)','High','f65ca802c90c9f80669fb4f18d8aa422da594875',1,1),('Lemmy','iPod 5','IOS','9.0.2','500MB','Dual-Core 1GHz','32','640 x 1136 (326ppi)','Obsolete','d4b31d4fef7b969148b9493b32cd53ffa280bf3a',1,1),('Link','Dell Laptop','Windows','','','','','','','',1,1),('Max Payne','iPad mini 4','IOS','10.1','2 GB','Quad-core 1.5 GHz','64','2048 x 1536 (326ppi)','High','03d9afd06672d3db910b3330f88d68290119022a',1,1),('Mr Bones','iPhone 7','IOS','10.3.3','2 GB','Quad-core 2.34 GHz','64','750 x 1334 (326ppi)','High','702c1adf30db79fd37da10e5866eb63157ef7356',1,1),('Mr Pricklepants','iPhone 7+','IOS','11.1.2','3 GB','Quad-core 2.34 GHz','64','1920 x 1080 (401ppi)','High','788e06f1bf0c9da090d5c51ad15034e699f793ce',1,1),('Mr X','iPhone x','IOS','11.1.2','3 GB','Hexa-core 2.39 GHz','64','2436 x 1125 (458ppi)','High','903e2d8c7291d8d3d386a3a0886f21d969704b54',1,1),('Pac Man','Chromebook','Windows','','','','','','','',0,1),('Princess Zelda','Dell E 6400','Windows','','','','','','','',1,1),('Q Bert','Amazon Fire HD 7','Android','4.5.5','1 GB','Dual-Core 1.5GHz','?','800 x 1280 (216ppi)','Low','None',1,1),('Roach','Nexus 9','Android','7 Preview','2 GB','Dual-Core 2.3GHz','?','1536 x 2048 (281ppi)','Medium','None',1,1),('Seifer','iPhone 8','IOS','11.0.3','2 GB','Hexa-core 2.39 GHz','64','750 x 1334 (326ppi)','High','',1,1),('Silver','iPad Mini','IOS','9.2','500MB','Dual-Core 1GHz','32','768 x 1024 (163 ppi)','Obsolete','e73f9b4cb93e83f718622016e31d90c06692d782',1,1),('Slippy Toad','iPod 6','IOS','10.3','1GB','Dual-Core 1.4GHz','64','750 x 1334 (326 ppi)','Low','cdc1507bc464102fb7321e72273b58d3bee8a6c5',1,1),('Sonic','iPad 2','IOS','8.4.1','500MB','Dual-Core 1GHz','32','768 x 1024 (132ppi)','Obsolete','6745ece4fd066224e05129278e7eb75c562fea28',1,1),('Squall','iPhone 6','IOS','10.3.2','1 GB DDR3','Dual-Core 1.4GHz','64','750 x 1334 (326ppi)','Medium','a3eb076b6f1d46fa40c3661ed928592df544b945',1,1),('Superman','Vive','VR','','','','','','','',1,1),('Toad','iPod 5','IOS','8.1.1','500MB','Dual-Core 1GHz','32','640 x 1136 (326ppi)','Obsolete','0395cc76b2f123d2debb5db2d26a8e4b44d44218',1,1),('UnusedDev','nintando','XV','101','1000','Giga-Core',NULL,NULL,NULL,NULL,1,1),('Vector','iPad Mini','IOS','8.4','500MB','Dual-Core 1GHz','32','768 x 1024 (163 ppi)','Obsolete','fc4fde35ea28101e8a11f9a706c3fc4eff4537cf',1,1),('Vincent','iPhone 4s','IOS','8.4.0','500MB','Dual-Core 1GHz','32','640 x 960 (326ppi)','Obsolete','369fcdf892d01f490215c4d9e0f2570d707c2f8a',1,1),('VR','Rift','VR','','','','','','','',1,1),('Wheatley','LG G3','Android','5.0.0','3 GB','Quad-Core 2.5GHz','?','1440 x 2560 (538ppi)','Medium','None',1,1),('Zangief','Galaxy Tab 4','Android','5.0.2','1.5 GB','Quad-Core 1.2GHz','?','800 x 1280 (216ppi)','Low','None',1,1);
/*!40000 ALTER TABLE `devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `Users_name` varchar(100) NOT NULL,
  `Phone` bigint NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Role` tinyint(1) DEFAULT '0',
  `Location` varchar(200) DEFAULT NULL,
  `Status` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`Users_name`),
  UNIQUE KEY `idusers_UNIQUE` (`Users_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Amol',2102950000,'1@a.com',1,'Office1',1),('Bob',2102950001,'2@a.com',0,'Office1',1),('Carl',2102950002,'3@a.com',0,'Office1',1),('Lora',2102950003,'4@a.com',0,'Office2',1),('Romeo',2102950004,'5@a.com',0,'Office2',1),('Sonam',2102950005,'6@a.com',0,'Office2',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usersdevices`
--

DROP TABLE IF EXISTS `usersdevices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersdevices` (
  `TransactionID` int NOT NULL AUTO_INCREMENT,
  `Device_name` varchar(100) NOT NULL,
  `Users_name` varchar(100) NOT NULL,
  `Start_Date` datetime DEFAULT NULL,
  `End_Date` datetime DEFAULT NULL,
  `Return_Date` datetime DEFAULT NULL,
  PRIMARY KEY (`TransactionID`),
  UNIQUE KEY `TransactionID_UNIQUE` (`TransactionID`),
  KEY `Device_name` (`Device_name`),
  KEY `Users_name` (`Users_name`),
  CONSTRAINT `usersdevices_ibfk_1` FOREIGN KEY (`Device_name`) REFERENCES `devices` (`Device_Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `usersdevices_ibfk_2` FOREIGN KEY (`Users_name`) REFERENCES `users` (`Users_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersdevices`
--

LOCK TABLES `usersdevices` WRITE;
/*!40000 ALTER TABLE `usersdevices` DISABLE KEYS */;
INSERT INTO `usersdevices` VALUES (362,'1Link','Amol','2022-03-24 08:35:41','2022-04-07 07:35:00','2022-03-24 20:36:19'),(363,'Akuma','Amol','2022-03-23 01:35:41','2022-03-23 07:35:00',NULL);
/*!40000 ALTER TABLE `usersdevices` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-25 20:16:16
