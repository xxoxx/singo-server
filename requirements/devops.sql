-- MySQL dump 10.17  Distrib 10.3.15-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: devops
-- ------------------------------------------------------
-- Server version	10.3.15-MariaDB-1:10.3.15+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'dba'),(3,'devops'),(1,'测试权限');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (7,1,61),(6,1,69),(15,3,58),(16,3,59),(17,3,60),(18,3,61),(19,3,62),(20,3,63),(8,3,64),(9,3,65),(10,3,66),(11,3,67),(12,3,70),(13,3,113),(14,3,119);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=172 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (58,'用户列表模块',4,'user_list'),(59,'创建用户',4,'user_add'),(60,'导出用户列表',4,'user_export'),(61,'编辑用户',4,'user_edit'),(62,'删除用户',4,'user_delete'),(63,'用户组模块',6,'user_group'),(64,'添加用户组',6,'user_group_add'),(65,'导出用户组列表',6,'user_group_export'),(66,'编辑用户组',6,'user_group_edit'),(67,'删除用户组',6,'user_group_delete'),(68,'修改密码',4,'change_password'),(69,'重置用户密码',4,'reset_password'),(70,'更改用户所在组',4,'user_group_change'),(71,'工单列表',13,'work_order'),(72,'工单导出',13,'work_order_export'),(73,'工单申请',13,'work_order_apply'),(74,'查看组权限',14,'group_permission_permission_list'),(75,'设置组权限',14,'group_permission_permission_set'),(76,'查看组成员',14,'group_permission_user_list'),(77,'设置组成员',14,'group_permission_user_set'),(82,'用户权限(导航栏)',14,'user_permission'),(83,'用户权限设置',14,'user_permission_set'),(84,'权限组(导航栏)',14,'group_permission'),(85,'创建权限组',14,'group_permission_add'),(86,'删除权限组',14,'group_permission_delete'),(87,'修改权限组',14,'group_permission_edit'),(88,'创建权限点',14,'permission_add'),(89,'删除权限点',14,'permission_delete'),(90,'修改权限点',14,'permission_edit'),(91,'权限点管理(导航栏)',14,'permission_list'),(113,'oa用户激活ldap',20,'ldap_activate'),(114,'ldap管理(导航栏)',20,'ldap_list'),(115,'添加成员',20,'member_add'),(116,'删除成员',20,'member_delete'),(117,'编辑成员',20,'member_edit'),(118,'修改ldap密码',20,'password_change'),(119,'SQL审核展示',21,'SQLAudit_list'),(171,'用户激活/禁用',4,'user_active_change');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `id` char(32) NOT NULL,
  `username` varchar(32) NOT NULL,
  `email` varchar(128) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `role` varchar(10) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `wechat` varchar(30) DEFAULT NULL,
  `dingTalk` varchar(30) DEFAULT NULL,
  `comment` longtext NOT NULL,
  `is_first_login` tinyint(1) NOT NULL,
  `properties` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES ('pbkdf2_sha256$36000$TjrQyp8NL0Lc$Ol0qpHN/lFafByBAoCuiISbd1ZHmsUgkuB+rFJsePTk=','2019-06-20 15:36:46.956258',0,'','',0,1,'2019-04-01 13:58:18.932121','41d94a2d0e43445ca55c6a31c4a4491c','000214','18058418418@189.com','蔡南杰','','User','18058418418',NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$EzV5xxh2hjZ6$m7HG0UJQxAcUiNn1F63DSUWFN44xUEVrEezpdYLldz0=','2019-04-22 17:15:45.612786',0,'','',0,1,'2019-04-22 15:29:55.926161','70c60b07a9ab4c17ae98956afe044142','infopath','18058418418@189.cn','测试账号','','User','18058418555',NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$y7BBlJOxTAou$O6LC2ARb86gsFTbY6eufX9iO5wbG0sPVLcs+EM8sRFE=','2019-05-08 08:42:41.606729',0,'','',0,1,'2019-03-31 23:09:54.127846','793cfb964bb944809f414c023fcd8e72','000093','zhangwenliang@ztocwst.com','张文亮','','User','18158685645',NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$Txqli51u7aCt$ROgYbHQxy4Prhcuu9URXhzMfBmh1nHx3IxS667zXRQ4=','2019-07-02 08:41:11.345532',1,'','',1,1,'2019-03-28 13:44:56.255532','8e1cde13e0794809aa1c472cfa0138f2','admin','cwst@cwst.com','超级用户','','User',NULL,NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$pz0xrqTaDYHf$EASMh4xoBgKCDK9bT3ZBAxHw3ZJXaFJ7nPM4OCfQ63E=','2019-06-03 17:37:21.075326',0,'','',0,1,'2019-04-01 09:17:59.861182','bf406563f99543c89d422450bb28b438','000343','000343@cwst.com','赵潮江','','User','18268620212',NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$WaKX2vimvOzv$FCJ6vf3Y9mCw4FJ5Ikj30pnFv3GGg3qlceJpVs8q+zQ=','2019-04-22 17:16:53.588532',0,'','',0,1,'2019-04-01 14:22:26.011254','c0b50352ed2d4af7873da6701f307660','000323','000323@cwst.com','卢晓','','User','18058716128',NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$uMXQ4LuXACHN$cootcvgF5xxzyPZZKak3ZOeeALd+qSX9emNfdtCG6SE=','2019-06-28 14:53:17.752417',0,'','',0,1,'2019-04-24 10:12:59.046516','cb1c4ed0e20447fb9f61a33418fdaa03','000370','000370@cwst.com','夏斌','','User','13867417196',NULL,NULL,'',0,'{\"activate_ldap\": false}'),('pbkdf2_sha256$36000$7ZJkUsP26GVg$lBnqx5xqSiwQsDApN3HFXRsrx6PvZhc3LZFbWdHq97Q=','2019-06-06 11:02:58.141162',0,'','',0,1,'2019-04-04 15:55:48.131305','eaacec0fbe88486c854df29fec55d04b','000151','000151@cwst.com','周金亮','','User','13656681557',NULL,NULL,'',0,'{\"activate_ldap\": false}');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_family`
--

DROP TABLE IF EXISTS `auth_user_family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_family` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` char(32) NOT NULL,
  `usergroup_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_family_user_id_usergroup_id_6b99bd47_uniq` (`user_id`,`usergroup_id`),
  KEY `auth_user_family_usergroup_id_d41a7f29_fk_users_usergroup_id` (`usergroup_id`),
  CONSTRAINT `auth_user_family_user_id_b66132c3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_family_usergroup_id_d41a7f29_fk_users_usergroup_id` FOREIGN KEY (`usergroup_id`) REFERENCES `users_usergroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_family`
--

LOCK TABLES `auth_user_family` WRITE;
/*!40000 ALTER TABLE `auth_user_family` DISABLE KEYS */;
INSERT INTO `auth_user_family` VALUES (3,'41d94a2d0e43445ca55c6a31c4a4491c','4183d7d341e24680a8ee399a6b3a9ec9'),(2,'793cfb964bb944809f414c023fcd8e72','4183d7d341e24680a8ee399a6b3a9ec9'),(4,'bf406563f99543c89d422450bb28b438','4183d7d341e24680a8ee399a6b3a9ec9'),(5,'c0b50352ed2d4af7873da6701f307660','4183d7d341e24680a8ee399a6b3a9ec9'),(6,'eaacec0fbe88486c854df29fec55d04b','4183d7d341e24680a8ee399a6b3a9ec9');
/*!40000 ALTER TABLE `auth_user_family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` char(32) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,'41d94a2d0e43445ca55c6a31c4a4491c',1),(2,'793cfb964bb944809f414c023fcd8e72',1),(7,'793cfb964bb944809f414c023fcd8e72',3),(4,'bf406563f99543c89d422450bb28b438',1),(9,'bf406563f99543c89d422450bb28b438',3),(5,'c0b50352ed2d4af7873da6701f307660',1),(10,'c0b50352ed2d4af7873da6701f307660',3),(8,'eaacec0fbe88486c854df29fec55d04b',3);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` char(32) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (40,'41d94a2d0e43445ca55c6a31c4a4491c',58),(41,'41d94a2d0e43445ca55c6a31c4a4491c',59),(42,'41d94a2d0e43445ca55c6a31c4a4491c',60),(43,'41d94a2d0e43445ca55c6a31c4a4491c',61),(39,'41d94a2d0e43445ca55c6a31c4a4491c',70),(23,'793cfb964bb944809f414c023fcd8e72',58),(24,'793cfb964bb944809f414c023fcd8e72',59),(25,'793cfb964bb944809f414c023fcd8e72',60),(26,'793cfb964bb944809f414c023fcd8e72',61),(27,'793cfb964bb944809f414c023fcd8e72',62),(28,'793cfb964bb944809f414c023fcd8e72',63),(16,'793cfb964bb944809f414c023fcd8e72',64),(17,'793cfb964bb944809f414c023fcd8e72',65),(18,'793cfb964bb944809f414c023fcd8e72',66),(19,'793cfb964bb944809f414c023fcd8e72',67),(20,'793cfb964bb944809f414c023fcd8e72',68),(21,'793cfb964bb944809f414c023fcd8e72',69),(22,'793cfb964bb944809f414c023fcd8e72',70),(45,'bf406563f99543c89d422450bb28b438',58),(46,'bf406563f99543c89d422450bb28b438',59),(13,'bf406563f99543c89d422450bb28b438',63),(12,'bf406563f99543c89d422450bb28b438',66),(15,'bf406563f99543c89d422450bb28b438',71),(14,'bf406563f99543c89d422450bb28b438',72),(48,'bf406563f99543c89d422450bb28b438',118),(49,'cb1c4ed0e20447fb9f61a33418fdaa03',119),(32,'eaacec0fbe88486c854df29fec55d04b',58),(33,'eaacec0fbe88486c854df29fec55d04b',59),(34,'eaacec0fbe88486c854df29fec55d04b',60),(35,'eaacec0fbe88486c854df29fec55d04b',61),(36,'eaacec0fbe88486c854df29fec55d04b',62),(29,'eaacec0fbe88486c854df29fec55d04b',68),(30,'eaacec0fbe88486c854df29fec55d04b',69),(31,'eaacec0fbe88486c854df29fec55d04b',70);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_deployenv`
--

DROP TABLE IF EXISTS `deploy_deployenv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_deployenv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(56) NOT NULL,
  `code` varchar(56) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `deploy_deployenv_parent_id_b90c351c_fk_deploy_deployenv_id` (`parent_id`),
  CONSTRAINT `deploy_deployenv_parent_id_b90c351c_fk_deploy_deployenv_id` FOREIGN KEY (`parent_id`) REFERENCES `deploy_deployenv` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_deployenv`
--

LOCK TABLES `deploy_deployenv` WRITE;
/*!40000 ALTER TABLE `deploy_deployenv` DISABLE KEYS */;
INSERT INTO `deploy_deployenv` VALUES (1,'测试环境','qafc',NULL),(2,'开发环境','dev',NULL),(3,'实施环境','imple',NULL),(4,'沙箱环境','sanbox',NULL),(5,'预发环境','pre',NULL),(6,'生产环境','online',NULL),(7,'devops-web','prod',6),(8,'qa','qa',1),(10,'wms','wms',6),(11,'devops-server','pro',6);
/*!40000 ALTER TABLE `deploy_deployenv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_deploymentorder`
--

DROP TABLE IF EXISTS `deploy_deploymentorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_deploymentorder` (
  `id` char(32) NOT NULL,
  `title` varchar(128) NOT NULL,
  `type` int(11) NOT NULL,
  `branche` varchar(64) NOT NULL,
  `commit_id` varchar(64) NOT NULL,
  `commit` varchar(256) NOT NULL,
  `content` longtext DEFAULT NULL,
  `apply_time` datetime(6) NOT NULL,
  `complete_time` datetime(6) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `result_msg` longtext NOT NULL,
  `deploy_times` int(11) NOT NULL,
  `applicant_id` char(32) NOT NULL,
  `assign_to_id` char(32) NOT NULL,
  `env_id` int(11) NOT NULL,
  `project_id` char(32) NOT NULL,
  `reviewer_id` char(32) NOT NULL,
  `version` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_deploymentorder_applicant_id_fe286776_fk_auth_user_id` (`applicant_id`),
  KEY `deploy_deploymentorder_assign_to_id_435de7a2_fk_auth_user_id` (`assign_to_id`),
  KEY `deploy_deploymentorder_env_id_b41423ca_fk_deploy_deployenv_id` (`env_id`),
  KEY `deploy_deploymentorder_reviewer_id_fcd5af73_fk_auth_user_id` (`reviewer_id`),
  KEY `deploy_deploymentorder_project_id_c6520532_fk_deploy_project_id` (`project_id`),
  CONSTRAINT `deploy_deploymentorder_applicant_id_fe286776_fk_auth_user_id` FOREIGN KEY (`applicant_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `deploy_deploymentorder_assign_to_id_435de7a2_fk_auth_user_id` FOREIGN KEY (`assign_to_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `deploy_deploymentorder_env_id_b41423ca_fk_deploy_deployenv_id` FOREIGN KEY (`env_id`) REFERENCES `deploy_deployenv` (`id`),
  CONSTRAINT `deploy_deploymentorder_project_id_c6520532_fk_deploy_project_id` FOREIGN KEY (`project_id`) REFERENCES `deploy_project` (`id`),
  CONSTRAINT `deploy_deploymentorder_reviewer_id_fcd5af73_fk_auth_user_id` FOREIGN KEY (`reviewer_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_deploymentorder`
--

LOCK TABLES `deploy_deploymentorder` WRITE;
/*!40000 ALTER TABLE `deploy_deploymentorder` DISABLE KEYS */;
INSERT INTO `deploy_deploymentorder` VALUES ('509f40741cef417286a033d3369be41e','20190620devops-web发布',2,'master','e0a1c646dd2803c3add1d04f6c70cdd545e6222c','添加数组剔除方法','devops-wbe上线测试','2019-06-20 15:37:42.266683','2019-07-02 10:59:43.188977',5,'Error in request. Possibly authentication failed [500]: Server Error\n\n\n\n\n\n  \n  <!DOCTYPE html><html><head resURL=\"/static/5b5711cc\" data-rooturl=\"\" data-resurl=\"/static/5b5711cc\">\n    \n\n    <title>Jenkins [Jenkins]</title><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/layout-common.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/style.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/color.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/responsive-grid.css\" type=\"text/css\" /><link rel=\"shortcut icon\" href=\"/static/5b5711cc/favicon.ico\" type=\"image/vnd.microsoft.icon\" /><link color=\"black\" rel=\"mask-icon\" href=\"/images/mask-icon.svg\" /><script>var isRunAsTest=false; var rootURL=\"\"; var resURL=\"/static/5b5711cc\";</script><script src=\"/static/5b5711cc/scripts/prototype.js\" type=\"text/javascript\"></script><script src=\"/static/5b5711cc/scripts/behavior.js\" type=\"text/javascript\"></script><script src=\'/adjuncts/5b5711cc/org/kohsuke/stapler/bind.js\' type=\'text/javascript\'></script><script src=\"/static/5b5711cc/scripts/yui/yahoo/yahoo-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/dom/dom-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/event/event-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/animation/animation-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/dragdrop/dragdrop-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/container/container-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/connection/connection-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/datasource/datasource-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/autocomplete/autocomplete-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/menu/menu-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/element/element-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/button/button-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/storage/storage-min.js\"></script><script src=\"/static/5b5711cc/scripts/hudson-behavior.js\" type=\"text/javascript\"></script><script src=\"/static/5b5711cc/scripts/sortable.js\" type=\"text/javascript\"></script><script>crumb.init(\"Jenkins-Crumb\", \"d35e02d36aae0801031b4f5da312d324\");</script><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/container/assets/container.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/assets/skins/sam/skin.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/container/assets/skins/sam/container.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/button/assets/skins/sam/button.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/menu/assets/skins/sam/menu.css\" type=\"text/css\" /><meta name=\"ROBOTS\" content=\"INDEX,NOFOLLOW\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" /><script src=\"/adjuncts/5b5711cc/org/kohsuke/stapler/jquery/jquery.full.js\" type=\"text/javascript\"></script><script>var Q=jQuery.noConflict()</script><link rel=\"stylesheet\" href=\"/plugin/jquery-ui/css/jquery-ui-1.8.9.custom.css\" type=\"text/css\" /><script src=\"/plugin/jquery-ui/js/jquery-ui-1.8.9.custom.min.js\"></script><link type=\"text/css\" rel=\"stylesheet\" href=\"http://172.16.102.33/jenkins-material-theme.css\"/><script src=\"/static/5b5711cc/jsbundles/page-init.js\" type=\"text/javascript\"></script></head><body data-model-type=\"hudson.model.Hudson\" id=\"jenkins\" class=\"yui-skin-sam two-column jenkins-2.164.1\" data-version=\"2.164.1\"><a href=\"#skip2content\" class=\"skiplink\">Skip to content</a><div id=\"page-head\"><div id=\"header\"><div class=\"logo\"><a id=\"jenkins-home-link\" href=\"/\"><img src=\"/static/5b5711cc/images/headshot.png\" alt=\"[Jenkins]\" id=\"jenkins-head-icon\" /><img src=\"/static/5b5711cc/images/title.png\" alt=\"Jenkins\" width=\"139\" id=\"jenkins-name-icon\" height=\"34\" /></a></div><div class=\"login\"> <a href=\"/login?from=%2Fjob%2Fsalt-devops-web%2Fapi%2Fjson\"><b>log in</b></a></div><div class=\"searchbox hidden-xs\"><form role=\"search\" method=\"get\" name=\"search\" action=\"/search/\" style=\"position:relative;\" class=\"no-json\"><div id=\"search-box-minWidth\"></div><div id=\"search-box-sizer\"></div><div id=\"searchform\"><input role=\"searchbox\" name=\"q\" placeholder=\"search\" id=\"search-box\" class=\"has-default-text\" /> <a href=\"https://jenkins.io/redirect/search-box\"><img src=\"/static/5b5711cc/images/16x16/help.png\" style=\"width: 16px; height: 16px; \" class=\"icon-help icon-sm\" /></a><div id=\"search-box-completion\"></div><script>createSearchBox(\"/search/\");</script></div></form></div></div><div id=\"breadcrumbBar\"><tr id=\"top-nav\"><td id=\"left-top-nav\" colspan=\"2\"><link rel=\'stylesheet\' href=\'/adjuncts/5b5711cc/lib/layout/breadcrumbs.css\' type=\'text/css\' /><script src=\'/adjuncts/5b5711cc/lib/layout/breadcrumbs.js\' type=\'text/javascript\'></script><div class=\"top-sticker noedge\"><div class=\"top-sticker-inner\"><div id=\"right-top-nav\"></div><ul id=\"breadcrumbs\"><li class=\"item\"><a href=\"/\" class=\"model-link inside\">Jenkins</a></li><li href=\"/\" class=\"children\"></li></ul><div id=\"breadcrumb-menu-target\"></div></div></div></td></tr></div></div><div id=\"page-body\" class=\"clear\"><div id=\"side-panel\"><div class=\"task\"><a href=\"https://jenkins.io/\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/next.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-next icon-md\" /></a> <a href=\"https://jenkins.io/\" class=\"task-link\">Jenkins project</a></div><div class=\"task\"><a href=\"https://jenkins.io/redirect/report-an-issue\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/gear2.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-gear2 icon-md\" /></a> <a href=\"https://jenkins.io/redirect/report-an-issue\" class=\"task-link\">Bug tracker</a></div><div class=\"task\"><a href=\"https://jenkins.io/redirect/mailing-lists\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/search.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-search icon-md\" /></a> <a href=\"https://jenkins.io/redirect/mailing-lists\" class=\"task-link\">Mailing Lists</a></div><div class=\"task\"><a href=\"https://twitter.com/jenkinsci\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/user.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-user icon-md\" /></a> <a href=\"https://twitter.com/jenkinsci\" class=\"task-link\">Twitter: @jenkinsci</a></div></div><div id=\"main-panel\"><a name=\"skip2content\"></a><h1 style=\"text-align: center\"><img src=\"/static/5b5711cc/images/rage.png\" width=\"154\" height=\"179\" /><span style=\"font-size:50px\"> Oops!</span></h1><div id=\"error-description\"><p>A problem occurred while processing the request.\n        Please check <a href=\"https://jenkins.io/redirect/issue-tracker\">our bug tracker</a> to see if a similar problem has already been reported.\n        If it is already reported, please vote and put a comment on it to let us gauge the impact of the problem.\n        If you think this is a new issue, please file a new issue.\n        When you file an issue, make sure to add the entire stack trace, along with the version of Jenkins and relevant plugins.\n        <a href=\"https://jenkins.io/redirect/users-mailing-list\">The users list</a> might be also useful in understanding what has happened.</p><h2>Stack trace</h2><pre style=\"margin:2em; clear:both\">org.acegisecurity.userdetails.UsernameNotFoundException: User cainanjie not found in directory.\n	at org.acegisecurity.ldap.search.FilterBasedLdapUserSearch.searchForUser(FilterBasedLdapUserSearch.java:126)\n	at hudson.security.LDAPSecurityRealm$LDAPUserDetailsService.loadUserByUsername(LDAPSecurityRealm.java:1314)\n	at hudson.security.LDAPSecurityRealm$LDAPUserDetailsService.loadUserByUsername(LDAPSecurityRealm.java:1251)\n	at jenkins.security.ImpersonatingUserDetailsService.loadUserByUsername(ImpersonatingUserDetailsService.java:32)\n	at hudson.model.User.getUserDetailsForImpersonation(User.java:398)\n	at jenkins.security.BasicHeaderApiTokenAuthenticator.authenticate(BasicHeaderApiTokenAuthenticator.java:35)\nCaused: javax.servlet.ServletException\n	at jenkins.security.BasicHeaderApiTokenAuthenticator.authenticate(BasicHeaderApiTokenAuthenticator.java:43)\n	at jenkins.security.BasicHeaderProcessor.doFilter(BasicHeaderProcessor.java:79)\n	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)\n	at org.acegisecurity.context.HttpSessionContextIntegrationFilter.doFilter(HttpSessionContextIntegrationFilter.java:249)\n	at hudson.security.HttpSessionContextIntegrationFilter2.doFilter(HttpSessionContextIntegrationFilter2.java:67)\n	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)\n	at hudson.security.ChainedServletFilter.doFilter(ChainedServletFilter.java:90)\n	at hudson.security.HudsonFilter.doFilter(HudsonFilter.java:171)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.kohsuke.stapler.compression.CompressionFilter.doFilter(CompressionFilter.java:49)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at hudson.util.CharacterEncodingFilter.doFilter(CharacterEncodingFilter.java:82)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.kohsuke.stapler.DiagnosticThreadNameFilter.doFilter(DiagnosticThreadNameFilter.java:30)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:533)\n	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:146)\n	at org.eclipse.jetty.security.SecurityHandler.handle(SecurityHandler.java:524)\n	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:132)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextHandle(ScopedHandler.java:257)\n	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:1595)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextHandle(ScopedHandler.java:255)\n	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1340)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextScope(ScopedHandler.java:203)\n	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:473)\n	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:1564)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextScope(ScopedHandler.java:201)\n	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:1242)\n	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:144)\n	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:132)\n	at org.eclipse.jetty.server.Server.handle(Server.java:503)\n	at org.eclipse.jetty.server.HttpChannel.handle(HttpChannel.java:364)\n	at org.eclipse.jetty.server.HttpConnection.onFillable(HttpConnection.java:260)\n	at org.eclipse.jetty.io.AbstractConnection$ReadCallback.succeeded(AbstractConnection.java:305)\n	at org.eclipse.jetty.io.FillInterest.fillable(FillInterest.java:103)\n	at org.eclipse.jetty.io.ChannelEndPoint$2.run(ChannelEndPoint.java:118)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.runTask(EatWhatYouKill.java:333)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.doProduce(EatWhatYouKill.java:310)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.tryProduce(EatWhatYouKill.java:168)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.run(EatWhatYouKill.java:126)\n	at org.eclipse.jetty.util.thread.ReservedThreadExecutor$ReservedThread.run(ReservedThreadExecutor.java:366)\n	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:765)\n	at org.eclipse.jetty.util.thread.QueuedThreadPool$2.run(QueuedThreadPool.java:683)\n	at java.lang.Thread.run(Thread.java:748)\n</pre></div></div></div><footer><div class=\"container-fluid\"><div class=\"row\"><div class=\"col-md-6\" id=\"footer\"></div><div class=\"col-md-18\"><span class=\"page_generated\">Page generated: Jul 2, 2019 10:59:43 AM CST</span><span class=\"rest_api\"><a href=\"api/\">REST API</a></span><span class=\"jenkins_ver\"><a href=\"https://jenkins.io/\">Jenkins ver. 2.164.1</a></span></div></div></div></footer></body></html>',14,'41d94a2d0e43445ca55c6a31c4a4491c','41d94a2d0e43445ca55c6a31c4a4491c',6,'70a6de14d4eb41ed9917754586ca4af9','eaacec0fbe88486c854df29fec55d04b',0.01),('9abe2a9e5a5343ecbb6841ce586f83be','20190624devops-servers发布',2,'master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy','测试','2019-06-27 13:23:50.977946','2019-06-28 09:20:24.303935',3,'上线完成',18,'8e1cde13e0794809aa1c472cfa0138f2','41d94a2d0e43445ca55c6a31c4a4491c',6,'15b669186481402489b353a360ad6fa9','eaacec0fbe88486c854df29fec55d04b',0.02),('b820a6a370d344ac8f07676bf90a9ab2','1111',0,'master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',NULL,'2019-06-27 15:55:53.801120',NULL,1,'',0,'41d94a2d0e43445ca55c6a31c4a4491c','41d94a2d0e43445ca55c6a31c4a4491c',6,'15b669186481402489b353a360ad6fa9','bf406563f99543c89d422450bb28b438',0.01),('c4445cbe83ea4438a23f0b7d62d04d9a','wms-docker-测试',2,'master','a4bab7cde550e18d639e7ba71d63fa4b4c806d96','称重自动揽件时添加非ZTO拦截',NULL,'2019-06-27 15:00:00.584426','2019-06-27 15:29:44.109230',3,'上线完成',4,'8e1cde13e0794809aa1c472cfa0138f2','41d94a2d0e43445ca55c6a31c4a4491c',6,'55ca84a411e543eb9d9801aa28844a06','bf406563f99543c89d422450bb28b438',0.02);
/*!40000 ALTER TABLE `deploy_deploymentorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_deploymentorder_deploy_maps`
--

DROP TABLE IF EXISTS `deploy_deploymentorder_deploy_maps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_deploymentorder_deploy_maps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deploymentorder_id` char(32) NOT NULL,
  `envserversmap_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `deploy_deploymentorder_d_deploymentorder_id_envse_68c116b0_uniq` (`deploymentorder_id`,`envserversmap_id`),
  KEY `deploy_deploymentord_envserversmap_id_4aa15701_fk_deploy_en` (`envserversmap_id`),
  CONSTRAINT `deploy_deploymentord_deploymentorder_id_757ec659_fk_deploy_de` FOREIGN KEY (`deploymentorder_id`) REFERENCES `deploy_deploymentorder` (`id`),
  CONSTRAINT `deploy_deploymentord_envserversmap_id_4aa15701_fk_deploy_en` FOREIGN KEY (`envserversmap_id`) REFERENCES `deploy_envserversmap` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_deploymentorder_deploy_maps`
--

LOCK TABLES `deploy_deploymentorder_deploy_maps` WRITE;
/*!40000 ALTER TABLE `deploy_deploymentorder_deploy_maps` DISABLE KEYS */;
INSERT INTO `deploy_deploymentorder_deploy_maps` VALUES (1,'509f40741cef417286a033d3369be41e',1),(2,'9abe2a9e5a5343ecbb6841ce586f83be',3),(4,'b820a6a370d344ac8f07676bf90a9ab2',3),(3,'c4445cbe83ea4438a23f0b7d62d04d9a',1);
/*!40000 ALTER TABLE `deploy_deploymentorder_deploy_maps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_envserversmap`
--

DROP TABLE IF EXISTS `deploy_envserversmap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_envserversmap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(56) NOT NULL,
  `parent_env_id` int(11) NOT NULL,
  `sub_env_id` int(11) DEFAULT NULL,
  `code` varchar(56) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_envserversmap_parent_env_id_370ba726_fk_deploy_de` (`parent_env_id`),
  KEY `deploy_envserversmap_sub_env_id_e45d1ad0_fk_deploy_deployenv_id` (`sub_env_id`),
  CONSTRAINT `deploy_envserversmap_parent_env_id_370ba726_fk_deploy_de` FOREIGN KEY (`parent_env_id`) REFERENCES `deploy_deployenv` (`id`),
  CONSTRAINT `deploy_envserversmap_sub_env_id_e45d1ad0_fk_deploy_deployenv_id` FOREIGN KEY (`sub_env_id`) REFERENCES `deploy_deployenv` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_envserversmap`
--

LOCK TABLES `deploy_envserversmap` WRITE;
/*!40000 ALTER TABLE `deploy_envserversmap` DISABLE KEYS */;
INSERT INTO `deploy_envserversmap` VALUES (1,'运维平台前端',6,7,'devops_web'),(3,'运维平台后端',6,11,'devops_server');
/*!40000 ALTER TABLE `deploy_envserversmap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_envserversmap_servers`
--

DROP TABLE IF EXISTS `deploy_envserversmap_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_envserversmap_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `envserversmap_id` int(11) NOT NULL,
  `server_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `deploy_envserversmap_ser_envserversmap_id_server__921ad84c_uniq` (`envserversmap_id`,`server_id`),
  KEY `deploy_envserversmap_server_id_fa6b71f9_fk_resources` (`server_id`),
  CONSTRAINT `deploy_envserversmap_envserversmap_id_3406dc6c_fk_deploy_en` FOREIGN KEY (`envserversmap_id`) REFERENCES `deploy_envserversmap` (`id`),
  CONSTRAINT `deploy_envserversmap_server_id_fa6b71f9_fk_resources` FOREIGN KEY (`server_id`) REFERENCES `resources_server` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_envserversmap_servers`
--

LOCK TABLES `deploy_envserversmap_servers` WRITE;
/*!40000 ALTER TABLE `deploy_envserversmap_servers` DISABLE KEYS */;
INSERT INTO `deploy_envserversmap_servers` VALUES (1,1,'3bb94d569a8e56e5604176045f5565f6'),(2,3,'3bb94d569a8e56e5604176045f5565f6');
/*!40000 ALTER TABLE `deploy_envserversmap_servers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_history`
--

DROP TABLE IF EXISTS `deploy_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` char(32) NOT NULL,
  `deploy_times` int(11) NOT NULL,
  `title` varchar(128) NOT NULL,
  `project_name` varchar(64) NOT NULL,
  `env` varchar(32) NOT NULL,
  `type` int(11) NOT NULL,
  `servers_ip` longtext NOT NULL,
  `servers_saltID` longtext NOT NULL,
  `branche` varchar(64) NOT NULL,
  `commit_id` varchar(64) NOT NULL,
  `commit` varchar(256) NOT NULL,
  `jk_number` int(11) NOT NULL,
  `jk_result` varchar(32) NOT NULL,
  `applicant` varchar(32) NOT NULL,
  `reviewer` varchar(32) NOT NULL,
  `assign_to` varchar(32) NOT NULL,
  `result` int(11) NOT NULL,
  `start` datetime(6) NOT NULL,
  `end` datetime(6) DEFAULT NULL,
  `log_file` varchar(128) NOT NULL,
  `error_msg` longtext DEFAULT NULL,
  `version` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `deploy_history_order_id_deploy_times_e3c7f412_uniq` (`order_id`,`deploy_times`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_history`
--

LOCK TABLES `deploy_history` WRITE;
/*!40000 ALTER TABLE `deploy_history` DISABLE KEYS */;
INSERT INTO `deploy_history` VALUES (1,'509f40741cef417286a033d3369be41e',1,'20190620devops-wbe发布','devops-web','生产环境',0,'172.16.102.40','devops','master','e0a1c646dd2803c3add1d04f6c70cdd545e6222c','添加数组剔除方法',17,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-20 16:02:22.639019','2019-06-20 16:04:42.899856','/srv/salt/deploy/logs/1561017741.1628587',NULL,0.01),(2,'509f40741cef417286a033d3369be41e',2,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','e0a1c646dd2803c3add1d04f6c70cdd545e6222c','添加数组剔除方法',-1,'FAILURE','蔡南杰','周金亮','超级用户',3,'2019-06-20 17:09:50.106023','2019-06-20 17:10:35.546200','/srv/salt/deploy/logs/1561021787.2199903','构建失败',0.01),(3,'509f40741cef417286a033d3369be41e',3,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','e0a1c646dd2803c3add1d04f6c70cdd545e6222c','添加数组剔除方法',21,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-20 17:13:52.011937','2019-06-20 17:15:21.219331','/srv/salt/deploy/logs/1561022029.2884467',NULL,0.01),(4,'509f40741cef417286a033d3369be41e',4,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','121317c4c70e3f776e56fd0d90d698dc2099a192','列表显示编码',22,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-24 13:17:08.251575','2019-06-24 13:19:28.861133','/srv/salt/deploy/logs/1561353426.9346654',NULL,0.01),(5,'9abe2a9e5a5343ecbb6841ce586f83be',1,'20190624devops-servers发布','devops-server','生产环境',0,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',21,'SUCCESS','超级用户','周金亮','超级用户',2,'2019-06-24 13:24:17.581475','2019-06-24 13:24:29.939246','/srv/salt/deploy/logs/1561353854.543784',NULL,0.01),(6,'509f40741cef417286a033d3369be41e',5,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','121317c4c70e3f776e56fd0d90d698dc2099a192','列表显示编码',23,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-24 13:52:58.837001','2019-06-24 13:54:37.933965','/srv/salt/deploy/logs/1561355577.1711617',NULL,0.01),(7,'509f40741cef417286a033d3369be41e',6,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','790fb297312b6d83b3ec777dabfcf2e9b0356429','不显示kv控件的问题',24,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-24 14:37:10.435502','2019-06-24 14:38:55.739012','/srv/salt/deploy/logs/1561358229.337981',NULL,0.01),(8,'9abe2a9e5a5343ecbb6841ce586f83be',2,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',22,'SUCCESS','超级用户','周金亮','超级用户',2,'2019-06-25 09:36:27.464450','2019-06-25 09:36:40.538044','/srv/salt/deploy/logs/1561426586.4244184',NULL,0.01),(9,'509f40741cef417286a033d3369be41e',7,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','790fb297312b6d83b3ec777dabfcf2e9b0356429','不显示kv控件的问题',25,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-25 09:37:46.233749','2019-06-25 09:39:24.192645','/srv/salt/deploy/logs/1561426663.78373',NULL,0.01),(10,'9abe2a9e5a5343ecbb6841ce586f83be',3,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',-1,'unknown','超级用户','周金亮','超级用户',3,'2019-06-27 13:54:57.904386','2019-06-27 13:54:58.100580','/srv/salt/deploy/logs/1561614896.5096583','HTTPConnectionPool(host=\'ci.ops.com\', port=80): Max retries exceeded with url: /crumbIssuer/api/json (Caused by NewConnectionError(\'<urllib3.connection.HTTPConnection object at 0x7f24fa77b978>: Failed to establish a new connection: [Errno -2] Name or service not known\',))',0.01),(11,'9abe2a9e5a5343ecbb6841ce586f83be',4,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',-1,'unknown','超级用户','周金亮','超级用户',3,'2019-06-27 13:57:56.699173','2019-06-27 13:57:56.722071','/srv/salt/deploy/logs/1561615075.659053','HTTPConnectionPool(host=\'ci.ops.com\', port=80): Max retries exceeded with url: /crumbIssuer/api/json (Caused by NewConnectionError(\'<urllib3.connection.HTTPConnection object at 0x7ff0a9a65128>: Failed to establish a new connection: [Errno -2] Name or service not known\',))',0.01),(12,'9abe2a9e5a5343ecbb6841ce586f83be',5,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',-1,'unknown','超级用户','周金亮','超级用户',3,'2019-06-27 13:59:32.545804','2019-06-27 13:59:32.557279','/srv/salt/deploy/logs/1561615171.6306489','HTTPConnectionPool(host=\'ci.ops.com\', port=80): Max retries exceeded with url: /crumbIssuer/api/json (Caused by NewConnectionError(\'<urllib3.connection.HTTPConnection object at 0x7f87c91a30f0>: Failed to establish a new connection: [Errno -2] Name or service not known\',))',0.01),(13,'9abe2a9e5a5343ecbb6841ce586f83be',6,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',-1,'unknown','超级用户','周金亮','超级用户',3,'2019-06-27 14:00:36.054134','2019-06-27 14:00:36.066324','/srv/salt/deploy/logs/1561615235.1720297','HTTPConnectionPool(host=\'ci.ops.com\', port=80): Max retries exceeded with url: /crumbIssuer/api/json (Caused by NewConnectionError(\'<urllib3.connection.HTTPConnection object at 0x7f7396ffd1d0>: Failed to establish a new connection: [Errno -2] Name or service not known\',))',0.01),(14,'9abe2a9e5a5343ecbb6841ce586f83be',7,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','dc943e2c7c86b81f3f906c5d8e56affdd0b03ff9','deploy',-1,'unknown','超级用户','周金亮','超级用户',3,'2019-06-27 14:01:55.620476','2019-06-27 14:01:55.637454','/srv/salt/deploy/logs/1561615314.2019255','HTTPConnectionPool(host=\'ci.ops.com\', port=80): Max retries exceeded with url: /crumbIssuer/api/json (Caused by NewConnectionError(\'<urllib3.connection.HTTPConnection object at 0x7f64eaf7a128>: Failed to establish a new connection: [Errno -2] Name or service not known\',))',0.01),(15,'9abe2a9e5a5343ecbb6841ce586f83be',8,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',23,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-27 14:11:56.276193','2019-06-27 14:12:09.860329','/srv/salt/deploy/logs/1561615911.0491173','devops执行salt sls失败',0.01),(16,'9abe2a9e5a5343ecbb6841ce586f83be',9,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',24,'SUCCESS','超级用户','周金亮','超级用户',2,'2019-06-27 14:13:56.702062','2019-06-27 14:14:11.248096','/srv/salt/deploy/logs/1561616035.970526',NULL,0.01),(17,'509f40741cef417286a033d3369be41e',8,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','450013cb2b8d2044423ae4e64d35809576f32460','修改用户列表的权限控制',26,'SUCCESS','蔡南杰','周金亮','超级用户',3,'2019-06-27 14:23:16.736068','2019-06-27 14:24:47.129994','/srv/salt/deploy/logs/1561616595.7701445','生成docker镜像失败',0.01),(18,'509f40741cef417286a033d3369be41e',9,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','450013cb2b8d2044423ae4e64d35809576f32460','修改用户列表的权限控制',27,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-27 14:26:10.884562','2019-06-27 14:27:11.961374','/srv/salt/deploy/logs/1561616769.504484',NULL,0.01),(19,'509f40741cef417286a033d3369be41e',10,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','8bc01576d542bfe197818f93637c67096e6dff24','修复kv控件的问题',28,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-27 14:31:44.818329','2019-06-27 14:32:45.062873','/srv/salt/deploy/logs/1561617103.6348243',NULL,0.01),(20,'c4445cbe83ea4438a23f0b7d62d04d9a',1,'wms-docker-测试','ztocwst-wms','生产环境',0,'172.16.102.40','devops','master','a4bab7cde550e18d639e7ba71d63fa4b4c806d96','称重自动揽件时添加非ZTO拦截',17,'SUCCESS','超级用户','赵潮江','超级用户',2,'2019-06-27 15:03:56.894366','2019-06-27 15:05:33.830803','/srv/salt/deploy/logs/1561619025.0338588',NULL,0.01),(21,'c4445cbe83ea4438a23f0b7d62d04d9a',2,'wms-docker-测试','ztocwst-wms','生产环境',2,'172.16.102.40','devops','master','a4bab7cde550e18d639e7ba71d63fa4b4c806d96','称重自动揽件时添加非ZTO拦截',18,'SUCCESS','超级用户','赵潮江','超级用户',3,'2019-06-27 15:17:44.926004','2019-06-27 15:19:13.321595','/srv/salt/deploy/logs/1561619857.101349','unsupported operand type(s) for +: \'DeploymentOrder\' and \'float\'',0.01),(22,'c4445cbe83ea4438a23f0b7d62d04d9a',3,'wms-docker-测试','ztocwst-wms','生产环境',2,'172.16.102.40','devops','master','a4bab7cde550e18d639e7ba71d63fa4b4c806d96','称重自动揽件时添加非ZTO拦截',19,'SUCCESS','超级用户','赵潮江','超级用户',2,'2019-06-27 15:21:37.369421','2019-06-27 15:23:09.273451','/srv/salt/deploy/logs/1561620094.4825578',NULL,0.01),(23,'c4445cbe83ea4438a23f0b7d62d04d9a',4,'wms-docker-测试','ztocwst-wms','生产环境',2,'172.16.102.40','devops','master','a4bab7cde550e18d639e7ba71d63fa4b4c806d96','称重自动揽件时添加非ZTO拦截',20,'SUCCESS','超级用户','赵潮江','超级用户',2,'2019-06-27 15:27:32.955675','2019-06-27 15:29:44.109236','/srv/salt/deploy/logs/1561620444.5000985',NULL,0.01),(24,'9abe2a9e5a5343ecbb6841ce586f83be',10,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',25,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-27 19:50:21.611895','2019-06-27 19:50:35.398662','/srv/salt/deploy/logs/1561636219.8158774','生成docker镜像失败',0.01),(25,'509f40741cef417286a033d3369be41e',11,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','16d77897c513b5d540e906b2bc00f67aa46732a7','调整主机列表样式',29,'SUCCESS','蔡南杰','周金亮','超级用户',3,'2019-06-27 19:51:17.438320','2019-06-27 19:52:38.517459','/srv/salt/deploy/logs/1561636276.7963495','生成docker镜像失败',0.01),(26,'509f40741cef417286a033d3369be41e',12,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','16d77897c513b5d540e906b2bc00f67aa46732a7','调整主机列表样式',30,'SUCCESS','蔡南杰','周金亮','超级用户',2,'2019-06-27 19:53:40.208121','2019-06-27 19:54:35.637877','/srv/salt/deploy/logs/1561636416.041217',NULL,0.01),(27,'9abe2a9e5a5343ecbb6841ce586f83be',11,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',26,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-27 19:56:37.861610','2019-06-27 19:56:52.338329','/srv/salt/deploy/logs/1561636596.9792526','devops执行salt sls失败',0.01),(28,'9abe2a9e5a5343ecbb6841ce586f83be',12,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',27,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-27 19:57:34.675885','2019-06-27 19:57:49.029567','/srv/salt/deploy/logs/1561636653.2933757','devops执行salt sls失败',0.01),(29,'9abe2a9e5a5343ecbb6841ce586f83be',13,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',28,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-28 08:54:39.949062','2019-06-28 08:54:54.461352','/srv/salt/deploy/logs/1561683273.0106876','devops执行salt sls失败',0.01),(30,'9abe2a9e5a5343ecbb6841ce586f83be',14,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',29,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-28 08:58:17.581703','2019-06-28 08:58:31.942913','/srv/salt/deploy/logs/1561683496.3837051','devops执行salt sls失败',0.01),(31,'9abe2a9e5a5343ecbb6841ce586f83be',15,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','a2c8f161c19e6759e5b340937c42436e96eb175e','t push -u origin masterMerge branch \'dev\'',30,'SUCCESS','超级用户','周金亮','超级用户',3,'2019-06-28 09:03:01.976054','2019-06-28 09:03:17.145000','/srv/salt/deploy/logs/1561683781.1174996','devops执行salt sls失败',0.01),(32,'9abe2a9e5a5343ecbb6841ce586f83be',16,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','7e702e1fdb457906640119d08728c175bbb6ef33','Merge branch \'dev\'t push -u origin master',31,'SUCCESS','超级用户','周金亮','超级用户',2,'2019-06-28 09:17:01.801700','2019-06-28 09:17:16.461827','/srv/salt/deploy/logs/1561684620.7497401',NULL,0.01),(33,'9abe2a9e5a5343ecbb6841ce586f83be',17,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','7e702e1fdb457906640119d08728c175bbb6ef33','Merge branch \'dev\'t push -u origin master',32,'SUCCESS','超级用户','周金亮','超级用户',2,'2019-06-28 09:18:39.028553','2019-06-28 09:18:53.578621','/srv/salt/deploy/logs/1561684717.2274737',NULL,0.01),(34,'9abe2a9e5a5343ecbb6841ce586f83be',18,'20190624devops-servers发布','devops-server','生产环境',2,'172.16.102.40','devops','master','7e702e1fdb457906640119d08728c175bbb6ef33','Merge branch \'dev\'t push -u origin master',33,'SUCCESS','超级用户','周金亮','超级用户',2,'2019-06-28 09:20:09.802283','2019-06-28 09:20:24.303940','/srv/salt/deploy/logs/1561684809.1104505',NULL,0.01),(35,'509f40741cef417286a033d3369be41e',13,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','e0a1c646dd2803c3add1d04f6c70cdd545e6222c','添加数组剔除方法',-1,'unknown','蔡南杰','周金亮','超级用户',3,'2019-07-02 10:59:32.414867','2019-07-02 10:59:32.481418','/srv/salt/deploy/logs/1562036370.3627214','Error in request. Possibly authentication failed [500]: Server Error\n\n\n\n\n\n  \n  <!DOCTYPE html><html><head resURL=\"/static/5b5711cc\" data-rooturl=\"\" data-resurl=\"/static/5b5711cc\">\n    \n\n    <title>Jenkins [Jenkins]</title><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/layout-common.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/style.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/color.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/responsive-grid.css\" type=\"text/css\" /><link rel=\"shortcut icon\" href=\"/static/5b5711cc/favicon.ico\" type=\"image/vnd.microsoft.icon\" /><link color=\"black\" rel=\"mask-icon\" href=\"/images/mask-icon.svg\" /><script>var isRunAsTest=false; var rootURL=\"\"; var resURL=\"/static/5b5711cc\";</script><script src=\"/static/5b5711cc/scripts/prototype.js\" type=\"text/javascript\"></script><script src=\"/static/5b5711cc/scripts/behavior.js\" type=\"text/javascript\"></script><script src=\'/adjuncts/5b5711cc/org/kohsuke/stapler/bind.js\' type=\'text/javascript\'></script><script src=\"/static/5b5711cc/scripts/yui/yahoo/yahoo-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/dom/dom-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/event/event-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/animation/animation-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/dragdrop/dragdrop-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/container/container-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/connection/connection-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/datasource/datasource-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/autocomplete/autocomplete-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/menu/menu-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/element/element-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/button/button-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/storage/storage-min.js\"></script><script src=\"/static/5b5711cc/scripts/hudson-behavior.js\" type=\"text/javascript\"></script><script src=\"/static/5b5711cc/scripts/sortable.js\" type=\"text/javascript\"></script><script>crumb.init(\"Jenkins-Crumb\", \"d35e02d36aae0801031b4f5da312d324\");</script><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/container/assets/container.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/assets/skins/sam/skin.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/container/assets/skins/sam/container.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/button/assets/skins/sam/button.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/menu/assets/skins/sam/menu.css\" type=\"text/css\" /><meta name=\"ROBOTS\" content=\"INDEX,NOFOLLOW\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" /><script src=\"/adjuncts/5b5711cc/org/kohsuke/stapler/jquery/jquery.full.js\" type=\"text/javascript\"></script><script>var Q=jQuery.noConflict()</script><link rel=\"stylesheet\" href=\"/plugin/jquery-ui/css/jquery-ui-1.8.9.custom.css\" type=\"text/css\" /><script src=\"/plugin/jquery-ui/js/jquery-ui-1.8.9.custom.min.js\"></script><link type=\"text/css\" rel=\"stylesheet\" href=\"http://172.16.102.33/jenkins-material-theme.css\"/><script src=\"/static/5b5711cc/jsbundles/page-init.js\" type=\"text/javascript\"></script></head><body data-model-type=\"hudson.model.Hudson\" id=\"jenkins\" class=\"yui-skin-sam two-column jenkins-2.164.1\" data-version=\"2.164.1\"><a href=\"#skip2content\" class=\"skiplink\">Skip to content</a><div id=\"page-head\"><div id=\"header\"><div class=\"logo\"><a id=\"jenkins-home-link\" href=\"/\"><img src=\"/static/5b5711cc/images/headshot.png\" alt=\"[Jenkins]\" id=\"jenkins-head-icon\" /><img src=\"/static/5b5711cc/images/title.png\" alt=\"Jenkins\" width=\"139\" id=\"jenkins-name-icon\" height=\"34\" /></a></div><div class=\"login\"> <a href=\"/login?from=%2FcrumbIssuer%2Fapi%2Fjson\"><b>log in</b></a></div><div class=\"searchbox hidden-xs\"><form role=\"search\" method=\"get\" name=\"search\" action=\"/search/\" style=\"position:relative;\" class=\"no-json\"><div id=\"search-box-minWidth\"></div><div id=\"search-box-sizer\"></div><div id=\"searchform\"><input role=\"searchbox\" name=\"q\" placeholder=\"search\" id=\"search-box\" class=\"has-default-text\" /> <a href=\"https://jenkins.io/redirect/search-box\"><img src=\"/static/5b5711cc/images/16x16/help.png\" style=\"width: 16px; height: 16px; \" class=\"icon-help icon-sm\" /></a><div id=\"search-box-completion\"></div><script>createSearchBox(\"/search/\");</script></div></form></div></div><div id=\"breadcrumbBar\"><tr id=\"top-nav\"><td id=\"left-top-nav\" colspan=\"2\"><link rel=\'stylesheet\' href=\'/adjuncts/5b5711cc/lib/layout/breadcrumbs.css\' type=\'text/css\' /><script src=\'/adjuncts/5b5711cc/lib/layout/breadcrumbs.js\' type=\'text/javascript\'></script><div class=\"top-sticker noedge\"><div class=\"top-sticker-inner\"><div id=\"right-top-nav\"></div><ul id=\"breadcrumbs\"><li class=\"item\"><a href=\"/\" class=\"model-link inside\">Jenkins</a></li><li href=\"/\" class=\"children\"></li></ul><div id=\"breadcrumb-menu-target\"></div></div></div></td></tr></div></div><div id=\"page-body\" class=\"clear\"><div id=\"side-panel\"><div class=\"task\"><a href=\"https://jenkins.io/\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/next.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-next icon-md\" /></a> <a href=\"https://jenkins.io/\" class=\"task-link\">Jenkins project</a></div><div class=\"task\"><a href=\"https://jenkins.io/redirect/report-an-issue\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/gear2.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-gear2 icon-md\" /></a> <a href=\"https://jenkins.io/redirect/report-an-issue\" class=\"task-link\">Bug tracker</a></div><div class=\"task\"><a href=\"https://jenkins.io/redirect/mailing-lists\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/search.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-search icon-md\" /></a> <a href=\"https://jenkins.io/redirect/mailing-lists\" class=\"task-link\">Mailing Lists</a></div><div class=\"task\"><a href=\"https://twitter.com/jenkinsci\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/user.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-user icon-md\" /></a> <a href=\"https://twitter.com/jenkinsci\" class=\"task-link\">Twitter: @jenkinsci</a></div></div><div id=\"main-panel\"><a name=\"skip2content\"></a><h1 style=\"text-align: center\"><img src=\"/static/5b5711cc/images/rage.png\" width=\"154\" height=\"179\" /><span style=\"font-size:50px\"> Oops!</span></h1><div id=\"error-description\"><p>A problem occurred while processing the request.\n        Please check <a href=\"https://jenkins.io/redirect/issue-tracker\">our bug tracker</a> to see if a similar problem has already been reported.\n        If it is already reported, please vote and put a comment on it to let us gauge the impact of the problem.\n        If you think this is a new issue, please file a new issue.\n        When you file an issue, make sure to add the entire stack trace, along with the version of Jenkins and relevant plugins.\n        <a href=\"https://jenkins.io/redirect/users-mailing-list\">The users list</a> might be also useful in understanding what has happened.</p><h2>Stack trace</h2><pre style=\"margin:2em; clear:both\">org.acegisecurity.userdetails.UsernameNotFoundException: User cainanjie not found in directory.\n	at org.acegisecurity.ldap.search.FilterBasedLdapUserSearch.searchForUser(FilterBasedLdapUserSearch.java:126)\n	at hudson.security.LDAPSecurityRealm$LDAPUserDetailsService.loadUserByUsername(LDAPSecurityRealm.java:1314)\n	at hudson.security.LDAPSecurityRealm$LDAPUserDetailsService.loadUserByUsername(LDAPSecurityRealm.java:1251)\n	at jenkins.security.ImpersonatingUserDetailsService.loadUserByUsername(ImpersonatingUserDetailsService.java:32)\n	at hudson.model.User.getUserDetailsForImpersonation(User.java:398)\n	at jenkins.security.BasicHeaderApiTokenAuthenticator.authenticate(BasicHeaderApiTokenAuthenticator.java:35)\nCaused: javax.servlet.ServletException\n	at jenkins.security.BasicHeaderApiTokenAuthenticator.authenticate(BasicHeaderApiTokenAuthenticator.java:43)\n	at jenkins.security.BasicHeaderProcessor.doFilter(BasicHeaderProcessor.java:79)\n	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)\n	at org.acegisecurity.context.HttpSessionContextIntegrationFilter.doFilter(HttpSessionContextIntegrationFilter.java:249)\n	at hudson.security.HttpSessionContextIntegrationFilter2.doFilter(HttpSessionContextIntegrationFilter2.java:67)\n	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)\n	at hudson.security.ChainedServletFilter.doFilter(ChainedServletFilter.java:90)\n	at hudson.security.HudsonFilter.doFilter(HudsonFilter.java:171)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.kohsuke.stapler.compression.CompressionFilter.doFilter(CompressionFilter.java:49)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at hudson.util.CharacterEncodingFilter.doFilter(CharacterEncodingFilter.java:82)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.kohsuke.stapler.DiagnosticThreadNameFilter.doFilter(DiagnosticThreadNameFilter.java:30)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:533)\n	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:146)\n	at org.eclipse.jetty.security.SecurityHandler.handle(SecurityHandler.java:524)\n	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:132)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextHandle(ScopedHandler.java:257)\n	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:1595)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextHandle(ScopedHandler.java:255)\n	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1340)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextScope(ScopedHandler.java:203)\n	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:473)\n	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:1564)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextScope(ScopedHandler.java:201)\n	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:1242)\n	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:144)\n	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:132)\n	at org.eclipse.jetty.server.Server.handle(Server.java:503)\n	at org.eclipse.jetty.server.HttpChannel.handle(HttpChannel.java:364)\n	at org.eclipse.jetty.server.HttpConnection.onFillable(HttpConnection.java:260)\n	at org.eclipse.jetty.io.AbstractConnection$ReadCallback.succeeded(AbstractConnection.java:305)\n	at org.eclipse.jetty.io.FillInterest.fillable(FillInterest.java:103)\n	at org.eclipse.jetty.io.ChannelEndPoint$2.run(ChannelEndPoint.java:118)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.runTask(EatWhatYouKill.java:333)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.doProduce(EatWhatYouKill.java:310)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.tryProduce(EatWhatYouKill.java:168)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.run(EatWhatYouKill.java:126)\n	at org.eclipse.jetty.util.thread.ReservedThreadExecutor$ReservedThread.run(ReservedThreadExecutor.java:366)\n	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:765)\n	at org.eclipse.jetty.util.thread.QueuedThreadPool$2.run(QueuedThreadPool.java:683)\n	at java.lang.Thread.run(Thread.java:748)\n</pre></div></div></div><footer><div class=\"container-fluid\"><div class=\"row\"><div class=\"col-md-6\" id=\"footer\"></div><div class=\"col-md-18\"><span class=\"page_generated\">Page generated: Jul 2, 2019 10:59:32 AM CST</span><span class=\"rest_api\"><a href=\"api/\">REST API</a></span><span class=\"jenkins_ver\"><a href=\"https://jenkins.io/\">Jenkins ver. 2.164.1</a></span></div></div></div></footer></body></html>',0.01),(36,'509f40741cef417286a033d3369be41e',14,'20190620devops-web发布','devops-web','生产环境',2,'172.16.102.40','devops','master','e0a1c646dd2803c3add1d04f6c70cdd545e6222c','添加数组剔除方法',-1,'unknown','蔡南杰','周金亮','超级用户',3,'2019-07-02 10:59:43.153002','2019-07-02 10:59:43.188984','/srv/salt/deploy/logs/1562036382.4364455','Error in request. Possibly authentication failed [500]: Server Error\n\n\n\n\n\n  \n  <!DOCTYPE html><html><head resURL=\"/static/5b5711cc\" data-rooturl=\"\" data-resurl=\"/static/5b5711cc\">\n    \n\n    <title>Jenkins [Jenkins]</title><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/layout-common.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/style.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/color.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/css/responsive-grid.css\" type=\"text/css\" /><link rel=\"shortcut icon\" href=\"/static/5b5711cc/favicon.ico\" type=\"image/vnd.microsoft.icon\" /><link color=\"black\" rel=\"mask-icon\" href=\"/images/mask-icon.svg\" /><script>var isRunAsTest=false; var rootURL=\"\"; var resURL=\"/static/5b5711cc\";</script><script src=\"/static/5b5711cc/scripts/prototype.js\" type=\"text/javascript\"></script><script src=\"/static/5b5711cc/scripts/behavior.js\" type=\"text/javascript\"></script><script src=\'/adjuncts/5b5711cc/org/kohsuke/stapler/bind.js\' type=\'text/javascript\'></script><script src=\"/static/5b5711cc/scripts/yui/yahoo/yahoo-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/dom/dom-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/event/event-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/animation/animation-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/dragdrop/dragdrop-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/container/container-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/connection/connection-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/datasource/datasource-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/autocomplete/autocomplete-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/menu/menu-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/element/element-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/button/button-min.js\"></script><script src=\"/static/5b5711cc/scripts/yui/storage/storage-min.js\"></script><script src=\"/static/5b5711cc/scripts/hudson-behavior.js\" type=\"text/javascript\"></script><script src=\"/static/5b5711cc/scripts/sortable.js\" type=\"text/javascript\"></script><script>crumb.init(\"Jenkins-Crumb\", \"d35e02d36aae0801031b4f5da312d324\");</script><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/container/assets/container.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/assets/skins/sam/skin.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/container/assets/skins/sam/container.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/button/assets/skins/sam/button.css\" type=\"text/css\" /><link rel=\"stylesheet\" href=\"/static/5b5711cc/scripts/yui/menu/assets/skins/sam/menu.css\" type=\"text/css\" /><meta name=\"ROBOTS\" content=\"INDEX,NOFOLLOW\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" /><script src=\"/adjuncts/5b5711cc/org/kohsuke/stapler/jquery/jquery.full.js\" type=\"text/javascript\"></script><script>var Q=jQuery.noConflict()</script><link rel=\"stylesheet\" href=\"/plugin/jquery-ui/css/jquery-ui-1.8.9.custom.css\" type=\"text/css\" /><script src=\"/plugin/jquery-ui/js/jquery-ui-1.8.9.custom.min.js\"></script><link type=\"text/css\" rel=\"stylesheet\" href=\"http://172.16.102.33/jenkins-material-theme.css\"/><script src=\"/static/5b5711cc/jsbundles/page-init.js\" type=\"text/javascript\"></script></head><body data-model-type=\"hudson.model.Hudson\" id=\"jenkins\" class=\"yui-skin-sam two-column jenkins-2.164.1\" data-version=\"2.164.1\"><a href=\"#skip2content\" class=\"skiplink\">Skip to content</a><div id=\"page-head\"><div id=\"header\"><div class=\"logo\"><a id=\"jenkins-home-link\" href=\"/\"><img src=\"/static/5b5711cc/images/headshot.png\" alt=\"[Jenkins]\" id=\"jenkins-head-icon\" /><img src=\"/static/5b5711cc/images/title.png\" alt=\"Jenkins\" width=\"139\" id=\"jenkins-name-icon\" height=\"34\" /></a></div><div class=\"login\"> <a href=\"/login?from=%2Fjob%2Fsalt-devops-web%2Fapi%2Fjson\"><b>log in</b></a></div><div class=\"searchbox hidden-xs\"><form role=\"search\" method=\"get\" name=\"search\" action=\"/search/\" style=\"position:relative;\" class=\"no-json\"><div id=\"search-box-minWidth\"></div><div id=\"search-box-sizer\"></div><div id=\"searchform\"><input role=\"searchbox\" name=\"q\" placeholder=\"search\" id=\"search-box\" class=\"has-default-text\" /> <a href=\"https://jenkins.io/redirect/search-box\"><img src=\"/static/5b5711cc/images/16x16/help.png\" style=\"width: 16px; height: 16px; \" class=\"icon-help icon-sm\" /></a><div id=\"search-box-completion\"></div><script>createSearchBox(\"/search/\");</script></div></form></div></div><div id=\"breadcrumbBar\"><tr id=\"top-nav\"><td id=\"left-top-nav\" colspan=\"2\"><link rel=\'stylesheet\' href=\'/adjuncts/5b5711cc/lib/layout/breadcrumbs.css\' type=\'text/css\' /><script src=\'/adjuncts/5b5711cc/lib/layout/breadcrumbs.js\' type=\'text/javascript\'></script><div class=\"top-sticker noedge\"><div class=\"top-sticker-inner\"><div id=\"right-top-nav\"></div><ul id=\"breadcrumbs\"><li class=\"item\"><a href=\"/\" class=\"model-link inside\">Jenkins</a></li><li href=\"/\" class=\"children\"></li></ul><div id=\"breadcrumb-menu-target\"></div></div></div></td></tr></div></div><div id=\"page-body\" class=\"clear\"><div id=\"side-panel\"><div class=\"task\"><a href=\"https://jenkins.io/\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/next.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-next icon-md\" /></a> <a href=\"https://jenkins.io/\" class=\"task-link\">Jenkins project</a></div><div class=\"task\"><a href=\"https://jenkins.io/redirect/report-an-issue\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/gear2.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-gear2 icon-md\" /></a> <a href=\"https://jenkins.io/redirect/report-an-issue\" class=\"task-link\">Bug tracker</a></div><div class=\"task\"><a href=\"https://jenkins.io/redirect/mailing-lists\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/search.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-search icon-md\" /></a> <a href=\"https://jenkins.io/redirect/mailing-lists\" class=\"task-link\">Mailing Lists</a></div><div class=\"task\"><a href=\"https://twitter.com/jenkinsci\" class=\"task-icon-link\"><img src=\"/static/5b5711cc/images/24x24/user.png\" style=\"width: 24px; height: 24px; width: 24px; height: 24px; margin: 2px;\" class=\"icon-user icon-md\" /></a> <a href=\"https://twitter.com/jenkinsci\" class=\"task-link\">Twitter: @jenkinsci</a></div></div><div id=\"main-panel\"><a name=\"skip2content\"></a><h1 style=\"text-align: center\"><img src=\"/static/5b5711cc/images/rage.png\" width=\"154\" height=\"179\" /><span style=\"font-size:50px\"> Oops!</span></h1><div id=\"error-description\"><p>A problem occurred while processing the request.\n        Please check <a href=\"https://jenkins.io/redirect/issue-tracker\">our bug tracker</a> to see if a similar problem has already been reported.\n        If it is already reported, please vote and put a comment on it to let us gauge the impact of the problem.\n        If you think this is a new issue, please file a new issue.\n        When you file an issue, make sure to add the entire stack trace, along with the version of Jenkins and relevant plugins.\n        <a href=\"https://jenkins.io/redirect/users-mailing-list\">The users list</a> might be also useful in understanding what has happened.</p><h2>Stack trace</h2><pre style=\"margin:2em; clear:both\">org.acegisecurity.userdetails.UsernameNotFoundException: User cainanjie not found in directory.\n	at org.acegisecurity.ldap.search.FilterBasedLdapUserSearch.searchForUser(FilterBasedLdapUserSearch.java:126)\n	at hudson.security.LDAPSecurityRealm$LDAPUserDetailsService.loadUserByUsername(LDAPSecurityRealm.java:1314)\n	at hudson.security.LDAPSecurityRealm$LDAPUserDetailsService.loadUserByUsername(LDAPSecurityRealm.java:1251)\n	at jenkins.security.ImpersonatingUserDetailsService.loadUserByUsername(ImpersonatingUserDetailsService.java:32)\n	at hudson.model.User.getUserDetailsForImpersonation(User.java:398)\n	at jenkins.security.BasicHeaderApiTokenAuthenticator.authenticate(BasicHeaderApiTokenAuthenticator.java:35)\nCaused: javax.servlet.ServletException\n	at jenkins.security.BasicHeaderApiTokenAuthenticator.authenticate(BasicHeaderApiTokenAuthenticator.java:43)\n	at jenkins.security.BasicHeaderProcessor.doFilter(BasicHeaderProcessor.java:79)\n	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)\n	at org.acegisecurity.context.HttpSessionContextIntegrationFilter.doFilter(HttpSessionContextIntegrationFilter.java:249)\n	at hudson.security.HttpSessionContextIntegrationFilter2.doFilter(HttpSessionContextIntegrationFilter2.java:67)\n	at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)\n	at hudson.security.ChainedServletFilter.doFilter(ChainedServletFilter.java:90)\n	at hudson.security.HudsonFilter.doFilter(HudsonFilter.java:171)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.kohsuke.stapler.compression.CompressionFilter.doFilter(CompressionFilter.java:49)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at hudson.util.CharacterEncodingFilter.doFilter(CharacterEncodingFilter.java:82)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.kohsuke.stapler.DiagnosticThreadNameFilter.doFilter(DiagnosticThreadNameFilter.java:30)\n	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1642)\n	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:533)\n	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:146)\n	at org.eclipse.jetty.security.SecurityHandler.handle(SecurityHandler.java:524)\n	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:132)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextHandle(ScopedHandler.java:257)\n	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:1595)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextHandle(ScopedHandler.java:255)\n	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1340)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextScope(ScopedHandler.java:203)\n	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:473)\n	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:1564)\n	at org.eclipse.jetty.server.handler.ScopedHandler.nextScope(ScopedHandler.java:201)\n	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:1242)\n	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:144)\n	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:132)\n	at org.eclipse.jetty.server.Server.handle(Server.java:503)\n	at org.eclipse.jetty.server.HttpChannel.handle(HttpChannel.java:364)\n	at org.eclipse.jetty.server.HttpConnection.onFillable(HttpConnection.java:260)\n	at org.eclipse.jetty.io.AbstractConnection$ReadCallback.succeeded(AbstractConnection.java:305)\n	at org.eclipse.jetty.io.FillInterest.fillable(FillInterest.java:103)\n	at org.eclipse.jetty.io.ChannelEndPoint$2.run(ChannelEndPoint.java:118)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.runTask(EatWhatYouKill.java:333)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.doProduce(EatWhatYouKill.java:310)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.tryProduce(EatWhatYouKill.java:168)\n	at org.eclipse.jetty.util.thread.strategy.EatWhatYouKill.run(EatWhatYouKill.java:126)\n	at org.eclipse.jetty.util.thread.ReservedThreadExecutor$ReservedThread.run(ReservedThreadExecutor.java:366)\n	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:765)\n	at org.eclipse.jetty.util.thread.QueuedThreadPool$2.run(QueuedThreadPool.java:683)\n	at java.lang.Thread.run(Thread.java:748)\n</pre></div></div></div><footer><div class=\"container-fluid\"><div class=\"row\"><div class=\"col-md-6\" id=\"footer\"></div><div class=\"col-md-18\"><span class=\"page_generated\">Page generated: Jul 2, 2019 10:59:43 AM CST</span><span class=\"rest_api\"><a href=\"api/\">REST API</a></span><span class=\"jenkins_ver\"><a href=\"https://jenkins.io/\">Jenkins ver. 2.164.1</a></span></div></div></div></footer></body></html>',0.01);
/*!40000 ALTER TABLE `deploy_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_project`
--

DROP TABLE IF EXISTS `deploy_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_project` (
  `id` char(32) NOT NULL,
  `name` varchar(64) NOT NULL,
  `jenkins_job` varchar(128) NOT NULL,
  `jenkins_params` varchar(128),
  `gitlab_project` varchar(128) NOT NULL,
  `package_url` varchar(128) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `desc` longtext DEFAULT NULL,
  `creator_id` char(32) NOT NULL,
  `deploy_type` int(11) NOT NULL,
  `version` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `deploy_project_creator_id_9f4fc5c0_fk_auth_user_id` (`creator_id`),
  CONSTRAINT `deploy_project_creator_id_9f4fc5c0_fk_auth_user_id` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_project`
--

LOCK TABLES `deploy_project` WRITE;
/*!40000 ALTER TABLE `deploy_project` DISABLE KEYS */;
INSERT INTO `deploy_project` VALUES ('15b669186481402489b353a360ad6fa9','devops-server','salt-devops-server','{}','cainanjie/devops-server','devops-server.tar.gz','2019-06-20 16:11:19.755770','运维平台后端','8e1cde13e0794809aa1c472cfa0138f2',1,0.03),('55ca84a411e543eb9d9801aa28844a06','ztocwst-wms','salt-wms','{}','ztocwst-wms/wms','build/libs/ztocwst-wms.war','2019-06-27 14:29:08.071345',NULL,'8e1cde13e0794809aa1c472cfa0138f2',1,0.03),('70a6de14d4eb41ed9917754586ca4af9','devops-web','salt-devops-web','{}','zhaochaojiang/devops-web','dist/devops-web.tar.gz','2019-06-20 15:33:17.900270','运维平台前端','8e1cde13e0794809aa1c472cfa0138f2',0,0.02);
/*!40000 ALTER TABLE `deploy_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_project_project_maps`
--

DROP TABLE IF EXISTS `deploy_project_project_maps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_project_project_maps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` char(32) NOT NULL,
  `envserversmap_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `deploy_project_project_m_project_id_envserversmap_23996361_uniq` (`project_id`,`envserversmap_id`),
  KEY `deploy_project_proje_envserversmap_id_bebd53b9_fk_deploy_en` (`envserversmap_id`),
  CONSTRAINT `deploy_project_proje_envserversmap_id_bebd53b9_fk_deploy_en` FOREIGN KEY (`envserversmap_id`) REFERENCES `deploy_envserversmap` (`id`),
  CONSTRAINT `deploy_project_proje_project_id_ec09d285_fk_deploy_pr` FOREIGN KEY (`project_id`) REFERENCES `deploy_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_project_project_maps`
--

LOCK TABLES `deploy_project_project_maps` WRITE;
/*!40000 ALTER TABLE `deploy_project_project_maps` DISABLE KEYS */;
INSERT INTO `deploy_project_project_maps` VALUES (2,'15b669186481402489b353a360ad6fa9',3),(3,'55ca84a411e543eb9d9801aa28844a06',1),(1,'70a6de14d4eb41ed9917754586ca4af9',1);
/*!40000 ALTER TABLE `deploy_project_project_maps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_apscheduler_djangojob`
--

DROP TABLE IF EXISTS `django_apscheduler_djangojob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_apscheduler_djangojob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `next_run_time` datetime(6) DEFAULT NULL,
  `job_state` longblob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_apscheduler_djangojob_next_run_time_2f022619` (`next_run_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_apscheduler_djangojob`
--

LOCK TABLES `django_apscheduler_djangojob` WRITE;
/*!40000 ALTER TABLE `django_apscheduler_djangojob` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_apscheduler_djangojob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_apscheduler_djangojobexecution`
--

DROP TABLE IF EXISTS `django_apscheduler_djangojobexecution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_apscheduler_djangojobexecution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `run_time` datetime(6) NOT NULL,
  `duration` decimal(15,2) DEFAULT NULL,
  `started` decimal(15,2) DEFAULT NULL,
  `finished` decimal(15,2) DEFAULT NULL,
  `exception` varchar(1000) DEFAULT NULL,
  `traceback` longtext DEFAULT NULL,
  `job_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_apscheduler_d_job_id_daf5090a_fk_django_ap` (`job_id`),
  KEY `django_apscheduler_djangojobexecution_run_time_16edd96b` (`run_time`),
  CONSTRAINT `django_apscheduler_d_job_id_daf5090a_fk_django_ap` FOREIGN KEY (`job_id`) REFERENCES `django_apscheduler_djangojob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_apscheduler_djangojobexecution`
--

LOCK TABLES `django_apscheduler_djangojobexecution` WRITE;
/*!40000 ALTER TABLE `django_apscheduler_djangojobexecution` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_apscheduler_djangojobexecution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (15,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(19,'authtoken','token'),(3,'contenttypes','contenttype'),(25,'deploy','deployenv'),(23,'deploy','deploymentorder'),(26,'deploy','envserversmap'),(24,'deploy','history'),(22,'deploy','project'),(17,'django_apscheduler','djangojob'),(18,'django_apscheduler','djangojobexecution'),(20,'ldap','permission'),(14,'purview','permission'),(8,'resources','ip'),(11,'resources','node'),(10,'resources','pots'),(7,'resources','provider'),(9,'resources','ram'),(12,'resources','server'),(16,'sessions','session'),(21,'SQLAudit','permission'),(5,'users','loginlog'),(4,'users','user'),(6,'users','usergroup'),(13,'workOrder','workorder');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-28 13:35:28.805482'),(2,'contenttypes','0002_remove_content_type_name','2019-03-28 13:35:28.922165'),(3,'auth','0001_initial','2019-03-28 13:35:29.170791'),(4,'auth','0002_alter_permission_name_max_length','2019-03-28 13:35:29.286914'),(5,'auth','0003_alter_user_email_max_length','2019-03-28 13:35:29.311571'),(6,'auth','0004_alter_user_username_opts','2019-03-28 13:35:29.337060'),(7,'auth','0005_alter_user_last_login_null','2019-03-28 13:35:29.360702'),(8,'auth','0006_require_contenttypes_0002','2019-03-28 13:35:29.368104'),(9,'auth','0007_alter_validators_add_error_messages','2019-03-28 13:35:29.394224'),(10,'auth','0008_alter_user_username_max_length','2019-03-28 13:35:29.463739'),(11,'users','0001_initial','2019-03-28 13:35:30.066129'),(12,'admin','0001_initial','2019-03-28 13:36:03.177672'),(13,'admin','0002_logentry_remove_auto_add','2019-03-28 13:36:03.211050'),(14,'authtoken','0001_initial','2019-03-28 13:36:03.283185'),(15,'authtoken','0002_auto_20160226_1747','2019-03-28 13:36:03.394073'),(16,'django_apscheduler','0001_initial','2019-03-28 13:36:03.528448'),(17,'django_apscheduler','0002_auto_20180412_0758','2019-03-28 13:36:03.598785'),(18,'sessions','0001_initial','2019-03-28 13:36:03.675338'),(19,'resources','0001_initial','2019-03-28 13:36:34.000483'),(20,'workOrder','0001_initial','2019-03-28 13:36:45.794079'),(21,'users','0002_user_properties','2019-04-19 17:36:42.687454'),(22,'users','0003_remove_user_properties','2019-04-19 17:37:13.026277'),(23,'users','0004_user_properties','2019-04-19 17:38:01.967110'),(25,'deploy','0001_initial','2019-06-20 15:05:37.660126'),(26,'deploy','0002_auto_20190624_1325','2019-06-24 13:25:41.634397'),(27,'deploy','0003_auto_20190627_1415','2019-06-27 14:16:02.424228'),(28,'deploy','0004_auto_20190627_1603','2019-06-27 16:03:29.989721'),(29,'deploy','0005_auto_20190627_1605','2019-06-27 16:05:15.530846');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4daxx8918d78nj0clt9fmvgrc1ii3345','MmRlMDk0NjBmZThkNzY5YWY5NWFmNDIwMWQ4MmRhOTllMWY1ODJlYjp7Il9hdXRoX3VzZXJfaWQiOiI4ZTFjZGUxMy1lMDc5LTQ4MDktYWExYy00NzJjZmEwMTM4ZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZjNjA4MjUxMjRiNzlkYmI0YTA2MmE4ODAzMmM1ODRiMjU5MWYwNWIifQ==','2019-06-17 14:30:00.003632'),('80imnpzuxoayl2y20mw9jzbbyc61rba8','MmRlMDk0NjBmZThkNzY5YWY5NWFmNDIwMWQ4MmRhOTllMWY1ODJlYjp7Il9hdXRoX3VzZXJfaWQiOiI4ZTFjZGUxMy1lMDc5LTQ4MDktYWExYy00NzJjZmEwMTM4ZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZjNjA4MjUxMjRiNzlkYmI0YTA2MmE4ODAzMmM1ODRiMjU5MWYwNWIifQ==','2019-07-04 16:21:44.974286'),('f90or2wkgbkersdpa2x4u0zivmpohais','NDIxOWE4MTlkZjcyOWNkMGE3ZWE5NTFjMzlhZmE2MTM2ZmUwNDFiNzp7Il9hdXRoX3VzZXJfaWQiOiI0MWQ5NGEyZC0wZTQzLTQ0NWMtYTU1Yy02YTMxYzRhNDQ5MWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImJjOWM1ZjIxOGM1YTE0NzU4YjIxZmNmYjZkYTYzYjQzODhkMDU0ZGMifQ==','2019-04-22 10:03:29.262273'),('i4s8e12d70b48tz4z7lq498sbl0nhdb9','YjBmNWZjMmM5MTk1ZmI3MTY0MjJkZjlmMzg3ZTJkYTI2MWYxZmE1OTp7Il9hdXRoX3VzZXJfaWQiOiI4ZTFjZGUxMy1lMDc5LTQ4MDktYWExYy00NzJjZmEwMTM4ZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZhNTBkYThjNGE5NjhlZjcyNDZjMTM2MmQyOTMyMGFlZjNmNTMyYjcifQ==','2019-04-23 16:23:35.140122'),('k8shtv1k6af01gw3m8n508algp4w2j3c','NDIxOWE4MTlkZjcyOWNkMGE3ZWE5NTFjMzlhZmE2MTM2ZmUwNDFiNzp7Il9hdXRoX3VzZXJfaWQiOiI0MWQ5NGEyZC0wZTQzLTQ0NWMtYTU1Yy02YTMxYzRhNDQ5MWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImJjOWM1ZjIxOGM1YTE0NzU4YjIxZmNmYjZkYTYzYjQzODhkMDU0ZGMifQ==','2019-06-11 17:16:27.795233'),('urjqgya7fr9m0aiihwomt7a2xh0g2oa6','MmRlMDk0NjBmZThkNzY5YWY5NWFmNDIwMWQ4MmRhOTllMWY1ODJlYjp7Il9hdXRoX3VzZXJfaWQiOiI4ZTFjZGUxMy1lMDc5LTQ4MDktYWExYy00NzJjZmEwMTM4ZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZjNjA4MjUxMjRiNzlkYmI0YTA2MmE4ODAzMmM1ODRiMjU5MWYwNWIifQ==','2019-06-18 08:40:30.797218'),('vj19ija8kg2oqazuny5qli4lufyp7105','MmRlMDk0NjBmZThkNzY5YWY5NWFmNDIwMWQ4MmRhOTllMWY1ODJlYjp7Il9hdXRoX3VzZXJfaWQiOiI4ZTFjZGUxMy1lMDc5LTQ4MDktYWExYy00NzJjZmEwMTM4ZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZjNjA4MjUxMjRiNzlkYmI0YTA2MmE4ODAzMmM1ODRiMjU5MWYwNWIifQ==','2019-06-17 08:58:22.936164'),('zue79v7koppjabau35ystmytf9j75qlh','YjBmNWZjMmM5MTk1ZmI3MTY0MjJkZjlmMzg3ZTJkYTI2MWYxZmE1OTp7Il9hdXRoX3VzZXJfaWQiOiI4ZTFjZGUxMy1lMDc5LTQ4MDktYWExYy00NzJjZmEwMTM4ZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZhNTBkYThjNGE5NjhlZjcyNDZjMTM2MmQyOTMyMGFlZjNmNTMyYjcifQ==','2019-06-05 15:12:11.976291');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_ip`
--

DROP TABLE IF EXISTS `resources_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` char(39) NOT NULL,
  `inner_id` char(32) DEFAULT NULL,
  `public_id` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `resources_ip_ip_85322bd8` (`ip`),
  KEY `resources_ip_inner_id_1852f418_fk_resources_server_id` (`inner_id`),
  KEY `resources_ip_public_id_0d13e142_fk_resources_server_id` (`public_id`),
  CONSTRAINT `resources_ip_inner_id_1852f418_fk_resources_server_id` FOREIGN KEY (`inner_id`) REFERENCES `resources_server` (`id`),
  CONSTRAINT `resources_ip_public_id_0d13e142_fk_resources_server_id` FOREIGN KEY (`public_id`) REFERENCES `resources_server` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_ip`
--

LOCK TABLES `resources_ip` WRITE;
/*!40000 ALTER TABLE `resources_ip` DISABLE KEYS */;
INSERT INTO `resources_ip` VALUES (4,'172.16.102.40','3bb94d569a8e56e5604176045f5565f6',NULL),(5,'172.16.102.51','a0974d56ba3701509a9a0319d729717d',NULL),(6,'172.17.0.1','a0974d56ba3701509a9a0319d729717d',NULL),(7,'172.16.102.64','c49e4d56aec1caf0c39c02144fd6633e',NULL),(8,'172.17.0.1','c49e4d56aec1caf0c39c02144fd6633e',NULL),(9,'172.18.38.205','df84e4e229294a4e974dae5512352515',NULL);
/*!40000 ALTER TABLE `resources_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_node`
--

DROP TABLE IF EXISTS `resources_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_node` (
  `id` char(32) NOT NULL,
  `key` varchar(64) NOT NULL,
  `child_mark` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `created` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_node`
--

LOCK TABLES `resources_node` WRITE;
/*!40000 ALTER TABLE `resources_node` DISABLE KEYS */;
INSERT INTO `resources_node` VALUES ('37aa232e66c54297b5fcbf29b30a2703','2:1:0:1',0,'devops','2019-04-22 17:35:27.191429'),('73915cd1c4164142a3b9e5a872696750','2:1:1',1,'测试环境','2019-06-05 13:46:01.168864'),('963c4af319644a8a845aa0c1d4d1326d','2:1:0',2,'运维平台','2019-06-05 13:44:37.199909'),('9d562f4b36014db08bcfd9edf3cc5e53','2:1:1:0',0,'wms项目','2019-06-05 13:46:13.845806'),('b94af7de164b4a2b85f41a12d550de8f','2:1',2,'杭州IDC机房','2019-06-05 13:43:54.238210'),('bfe50c7822c74b3498d90aeb527325d8','1',0,'服务器','2019-04-04 16:47:55.978972'),('e83b2c95adb3466790f63d360174169a','0',0,'SERVER','2019-04-04 16:05:06.815624'),('f3ab615076e54913865011cb63542136','2',2,'SERVERS','2019-04-19 17:51:49.054774');
/*!40000 ALTER TABLE `resources_node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_pots`
--

DROP TABLE IF EXISTS `resources_pots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_pots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resources_name` varchar(64) NOT NULL,
  `node_name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resources_name` (`resources_name`),
  UNIQUE KEY `node_name` (`node_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_pots`
--

LOCK TABLES `resources_pots` WRITE;
/*!40000 ALTER TABLE `resources_pots` DISABLE KEYS */;
INSERT INTO `resources_pots` VALUES (1,'SERVER','SERVER'),(2,'SERVERS','SERVERS');
/*!40000 ALTER TABLE `resources_pots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_provider`
--

DROP TABLE IF EXISTS `resources_provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_provider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `code` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_provider`
--

LOCK TABLES `resources_provider` WRITE;
/*!40000 ALTER TABLE `resources_provider` DISABLE KEYS */;
INSERT INTO `resources_provider` VALUES (1,'杭州总部机房','hangzhou'),(2,'阿里云','002'),(3,'天翼云','003');
/*!40000 ALTER TABLE `resources_provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_ram`
--

DROP TABLE IF EXISTS `resources_ram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_ram` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `physical` int(11) DEFAULT NULL,
  `swap` int(11) DEFAULT NULL,
  `server_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `server_id` (`server_id`),
  CONSTRAINT `resources_ram_server_id_d39e7f29_fk_resources_server_id` FOREIGN KEY (`server_id`) REFERENCES `resources_server` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_ram`
--

LOCK TABLES `resources_ram` WRITE;
/*!40000 ALTER TABLE `resources_ram` DISABLE KEYS */;
INSERT INTO `resources_ram` VALUES (4,3945,3944,'3bb94d569a8e56e5604176045f5565f6'),(5,16047,8191,'a0974d56ba3701509a9a0319d729717d'),(6,7983,8191,'c49e4d56aec1caf0c39c02144fd6633e'),(7,7822,0,'df84e4e229294a4e974dae5512352515');
/*!40000 ALTER TABLE `resources_ram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_server`
--

DROP TABLE IF EXISTS `resources_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_server` (
  `id` char(32) NOT NULL,
  `hostname` varchar(128) NOT NULL,
  `saltID` varchar(128) DEFAULT NULL,
  `planform` varchar(56) NOT NULL,
  `os` varchar(128) NOT NULL,
  `cpu_model` varchar(256) DEFAULT NULL,
  `cpu_arch` varchar(32) DEFAULT NULL,
  `cpu_count` int(11) DEFAULT NULL,
  `protocol` varchar(8) NOT NULL,
  `port` int(11) NOT NULL,
  `_IP` char(39) DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `provider_id` int(11) DEFAULT NULL,
  `env` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `saltID` (`saltID`),
  KEY `resources_server_provider_id_87203cd4_fk_resources_provider_id` (`provider_id`),
  KEY `resources_server_hostname_2a827d99` (`hostname`),
  CONSTRAINT `resources_server_provider_id_87203cd4_fk_resources_provider_id` FOREIGN KEY (`provider_id`) REFERENCES `resources_provider` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_server`
--

LOCK TABLES `resources_server` WRITE;
/*!40000 ALTER TABLE `resources_server` DISABLE KEYS */;
INSERT INTO `resources_server` VALUES ('3bb94d569a8e56e5604176045f5565f6','devops','devops','Linux','Ubuntu 18.4 amd64','Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz','x86_64',2,'ssh',22,'172.16.102.40','来自salt添加','2019-05-31 15:44:26.462770',1,0),('a0974d56ba3701509a9a0319d729717d','hz01-qa-ops-docker-03','hz01-qa-ops-docker-03','Linux','CentOS 7.5.1804 x86_64','Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz','x86_64',2,'ssh',22,'172.16.102.51','来自salt添加','2019-06-05 11:53:35.196793',1,2),('c49e4d56aec1caf0c39c02144fd6633e','hz01-qa-ops-docker-04','hz01-qa-ops-docker-04','Linux','CentOS 7.5.1804 x86_64','Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz','x86_64',2,'ssh',22,'172.16.102.64','来自salt添加','2019-06-05 14:02:21.921173',1,2),('df84e4e229294a4e974dae5512352515','ali02-pre-wms-wms-01','ali02-pre-wms-wms-01','Linux','CentOS 7.4.1708 x86_64','Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz','x86_64',2,'ssh',22,'172.18.38.205','来自salt添加','2019-06-10 11:25:53.118425',2,1);
/*!40000 ALTER TABLE `resources_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_server_nodes`
--

DROP TABLE IF EXISTS `resources_server_nodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources_server_nodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_id` char(32) NOT NULL,
  `node_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resources_server_nodes_server_id_node_id_22e05330_uniq` (`server_id`,`node_id`),
  KEY `resources_server_nodes_node_id_eef93a84_fk_resources_node_id` (`node_id`),
  CONSTRAINT `resources_server_nodes_node_id_eef93a84_fk_resources_node_id` FOREIGN KEY (`node_id`) REFERENCES `resources_node` (`id`),
  CONSTRAINT `resources_server_nodes_server_id_350853c2_fk_resources_server_id` FOREIGN KEY (`server_id`) REFERENCES `resources_server` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_server_nodes`
--

LOCK TABLES `resources_server_nodes` WRITE;
/*!40000 ALTER TABLE `resources_server_nodes` DISABLE KEYS */;
INSERT INTO `resources_server_nodes` VALUES (9,'3bb94d569a8e56e5604176045f5565f6','37aa232e66c54297b5fcbf29b30a2703'),(8,'3bb94d569a8e56e5604176045f5565f6','f3ab615076e54913865011cb63542136'),(13,'a0974d56ba3701509a9a0319d729717d','9d562f4b36014db08bcfd9edf3cc5e53'),(10,'a0974d56ba3701509a9a0319d729717d','f3ab615076e54913865011cb63542136'),(14,'c49e4d56aec1caf0c39c02144fd6633e','9d562f4b36014db08bcfd9edf3cc5e53'),(12,'c49e4d56aec1caf0c39c02144fd6633e','f3ab615076e54913865011cb63542136'),(15,'df84e4e229294a4e974dae5512352515','f3ab615076e54913865011cb63542136');
/*!40000 ALTER TABLE `resources_server_nodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_loginlog`
--

DROP TABLE IF EXISTS `users_loginlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_loginlog` (
  `id` char(32) NOT NULL,
  `username` varchar(32) NOT NULL,
  `type` varchar(16) NOT NULL,
  `ip` char(39) NOT NULL,
  `city` varchar(128) DEFAULT NULL,
  `agent` varchar(256) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `logined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_loginlog`
--

LOCK TABLES `users_loginlog` WRITE;
/*!40000 ALTER TABLE `users_loginlog` DISABLE KEYS */;
INSERT INTO `users_loginlog` VALUES ('01a479268614434da37a6f3962c1c67a','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 17:38:22.490353'),('04cc64b4fe514cd2b0bf305bc0eb2ada','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-28 15:29:43.972685'),('091bc48980ae44b18c0c26c37d7bdc51','000093','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',1,'2019-03-31 23:09:54.841195'),('0a4933f091dc4ff79f9e62d883cd9b2d','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-01 11:25:21.214346'),('0b045bb992494570b39edfe8cd35c0b6','admin','JWT','172.16.10.131','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-04 10:02:51.602035'),('0b737b218750420ea6b9d2fa3e327c18','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-24 13:41:40.659024'),('0bf2ed6778e34363b9faba823203913c','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-10 11:24:48.019395'),('119faa9a59e0437cab95d1f9cd9aeb17','infopath','JWT','172.16.210.103','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-22 17:15:46.146121'),('17cf01f0c9194785b1c186ab6a38539e','000370','JWT','172.16.10.235','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-04 19:46:58.521628'),('18546df72b014402820a7aeebfcfde34','admin','JWT','172.16.210.29','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-26 17:05:58.393358'),('18a386f6850440098938a8e8fc3ea0cf','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-06-03 18:31:05.624224'),('1cbbec6ae16c41219c7b31afb80faeff','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-24 10:31:54.717433'),('1d3d7899b2d147a6883bd8994f5f6bd5','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-22 15:30:28.416667'),('1e1cfff9064042e4b72bb722793d0472','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',1,'2019-03-31 23:10:37.081835'),('20f0ce2581974617a9a2f8ab57414c31','admin','JWT','2.0.1.13','法国 XX','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-28 20:27:56.256041'),('24d4a9e73de44ad78fc96823f3d33efb','admin','JWT','172.16.210.29','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-27 08:36:33.413235'),('24e81d2c5e5c4571b9e8a185f8a43500','18868877661','JWT','172.16.210.19','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',0,'2019-04-02 11:12:31.047059'),('26f837ed0f8643b5994f7e3ffe2e324b','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-27 15:36:51.013540'),('27ad94ab3dea4db8bfccc58df320515b','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-11 09:04:02.943539'),('29d8f0753eed431cb2e5c60587eb1775','admin','JWT','2.0.1.3','法国 XX','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-24 13:14:16.833299'),('2cf2ed0d9bf344f885e0ab3c60a06d11','000214','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',1,'2019-06-04 08:33:36.035189'),('2d8d67467bce4ea5b2aec718121ed43a','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-05 15:53:07.152238'),('30dcaf037d7044a2abd71db652b51123','admin','JWT','172.16.210.199','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-17 09:11:47.120619'),('33ad9c8f321e4029bf52a17848567b2d','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 17:32:52.393298'),('33fc06122efd467082815c039669ac8e','admin','JWT','172.16.10.121','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',1,'2019-06-26 17:25:30.483014'),('344ec32fd6be43e2b1c6d740602e7a88','admin','JWT','172.16.210.158','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',0,'2019-04-01 09:06:09.095017'),('37832996969d445680cdfc8a62a46002','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-28 14:16:17.678707'),('38847e3129bb4ed1a14f73d7cf69eef6','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-30 09:04:38.918345'),('3b8a758dcd734b9387c82cf6ed34d6a0','admin','JWT','2.0.1.8','法国 XX','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-16 00:24:37.141387'),('3dfdbcf2656c4ae39ddcfdee8b92abfb','admin','JWT','172.16.10.121','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',1,'2019-06-24 14:09:21.428775'),('3ee6d902c0f143c59c3ddd8b6c4bedcd','admin','JWT','172.16.210.14','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',1,'2019-06-27 17:13:51.791396'),('4129d6bed7e148e2bad770071df83064','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-20 17:16:23.924059'),('41a96021b3224e989c79265b4766cb47','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-06-04 08:32:23.881860'),('4525794685474e489b2a2898820eb5a6','admin','JWT','172.16.210.103','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-22 09:32:16.126955'),('47cf50f0d8e24e2aafc0ba045a6e1d95','000151','JWT','172.16.100.20','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-06 11:02:58.175118'),('4fc287b6053d4cdaacb689d835a3d5c9','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-18 14:40:01.697098'),('54a620164f414331a26e67104b7740f4','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-29 08:37:45.178048'),('5518a5d2db7648cc8d01c8f6128af6a0','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-24 10:02:26.875439'),('55d02352983444d68e8bc8acf1c99303','000214','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-04 11:10:46.271679'),('5cef729932804a779947d9ed556f24b2','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-24 14:35:08.885482'),('5fa6e5cdba7e48ba8a8934eab56eefb5','000214','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-06-03 17:29:00.833260'),('602ec60ff10a4b7397ef952cd484d18c','zhoujinliang','JWT','172.16.100.20','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',0,'2019-06-06 11:02:41.696198'),('606bc304b77046529302846eaef379f9','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-11 08:42:55.309750'),('62154de27bce4337bf67d96f6b226cb2','admin','JWT','172.16.210.29','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-28 08:52:45.153833'),('63ae687175f64705af9a76145c7aadfc','000343','JWT','172.16.10.58','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-04 14:13:17.684385'),('64ea534df9004081bb750251d8f0df8e','admin','JWT','172.16.210.29','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-27 13:45:39.058484'),('6635b490fe554e76b108be05f25c7d07','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-28 09:36:30.256806'),('669d59318c654813a56b4eee49f82823','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-29 08:27:52.828735'),('66ea7ffad26f4beeb5a6bbbc03f5bfa2','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-01 14:09:41.866842'),('67475e6c6fbc4721b5be4b262ba1c850','000214','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-10 10:12:32.607162'),('6830dcd59fe94a8c8d8c0ace27afdf36','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-29 10:03:40.970913'),('698e7d33a3a741cb85917739adc26f7e','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',1,'2019-05-14 09:28:22.223450'),('72488e9e219f4ae7bac80b3e47c71818','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-28 10:22:57.590246'),('772ab585ef2f4ad78e531689e9b1eb60','000343','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 11:12:18.310997'),('78552fe0b5554dfda25b514f1ca8b349','admin1','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',0,'2019-05-29 08:41:24.447634'),('7888e4df638a46bc9f7864580ba988cf','000093','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-22 10:44:43.865659'),('7d050eab1c874a329da08c2a0cfcdf53','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-29 08:27:38.066756'),('7e3731c6991e4d13a1e54c3450d13021','admin','JWT','172.16.210.158','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-04 15:46:44.148220'),('817ec9f1e2da47629073e6f3d329dd9e','000214','JWT','172.16.210.103','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-22 17:19:08.590362'),('862f919867d84f75a9fed63451321d97','000370','JWT','172.16.210.222','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',1,'2019-04-25 15:49:16.646332'),('871b7aa8f386408dbb2a5475e507acfc','000323','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-22 17:16:53.658683'),('8890617e698042c4ac5fd6b936f01d31','admin','JWT','172.16.210.158','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-04 15:56:06.407430'),('8eb559bb87204acf831b1736734e6c8c','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-05-30 15:09:45.463228'),('8f102adcaca44fc7be19780c5fdef8d6','000214','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-06 10:36:11.542611'),('90c0ecac511340d28551212d508166e4','000343','JWT','172.16.10.58','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-08 09:44:49.271677'),('9183db9998154aaea3fe9a3f56735aa4','000343','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 11:14:03.046038'),('94c12b1dd8194ff9a8ad9f579580a112','admin','JWT','172.16.210.103','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 18:46:22.685775'),('99de276fdd9541a38c647e16f0648682','admin','JWT','172.16.10.58','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 17:23:06.624519'),('9dd8acc0318a4faf9edd5154423e503f','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-27 09:22:02.775047'),('9f27590237cd4618867e9ea01691e1c6','admin','JWT','172.16.10.121','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',1,'2019-06-28 09:12:01.181728'),('a1b3b130844b49c3a6d1c4366720624d','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-06-03 14:37:36.776864'),('a3db11ce4ebf4a1da1bd70d5c35f106a','000214','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-10 11:31:29.713221'),('a4cfaef77d10495da13f9034279e2d5f','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-05-31 15:41:57.197416'),('a8ba90de94cd484a800086dddcacc5c0','admin','JWT','172.16.210.84','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 14:23:37.177579'),('a9058afe605d4da0aa3c2241468a5fe5','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-01 14:09:36.670732'),('a99dd6a63ca64beb9d6bd64d245869f0','000214','JWT','172.16.100.51','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-01 12:27:17.513120'),('a9d44ecbadb645f189214f32b4f15dc5','admin','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 11:13:14.607779'),('ac6f2b48b277405ab86c570bef82dae1','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-10 17:12:12.377962'),('ac761180d53b467abb1076fd012675bc','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',0,'2019-04-01 08:35:18.875598'),('acf9e465acc0439ab8a9efb3ed24d8b7','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 17:31:51.116693'),('aeff1a8c6cc6436bb243c4a0a3f85e20','admin','JWT','172.16.210.14','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',1,'2019-06-27 08:36:38.423353'),('b700be674f6244fa87b37b0aab5685f3','000214','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 17:46:04.982631'),('b72747218b1c44c7a220823584d6590a','admin','JWT','172.16.10.131','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-05 09:34:02.513139'),('bf8427514e434a039c8858b7a259d67d','000365','JWT','172.16.210.84','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 14:17:09.462448'),('c7a3f11e89224989add903a1023a5349','000343','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 13:58:34.040916'),('c7c8c042c78b46e5b4397d4b0c11ac06','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-05-06 15:36:19.142928'),('c96b08ed898d4e3085739946d085564d','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',0,'2019-05-27 10:41:32.365553'),('cbc0f4993af74802a20ba06eb96a4255','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-10 10:24:26.000420'),('cc945de611364f28a03db5cbf9961e43','admin','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 09:18:45.300901'),('d52286da7622410b9146db50dbbe9883','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-03 14:39:59.643688'),('dbad1871f6fc44718de67d1a2ab140af','000323','JWT','172.16.210.22','内网IP','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',1,'2019-04-01 14:22:26.308745'),('dc816960856e4090a7ba01365813fff3','admin','JWT','172.16.10.58','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-08 09:50:38.808818'),('de3d725802824fd48d6622a8d32b58fa','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-01 13:37:53.014483'),('de5b4dcf797845f5b88c4744c812934d','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',0,'2019-05-27 10:41:29.843792'),('e06d4d7b9eba46c08c6aac2957af3e85','000343','JWT','172.16.10.58','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-08 09:50:21.948483'),('e16d3fdd5c414fb683b499558121f2f9','admin','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 14:29:42.671633'),('e2334118bbc74bd2b1bfaa12f572b5f1','admin','JWT','172.16.210.103','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 17:29:13.019025'),('e243556d19c542d2924ead9e3d3dba19','000343','JWT','172.16.210.127','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-01 09:18:00.517821'),('e94efe5406a540d58c1614037a6c7f2f','admin','JWT','172.16.210.199','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-20 09:18:58.629534'),('ec86fc206bf24fc9a260436dda62abb0','zhoujinliang','JWT','172.16.100.20','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',0,'2019-06-06 11:02:36.446004'),('ee72653a145c45bfb19a3ab00168993e','admin','JWT','172.16.210.29','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-27 19:42:08.538177'),('f2c844ca8ed8485a9832af18f2d09210','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',1,'2019-06-03 08:52:48.834209'),('f33a9046720c414788eb6177d71ec528','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-20 16:17:04.529609'),('f454869c3c1f400ea1ff97d0b5f48ba4','000214','JWT','172.16.210.103','Unknown','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-19 18:46:36.876921'),('f53dfd80542d4149877992346af8a839','000151','JWT','172.16.210.158','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',1,'2019-04-04 16:01:38.990317'),('f75eabcd4da9489ab70d9d592ac0cc1e','admin','JWT','172.16.10.58','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',1,'2019-04-08 10:02:03.178157'),('f9a8bb2c467240f09f03ee4dc8e979bf','admin','JWT','172.16.10.237','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',0,'2019-05-27 10:41:59.212965'),('fcafbb64ea2440ec9054380f341b1dff','admin','JWT','172.16.210.103','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',1,'2019-06-20 17:06:43.570973'),('fd09387d058b4e0d8a0444aa2cc6f1c7','admin','JWT','172.16.100.51','内网IP','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',1,'2019-04-01 13:59:16.359215');
/*!40000 ALTER TABLE `users_loginlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_usergroup`
--

DROP TABLE IF EXISTS `users_usergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_usergroup` (
  `id` char(32) NOT NULL,
  `name` varchar(30) NOT NULL,
  `comment` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `creator_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `users_usergroup_creator_id_d4a560d1_fk_auth_user_id` (`creator_id`),
  CONSTRAINT `users_usergroup_creator_id_d4a560d1_fk_auth_user_id` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_usergroup`
--

LOCK TABLES `users_usergroup` WRITE;
/*!40000 ALTER TABLE `users_usergroup` DISABLE KEYS */;
INSERT INTO `users_usergroup` VALUES ('4183d7d341e24680a8ee399a6b3a9ec9','运维组','','2019-04-01 08:36:05.969752','8e1cde13e0794809aa1c472cfa0138f2');
/*!40000 ALTER TABLE `users_usergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workOrder_workorder`
--

DROP TABLE IF EXISTS `workOrder_workorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workOrder_workorder` (
  `id` char(32) NOT NULL,
  `title` varchar(128) NOT NULL,
  `type` int(11) NOT NULL,
  `contents` longtext NOT NULL,
  `comment` longtext DEFAULT NULL,
  `status` int(11) NOT NULL,
  `result` longtext DEFAULT NULL,
  `applied` datetime(6) NOT NULL,
  `completed` datetime(6) NOT NULL,
  `applicant_id` char(32) NOT NULL,
  `current_processor_id` char(32) DEFAULT NULL,
  `designator_id` char(32) NOT NULL,
  `finally_processor_id` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `workOrder_workorder_applicant_id_4983d324_fk_auth_user_id` (`applicant_id`),
  KEY `workOrder_workorder_current_processor_id_ec52edce_fk_auth_user` (`current_processor_id`),
  KEY `workOrder_workorder_designator_id_fd617629_fk_auth_user_id` (`designator_id`),
  KEY `workOrder_workorder_finally_processor_id_f9f8436e_fk_auth_user` (`finally_processor_id`),
  CONSTRAINT `workOrder_workorder_applicant_id_4983d324_fk_auth_user_id` FOREIGN KEY (`applicant_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `workOrder_workorder_current_processor_id_ec52edce_fk_auth_user` FOREIGN KEY (`current_processor_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `workOrder_workorder_designator_id_fd617629_fk_auth_user_id` FOREIGN KEY (`designator_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `workOrder_workorder_finally_processor_id_f9f8436e_fk_auth_user` FOREIGN KEY (`finally_processor_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workOrder_workorder`
--

LOCK TABLES `workOrder_workorder` WRITE;
/*!40000 ALTER TABLE `workOrder_workorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `workOrder_workorder` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-03  9:29:36
