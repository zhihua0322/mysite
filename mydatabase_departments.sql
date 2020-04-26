-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `Dept_ID` varchar(3) NOT NULL,
  `Dept_Name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`Dept_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES ('0','Accountancy'),('1','Advertising'),('10','American Indian Studies Progr'),('100','Program in Medieval Studies'),('101','Provost Courses'),('102','Psychology'),('103','Recreation, Sport and Tourism'),('104','Religion'),('105','Russian,E European,Eurasn Ctr'),('106','Sch Earth Soc Env Courses'),('107','School of Integrative Biology'),('108','School of Labor & Empl. Rel.'),('109','School of Molecular & Cell Bio'),('11','Animal Sciences'),('110','School of Social Work'),('111','Slavic Languages & Literature'),('112','SLCL Courses'),('113','Sociology'),('114','Spanish and Portuguese'),('115','Special Education'),('116','Speech & Hearing Science'),('117','Statistics'),('118','Technology Entrepreneur Ctr'),('119','Theatre'),('12','Anthropology'),('120','Urban & Regional Planning'),('121','Vet Clinical Medicine'),('122','Vet Med College-Wide Programs'),('13','Applied Health Sci Courses'),('14','Architecture'),('15','Art & Design'),('16','Asian American Studies'),('17','Astronomy'),('18','Atmospheric Sciences'),('19','Biochemistry'),('2','Aerospace Engineering'),('20','Bioengineering'),('21','Business Administration'),('22','Carle Illinois COM Pgm & Crse'),('23','Cell & Developmental Biology'),('24','Center for Adv Study Courses'),('25','Center for African Studies'),('26','Center for Writing Studies'),('27','Chemical & Biomolecular Engr'),('28','Chemistry'),('29','CIC Traveling Scholars'),('3','African American Studies'),('30','Civil & Environmental Eng'),('31','Classics'),('32','College of Media Programs Crse'),('33','Communication'),('34','Comparative & World Literature'),('35','Comparative Biosciences'),('36','Computational Science & Engr'),('37','Computer Science'),('38','Council Teacher Ed Admin'),('39','Crop Sciences'),('4','Agr & Consumer Economics'),('40','Ctr S. Asian & MidEast Studies'),('41','Curriculum and Instruction'),('42','Dance'),('43','E. Asian Languages & Cultures'),('44','Economics'),('45','Educ Policy, Orgzn & Leadrshp'),('46','Education Administration'),('47','Educational Psychology'),('48','Electrical & Computer Eng'),('49','Engineering Courses'),('5','Agr, Consumer, & Env Sciences'),('50','Engineering Honors'),('51','English'),('52','Entomology'),('53','Finance'),('54','Fine & Applied Arts Courses'),('55','Food Science & Human Nutrition'),('56','French and Italian'),('57','Gender and Women\'s Studies'),('58','General Studies Courses'),('59','Geography & Geographic InfoSci'),('6','Agricultural & Biological Engr'),('60','Geology'),('61','Germanic Languages & Lit'),('62','Graduate College Programs'),('63','History'),('64','Human Dvlpmt & Family Studies'),('65','i-Health Program'),('66','Illinois Informatics Institute'),('67','Industrial&Enterprise Sys Eng'),('68','Information Sciences'),('69','Journalism'),('7','Agricultural Comm Pgm & Crse'),('70','Kinesiology & Community Health'),('71','Landscape Architecture'),('72','Latin American & Carib Studies'),('73','Latina/Latino Studies'),('74','Law'),('75','Liberal Arts & Sciences Course'),('76','Life Sciences'),('77','Linguistics'),('78','Materials Science & Engineerng'),('79','Mathematics'),('8','Agricultural Education Program'),('80','MBA Program Administration'),('81','Mechanical Sci & Engineering'),('82','Media and Cinema Studies'),('83','Medicine at UC Admin'),('84','Microbiology'),('85','Military Science'),('86','Molecular & Integrative Physl'),('87','Music'),('88','Natural Res & Env Sci'),('89','Naval Science'),('9','Air Force Aerospace Studies'),('90','Neuroscience Program'),('91','Nuclear, Plasma, & Rad Engr'),('92','Nutritional Sciences'),('93','Office of the Registrar'),('94','Pathobiology'),('95','Philosophy'),('96','Physics'),('97','Plant Biology'),('98','Political Science'),('99','Prg in Jewish Culture & Society');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-25 21:13:19
