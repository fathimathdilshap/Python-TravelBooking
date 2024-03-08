/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - travelershub
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`travelershub` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `travelershub`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `Chat_id` int(50) NOT NULL AUTO_INCREMENT,
  `Sender_id` varchar(50) DEFAULT NULL,
  `Receiver` varchar(50) DEFAULT NULL,
  `Message` varchar(50) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`Chat_id`,`Sender_id`,`Receiver`,`Message`,`Date`) values (1,'2','1','HLOOOOO','2022-02-10 04:11:04'),(2,'1','2','HEY','2022-02-10 04:18:15'),(3,'1','2','fghj','2022-02-10 14:50:09'),(4,'1','2','drtyhjk','2022-02-10 14:50:32'),(5,'2','1','xfyhbjk','2022-02-10 14:50:58'),(6,'2','1','sertghjk','2022-02-10 14:51:03'),(7,'2','1','erfghj','2022-02-10 14:51:08'),(8,'1','2','gmiotj','2022-02-11 03:34:14');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Complaint_id` int(50) NOT NULL AUTO_INCREMENT,
  `User_id` varchar(50) DEFAULT NULL,
  `Complaint` varchar(50) DEFAULT NULL,
  `Reply` varchar(50) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Complaint_id`,`User_id`,`Complaint`,`Reply`,`Date`) values (1,'1','slow drive','ok','2022-02-10'),(2,'2','hloo','hai','2022-02-10'),(3,'2','hloo','tgyhb','2022-02-10'),(4,'2','hloo','ok','2022-02-10'),(5,'2','hloo','pending','2022-02-10'),(6,'5','no','pending','2022-02-10'),(7,'4','hello','pending','2022-02-10'),(8,'6','tyuerjhrjt','pending','2022-02-10'),(9,'1','dfg','pending','2022-02-11');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `Feedback_id` int(50) NOT NULL AUTO_INCREMENT,
  `Trip_id` varchar(50) DEFAULT NULL,
  `User_id` varchar(50) DEFAULT NULL,
  `Feedback` varchar(50) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`Feedback_id`,`Trip_id`,`User_id`,`Feedback`,`Date`) values (1,'1','2','I LIKEED','2022-02-10');

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `File_id` int(50) NOT NULL AUTO_INCREMENT,
  `Trip_id` varchar(50) DEFAULT NULL,
  `Files` varchar(500) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`File_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `files` */

insert  into `files`(`File_id`,`Trip_id`,`Files`,`Date`) values (1,'1','static/c63658e8-d6b9-4672-99ec-5e55ce74dae8Calculate.png','2022-02-10'),(2,'2','static/fb63357e-a239-40c9-8652-47dcde6f2422Menudrvn.png','2022-02-10'),(3,'2','static/b6415c5c-ea7f-4a27-b334-0f01ce40333aperson (2).png','2022-02-10'),(4,'1','static/6d45a5cf-cd22-4233-a169-2b0db6570fe9eng.jpeg','2022-02-10'),(5,'6','static/be926c72-c192-4e52-b904-77d831e20327CO4Pgrm4.png','2022-02-10'),(6,'6','static/0f213cc5-2194-4181-bb7d-1d52fdd91108','2022-02-10');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'Fathimath ','Fathimath ','user'),(2,'admin','admin','admin'),(3,'Basil','Basil','user'),(4,'Anagha','Anagha','user'),(5,'Maneesha','Maneesha','user'),(6,'Babu','Babu','user'),(7,'aki','aki','reject');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `Request_id` int(50) NOT NULL AUTO_INCREMENT,
  `Trip_id` varchar(50) DEFAULT NULL,
  `User_id` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`Request_id`,`Trip_id`,`User_id`,`Status`,`Date`) values (1,'1','2','Accept','2022-02-10 04:09:16'),(2,'2','3','pending','2022-02-10 14:47:04'),(3,'4','5','pending','2022-02-10 21:28:26'),(4,'4','5','pending','2022-02-10 21:31:23'),(26,'3','2','pending','2022-02-12 00:22:47'),(25,'3','1','pending','2022-02-10 22:02:44'),(24,'2','1','pending','2022-02-10 22:02:43'),(23,'2','4','reject','2022-02-10 21:47:23'),(22,'1','4','Accept','2022-02-10 21:47:21'),(21,'5','4','pending','2022-02-10 21:47:19'),(20,'2','5','reject','2022-02-10 21:44:21'),(19,'1','5','pending','2022-02-10 21:43:08'),(18,'3','5','pending','2022-02-10 21:43:06'),(15,'4','5','Accept','2022-02-10 21:39:20'),(17,'2','5','pending','2022-02-10 21:43:05');

/*Table structure for table `trips` */

DROP TABLE IF EXISTS `trips`;

CREATE TABLE `trips` (
  `Trips_id` int(50) NOT NULL AUTO_INCREMENT,
  `User_id` int(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Vehicle` varchar(50) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  `Tripstartdate` varchar(50) DEFAULT NULL,
  `Tripenddate` varchar(50) DEFAULT NULL,
  `Starttime` varchar(50) DEFAULT NULL,
  `Startplace` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Trips_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `trips` */

insert  into `trips`(`Trips_id`,`User_id`,`Place`,`Vehicle`,`Description`,`Tripstartdate`,`Tripenddate`,`Starttime`,`Startplace`) values (1,1,'Banglur','Bike','Good','1/02/2022','10/03/2022','1:00 Am','PMNA'),(2,2,'Banglur','Bike','Amazing','1/02/2022','13/03/2022','1:00 Am','Bypass'),(3,3,'Banglur','Bike','good','1/02/2022','13/03/2022','12:00 Am','Perinthalmanna'),(4,4,'Manali','Bike','Amazing','7/02/2022','11/02/2022','3:00 AM','Kolathur'),(5,5,'Manali','Bike','good','7/02/2022','11/02/2022','3:00 AM','Valumbur'),(6,6,'Goa','Bike','good','7/02/2022','10/03/2022','3:00 AM','Bypass');

/*Table structure for table `userregistration` */

DROP TABLE IF EXISTS `userregistration`;

CREATE TABLE `userregistration` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `Firstname` varchar(50) DEFAULT NULL,
  `Lastname` varchar(50) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Age` varchar(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Phoneno:` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Idproof` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `userregistration` */

insert  into `userregistration`(`user_id`,`login_id`,`Firstname`,`Lastname`,`Address`,`Age`,`Place`,`Phoneno:`,`Email`,`Idproof`,`Status`,`Gender`) values (1,1,'Fathimath Dilsha','Dilsha','Pathari(H),Anghadippuram','33','Angadippuram','9746925349','fathimathdilshap@gmail.com','pexels-shalender-kumar-3574440.jpg','accept','male'),(2,3,'Basil','Babu','Aliyns(H)','23','Kottakkal','7659745367','Babu@gmail.com','Employ.png','accept','male'),(3,4,'Anagha','K','Kavumpurath(h)','22','Cherukara','8767544567','anu@gmail.com','CO4Pgrm2.png','accept','female'),(4,5,'Maneesha','PR','Alice(H)','22','Kolathur','9876543219','mani@gmail.com','CO3Pgrm6.png','accept','female'),(5,6,'Babu','P','Vadketh(H)','25','Valambur','7896543212','Babu@gmail.com','CO4Pgrm5.png','accept','male'),(6,7,'Akil','K','erfhsdn','23','ertyu','987654321','aki@gmail.com','CO4Pgrm5.png','reject','male');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
