.. include:: _templates/icons.rst

.. _AttenuationDataSection:

Attenuation Data
================

The **AttenuationViewer** shows a plot of the attenuation coefficient as a function of the radiation's energy (:numref:`tools-attenuation1`) in the tab *Graph*. It consists of different graphs:

* photo effect (blue graph)
* incoherent/Compton scattering (red graph)
* coherent/Rayleigh scattering (green graph)
* pair production (violet graph)
* total, sum of the above attenuation coefficients (black graph)

In the tab *Text* the corresponding data are shown in text format.

|16x16_document-save-as|: The displayed data can be saved in tabulated or graphical form. The following formats are available: TXT, EPS, and PDF.

In the row above the *Graph* or *Text* tab the actual chosen paramaters are shown:

* Material: With the drop-down menue any material can be chosen from the list of available materials. If the material is changed, the attenuation coefficients will be automatically recalculated.
* Minimum energy [keV] and Maximum enrergy [keV] for which energy range the attenuation coefficients should be calculated.
* Energy resolution [kev] gives the energy steps for which the attenuation coefficients should be calculated.
* Log. spacing is recomended to be switched on.

In the row below the *Graph* tab it can be choosen how to show the graph, e.g., logarithmic or linear scale for the X and/or Y axis and if the grid should be shown or not.

.. _tools-attenuation1:
.. figure:: pictures/tools-attenuation1.png
    :alt: AttenuationViewer
    :width: 70.3%

    AttenuationViewer.