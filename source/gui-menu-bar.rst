
Menu bar
--------

The Menu bar consists of different drop-down menus with common Windows commands and program specific functions. Some of the menu entries can also be found in the toolbar indicated by the same icon. If that is the case, the icon is next to the command/option in this manual.

File menu
^^^^^^^^^

The :guilabel:`File` drop-down menu comprises commands referring to the current project.

.. _guiFileMenu:
.. figure:: pictures/gui-menu-file.png
    :alt: aRTist file menu
    :scale: 100%

    File menu.

* **New Project** opens a new *aRT*\ ist scheme. This may also be done by pressing :kbd:`ctrl` + :kbd:`n`. The program will ask you if you want to save the changes on your current project.
* |icon-open| **Open** is used to search an existing project. Then select a project file in the dialog boxes that follow. Alternatively, press :kbd:`ctrl` + :kbd:`o`.
* |icon-library| **Open Library**  is used to load something from the collection of example parts and projects. It can also be opened by pressing :kbd:`ctrl` + :kbd:`l`.
* |icon-save| **Save** the current project to a single file. Alternatively, press :kbd:`ctrl` + :kbd:`s`.
* |icon-saveas| **Save As** renames a project or changes the location of where you want to save it. Alternatively, press :kbd:`ctrl` + :kbd:`shift` + :kbd:`s`.
* **Reload External Files** serves to check and update external dependencies (incorporated data files) of the current project. There you can choose file versions from the project or the file system in the dialog box that follow.
* **Last Directories** shows a list of recently opened directories. By clicking on an entry, a file open dialog for this directory will pop up.
* **Open New Window** starts a new, additional instance of *aRT*\ ist.
* **Restart** reboots the program. Before restarting, the program will ask you if you want to save the changes on your current project.
* **Quit** terminates the program. Before quitting the program will ask you if you want to save the changes on your current project. Alternatively, press :kbd:`ctrl` + :kbd:`q`.


.. |icon-open| image:: pictures/icons/16x16/document-open-folder.png
.. |icon-library| image:: pictures/icons/16x16/library.png
.. |icon-save| image:: pictures/icons/16x16/document-save.png
.. |icon-saveas| image:: pictures/icons/16x16/document-save-as.png


Edit menu
^^^^^^^^^

The :guilabel:`Edit` menu contains undo/redo functionalities with the project's history, whereas the usual commands (cut, copy, paste and delete) refer to parts in the assembly.

.. _guiEditMenu:
.. figure:: pictures/gui-menu-edit.png
    :alt: aRTist edit menu
    :scale: 100%

    Edit menu.

* |icon-undo| **Undo** erases the last change done to the project reverting it to its previous state. Alternatively, press :kbd:`ctrl` + :kbd:`z`.
* |icon-redo| **Redo** reverses the Undo or advances the buffer to its former state. Alternatively, press :kbd:`ctrl` + :kbd:`y`. The opposite of Undo is Redo. The Undo and Redo commands restrict you to an incremental sequence of changes.
* **History** displays the chronology of your recent actions and lets you revert back to any previous state. Alternatively, press :kbd:`ctrl` + :kbd:`h` to open the history.
* |icon-cut| **Cut** removes parts from the assembly and keeps them in the clipboard. In the scene or in the *Assembly list* (in the *Parameter panel*), you can left-click to select any part(s) that you want to cut. Select multiple parts by keeping the :kbd:`ctrl` key pressed on the keyboard.
* |icon-copy| **Copy** can create a duplicate of the selected part(s). First, select the part(s) you want to copy by using the Ctrl key on the keyboard and click on them with the left mouse either in the scene or in the *Assembly List* (of *Parameter Panel*). The selected parts are kept in the clipboard.
* |icon-paste| **Paste** appends parts from the clipboard to the *Assembly List*.
* |icon-delete| **Delete** removes selected parts from the *Assembly List*. 

.. |icon-undo| image:: pictures/icons/16x16/edit-undo.png
.. |icon-redo| image:: pictures/icons/16x16/edit-redo.png
.. |icon-cut| image:: pictures/icons/16x16/edit-cut.png
.. |icon-copy| image:: pictures/icons/16x16/edit-copy.png
.. |icon-paste| image:: pictures/icons/16x16/edit-paste.png
.. |icon-delete| image:: pictures/icons/16x16/edit-delete.png


Geometry menu
^^^^^^^^^^^^^

The :guilabel:`Geometry` menu includes all functions regarding the geometry application for parts from the assembly. *aRT*\ ist's functionality regarding "Geometry Manipulation" (→ *Union, Intersection, Difference, Arrange* and *Pick Destination*) for creating and arranging more complicated parts are described more in-depth in the separate chapter.

.. _guiGeometryMenu:
.. figure:: pictures/gui-menu-geometry.png
    :alt: aRTist geometry menu
    :scale: 100%

    Geometry menu.

* |icon-centernew| **Center New Parts** positions newly loaded parts (.stl or .ply files) at the origin of the global coordinate system, if activated. If deactivated, new parts will be placed at their native, original coordinates.
* **Isolate** deactivates all parts in the scene except the selected ones. Alternatively you can deactivate or activate a part with a click on the |icon-eye| eye symbol at the *Parameter Panel* → *Setup* → *Assembly List*.
* **Activate/Deactivate** selected item(s) of the assembly. If you deactivate an item, it will be ignored during simulation and be nearly invisible in the scene. Please note that you have to select the respective item first. Otherwise you may use the |icon-eye| eye symbol in the *Assembly List* of the *Parameter Panel* to achieve the same effect.
* **Set Material** changes the material of a selected part. As an alternative, you may click on the material name of a part in the *Assembly List* of the parameter panel to open a drop-down menu with the same options.
* |icon-union| **Union,** |icon-intersection| **Intersection** and |icon-difference| **Difference** can be used to create complex parts in the scene. For these commands, parts have to be created (e.g. with the |icon-solid| *Solid* module) and placed in the scene, so that they overlap. Then, select parts by using the :kbd:`Ctrl` key on the keyboard and click on them with the left mouse. The first selected part can be recognized by its yellow corners. All subsequent parts will be marked with white corners. The so-called *Geometry Manipulation* commands are explained more detailed in another section.

	* |icon-union| **Union** joins two or more parts. The order of selection is not important.
	* |icon-intersection| **Intersection** creates a new part from the overlapping areas of at least two parts. Everything else will be removed. The order of your selection is not important.
	* |icon-difference| **Difference** is used to create a new part from the difference of at least two other parts. By selecting this command the order of selection will be important for the result. The first selected part (yellow corner) is the minuend and all other selected parts (white corners) are subtracted from the first part.
* |icon-arrange| **Arrange** is used to put parts in order to the assembly. Select the parts which have to be arranged, and activate this command. In the opening dialog box four options: *none*, *-*, *center*, *+* are available for each of the three axes. The parts will be aligned with the first selected part.
* |icon-pickposition| **Pick Destination** moves item(s) from one point of the scene view to another. Click with the left mouse on the desired destination to relocate selected item(s).

.. |icon-centernew| image:: pictures/icons/16x16/center-new.png
.. |icon-eye| image:: pictures/icons/16x16/object-visible-on.png
.. |icon-union| image:: pictures/icons/16x16/boolean-union.png
.. |icon-intersection| image:: pictures/icons/16x16/boolean-intersection.png
.. |icon-difference| image:: pictures/icons/16x16/boolean-difference.png
.. |icon-solid| image:: pictures/icons/16x16/icon-solid.png
.. |icon-arrange| image:: pictures/icons/16x16/icon-arrange.png
.. |icon-pickposition| image:: pictures/icons/16x16/edit-pickposition.png