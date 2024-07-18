- Name: Renderización con Iluminación Aleatoria
- Descripción del script: Este proyecto rota un objeto y cambia la iluminación aleatoriamente para cada render.
- Versión de Blender: 4.2.0 (LTS)
- Tipo: Utility
- Job type: Array
- Envs: None
- Project structure: Custom Folder Structure
[]: #
```plaintext
render_random_light/
├── assets/
│   ├── hdri/
│   └── textures/
├── scripts/
│   ├── __init__.py
│   ├── random_light.py
│   └── render.py
├── README.md
└── main.py
```
- Nota: El script `random_light.py` se encarga de cambiar la iluminación aleatoriamente y el script `render.py` se encarga de renderizar el objeto.
- Entrypoint: `main.py`
- References: [Renderización con Iluminación Aleatoria]()
- Screenshot: ![Renderización con Iluminación Aleatoria](https://i.imgur.com/1Q2J9Q4.png)

