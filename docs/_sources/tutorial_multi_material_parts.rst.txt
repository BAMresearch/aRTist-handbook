.. note:: We continue with the project from the last tutorial. You can download it here if you need the current state:

	 :download:`tutorial_materials.aRTist <files/tutorial_materials.aRTist>` |nbsp| (4.6 MB)

Multi-Component Parts
=====================

Each part on the *Assembly List* is a solid that can only have one single material. We can place multiple parts into the scene, each with a different material. In regions of space where these parts overlap, there is a strict hierarchy: objects that appear later in the *Assembly List* (towards the bottom) have a higher priority and completely replace previous objects (of lower priority). We can use this fact to build objects from components that all have different materials.

In this tutorial, we will create a small air pocket and place it inside the *Rotor*.


Solid Module
-------------

The *Solid* module can generate simple geometric solids like spheres, cuboids, etc.

.. note:: In the *Toolbar*, click the button |icon-solid| :guilabel:`Generate simple geometric object` or open the module from the menu bar: :guilabel:`Modules` → :guilabel:`Solid`. (:numref:`solidModule`)

.. |icon-solid| image:: pictures/icons/32x32/icon-solid.png

.. _solidModule:
.. figure:: pictures/tutorial-multimaterial-solid-module.png
	:width: 65%

	We use the *Solid* module to create a sphere that we will use as an air pocket.

You can choose the :guilabel:`Type` of solid that you would like to generate. Examples for the available types are shown in :numref:`availableSolids`. For each solid, you can tune its geometric properties. Typically, the aspect ratio can be controlled with the parameters :guilabel:`X`, :guilabel:`Y` and :guilabel:`Z` which specify the dimensions of the bounding box. :guilabel:`W` is an additional parameter that is sometimes necessary, for example to set the diameter of a tube's inner hole or the size of the foundation of a wedge that is not angled.

:guilabel:`Phi steps` basically controls the resolution of the solid's mesh, or the number of steps on a step wedge. :guilabel:`Theta steps` is available for ellipsoids if you create a :guilabel:`regular ellipsoid grid`. In this case, :guilabel:`phi` and :guilabel:`theta` refer to the two angles of a spherical coordinate system.

.. _availableSolids:
.. figure:: pictures/solids.png
	:width: 90%

	The basic geometric solids that can be generated in the *Solids* module.

.. note:: Create a small sphere that we will use as an air pocket.

	1. Set :guilabel:`Type` to :code:`ellipsoid`.
	2. Activate :guilabel:`X=Y=Z` to generate an ideal sphere.
	3. Make sure :guilabel:`regular ellipsoid grid` is deactivated.
	4. For the diameter :guilabel:`X`, enter :code:`2` mm.
	5. For :guilabel:`Phi steps`, set :code:`42` to create a relatively smooth sphere.
	6. Click :guilabel:`Create`.

The sphere will appear with the name *"ellipsoid"* on the *Assembly List*. It is made of iron and will have a random colour.

.. note:: Click on the name of the *"ellipsoid"* and rename it to :code:`Air Pocket`. Press :kbd:`Enter` once you have typed the new name. Click on the *Air Pocket's* current material (Fe) and choose :code:`air` from the drop-down menu.

When you click |icon-zoom-to-selection| :guilabel:`Zoom to Selection` in the *Toolbar*, you should see the sphere, located in the centre of the detector at the origin of the coordinate system (:numref:`airpocketCreated`).

.. |icon-zoom-to-selection| image:: pictures/icons/32x32/zoom-select.png

.. _airpocketCreated:
.. figure:: pictures/tutorial-multimaterial-airpocket-created.png
	:width: 100%

	We created a spherical *ellipsoid*, renamed it to *Air Pocket*, set its material to *air* and zoomed in to its current location at the coordinate origin.


Overlapping Parts
-----------------

The *Air Pocket* appears after the *Rotor* in the *Assembly List*. Therefore, it has a higher priority and will replace the *Rotor* wherever they overlap. All we have to do now is move it into the *Rotor*.

.. note:: Enter the following :guilabel:`Position` for the *Air Pocket*: :guilabel:`X`: :code:`4`, :guilabel:`Y`: :code:`3`, :guilabel:`Z`: :code:`200`. Press :kbd:`Enter` to set the position. (:numref:`airpocketCoordinates`)

.. _airpocketCoordinates:
.. figure:: pictures/tutorial-multimaterial-airpocket-coordinates.png
	:scale: 85%

	We place the *Air Pocket* at coordinates inside the *Rotor*.

.. note:: To see the *Air Pocket* in the virtual scene, make the *Rotor* transparent: double-click on its colour in the *Assembly List* and decrease its *Opacity* (:numref:`rotorTransparency`). Alternatively, you could switch its rendering mode to |icon-wireframe| **Wireframe View**.

.. |icon-wireframe| image:: pictures/icons/32x32/switch-wireframe.png

.. _rotorTransparency:
.. figure:: pictures/tutorial-multimaterial-rotor-transparency.png
	:width: 100%

	We decreased the opacity of the *Rotor* to 0.2 to see the *Air Pocket* inside it in the virtual scene.

You should now also be able to identify the *Air Pocket* in the projection image that the *Image Viewer* displays. It is easier to see when you simulate a full projection image (click the |icon-run| :guilabel:`Compute` button) and zoom in. You may even select a region of interest (ROI) to enhance the local contrast (:numref:`airpocketImageViewer`).

.. |icon-run| image:: pictures/icons/32x32/compute-radiography.png

.. _airpocketImageViewer:
.. figure:: pictures/tutorial-multimaterial-imageviewer-airpocket.png
	:scale: 85%

	The *Air Pocket* becomes visible in the projection image. A region of interest (blue rectangle) is selected to rescale the display range and enhance the local contrast.

.. note:: Toggle the visibility of the *Air Pocket* with its |icon-visible| **visibility switch** in the *Assembly List.* Observe how it disappears and reappears in the projection image. When you are done, please keep it visible so that you can still see it for the next step.

.. |icon-visible| image:: pictures/icons/16x16/object-visible-on.png


Order of Parts (Hierarchy)
---------------------------

As described at the beginning of this tutorial, parts that appear later in the list completely replace earlier parts in regions where they overlap. You can rearrange the parts on the *Assembly List* to establish a different order and therefore a different hierarchy of priorities.

.. note:: Click on the *Air Pocket* in the *Assembly List* and keep holding your mouse button. Drag the part one step upwards such that it will take a place before the *Rotor*. Release your mouse button to drop it there. (:numref:`rearrangeParts`)

.. _rearrangeParts:
.. figure:: pictures/tutorial-multimaterial-rearrange-parts.png
	:width: 85%

	We drag the *Air Pocket* to a position before the *Rotor*. (Left: while dragging, right: dropped.)

After we re-arranged the order of parts, the *Air Pocket* is not visible anymore in the projection image (:numref:`airpocketInvisible`). It is now completely replaced by the *Rotor* material because the *Rotor* has a higher priority. Also note that each part keeps its unique part *ID* (*Rotor*: |nbsp| 1, *Air Pocket*: |nbsp| 2). This ID is used by some modules to refer to parts. It is independent from the part order and will not change.

.. _airpocketInvisible:
.. figure:: pictures/tutorial-multimaterial-imageviewer-airpocket-disappeared.png
	:scale: 85%

	The *Air Pocket* disappeared from the projection image as it is replaced by *Rotor* material.

.. note:: Move the *Air Pocket* back to its previous position underneath the *Rotor* in the *Assembly List*. It should now appear again in the projection image. (As we saw in :numref:`airpocketImageViewer`.)


Transforming Groups of Parts
----------------------------

While *aRT*\ ist doesn't provide the ability to permanently group parts, you can select multiple parts on the *Assembly List* and transform them all at the same time. They will then keep their relative positions. You can choose multiple parts by pressing :kbd:`Ctrl` while selecting them with a click.

The first part you select will be displayed with a **yellow-cornered** bounding box in the scene view. Any additional parts selected after that will get a **white-cornered** bounding box. The first selected part is special: its centre will be the centre of rotation or scaling for the whole group of parts. Alternatively, you may enter a different **reference position** after you have selected all the parts.

Let's try this. First, we rotate the *Rotor* around its central axis together with the *Air Pocket.*

.. note:: 
	1. Deselect everything: click on the free, white space at the bottom of the *Assembly List*.
	2. Select the *Rotor* from the *Assembly List*.
	3. Hold down the :kbd:`Ctrl` key on your keyboard while you select the *Air Pocket.*

Both the *Rotor* and the *Air Pocket* should now be selected. There should be a yellow-cornered bounding box around the *Rotor* and a white-cornered bounding box around the *Air Pocket* (:numref:`twoPartsSelected`).

.. _twoPartsSelected:
.. figure:: pictures/tutorial-multimaterial-two-parts-selected.png
	:width: 100%

	We have first selected the *Rotor*, then the *Air Pocket.*

.. note:: 
	1. Under *Transformation of 2 parts*, select the |icon-world| **world coordinate system.** (This is important: if you select *local* instead, each part will rotate around its own axis instead of a common axis.)
	2. Select the |icon-rotation| **Rotation Mode.**
	3. Select the |icon-arrow-down| **Z axis.**
	4. For the :guilabel:`Value`, enter :code:`45` degrees.
	5. Click to the **right** of the transform slider handle to perform one rotation step.

.. |icon-world| image:: pictures/icons/22x22/world-coordinate-system.png
.. |icon-rotation| image:: pictures/icons/22x22/transformation-rotate.png
.. |icon-arrow-down| image:: pictures/icons/22x22/set-coordinate-arrow-down.png

Both the *Rotor* and the *Air Pocket* should now rotate around the *Rotor's* central axis and keep their relative positions. This means that the *Air Pocket* travels by 45° in counter-clockwise direction in the projection image. (This is because the *Z* vector points away from the detector towards the source.)

.. _twoPartsRotated:
.. figure:: pictures/tutorial-multimaterial-two-parts-rotated.png
	:width: 100%

	We rotated both parts around the common central axis of the *Rotor.*

We have not set any *reference position,* which means that the centre of rotation is the centre of the first-selected part (the *Rotor*). Let us now set a different **Reference Position.**

.. note:: For the :guilabel:`Reference Pos.`, enter the following coordinates: :guilabel:`X`: :code:`0`, :guilabel:`Y`: :code:`-15`, :guilabel:`Z`: :code:`200`. Press :kbd:`Enter` to set it.

The reference position (displayed as a red sphere in the virtual scene) now moves to the new coordinates away from the *Rotor's* centre (:numref:`twoPartsReferencePosition`). The axis of rotation (still pointing in the direction of the *Z* axis of the world coordinate system) is drawn as a yellow vector through the reference position. 

.. _twoPartsReferencePosition:
.. figure:: pictures/tutorial-multimaterial-reference-position.png
	:width: 100%

	We moved the reference position away from the *Rotor's* principal axis.

We can now use this new reference position as the centre of rotation.

.. note:: 
	1. In the *Image Viewer*, click |icon-zoom-to-fit| :guilabel:`Zoom to fit window` to see the whole projection image again. (Just in case you zoomed in previously.)
	2. Click 8× to the **right** of the transform slider to perform one full rotation of the group of parts. Observe how they both rotate around the reference position, both in the virtual scene and in the projection image. They keep their positions relative to each other.
	3. When playing around, try to reach their initial position again.

.. |icon-zoom-to-fit| image:: pictures/icons/22x22/zoom-fit-best.png

You can also use the reference position as the **scaling centre**; this works in the same way. And, of course, you can also use the *Transformation* controls to translate selected parts as a group.


Summary
-------

In this tutorial, we have demonstrated how to create simple geometric solids and how to handle assemblies of multiple components.

* You know about the **Solid module** and how to use it to create simple geometric solids.
* You have learned that the **order of parts** on the *Assembly List* plays an important role in regions where parts overlap. Parts at positions later on the list (further to the bottom) replace parts that are earlier on the list.
* You have selected **multiple parts** using the :kbd:`Ctrl` key on your keyboard.
* You know that the **first part** that you select has a special role: its centre will be the reference position for rotations and scalings, unless you set a different one.
* You have learned how to use the **reference position** as a centre of rotation (or scaling) for groups of objects.

| The scene that we created up to this point is available for download:
| :download:`tutorial_multiple_components.aRTist <files/tutorial_multiple_components.aRTist>` (4.6 MB)