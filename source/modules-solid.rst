.. include:: _templates/icons.rst

.. _SolidSection:

|32x32_icon-solid| Solid
========================

The |16x16_icon-solid| **Solid** module allows you to create simple parts of different sizes to construct your assembly as desired (:numref:`modules-solid1`). 

.. _modules-solid1:
.. figure:: pictures/modules-solid1.png
    :alt: Solid
    :width: 60%
    
    Solid.

Under **Geometry** you can select the **Type**. The following types are available for selection:

* :class:`cuboid`
* :class:`ellipsoid`
* :class:`cylinder`
* :class:`tube`
* :class:`cone`
* :class:`text`
* :class:`wedge`
* :class:`step wedge`


Select the part of your choice from the drop-down menu and set the **Dimensions** in mm and the **Phi steps** and **Theta steps** if applicable. You may predetermine equal values for 
**X [mm]**, **Y [mm]** and **Z [mm]** by checking the box at the bottom of the module. If you choose **Text** the input field at the top of the module is enabled. When finished press the :guilabel:`Create` button.

Additionally, when selecting **wedge**, **step wedge**  or **tube**, it is possible to set the **W** parameter. Then for example the diameter of a tube or the foundation size of a wedge can be set. 
If you choose **cylinder** and **cone**, you can turn **volume correction** on and off in **Options**. If you select an **ellipsoid**, you can additionally decide whether to use a **regular ellipsoid grid**.

In case the **volume correction** under **Options** is deactivated, the object to be created always approaches the volume of the ideal object determined by the set parameters x y z and becomes smaller. 
The reason is that the faceting of the object via triangles basically takes place within an object. 
If the **Volume correction** is activated, the exact volume of the ideal object is forced, but a larger created object is accepted in order to obtain the correct volume.

The default material for new parts is :class:`Fe`. 

.. hint::
    A list with available materials can be accessed from the :guilabel:`Menu Bar` → **Geometry**  → **Set Material** or 
    the Assembly List of the :ref:`Parameter Panel <ParameterPanel>`

.. tip::

    After the object has been created, it can also be saved individually. To do this, select your object in the :ref:`Parameter Panel <ParameterPanel>` so that it is highlighted in blue. Then go via :guilabel:`File` to |16x16_document-save-as| ***Save as***... . A new window will open. 
    At the bottom you can now choose under **File type** :class:`selected parts`. This way you can also create :code:`.stl` files with artist for instance.