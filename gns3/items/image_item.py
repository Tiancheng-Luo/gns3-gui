# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Graphical representation of an image on the QGraphicsScene.
"""

import xml.etree.ElementTree as ET

from ..qt import QtWidgets, QtCore, QtSvg
from ..qt.qimage_svg_renderer import QImageSvgRenderer
from .drawing_item import DrawingItem


class ImageItem(QtSvg.QGraphicsSvgItem, DrawingItem):

    """
    Class to insert an image on the scene.
    """


    def __init__(self, image_path=None, pos=None,  svg=None, **kws):

        self._image_path = image_path
        super().__init__(pos=pos, **kws)

        if self._image_path:
            renderer = QImageSvgRenderer(image_path)
            self.setSharedRenderer(renderer)

        # By default center the image
        if pos is None:
            x = self.pos().x() - (self.boundingRect().width() / 2)
            y = self.pos().y() - (self.boundingRect().height() / 2)
            self.setPos(x, y)

        if svg:
            svg = self.fromSvg(svg)

        if self._id is None:
            self.create()

    def fromSvg(self, svg):
        renderer = QImageSvgRenderer(svg)
        self.setSharedRenderer(renderer)

    def toSvg(self):
        """
        Return an SVG version of the shape
        """
        return self.renderer().svg()
