Position, Orientation & Size
============================

.. |nbsp| unicode:: 0xA0 
   :trim:

.. note:: We continue with the project from the last tutorial. You can download it here if you need the current state: :download:`tutorial_virtual_scene.aRTist <files/tutorial_virtual_scene.aRTist>` (4.6 MB)


Local and World Coordinate Systems
----------------------------------

In the previous tutorial, we have already seen that *aRT*\ ist puts the detector by default at the origin of the coordinate system and the source at some point in positive *z* direction. This main frame of reference is called the **world coordinate system**. You can imagine it as a fixed frame, or stage, that is *absolute* and will never change.

When placing objects into the scene, we can express their position and orientation in terms of the world coordinate system. In *aRT*\ ist, the position of an object is a tuple of three coordinates (x, |nbsp| y, |nbsp| z) that refer to the position of the object's centre (i.e. the centre of its bounding box) in the world coordinate system. This centre point is the origin of the object's **local coordinate system**. Each object comes with three intrinsic axes. For example, the coordinates of the triangles in the surface mesh of an STL or PLY file are expressed in terms of its own, specific coordinate system. The axes of this intrinsic coordinate system must not necessarily align with *aRT*\ ist's world coordinate system, as illustrated in the example of the tilted *Rotor* in :numref:`worldLocalCoordinateSystem`.

When an object rotates in space, the directions of the three axes of its **local coordinate** system change in relation to the world coordinate system. Mathematically, we can express the local axes as vectors within the world coordinate system to know an object's orientation.

In the example illustrated in :numref:`worldLocalCoordinateSystem`, the detector's local coordinate system {X\ :sub:`D`, Y\ :sub:`D`, Z\ :sub:`D`} has the same origin and alignment as the world coordinate system. The source's local coordinate system {X\ :sub:`S`, Y\ :sub:`S`, Z\ :sub:`S`} has the same alignment, but its origin is at a different point in the world coordinate system, somewhere along the positive *Z* axis. The *Rotor's* local coordinate system has also a different origin, and additionally a different alignment (orientation) relative to the world coordinate system.

.. _worldLocalCoordinateSystem:
.. figure:: pictures/coordinate-system-world-local.png
    :width: 80%

    The world coordinate system {X, Y, Z} and the local coordinate systems of the three objects in the scene.




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

The panel also tells us that the detector has a size of 100 |nbsp| mm in *X* direction and 100 |nbsp| mm in *Y* direction. It has no thickness (0 |nbsp| mm in *Z* direction). The size always refers to an object's **bounding box**, i.e. its local coordinate system. In the case of our specific detector, the axes of its local coordinate system and the world coordinate system point in the same direction. In general, this is not the case for any object.

We can also get the information about the position of the source.

.. note:: Select the *Source* from the *Assembly List* and check its *Z* position.

The source is located 100 |nbsp| mm away from the detector on the *Z* axis.


Position
--------

In the field of computed tomography, two very important parameters of a system's geometry are the **source-detector distance (SDD)** and the **source-object distance (SOD)**. We will now change our scene to get the  geometry shown in :numref:`goalSetup`, with an SDD of 500 |nbsp| mm and an SOD of 300 |nbsp| mm.

.. _goalSetup:
.. figure:: pictures/tutorial-positioning-goal-setup.png
    :width: 100%

    Illustration of the geometry that we want to set up.

Setting up the :abbr:`SDD (source-detector distance)` is the easier part. We have to place the source at the position *Z* |nbsp| = |nbsp| 500 |nbsp| mm, because the detector is located at the origin of the coordinate system and we want to keep the convention to place the source in positive *Z* direction.

.. note:: Select the *Source* from the *Assembly List*. Set :code:`500` for the *Z* coordinate of the **Position** (:numref:`sourceTransformProperties`) and press :kbd:`Enter`.

The number in the input field will be displayed in blue until it is applied to the scene.

.. _sourceTransformProperties:
.. figure:: pictures/tutorial-positioning-source-properties.png
    :scale: 80%

    Placing the source at 500 |nbsp| mm. The number remains blue until we press :kbd:`Enter` to apply the change.

The *Rotor* is still at the origin of the coordinate system, basically "inside" the detector. To move it to the correct :abbr:`SOD (source-object distance)` of 300 |nbsp| mm, we have to keep in mind that we need to set its position on the *Z* axis, which starts at the detector. This means that we have to calculate the **object-source distance (ODD)** first:

**ODD = SDD – SOD = 200 mm.**

We can now place the *Rotor* 200 |nbsp| mm away from the detector to get the required :abbr:`SOD (source-object distance)` of 300 |nbsp| mm.

.. note:: Select the *Rotor* from the *Assembly List* and set its *Z* position to :code:`200`. Press :kbd:`Enter`.

When you take a look at the full view of your scene, it should now look like in :numref:`SODandSDDsetup`.

.. _SODandSDDsetup:
.. figure:: pictures/tutorial-positioning-SOD-SDD.png
    :width: 100%

    We have changed the geometry to an SOD of 300 |nbsp| mm and an SDD of 500 |nbsp| mm.

To set up horizontal and vertical shifts, you can change the *X* position and *Y* position of any object in the same way.


Orientation
-----------

One row below the *Position* settings in the *Parameter Panel* you can set up the **Orientation**. This is a set of three angles (in degrees) that represent consecutive rotations around an object's coordinate axes.

Whenever you load a new object into the scene, the axes of its local coordinate system are aligned with the axes of the world coordinate system. To reach the orientation specified by the three angles, *aRT*\ ist will perform three rotations in the following order.

1. The object is rotated by the **third angle** around its **local Z axis**.
2. The object is rotated by the **first angle** around the **resulting local X axis**.
3. The object is rotated by the **second angle** around the **resulting local Y axis**.