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
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor` (
  `NetID` varchar(10) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`NetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES ('afliflet','Arne Fliflet','afliflet@illinois.edu'),('agha','Gul Agha','agha@illinois.edu'),('aharris','Albert Harris','aharris@illinois.edu'),('alawini','AbdussalamAlawini','alawini@illinois.edu'),('alvarez','Juan Alvarez','alvarez@illinois.edu'),('amayer','Alexander Mayer','amayer@illinois.edu'),('andreask','Andreas Kloeckner','andreask@illinois.edu'),('angrave','Lawrence Angrave','angrave@illinois.edu'),('arijit','Arijit Banerjee','arijit@illinois.edu'),('asandur2','Amitha Sandur','asandur2@illinois.edu'),('aschwing','Alexander Schwing','aschwing@illinois.edu'),('b-hajek','Bruce Hajek','b-hajek@illinois.edu'),('basar1','Tamer Ba?ar','basar1@illinois.edu'),('batesa','Adam Bates','batesa@illinois.edu'),('binhu7','Bin Hu','binhu7@illinois.edu'),('boses','Subhonmesh Bose','boses@illinois.edu'),('bpbailey','Brian Bailey','bpbailey@illinois.edu'),('brsnstck','Bruce Rosenstock','brsnstck@illinois.edu'),('caesar','Matthew Caesar','caesar@illinois.edu'),('cbayram','Can Bayram','cbayram@illinois.edu'),('cdschmit','Christopher Schmitz','cdschmit@illinois.edu'),('cgunter','Carl Gunter','cgunter@illinois.edu'),('challen','Geoffrey Challen','challen@illinois.edu'),('chekuri','Chandra Chekuri','chekuri'),('choquette','Kent Choquette','choquette@illinois.edu'),('cradhak','Chandrasekhar Radhakrishnan','cradhak@illinois.edu'),('croy','Romit Choudhury','croy@illinois.edu'),('cwfletch','Christopher Fletcher','cwfletch@illinois.edu'),('czhai','ChengXiang Zhai','czhai@illinois.edu'),('daf','David Forsyth','daf@illinois.edu'),('davis68','Neal Davis','davis68@illinois.edu'),('dchen','Deming Chen','dchen@illinois.edu'),('dpv','David Varodayan','dpv@illinois.edu'),('egunter','Elsa Gunter','egunter@illinois.edu'),('elyse','Elyse Rosenbaum','elyse@illinois.edu'),('erhan','Erhan Kudeki','erhan'),('fischerp','Paul Fischer','fischerp@illinois.edu'),('gcevans','Graham Evans','gcevans@illinois.edu'),('glherman','Geoffrey Herman','glherman@illinois.edu'),('gpopescu','Gabriel Popescu','gpopescu@illinois.edu'),('gross','George Gross','gross@illinois.edu'),('grosu','Grigore Rosu','grosu@illinois.edu'),('haitham','Haitham Al-Hassanieh','haitham@illinois.edu'),('han51','Aiguo Han','han51@illinois.edu'),('hanj','Jiawei Han','hanj'),('hanumolu','Pavan Hanumolu','hanumolu@illinois.edu'),('heath','Michael Heath','heath@illinois.edu'),('hillmer','Philip Hillmer','hillmer@illinois.edu'),('ihajj','Ibrahim Hajj','ihajj'),('ilans','Ilan Shomorony','ilans@illinois.edu'),('indy','Indranil Gupta','indy@illinois.edu'),('jdallesa','John Dallesasse','jdallesa@illinois.edu'),('jebel','Jonathon Ebel','jebel@illinois.edu'),('jeffe','Jeff Erickson','jeffe@illinois.edu'),('jesa','Jose Schutt-Aine','jesa@illinois.edu'),('jhazegaw','Mark Hasegawa-Johnson','jhazegaw@illinois.edu'),('jianpeng','Jian Peng','jianpeng@illinois.edu'),('jontalle','Jont Allen','jontalle@illinois.edu'),('juliahmr','Julia Hockenmaier','juliahmr'),('kale','Laxmikant Kale','kale@illinois.edu'),('katselis','Dimitrios Katselis','katselis@illinois.edu'),('kcchang','Kevin Chang','kcchang@illinois.edu'),('kevinkim','Kyekyoon Kim','kevinkim@illinois.edu'),('kfang3','Kejie Fang','kfang3'),('kirlik','Alex Kirlik','kirlik@illinois.edu'),('kkarahal','Karrie Karahalios','kkarahal@illinois.edu'),('krdc','Katherine Driggs-Campbell','krdc@illinois.edu'),('l-haken','Lippold Haken','l-haken@illinois.edu'),('liberzon','Daniel Liberzon','liberzon@illinois.edu'),('lrs','Lui Sha','lrs@illinois.edu'),('ludaesch','Bertram Ludaescher','ludaesch@illinois.edu'),('lwaldrop','Lara Waldrop','lwaldrop@illinois.edu'),('lyding','Joseph Lyding','lyding@illinois.edu'),('madhu','Madhusudan Parthasarathy','madhu@illinois.edu'),('marinov','Darko Marinov','marinov@illinois.edu'),('mattox','Mattox Beckman','mattox@illinois.edu'),('maxim','Maxim Raginsky','maxim@illinois.edu'),('mdbailey','Michael Bailey','mdbailey@illinois.edu'),('meseguer','Jose Meseguer','meseguer'),('mfleck','Margaret Fleck','mfleck@illinois.edu'),('mfsilva','Mariana Silva','mfsilva@illinois.edu'),('mhd','Michael Dann','mhd@illinois.edu'),('miforbes','Michael Forbes','miforbes@illinois.edu'),('minhdo','Minh Do','minhdo@illinois.edu'),('misailo','Sasa Misailovic','misailo@illinois.edu'),('mitras','Sayan Mitra','mitras@illinois.edu'),('mjt','Matus Telgarsky','mjt@illinois.edu'),('mllee','Minjoo Lee','mllee@illinois.edu'),('mwoodley','Michael Woodley','mwoodley@illinois.edu'),('nikita','Nikita Borisov','nikita@illinois.edu'),('paris','Paris Smaragdis','paris@illinois.edu'),('pbg','Philip Godfrey','pbg@illinois.edu'),('psauer','Peter Sauer','psauer@illinois.edu'),('rakeshk','Rakesh Kumar','rakeshk@illinois.edu'),('rbhttchr','Rini Mehta','rbhttchr@illinois.edu'),('rcunnin2','Ryan Cunningham','rcunnin2@illinois.edu'),('rhc','Roy Campbell','rhc@illinois.edu'),('rhk','Robin Kravets','rhk@illinois.edu'),('rilie','Raluca Ilie','rilie@illinois.edu'),('rlayton','Richard Layton','rlayton'),('sadve','Sarita Adve','sadve@illinois.edu'),('schuh4','Jonathon Schuh','schuh4@illinois.edu'),('selevins','Stephen Levinson','selevins@illinois.edu'),('shaffer1','Eric Shaffer','shaffer1'),('shanbhag','Naresh Shanbhag','shanbhag@illinois.edu'),('shj','Sheldon Jacobson','shj@illinois.edu'),('sibin','Sibin Mohan','sibin@illinois.edu'),('sinhas','Saurabh Sinha','sinhas@illinois.edu'),('slazebni','Svetlana Lazebnik','slazebni@illinois.edu'),('songbin','Songbin Gong','songbin@illinois.edu'),('songp','Pengfei Song','songp'),('t-huang1','Thomas Huang','t-huang1@illinois.edu'),('taoxie','Tao Xie','taoxie@illinois.edu'),('teng12','Dawei Teng','teng12@illinois.edu'),('tmc','Timothy Chan','tmc@illinois.edu'),('torrella','Josep Torrellas','torella@illinois.edu'),('tyxu','Tianyin Xu','tyxu@illinois.edu'),('vgruev','Viktor Gruev','vgruev@illinois.edu'),('vhoffman','Valerie Hoffman','vhoffman@illinois.edu'),('vvv','Venugopal Veeravalli','vvv@illinois.edu'),('w-hwu','Wen-mei Hwu','w-hwu@illinois.edu'),('waf','Wade Fagen-Ulmschneider','waf@illinois.edu'),('weihe','Wei He','weihe@illinois.edu'),('wjzhu','Wenjuan Zhu','wjzhu@illinois.edu'),('xuchen1','Xu Chen','xuchen1@illinois.edu'),('yihchun','Yih-Chun Hu','yihchun@illinois.edu'),('yilu4','Yi Lu','yilu4@illinois.edu'),('ymb','Yuliy Baryshnikov','ymb@illinois.edu'),('yvlasov','Yurii Vlasov','yvlasov@illinois.edu'),('zhizhenz','Zhizhen Zhao','zhizhenz'),('zilles','Craig Zilles','zilles@illinois.edu');
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-25 21:13:17
