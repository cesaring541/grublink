-- phpMyAdmin SQL Dump
-- version 3.5.4
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 18-11-2013 a las 06:47:21
-- Versión del servidor: 5.5.29
-- Versión de PHP: 5.3.20

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `app`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'infelcom');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_a7792de1` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  `origen` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`, `origen`) VALUES
(1, 'administrador', 'Admin', 'Uptc', 'admin@uptc.edu.co', 'pbkdf2_sha256$10000$JjHPV5nNKFeg$BOfVMu4kN/3Ny+0zsVmYx5IckUnhZOQQuBFZmJcmQ3o=', 1, 1, 1, '2013-11-18 10:31:44', '2013-11-03 05:00:00', 0),
(2, 'admin_infelcom', 'Admin', 'Infelcom', 'admin_infelcom@uptc.edu.co', 'pbkdf2_sha256$10000$UwHsMITQVEm7$RRZfkP4sBD9cAl+AfBDE2aWGpLhD/i3gy5vJ1q4qyiU=', 0, 1, 1, '2013-11-18 10:33:57', '2013-11-03 05:00:00', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f0ee9890` (`group_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(2, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `content_type_id_refs_id_288599e6` (`content_type_id`),
  KEY `user_id_refs_id_c8665aa` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2013-11-18 09:21:21', 1, 2, '1', 'infelcom', 1, ''),
(2, '2013-11-18 09:21:30', 1, 2, '1', 'infelcom', 2, 'No ha cambiado ningún campo.'),
(3, '2013-11-18 09:26:42', 1, 3, '2', 'admin_infelcom', 2, 'Modificado/a password, email y groups.'),
(4, '2013-11-18 09:34:28', 1, 3, '2', 'admin_infelcom', 2, 'Modificado/a password y is_staff.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'site', 'sites', 'site');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0529ba9f370fb8430f7cf3c1b6068912', 'NjRiMWI2ZDZlYjY0ZGQ1ZjBkNGU3OThkNWE3ZGU1ZGIwODlmZGFiZjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2013-12-02 10:33:57');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'foo', 'Foo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_aspect`
--

CREATE TABLE IF NOT EXISTS `infelcom_aspect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `icon_name` varchar(50) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `index` int(11) NOT NULL,
  `lang` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_content`
--

CREATE TABLE IF NOT EXISTS `infelcom_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section_id_id` int(11) NOT NULL,
  `text` mediumtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_media`
--

CREATE TABLE IF NOT EXISTS `infelcom_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `media_url` mediumtext NOT NULL,
  `media_type` mediumtext NOT NULL,
  `content_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_member`
--

CREATE TABLE IF NOT EXISTS `infelcom_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `charge` varchar(50) NOT NULL,
  `profile_img` varchar(100) NOT NULL,
  `about` varchar(1000) NOT NULL,
  `cv_lac` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Volcado de datos para la tabla `infelcom_member`
--

INSERT INTO `infelcom_member` (`id`, `name`, `last_name`, `charge`, `profile_img`, `about`, `cv_lac`) VALUES
(6, 'gdfgdsfg', 'sdfgdsgdsfg', 'Director', 'profiles_img/staff4_1.jpg', 'vzcxvzdsfegrbvdsgsrthsdgdsghdsfgsdfadsggadsfd', 'No se ha añadidio CvLACasdfasdfasdfasdfasdf'),
(7, 'jojo', 'kaka', 'Semillero', 'profiles_img/staff2_1.jpg', 'dfgfjghnxgertyreywtyer', 'CvLAC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_product`
--

CREATE TABLE IF NOT EXISTS `infelcom_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `aditional_info` varchar(1000) NOT NULL,
  `url` varchar(200) NOT NULL,
  `product_img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Volcado de datos para la tabla `infelcom_product`
--

INSERT INTO `infelcom_product` (`id`, `title`, `description`, `aditional_info`, `url`, `product_img`) VALUES
(6, 'HTTAP', 'App en HTML5, muy buenassssssssssssss', '', 'htaAPP', 'products_img/html5_1.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_product_members`
--

CREATE TABLE IF NOT EXISTS `infelcom_product_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`,`member_id`),
  KEY `infelcom_product_members_bb420c12` (`product_id`),
  KEY `infelcom_product_members_56e38b98` (`member_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=36 ;

--
-- Volcado de datos para la tabla `infelcom_product_members`
--

INSERT INTO `infelcom_product_members` (`id`, `product_id`, `member_id`) VALUES
(34, 6, 6),
(35, 6, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_profilelinks`
--

CREATE TABLE IF NOT EXISTS `infelcom_profilelinks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL,
  `title` varchar(30) NOT NULL,
  `url` varchar(100) NOT NULL,
  `icon` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `infelcom_profilelinks_56e38b98` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_project`
--

CREATE TABLE IF NOT EXISTS `infelcom_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `status` varchar(50) NOT NULL,
  `progress` int(11) NOT NULL,
  `aditional_info` varchar(1000) NOT NULL,
  `url` varchar(200) NOT NULL,
  `project_img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Volcado de datos para la tabla `infelcom_project`
--

INSERT INTO `infelcom_project` (`id`, `title`, `description`, `status`, `progress`, `aditional_info`, `url`, `project_img`) VALUES
(1, 'Proyecto de ejemplo A', 'ejemplo de proyecto', 'Activo', 10, 'nada en especial', 'gsdfgsgsdfgsdgsdfgsdgsdfgsdfgdsf', 'projects_img/twitter.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_project_members`
--

CREATE TABLE IF NOT EXISTS `infelcom_project_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_id` (`project_id`,`member_id`),
  KEY `infelcom_project_members_b6620684` (`project_id`),
  KEY `infelcom_project_members_56e38b98` (`member_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Volcado de datos para la tabla `infelcom_project_members`
--

INSERT INTO `infelcom_project_members` (`id`, `project_id`, `member_id`) VALUES
(17, 1, 6),
(18, 1, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_section`
--

CREATE TABLE IF NOT EXISTS `infelcom_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section_name` varchar(100) NOT NULL,
  `section_title` varchar(100) NOT NULL,
  `section_lang` varchar(2) NOT NULL,
  `section_author` varchar(100) NOT NULL,
  `last_modify` date NOT NULL,
  `section_index` int(11) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `section_name` (`section_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Volcado de datos para la tabla `infelcom_section`
--

INSERT INTO `infelcom_section` (`id`, `section_name`, `section_title`, `section_lang`, `section_author`, `last_modify`, `section_index`, `locked`) VALUES
(1, 'inicio', 'Inicio', 'es', 'admin', '2013-11-17', 1, 1),
(2, 'grupo', 'Grupo', 'es', 'admin', '2013-11-17', 2, 1),
(3, 'miembros', 'Miembros', 'es', 'admin', '2013-11-17', 3, 1),
(4, 'proyectos', 'Proyectos', 'es', 'admin', '2013-11-17', 4, 1),
(5, 'productos', 'Productos', 'es', 'admin', '2013-11-17', 5, 1),
(6, 'contacto', 'Contacto', 'es', 'admin', '2013-11-17', 6, 1),
(9, 'home', 'Home', 'en', 'admin', '2013-11-17', 1, 0),
(10, 'group', 'Group', 'en', 'admin', '2013-11-17', 2, 0),
(11, 'projects', 'Projects', 'en', 'admin', '2013-11-17', 4, 0),
(12, 'products', 'Products', 'en', 'admin', '2013-11-17', 5, 0),
(13, 'members', 'Members', 'en', 'admin', '2013-11-17', 3, 0),
(14, 'contact', 'Contact', 'en', 'admin', '2013-11-17', 6, 0),
(16, 'test', 'Test', 'es', 'admin_infelcom', '2013-11-18', 5, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infelcom_slide`
--

CREATE TABLE IF NOT EXISTS `infelcom_slide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slide_name` varchar(60) NOT NULL,
  `slide_title` varchar(150) NOT NULL,
  `slide_abstract` varchar(500) NOT NULL,
  `slide_lang` varchar(2) NOT NULL,
  `slide_author` varchar(100) NOT NULL,
  `slide_link` varchar(100) NOT NULL,
  `slide_bg` varchar(100) NOT NULL,
  `slide_icon` varchar(100) NOT NULL,
  `slide_index` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slide_name` (`slide_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `infelcom_slide`
--

INSERT INTO `infelcom_slide` (`id`, `slide_name`, `slide_title`, `slide_abstract`, `slide_lang`, `slide_author`, `slide_link`, `slide_bg`, `slide_icon`, `slide_index`) VALUES
(1, 's1', 'S222', 'dsfasdfasd', 'es', 'admin', 'ffdasdfa', 'slides_bg/slide-1_4.jpg', 'slides_icon/bootstrap_4.png', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `main_aspect`
--

CREATE TABLE IF NOT EXISTS `main_aspect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `icon_name` varchar(50) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `index` int(11) NOT NULL,
  `lang` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `main_content`
--

CREATE TABLE IF NOT EXISTS `main_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section_id_id` int(11) NOT NULL,
  `text` mediumtext NOT NULL,
  `lang` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Volcado de datos para la tabla `main_content`
--

INSERT INTO `main_content` (`id`, `section_id_id`, `text`, `lang`) VALUES
(9, 22, 'No se ha definido contenido para esta jajajajjajaja', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `main_media`
--

CREATE TABLE IF NOT EXISTS `main_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `media_url` mediumtext NOT NULL,
  `media_type` mediumtext NOT NULL,
  `content_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `main_section`
--

CREATE TABLE IF NOT EXISTS `main_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section_name` varchar(100) NOT NULL,
  `section_title` varchar(100) NOT NULL,
  `section_lang` varchar(2) NOT NULL,
  `section_author` varchar(100) NOT NULL,
  `last_modify` date NOT NULL,
  `section_index` int(11) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `section_name` (`section_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Volcado de datos para la tabla `main_section`
--

INSERT INTO `main_section` (`id`, `section_name`, `section_title`, `section_lang`, `section_author`, `last_modify`, `section_index`, `locked`) VALUES
(1, 'inicio', 'Inicio', 'es', 'admin', '2013-11-16', 1, 1),
(2, 'escuela', 'La escuela', 'es', 'admin', '2013-11-16', 2, 1),
(3, 'investigacion', 'Investigación', 'es', 'admin', '2013-11-16', 3, 1),
(4, 'contacto', 'Contacto', 'es', 'admin', '2013-11-16', 4, 1),
(5, 'home', 'Home', 'en', 'admin', '2013-11-17', 1, 1),
(6, 'school', 'School', 'en', 'admin', '2013-11-17', 2, 1),
(7, 'research', 'Research', 'en', 'admin', '2013-11-17', 3, 1),
(8, 'contact', 'Contact', 'en', 'admin', '2013-11-17', 4, 1),
(20, 'colosus', 'Colossus', 'en', 'admin', '2013-11-17', 5, 0),
(22, 'eventos', 'Eventos', 'es', 'admin', '2013-11-17', 3, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `main_slide`
--

CREATE TABLE IF NOT EXISTS `main_slide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slide_name` varchar(60) NOT NULL,
  `slide_title` varchar(150) NOT NULL,
  `slide_abstract` varchar(500) NOT NULL,
  `slide_lang` varchar(2) NOT NULL,
  `slide_author` varchar(100) NOT NULL,
  `slide_link` varchar(100) NOT NULL,
  `slide_bg` varchar(100) NOT NULL,
  `slide_icon` varchar(100) NOT NULL,
  `slide_index` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slide_name` (`slide_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `infelcom_product_members`
--
ALTER TABLE `infelcom_product_members`
  ADD CONSTRAINT `product_id_refs_id_1ca87ce1` FOREIGN KEY (`product_id`) REFERENCES `infelcom_product` (`id`),
  ADD CONSTRAINT `member_id_refs_id_fc0267ed` FOREIGN KEY (`member_id`) REFERENCES `infelcom_member` (`id`);

--
-- Filtros para la tabla `infelcom_profilelinks`
--
ALTER TABLE `infelcom_profilelinks`
  ADD CONSTRAINT `member_id_refs_id_4f75e9a7` FOREIGN KEY (`member_id`) REFERENCES `infelcom_member` (`id`);

--
-- Filtros para la tabla `infelcom_project_members`
--
ALTER TABLE `infelcom_project_members`
  ADD CONSTRAINT `project_id_refs_id_e4c8c841` FOREIGN KEY (`project_id`) REFERENCES `infelcom_project` (`id`),
  ADD CONSTRAINT `member_id_refs_id_d550998b` FOREIGN KEY (`member_id`) REFERENCES `infelcom_member` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
