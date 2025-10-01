# Data Analysis Projects

Este repositorio contiene diversos proyectos de análisis de datos, cada uno organizado en su propio subdirectorio. Los proyectos están diseñados para ilustrar técnicas y metodologías aplicadas a conjuntos de datos reales, utilizando herramientas modernas de Python.

## 📂 Estructura del Repositorio

```
data-analysis/
├── texas-holdem/
│   ├── main.py
│   └── README.md
├── clasification-model/
│   ├── model.py
│   └── README.md
├── docs/
│   └── ...
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## 🚀 Comenzando

### Requisitos Previos

Este proyecto utiliza [uv](https://astral.sh/uv/) para la gestión de entornos y dependencias en Python. Para instalarlo, ejecuta:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/MMaxx0/data-analysis.git
cd data-analysis
```

2. Instala las dependencias del proyecto:

```bash
uv install
```

### Uso

Para ejecutar un proyecto o script, navega al directorio correspondiente y ejecuta el script principal. Por ejemplo:

```bash
cd texas-holdem
uv run main.py
```

### Gestión de Dependencias

- Para agregar un nuevo paquete:

```bash
uv add <nombre-del-paquete>
```

- Para eliminar un paquete:

```bash
uv remove <nombre-del-paquete>
```

## 📁 Descripción de los Subproyectos

### texas-holdem/

Análisis de datos relacionados con el juego de póker Texas Hold'em. Este proyecto incluye simulaciones y análisis estadísticos para comprender mejor las probabilidades y estrategias del juego.

### clasification-model/

Implementación de un modelo de clasificación utilizando técnicas de aprendizaje automático. El proyecto incluye la preparación de datos, entrenamiento del modelo y evaluación del rendimiento.

## 📄 Documentación

La documentación adicional se encuentra en el directorio `docs/`. Puedes acceder a ella para obtener más detalles sobre cada proyecto, metodologías utilizadas y resultados obtenid