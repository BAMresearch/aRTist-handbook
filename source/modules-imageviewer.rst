.. include:: _templates/icons.rst

.. _ImageViewerSection:

|32x32_image-radiography| Image Viewer 
======================================

The |16x16_image-radiography| **Image Viewer** module displays the simulation results (:numref:`ImageViewerPic1`). 

.. _ImageViewerPic1:
.. figure:: pictures/modules-imageviewer-ViewerPic1.png
    :alt: View of the Image Viewer at program start
    :width: 71.3%

    Image Viewer module.

.. _UpperBarSubSection:

Upper toolbar
-------------

|16x16_image-status-undefined| : A grayed out check mark means that no images have been loaded into Image Viewer before.

|16x16_image-preview| : A crossed out red circle means that you are currently viewing a preview of the simulation. The preview has a lower resolution and is calculated with different parameters for faster results.

|16x16_image-final| : Run |16x16_aRTist| the simulation and a green tick will appear indicating that the simulation was successful.

The drop-down menu to the right of the icon offers different images of the simulation steps (:class:`energy density J/m²` or :class:`primary intensities`). 
The available options depend on the current settings.

The three gray fields next to the drop-down menu display the mouse position (first grey field: X-axis, second grey field: Y-axis) 
and the energy density [in J/m²] or primary intensities [in gray value] or thickness [in mm] (third grey field) at that position. Those figures are also displayed in the status bar (see: :numref:`guiMainWindow`).

.. _LowerBarSubSection:

Lower toolbar
-------------

**display range** indicates the minimum and maximum grey value/thickness of the current image. If needed, you may change those values with your keyboard. Press :kbd:`Enter` when finished.

|16x16_optimize-contrast| Optimize the display range (dependent on current image).

|16x16_reset-contrast| Reset the display to default the range (maximum and minimum output in the image).

|16x16_image-invert| inverts the display to a negative of the image and back.

 .. |ImageViewer-Zoomfit| image:: pictures/modules-ImageViewer-Zoomfit.png

|ImageViewer-Zoomfit| **Zoom** in and out with the up-down arrows right to the displayed zoom factor or by typing in the zoom fachtor. Alternatively, you may use the mouse wheel or the right mouse button. Default: image fits to window.

|16x16_zoom-original| Show the current image in actual size: one pixel in the actual image corresponds to one pixel on the display (1:1).

|16x16_zoom-fit-best| Zoom to fit actual image to the window which resets the zoom after zooming in or out.

|16x16_zoom-select| Zoom enlarges th current image to a selected part of the image. Select the desired part with the left mouse button and draw a box in which it sould be zoomed.

.. _BarOnTheRightSubsection:

Right toolbar
-------------

|16x16_document-save| Save the current image.

|16x16_document-preview| Show in external viewer opens the current image in an external viewer. 

.. note::

    With the implementation of |artist| the software ISee! v1.11.1-free is provided as an external viewer. The free version lacks all saving facilities - you can load images and can do everything inside the program, but the saving of measurement results or filtered/transformed images is missing. Both, the free and licensed versions you can find here: http://www.uzscherpel.de/BAM/ic/index.html. Under :ref:`Settings <Tools-Settings>` any suitable external viewer can be choosen.

|16x16_latitude-warning| Displays the exposure latitude warning (de)activates warning for over- or underexposure. Overexposed areas will be marked in red whereas underexposed areas will be marked in blue.

|16x16_zoom-pixel-by-pixel| The pixel for pixel mode changes between actual pixel size and screen pixel size. This option is only active when Zoom = Fit.

|16x16_object-flip-turn| Change image orientation opens a menu with different options to mirror or rotate the image.

* **Reset** is used for resetting the settings in the image orientation.

* **Mirror X/Mirror Y** is used to reflect the image orientation on X-axis or Y-axis.

* **Rotate CW/Rotate CCW** is used to rotate the image clockwise or counter-clockwise.

* **0°** / **90°** / **180°** / **270°**  is used to orientate the image (between four different angles).

   .. seealso::
    
       The same menu like in :numref:`ImageViewRot` can be found in the :guilabel:`Tools` menu under  **Image Viewer** → **View** → **Orientation**. Please note that the changes made with commands from either one of those menus do not have lasting effects, for example, when saving the image. If you want to permanently edit an image use the commands from the following menu: :guilabel:`Tools` →  **Image Viewer** → **Image**.
    
.. _ImageViewRot:
.. figure:: pictures/modules-ImageViewRot.png
    :alt: Image View: Change image orientation
    :width: 15.3%

    Image View: Change image orientation.


|16x16_lineal| **Show ruler** displays a ruler on the bottom of the image. It measures the image width in millimeters by default. If the ruler is turned on, you can also measure in pixels. To do this press the icon for pixel mode |16x16_zoom-pixel-by-pixel|.

|16x16_legend| **Show legend** opens a legend with the grey or thickness values. The minimum and maximum values are determined by the display range. Height, width, and position of the legend are adjustable.

.. _ImageViewerToolsMenuSubsection:

Tools Menu: Image Viewer
------------------------

In the following every command of the :ref:`Image Viewer <ImageViewerSection>` submenu from the :ref:`Tools Menu <ToolsMenuSubsection>` (:numref:`ImageViewToolsNeu`) will be explained.

.. _ImageViewToolsNeu:
.. figure:: pictures/modules-ImageView-tools_neu.png
    :alt: Tools Menu, Image Viewer Menu
    :width: 41.3%

    Tools Menu,  Image Viewer Menu.

This submenu offers specific settings for the :ref:`Image Viewer <ImageViewerSection>` and consists of different additional submenus:

* File
* Image
* View

.. _FileSubsubSection:

File
^^^^
It consists of three additional submenus: Under File you can find commands to open a new image , save the current simulation 
(you may also use the Save button |16x16_document-save| in  Image Viewer) or clear the image list (:numref:`image_viewer1`).

.. _image_viewer1:
.. figure:: pictures/modules-image_viewer1.jpg
    :alt: Image Viewer, File Menu
    :width: 30.3%

    Image Viewer, File Menu.

.. _ImageSubsubSection:

Image
^^^^^

Under Image you can find different filters and different options to mirror or rotate the current image (:numref:`image_viewer2`). 

.. note::

    Please note that changes made with commands from this submenu are permanent (for example when saving the image).
    For non-permanent modifications use commands from the View submenu.

.. _image_viewer2:
.. figure:: pictures/modules-image_viewer2.jpg
    :alt: Image Viewer, Image Menu
    :width: 25.3%

    Image Viewer, Image Menu.

* **Gradient**, **Laplacian**, and **Smooth** are used to choose between the corresponding filters.

    .. |modules-ImagViewerScale-closedSymbol| image:: pictures/modules-ImagViewerScale-closedSymbol.png
    .. |modules-ImageViewer-openSymbole| image:: pictures/modules-ImageViewer-openSymbole.png

* **Scale** is used to fill in the values for X and Y scaling/resampling (:numref:`ImageView-toolsscale`). Next to the output fields is a button |modules-ImagViewerScale-closedSymbol|. When you click on this button, the symbol changes into an open chain |modules-ImageViewer-openSymbole| or into a closed chain |modules-ImagViewerScale-closedSymbol|. The closed chain symbol |modules-ImagViewerScale-closedSymbol| gives a square image, i.e., the scaling in X and Y is equal. The open symbol |modules-ImageViewer-openSymbole| allows rectangular pixels, as X and Y can have different values.

.. _ImageView-toolsscale:
.. figure:: pictures/modules-ImageView-toolsscale.png
    :alt: Image Viewer, Image, Scale
    :width: 25.3%

    Image Viewer, Image, Scale.

* **Mirror X/Y** reflects the current image on the X-axis or the Y-axis.

* **Rotate CW/CCW** rotates the current image in 90 degree steps clockwise or counter-clockwise.

* **Math** opens the **ImageMath** window (:numref:`imagemath1`). It offers several arithmetic and point operations that can be applied to the current image.

    The first drop-down menu of the **ImageMath** offers the following arithmetic or point operations. In order for them to work the input field for **C** or **K** has to be filled in. Except for the first two operations, :class:`MultiplyByK` and :class:`AddConstant`, the actual numbers are not important. Press :guilabel:`Compute` to run the operation and :guilabel:`Cancel` to reverse it:

.. _imagemath1:
.. figure:: pictures/modules-ImageView-imagemath1.jpg
    :alt: Image Viewer, Image, Math
    :width: 41.3%

    Image Viewer, Image, Math.


* :class:`MultiplyByK` is used for the pointwise multiplication of each pixel with the value **K**.
* :class:`AddConstant` is used for the pointwise addition of each pixel with the constant **C**.
* :class:`Exp` is a point operator based on the exponential function and changes the dynamic range of the image.
* :class:`Log` is a point operator based on the log function and changes the dynamic range of the image. **** **REMARK: with this explanation change the dynamic range of the image, I assume, that Log is log10** ****
* :class:`Invert` inverts the current image.
* :class:`AbsoluteValue` takes the absolute value of each pixel.
* :class:`Square` squares the value of each pixel.
* :class:`SquareRoot` takes the square root of each pixel.
* :class:`Sin` calculates the sine of each pixel.
* :class:`Cos` calculates the cosine of each pixel.
* :class:`ATAN` calculates the arctangent of each pixel.

The following operations calculate a new image out of two images therefore the third drop-down menu is enabled. 

.. hint::
    
    **C** and **K** may be left empty.

* :class:`Add` sums the corresponding pixel values of the two images.
* :class:`Subtract` substracts the corresponding pixel values of the second image from the first image.
* :class:`Multiply` multiplies the corresponding pixel values of the two images.
* :class:`Divide` divides the corresponding pixel values of the first image by the second image.
* :class:`Min` shows the minimum grey values of the two images.
* :class:`Max` shows the maximum grey values of the two images.

.. _ViewSubsubSection:

View
^^^^

Under **View** you can find the same four mirror and rotate commands explained under **Image** and additional options (:numref:`image_viewer3`). 

.. note::
    
    Please note that the changes made here are non-permanent modifications and will not be visible when you save the image or open it in an external viewer as opposed to the commands found in the Image submenu.

.. _image_viewer3:
.. figure:: pictures/modules-image_viewer3.jpg
    :alt: Image Viewer, View, Orientation Menu
    :width: 41.3%

    Image Viewer, View, Orientation Menu.

**Interpolate** activates/deactivates interpolation. |artist| uses linear interpolation.

**Logarithmic** is a point operator based on the log function and changes the dynamic range of the image.

**Orientation** is used for the following commands, which also can be accessed with the |16x16_object-flip-turn| button in the  Image Viewer (see: :ref:`Bar on the right <BarOnTheRightSubsection>`).