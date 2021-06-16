Position, Orientation & Size
============================

.. |nbsp| unicode:: 0xA0 
   :trim:

.. note:: We continue with the project from the last tutorial. You can download it here if you need the current state: :download:`tutorial_virtual_scene.aRTist <files/tutorial_virtual_scene.aRTist>` (4.6 MB)


Parameter Panel
---------------

If we take a look at the full scene again, we see that the source seems to be a little bit close to the detector.

.. note:: Deselect the rotor by clicking on the unoccupied white area in the *Assembly List* or on the brackground colour in the *Virtual Scene*. Now click on |icon-zoom-to-selection| :guilabel:`Zoom to Selection` to see the full scene again.

.. |icon-zoom-to-selection| image:: pictures/icons/32x32/zoom-select.png

We already know that the detector is at the origin of the coordinate system: its centre lies at the point (0, |nbsp| 0, |nbsp| 0) in space. You can check this by selecting the *Detector* item from the *Assembly List* and inspecting its properties in the *Transformation* section of the *Parameter Panel* (:numref:`detectorTransformProperties`).

.. _detectorTransformProperties:
.. figure:: pictures/tutorial-positioning-detector-properties.png
    :scale: 80%

    The lower three rows of the *Parameter Panel* show the position, orientation and size of the selected *Detector*.

The panel also tells us that the detector has a size of 100 |nbsp| mm in *x* direction and 100 |nbsp| mm in *y* direction. It has no thickness (0 |nbsp| mm in *z* direction). The size always refers to an object's **bounding box**, i.e. its local coordinate system. In the case of our specific detector, the axes of its local coordinate system and the world coordinate system point in the same direction. In general, this is not the case for any object.

We can also get the information about the position of the source.

.. note:: Select the *Source* from the *Assembly List* and check its *z* position.

The source is located 100 |nbsp| mm away from the detector on the *z* axis.


Positioning
-----------

In the field of computed tomography, two very important parameters of a system's geometry are the **source-detector distance (SDD)** and the **source-object distance (SOD)**. We will now change our scene to get the  geometry shown in :numref:`goalSetup`, with an SDD of 500 |nbsp| mm and an SOD of 300 |nbsp| mm.

.. _goalSetup:
.. figure:: pictures/tutorial-positioning-goal-setup.png
    :width: 100%

    Illustration of the geometry that we want to set up.

Setting up the :abbr:`SDD (source-detector distance)` is the easier part. We have to place the source at the position *z* |nbsp| = |nbsp| 500 |nbsp| mm, because the detector is located at the origin of the coordinate system and we want to keep the convention to place the source in positive *z* direction.

.. note:: Select the *Source* from the *Assembly List*. Set :code:`500` for the *z* coordinate of the **Position** (:numref:`sourceTransformProperties`) and press :kbd:`Enter`.

The number in the input field will be displayed in blue until it is applied to the scene.

.. _sourceTransformProperties:
.. figure:: pictures/tutorial-positioning-source-properties.png
    :scale: 80%

    Placing the source at 500 |nbsp| mm. The number remains blue until we press :kbd:`Enter` to apply the change.

The *Rotor* is still at the origin of the coordinate system, basically "inside" the detector. To move it to the correct SOD of 300 |nbsp| mm, we have to keep in mind that we need to set its position on the *z* axis, which starts at the detector. This means that we have to calculate the *object-source distance (ODD)* first:

**ODD = SDD – SOD = 200 mm.**

We can now place the *Rotor* 200 |nbsp| mm away from the detector to get the required SOD of 300 |nbsp| mm.

.. note:: Select the *Rotor* from the *Assembly List* and set its *z* position to :code:`200`. Press :kbd:`Enter`.

When you take a look at the full view of your scene, it should now look like in :numref:`SODandSDDsetup`.

.. _SODandSDDsetup:
.. figure:: pictures/tutorial-positioning-SOD-SDD.png
    :width: 100%

    We have changed the geometry to an SOD of 300 |nbsp| mm and an SDD of 500 |nbsp| mm.

To set up horizontal and vertical shifts, you can change the *x* position and *y* position of any object in the same way.