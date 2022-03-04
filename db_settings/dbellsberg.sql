-- Accedemos a la cli de PostgreSQL sin cambiar de cuenta
-- sudo -iu postgres psql
-- Si existe, eliminamos la base de datos
DROP DATABASE ellsberg_db;

-- Creamos la base de datos del proyecto
CREATE DATABASE ellsberg_db;

-- Creamos un usuario para la bd del proyecto
---CREATE USER ellsberg_user WITH PASSWORD 'ellsberg_user';

-- Damos privilegios de administrador al usuario
GRANT ALL PRIVILEGES ON DATABASE ellsberg_db TO ellsberg_user;

-- Nos conectamos a la db
-- \c ellsberg_db ;
