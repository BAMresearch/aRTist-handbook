.. include:: _templates/icons.rst

.. _Tools-materials:

|32x32_edit-materials| Materials
================================

The |22x22_edit-materials| **Materials** editor lists all materials that are available within |artist| including density and composition (:numref:`tools-materialseditor1`). You may dock the editor with |16x16_window-undock| in the docking area.
It provides the following possibilities to edit materials:

* Edit selected material. Click on an entry you wish to edit, for example density or composition. Press :kbd:`enter` when finished.
* |16x16_list-add| is used to add a new material definition.
* |16x16_list-remove| Delete is used to erase currently selected material.
* |16x16_choose-color| Edit display is used to revise material display parameters for currently selected material.
* |16x16_show-attenuation| **Attenuation** plots the attenuation data for the currently selected material (for details see :ref:`Attenuation Data <AttenuationDataSection>`)
* :guilabel:`Apply` is used to update material database with table of content.
* :guilabel:`Refresh` is used to reload table contents from material database.

.. note::
    
    Densities are given in g/cm³. The composition can be given bei the chemical formula, e.g., H2O plus density for water, or by the chemical elements and the mass ratio between the elements, e.g., N2 0.756 O2 0.231 Ar 0.013 plus density for air. The sum of the mass ratios of all chemical elements should be one. If not, |artist| will automatically normalize the sum of the mass rations to one.

.. _tools-materialseditor1:
.. figure:: pictures/tools-materialseditor1.jpg
    :alt: Materials editor
    :width: 70.3%

    Materials editor.