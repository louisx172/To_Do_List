-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-01-2023 a las 19:45:22
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `to_do_list`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ids`
--

CREATE TABLE `ids` (
  `ID_Fila` bigint(20) DEFAULT NULL,
  `ID_Tabla` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tareas`
--

CREATE TABLE `registro_tareas` (
  `fecha` date NOT NULL,
  `tareas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registro_tareas`
--

INSERT INTO `registro_tareas` (`fecha`, `tareas`) VALUES
('2023-01-15', 3),
('2023-01-16', 9),
('2023-01-17', 6),
('2023-01-18', 7),
('2023-01-19', 11),
('2023-01-20', 10),
('2023-01-21', 2),
('2023-01-22', 5),
('2023-01-23', 7),
('2023-01-24', 4),
('2023-01-25', 7),
('2023-01-26', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tareas`
--

CREATE TABLE `tareas` (
  `ID` bigint(20) NOT NULL,
  `Titulo` varchar(50) DEFAULT NULL,
  `Descripcion` varchar(200) DEFAULT NULL,
  `Prioridad` varchar(20) DEFAULT NULL,
  `FechaLimite` varchar(30) DEFAULT NULL,
  `TiempoEstimado` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tareas`
--

INSERT INTO `tareas` (`ID`, `Titulo`, `Descripcion`, `Prioridad`, `FechaLimite`, `TiempoEstimado`) VALUES
(16, 'REDES I\n', 'Hacer los ejercicios de subneteo y estudiar para el examen\n', 'Prioridad maxima', '1 hora', '6/7/2025'),
(17, 'Ingles\n', 'Estudiar para el examen - 25/04/2023\n', 'Prioridad media', '30 minutos', '24/4/2023'),
(18, 'Desarrollo Humano\n', 'Terminar la presentación\n', 'Prioridad maxima', '30 minutos', '4/4/2024');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `registro_tareas`
--
ALTER TABLE `registro_tareas`
  ADD PRIMARY KEY (`fecha`);

--
-- Indices de la tabla `tareas`
--
ALTER TABLE `tareas`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tareas`
--
ALTER TABLE `tareas`
  MODIFY `ID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
