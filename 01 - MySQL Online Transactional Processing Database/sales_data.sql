-- Crear la base de datos "sales"
CREATE DATABASE sales;

-- Usar la base de datos "sales"
USE sales;

-- Crear la tabla "productos"
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- Crear la tabla "clientes"
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Crear la tabla "ventas"
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    id_cliente INT,
    cantidad INT,
    fecha_venta DATE,
    FOREIGN KEY (id_producto) REFERENCES productos(id),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
