.. include:: _templates/icons.rst

Menu bar
--------
.. _MenuBarSection:

The Menu bar consists of different drop-down menus with common Windows commands and program specific functions. Some of the menu entries can also be found in the toolbar indicated by the same icon. If that is the case, the icon is next to the command/option in this manual.

File menu
^^^^^^^^^
.. _FileMenuSubsection:

The :guilabel:`File` drop-down menu comprises commands referring to the current project.

.. _guiFileMenu:
.. figure:: pictures/gui-menu-file.png
    :alt: aRTist file menu
    :width: 60%

    File menu.

* **New Project** opens a new |artist| scheme. This may also be done by pressing :kbd:`ctrl` + :kbd:`n`. The program will ask you if you want to save the changes on your current project.
* |16x16_document-open-folder| **Open** is used to search an existing project. Then select a project file in the dialog boxes that follow. Alternatively, press :kbd:`ctrl` + :kbd:`o`.
* |16x16_library| **Open Library**  is used to load something from the collection of example parts and projects. It can also be opened by pressing :kbd:`ctrl` + :kbd:`l`.
* |16x16_document-save| **Save** the current project to a single file. Alternatively, press :kbd:`ctrl` + :kbd:`s`.
* |16x16_document-save-as| **Save As** renames a project or changes the location of where you want to save it. Alternatively, press :kbd:`ctrl` + :kbd:`shift` + :kbd:`s`.
* **Reload External Files** serves to check and update external dependencies (incorporated data files) of the current project. There you can choose file versions from the project or the file system in the dialog box that follow.
* **Last Directories** shows a list of recently opened directories. By clicking on an entry, a file open dialog for this directory will pop up.
* **Open New Window** starts a new, additional instance of |artist|.
* **Restart** reboots the program. Before restarting, the program will ask you if you want to save any changes to your current project.
* **Quit** terminates the program. Before quitting the program will ask you if you want to save any changes on your current project. Alternatively, press :kbd:`ctrl` + :kbd:`q`.


Edit menu
^^^^^^^^^
.. _EditMenuSubsection:

The :guilabel:`Edit` menu contains undo/redo functionalities with the project's history, whereas the usual commands (cut, copy, paste and delete) refer to parts in the assembly.

.. _guiEditMenu:
.. figure:: pictures/gui-menu-edit.png
    :alt: aRTist edit menu
    :width: 20%

    Edit menu.

* |16x16_edit-undo| **Undo** erases the last change done to the project reverting it to its previous state. Alternatively, press :kbd:`ctrl` + :kbd:`z`.
* |16x16_edit-redo| **Redo** reverses the Undo or advances the buffer to its former state. Alternatively, press :kbd:`ctrl` + :kbd:`y`. The opposite of Undo is Redo. The Undo and Redo commands restrict you to an incremental sequence of changes.
* **History** displays the chronology of your recent actions and lets you revert back to any previous state. Alternatively, press :kbd:`ctrl` + :kbd:`h` to open the history.
* |16x16_edit-cut| **Cut** removes parts from the assembly and keeps them in the clipboard. In the scene or in the *Assembly list* (in the *Parameter panel*), you can left-click to select any part(s) that you want to cut. Select multiple parts by keeping the :kbd:`ctrl` key pressed on the keyboard.
* |16x16_edit-copy| **Copy** can create a duplicate of the selected part(s). First, select the part(s) you want to copy by using the Ctrl key on the keyboard and click on them with the left mouse either in the scene or in the *Assembly List* (of *Parameter Panel*). The selected parts are kept in the clipboard.
* |16x16_edit-paste| **Paste** appends parts from the clipboard to the *Assembly List*.
* |16x16_edit-delete| **Delete** removes selected parts from the *Assembly List*. 


Geometry menu
^^^^^^^^^^^^^
.. _GeometryMenuSubsection:

The :guilabel:`Geometry` menu includes all functions regarding the geometry application for parts from the assembly. |artist|'s functionality regarding "Geometry Manipulation" (→ *Union, Intersection, Difference, Arrange* and *Pick Destination*) for creating and arranging more complicated parts are described more in-depth in the separate chapter.

.. _guiGeometryMenu:
.. figure:: pictures/gui-menu-geometry.png
    :alt: aRTist geometry menu
    :width: 20%

    Geometry menu.

* |16x16_center-new| **Center New Parts** positions newly loaded parts (.stl or .ply files) at the origin of the global coordinate system, if activated. If deactivated, new parts will be placed at their native, original coordinates.
* **Isolate** deactivates all parts in the scene except the selected ones. Alternatively you can deactivate or activate a part with a click on the |16x16_object-visible-on| eye symbol at the *Parameter Panel* → *Setup* → *Assembly List*.
* **Activate/Deactivate** selected item(s) of the assembly. If you deactivate an item, it will be ignored during simulation and be nearly invisible in the scene. Please note that you have to select the respective item first. Otherwise you may use the |16x16_object-visible-on| eye symbol in the *Assembly List* of the *Parameter Panel* to achieve the same effect.
* **Set Material** changes the material of a selected part. As an alternative, you may click on the material name of a part in the *Assembly List* of the parameter panel to open a drop-down menu with the same options.
* |16x16_boolean-union| **Union,** |16x16_boolean-intersection| **Intersection** and |16x16_boolean-difference| **Difference** can be used to create complex parts in the scene. For these commands, parts have to be created (e.g. with the |16x16_icon-solid| *Solid* module) and placed in the scene, so that they overlap. Then, select parts by using the :kbd:`Ctrl` key on the keyboard and click on them with the left mouse. The first selected part can be recognized by its yellow corners. All subsequent parts will be marked with white corners. The so-called *Geometry Manipulation* commands are explained more detailed in another section.

	* |16x16_boolean-union| **Union** joins two or more parts. The order of selection is not important.
	* |16x16_boolean-intersection| **Intersection** creates a new part from the overlapping areas of at least two parts. Everything else will be removed. The order of your selection is not important.
	* |16x16_boolean-difference| **Difference** is used to create a new part from the difference of at least two other parts. By selecting this command the order of selection will be important for the result. The first selected part (yellow corner) is the minuend and all other selected parts (white corners) are subtracted from the first part.
* |16x16_icon-arrange| **Arrange** is used to put parts in order to the assembly. Select the parts which have to be arranged, and activate this command. In the opening dialog box four options: *none*, *-*, *center*, *+* are available for each of the three axes. The parts will be aligned with the first selected part.
* |16x16_edit-pickposition| **Pick Destination** moves item(s) from one point of the scene view to another. Click with the left mouse on the desired destination to relocate selected item(s).
