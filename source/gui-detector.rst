.. include:: _templates/icons.rst

Detector Panel
==============

The :guilabel:`Detector` tab of the Parameter Panel is designed for the settings of the detector properties like geometry and type (:numref:`guiparameterPsetupdetector`).

.. _guiparameterPsetupdetector:
.. figure:: pictures/gui-parameterP-setup_detector.jpg
    :alt: Parameter panel: Detector
    :width: 41.3%

    Parameter panel: Detector.

.. _GeometrySubsection:

Geometry
--------

 .. |modules-ImagViewerScale-closedSymbol| image:: pictures/modules-ImagViewerScale-closedSymbol.png
 .. |modules-ImageViewer-openSymbole| image:: pictures/modules-ImageViewer-openSymbole.png

.. _guiparameterPdetectorGeometry:
.. figure:: pictures/gui-parameterP-detector_geometry.jpg
    :alt: Geometry settings
    :width: 41.3%

    Geometry settings.

In this part of the :guilabel:`Detector` tab, you can adjust the **Geometry** of the detector (:numref:`guiparameterPdetectorGeometry`). 
Choose which quantity you want to update automatically (**Size [mm]**, **Pixel**, and **Resolution [mm]**) and set the values for the other two quantaties. In (:numref:`guiparameterPdetectorGeometry`) the **Size [mm]** is choosed to be automatically updated, **Pixel** and **Resolution [mm]** has to be set by the user.
Next to the input fields is a button |modules-ImagViewerScale-closedSymbol|. When you click this button, the symbol changes, once into an open chain |modules-ImageViewer-openSymbole| and once into a closed chain |modules-ImagViewerScale-closedSymbol|. The closed chain symbol |modules-ImagViewerScale-closedSymbol| gives a square pixel area, i.e., the resolution in X and Y direction is equal. The open chain symbol |modules-ImageViewer-openSymbole| allows a rectangular pixel area, as X and Y can have different values.

**Multisampling** is used for anti-aliasing. 
The default setting is source dependent, which means, that the source's sampling pattern will also be used for the image resulting in reduced computation time. 
The other available patterns of the list are: :class:`5`, :class:`10`, :class:`20`, :class:`30` and :class:`1×1`, :class:`2×2`, :class:`3×3`, :class:`4×4`, :class:`5×5`. 
Thereby you can also enter your own values. A single integer denotes the number of samples randomly distributed and an entry of the form NxM denotes a regular grid.

**Curvature** is used to have a curved detector around its reference point along the selected axis (the reference point of the detector should not be the same as its position, but e.g. the central axis of a cylindrical part). 
This can be used to wrap teh detector onto curved parts like a pipe. Thereby you can choose between a curvature in :class:`X` or :class:`Y` direction of the detector.
In curvature mode, the projections are calculated line by line, which taces much more time.

.. _CharacteristicSubsection:

Characteristic
--------------
.. _DetectorPanelSection:

2.6	Detector Panel (incl. menu description)
2.6.1	Parameter override
2.6.2	Flat-field correction
