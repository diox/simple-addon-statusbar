#!/usr/bin/env python
import os
import os.path
from cStringIO import StringIO
from PIL import Image
from zipfile import ZipFile


letters = {
    # Colors partly stolen from d3.js' d3.scale.category20().
    'A': '#1f77b4',
    'B': '#aec7e8',
    'C': '#ff7f0e',
    'D': '#ffbb78',
    'E': '#2ca02c',
    'F': '#98df8a',
    'G': '#d62728',
    'H': '#ff9896',
    'I': '#9467bd',
    'J': '#c5b0d5',
    'K': '#c49c94',
    'L': '#8c564b',
    'M': '#fcee07',
    'N': '#e377c2',
    'O': '#f7b6d2',
    'P': '#7f7f7f',
    'Q': '#c7c7c7',
    'R': '#bcbd22',
    'S': '#dbdb8d',
    'T': '#17becf',
    'U': '#9edae5',
    'V': '#abff00',
    'W': '#fffc00',
    'X': '#636363',
    'Y': '#00ecff',
    'Z': '#d9d9d9',
}

if not os.path.exists('dist'):
    os.mkdir('dist')

with open('manifest.json') as f:
    manifest_template = f.read()
with open('addon.js') as f:
    addon_template = f.read()
with Image.open('icon.png') as icon:
    for letter, color in letters.items():
        addon = addon_template.replace(
            '{color}', color).replace('{letter}', letter)
        manifest = manifest_template.replace('{letter}', letter)

        filename = 'dist/%s-in-status-bar.zip' % letter.lower()
        zip_file = ZipFile(filename, mode='w')
        zip_file.writestr('manifest.json', manifest)
        zip_file.writestr('addon.js', addon)

        rgb = [ord(c) for c in color[1:].decode('hex')]
        icon.putpalette([0, 0, 0, rgb[0], rgb[1], rgb[2]])
        icon_contents = StringIO()
        icon.save(icon_contents, format='PNG')
        icon_contents.seek(0)
        zip_file.writestr('icon.png', icon_contents.read())
        zip_file.close()
