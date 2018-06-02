3DEngine
==============

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

3DEngine est un projet expérimental à but éducatif de création d'un moteur de rendu 3D logiciel en Python. Il a été réalisé dans le cadre de l'option ISN du Lycée Charlemagne (Paris).

![N|Solid](https://vard.pw/i/Om8hY.png)

## Requirement
- Python (3.6 ou ultérieur)
- Module Tkinter


## Usage

Les dépendances sont normalement livrées avec Python.
```
python app.py
```

## Configuration

Personnalisez votre définition et le nombre d'image par seconde ciblé dans le fichier [app.py](app.py).
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Engine import Engine

Engine(1280, 720, 60)
```
