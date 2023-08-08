.. include:: _templates/icons.rst

.. _Tools-detectorProperties:

Detector Properties
===================

The **DetectorViewer** contains the plots of the properties of the current detector (:numref:`DetectorViewer`):

* :class:`Characteristic` is used for grey values, film densities or air dose [mGy] as a function of energy density J/m².
* :class:`Noise` displays the :abbr:`SNR (Signal-to-Noise Ratio)` as a function of energy density.
* :class:`Sensitivity` displays the deposited energy as a function of energy.
* :class:`Deposit` displays the deposited energy per interaction.
* :class:`Attenuation` displays the interaction probability as function of energy.

.. note::
    
    The type of graph(s) available via the drop-down menue is dependent on the current detector.

On the left-hand side of the **DetectorViewer** (:numref:`DetectorViewer`) details of the current detector are shown. On the right hand side the choosen detctor properties are displayd as *Graph* or *Text*. 

In the row below the *Graph* tab it can be choosen how to show the graph, e.g., logarithmic or linear scale for the X and/or Y axis and if the grid should be shown or not.  


.. _DetectorViewer:
.. figure:: pictures/tools-detector_viewer.jpg
    :alt: DetectorViewer
    :width: 90.3%

    DetectorViewer.