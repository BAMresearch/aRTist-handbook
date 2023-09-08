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

The three gray fields next to the drop-down menu show the mouse position (first gray field: X-axis, second gray field: Y-axis) 
and the intensity value of the displayed image at this position, where the unit dependents on the image type.

.. _LowerBarSubSection:

Lower toolbar
-------------

The **display range** controls indicate the minimum and maximum pixel value (intensity or thickness) used to display the current image. For manual contrast control, you may change those values with your keyboard. Press :kbd:`Enter` when finished.

|16x16_optimize-contrast| **Optimize**: If this function is activated, the display area is always automatically adjusted to the pixel value range of the current image. You can select a rectangular box of the image by mouse to limit the adjustment to the pixel value range within that ROI.

|16x16_reset-contrast| **Reset**: Resets the display to the default range. The default settings depend on the image type, e.g., 0 ... 65535 for 16bit images, or 0.5 ... 3.5 for the optical density of X-ray films.

|16x16_image-invert| **Invert**: Inverts the display to a negative of the image.

 .. |ImageViewer-Zoomfit| image:: pictures/modules-ImageViewer-Zoomfit.png

|ImageViewer-Zoomfit| **Zoom** in and out with the up-down arrows right to the displayed zoom factor or by typing in the zoom factor. Alternatively, you may use the mouse wheel or the right mouse button. Default: *Fit*, image fits to window (automatic zoom factor).

|16x16_zoom-original| Show the current image in actual size: one millimeter in the actual image corresponds to one millimeter on the display (1:1), or in |16x16_zoom-pixel-by-pixel| *pixel for pixel mode*: one pixel in the actual image corresponds to one pixel on the display.

|16x16_zoom-fit-best| Activates automatic zooming to fit the current image to the window.

|16x16_zoom-select| Zoom enlarges th current image to a selected part of the image. Draw a box with the mouse beforehand to select the desired ROI.

.. _BarOnTheRightSubsection:

Right toolbar
-------------

|16x16_document-save| Save the current image.

|16x16_document-preview| Opens the current image in an external viewer. Under :ref:`Settings <Tools-Settings>` any suitable external viewer can be configured. Default: software ISee!

.. note::

    With the implementation of |artist| the software ISee! v1.11.1-free is provided as an external viewer. The free version lacks all saving facilities - you can load images and can do everything inside the program, but the saving of measurement results or filtered/transformed images is missing. Both, the free and licensed versions you can find here: http://www.uzscherpel.de/BAM/ic/index.html.

|16x16_latitude-warning| Displays the exposure latitude warning for over- or underexposed regions. Overexposed areas will be marked in red whereas underexposed areas will be marked in blue.

|16x16_zoom-pixel-by-pixel| The pixel for pixel mode changes between actual pixel size and screen pixel size. This option effects the zoom and the ruler.

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


|16x16_lineal| **Show ruler**: An adjustable ruler is displayed over the image. It measures in millimeters or in pixels depending on |16x16_zoom-pixel-by-pixel| pixel for pixel mode.

|16x16_legend| **Show legend** opens an adjustable legend with the grey or thickness values. The minimum and maximum values correspond to the display range.

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
It consists of three additional submenus where you can find commands to open a new image from file, save the current simulation 
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

* **Gradient**, **Laplacian**, and **Smooth** are used to apply the corresponding filters.

    .. |modules-ImagViewerScale-closedSymbol| image:: pictures/modules-ImagViewerScale-closedSymbol.png
    .. |modules-ImageViewer-openSymbole| image:: pictures/modules-ImageViewer-openSymbole.png

* **Scale** is used to fill in the values for X and Y scaling/resampling (:numref:`ImageView-toolsscale`). Next to the output fields is a button |modules-ImagViewerScale-closedSymbol|. When you click on this button, the symbol changes into an open chain |modules-ImageViewer-openSymbole| or into a closed chain |modules-ImagViewerScale-closedSymbol|. The closed chain mode |modules-ImagViewerScale-closedSymbol| indicates to preserve the aspect ratio of the image, i.e., when changing the X or Y value, the other value will be adjusted automatically.

.. _ImageView-toolsscale:
.. figure:: pictures/modules-ImageView-toolsscale.png
    :alt: Image Viewer, Image, Scale
    :width: 25.3%

    Image Viewer, Image, Scale.

* **Mirror X/Y** refinverts the pixel order in X or Y direction.

* **Rotate CW/CCW** rotates the current image in 90 degree steps clockwise or counter-clockwise.

* **Math** opens the **ImageMath** dialog (:numref:`imagemath1`). It offers several arithmetic and point operations that can be applied to the current image.

    The first drop-down menu of the **ImageMath** offers the following arithmetic or point operations. In order for them to work the input field for **C** or **K** has to be filled in. Except for the first two operations, :class:`MultiplyByK` and :class:`AddConstant`, the actual numbers are not important. Press :guilabel:`Compute` to run the operation and :guilabel:`Cancel` to reverse it:

    * :class:`MultiplyByK` is used for the pointwise multiplication of each pixel with the value **K**.
    * :class:`AddConstant` is used for the pointwise addition of each pixel with the constant **C**.
    * :class:`Exp` takes the exponential of each pixel (*e* raised to the powr of the pixel value, where *e* is the base of a natural log).
    * :class:`Log` takes the natural log of each pixel. 
    * :class:`Invert` inverts the current image.
    * :class:`AbsoluteValue` takes the absolute value of each pixel.
    * :class:`Square` squares the value of each pixel.
    * :class:`SquareRoot` takes the square root of each pixel.
    * :class:`Sin` calculates the sine of each pixel.
    * :class:`Cos` calculates the cosine of each pixel.
    * :class:`ATAN` calculates the arctangent of each pixel.

    The following operations calculate a new image out of two images therefore the third drop-down menu is enabled. Hint: **C** and **K** may be left empty.

    * :class:`Add` sums the corresponding pixel values of the two images.

    * :class:`Subtract` substracts the corresponding pixel values of the second image from the first image.
    * :class:`Multiply` multiplies the corresponding pixel values of the two images.
    * :class:`Divide` divides the corresponding pixel values of the first image by the second image.
    * :class:`Min` shows the minimum grey values of the two images.
    * :class:`Max` shows the maximum grey values of the two images.

.. _imagemath1:
.. figure:: pictures/modules-ImageView-imagemath1.jpg
    :alt: Image Viewer, Image, Math
    :width: 41.3%

    Image Viewer, Image, Math.



.. _ViewSubsubSection:

View
^^^^

Under **View** you will find commands to change the display, but not the content of an image(:numref:`image_viewer3`). 

.. note::
    
    Please note that the changes made here are non-permanent modifications and will not be visible when you save the image or open it in an external viewer as opposed to the commands found in the Image submenu.

.. _image_viewer3:
.. figure:: pictures/modules-image_viewer3.jpg
    :alt: Image Viewer, View, Orientation Menu
    :width: 41.3%

    Image Viewer, View, Orientation Menu.

**Interpolate** activates/deactivates interpolation. |artist| uses linear interpolation.

**Logarithmic** is a point operator based on the log function and changes the dynamic range of the image.

**Orientation** is used for the commands, which also can be accessed with the |16x16_object-flip-turn| button in the  Image Viewer (see: :ref:`Bar on the right <BarOnTheRightSubsection>`).