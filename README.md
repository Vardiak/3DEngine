3DEngine
==============

![N|Solid](https://vard.pw/i/Om8hY.png)

## ℹ️ À propos du projet

3DEngine est un projet expérimental à but éducatif de création d'un moteur de rendu 3D logiciel en Python. Il a été réalisé dans le cadre de l'option ISN du Lycée Charlemagne (Paris).

## Requirement
- Python (3.6 ou ultérieur)
- Module Tkinter


## Usage

Les dépendances sont normalement livrées avec Python.
```
python app.py
```

## Configuration

Personnalisez la définiton et le nombre d'image par seconde ciblé dans le fichier [app.py](app.py).
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Engine import Engine

Engine(1280, 720, 60)
```

## License
 
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.