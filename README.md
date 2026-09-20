# 🚀 CODE RIDER - Fleet Management System v2.0 🏎️⚡

[![Render Status](https://img.shields.io/badge/Render-Live%20Demo-00f0ff?style=for-the-badge&logo=render&logoColor=white)](https://sql-rider.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Plataforma web interactiva para la gestión integral de flotas de transporte, empresas, conductores, licencias de conducción y rutas. Diseñada con una arquitectura robusta en **Django**, persistencia de datos relacional en **SQL** y un panel de control con interfaz **Cyberpunk / Glassmorphism 3D**.

🌐 **Demo en Vivo:** [https://sql-rider.onrender.com/](https://sql-rider.onrender.com/)

---

## 👨‍💻 Desarrollador

* **Autor:** Angel Esteban Rivera Camayo ⚡
* **Rol:** Full Stack Developer & Arquitecto del Sistema
* **Ubicación:** Cauca, Colombia 🇨🇴

---

## 🛠️ Tecnologías y Herramientas

* **Backend:** Python 3.11+, Django 6, WSGI/Gunicorn.
* **Frontend:** HTML5, CSS3 Custom (Glassmorphism + Neón), JavaScript Nativo, FontAwesome Icons.
* **Base de Datos:** SQLite / PostgreSQL (Relacional SQL).
* **Gestión de Estáticos & Despliegue:** WhiteNoise, Git, GitHub Actions, Render Cloud.

---

## 📑 Modelo de Datos y Relaciones SQL

El sistema implementa las cuatro relaciones fundamentales del modelo relacional:

1. **🏢 Empresas (Base):** Entidad principal que agrupa la infraestructura operacional.
2. **👨‍✈️ Conductores (Relación 1 a N):** Una empresa puede tener múltiples conductores asociados.
3. **🪪 Licencias (Relación 1 a 1):** Cada conductor posee una única licencia de conducción oficial categorizada.
4. **🗺️ Rutas (Relación N a M):** Múltiples conductores pueden cubrir distintas rutas intermunicipales y viceversa.

