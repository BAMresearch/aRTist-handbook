.. include:: _templates/icons.rst

Setup Panel
-----------
.. _SetupPanelSection:

The :guilabel:`Setup` panel allows you to arrange the geometry of the X-ray setup. The assembly list contains an entry for each geometric object, starting with the source and the detector, followed by the parts (components) to be irradiated. The material assignment is also controlled here.

.. The default settings of the Setup for the environment is air, for the Transformation are |16x16_world-coordinate-system| world coordinate system and |16x16_transformation-move| translate mode. This settings can be seen in :numref:`guiSetupDefault`.

.. _guiSetupDefault:
.. figure:: pictures/gui-parameterP-SetupDefault.png
    :alt: The parameter panel Setup.
    :width: 41.3%

    The parameter panel Setup.

.. _SetupEnvironmentSubSection:

Environment
^^^^^^^^^^^

Select the environmental material of your choice from the Material drop-down list. 
This material applies everywhere in the space of the scene outside of any parts. 

.. note::

   You can choose between any preset or self-defined material. :class:`air` is the default setting. 
   All available materials are provided by the :ref:`Materials Editor <Tools-materials>`, which allows adding new materials.

.. _SetupAssemblyListSubSection:

Assembly list
^^^^^^^^^^^^^

The assembly list contains an entry for each geometric object. There is always an entry for the source and the detector. Additional entries are created for each loaded STL file representing the part (components) to be irradiated. To manipulate, you can select one ore more item(s) from the assembly either from the list or by clicking on them in the virtual scene. Selected parts will be highlighted blue in the list and taged with yellow corners of their bounding box in the virtual scene. 

.. _guiEnvironmentAssembly:
.. figure:: pictures/gui-parameterP-EnvironmentAssembly.png
    :alt: Environment, Assembly List
    :width: 41.3%

    Parameter groups Environment and Assembly List.

The assembly list shows five columns (:numref:`guiEnvironmentAssembly`):

* **ID** represents an unique identifier for an entry.
* |16x16_object-visible-on| activates/deactivates an entry by a click on the eye symbol. Alternatively, you may use the corresponding commands from the :ref:`Geometry menu <GeometryMenuSubsection>`.
* **Name** shows the name of the part. Click on the name to edit it. It is not possible to change the names of detector and source.
* **Material** shows the material of a part. Click on it to assign a different material from the drop-down list of materials. 
* **Display** shows the color and the opacity (value) of the item. Double-click to edit it.

.. _SetupTransformationSubSection:

Transformation
^^^^^^^^^^^^^^

Under Transformation, you will find options for geometric manipulation of the parts in the assembly list. (:numref:`guiSetupTransformation`). Proceed in the following way:

 .. |gui-parameterP-SetupSelectAxis| image:: pictures/gui-parameterP-SetupSelectAxis.png
 .. |gui-parameterP-SetupSlideTransform| image:: pictures/gui-parameterP-SetupSlideTransform.png

Basic manipulation of a part:

1. Select one or more parts.

2. Choose between the |16x16_world-coordinate-system| **world coordinate system** or the |16x16_object-coordinate-system| **local coordinate system**.

3.  Choose the type of transformation: |16x16_transformation-rotate| **rotate**, |16x16_transformation-move| **translate** or |16x16_transformation-scale| **scale**.

4.  At |gui-parameterP-SetupSelectAxis| you can select the axis of transformation with a click on one of the green arrows. Or define the direction vector by using the X, Y and Z entries of the **Axis** row directly.

5.  |16x16_set-coordinate-arrow-down| |16x16_set-coordinate-arrow-up| set the step size with the green arrows or type in a **Value**. The unit matches the type of transformation: degree (for |16x16_transformation-rotate| rotation), mm (for |16x16_transformation-move| translation), or 10% magnification (for |16x16_transformation-scale| scaleing).

6. Apply the transformation With the slide control |gui-parameterP-SetupSlideTransform| or do it directly in the scene by dragging the part with the left mouse button.  

You can monitor the movement/modification of **Reference position**, **Position**, **Orientation**, and **Size** over the display fields in the bottom of the **Transformation** page or put in values by yourself as an alternative to the previously explained approach.

.. _guiSetupTransformation:
.. figure:: pictures/gui-parameterPsetup_transformation.jpg
    :alt: Parameter group Transformation.
    :width: 41.3%

    Parameter group Transformation for the geometric modification of parts.
