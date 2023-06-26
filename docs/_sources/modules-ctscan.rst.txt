.. include:: _templates/icons.rst

.. _CtScanSection:

CtScan
======

The **CtScan** module can be used to simulate cone beam :abbr:`CT (computerized tomography)` scans, applying the conventional circular scanning trajectory.
The module is accomplished by Feldkamp reconstruction and volume visualization. 
The simulated projections can be processed in the same way as experimental CT projections by external reconstruction programs. 

.. note::
    
    It is recommended to use the :abbr:`TIFF (Tagged Image File Format)` file format for easy data exchange, while the internal Feldkamp reconstruction requires projections in *BAM CT* format.

The CtScan module consists of three separate pages that can be navigated using the tabs at the top of the window - the **Setup**, the **Feldkamp** and the **Volume View** (:numref:`modules-CtScan1`). 
At bottom of module window, you can find a :guilabel:`Run` button to start or to :guilabel:`Stop` the simulation and a progress bar. 
The first two pages offer settings for the scan and for reconstruction (|artist| uses the Feldkamp algorithm for reconstruction). 
The finished tomogram can be viewed in the scene with the help of the first (**Setup**) or third (**Volume View**) tab by clicking on the :guilabel:`Show` button. 

.. note::
    
    In :ref:`Image Viewer <ImageViewerSection>` the sectional image can be seen with the Slice View in the third (Volume View) tab. 

All three pages will be explained in detail below.



.. _modules-CtScan1:
.. figure:: pictures/modules-CtScan1.*
    :alt: CtScan1
    :width: 71.3%
    
    CtScan: General settings.


.. _SetupSubsection:

Setup
-----

The :guilabel:`Setup` tab is used to configure the CT.

.. _ScanParametersSubsubsection:

Scan Parameters
^^^^^^^^^^^^^^^

The adjustable **Scan Parameters** are **Total Angle [°]**, **Number of Steps** and
**Angle Step Size [°]**.

.. _OutputSubsubsection:

Output
^^^^^^

At the **Output** choose **Directory** and **File Type** and put in a **File Name**. The **File Type** can be chosen between :class:`BAM CT` or :class:`TIFF` and :class:`16 bit` or :class:`float`. 

.. note::

    If fields are left blank they will be filled in automatically. 

If you wish to start reconstruction directly after the scan is finished check the corresponding box, **Run Feldkamp**. 
You may set the parameters for Feldkamp on the second page. Press the :guilabel:`Run` button on either one of the three pages when finished with the settings. 
If you choose not to check the **Run Feldkamp** box before starting the simulation you may initiate reconstruction manually (see: :ref:`Feldkamp <FeldkampSubsection>`). 
Click on the :guilabel:`Show` button when the simulation is finished to see the tomogram in the scene. 

.. hint::
    
    For an improved view deactivate the solid or minimize the opacity (double-click on the number of the object to change the opacity: **Parameter Panel** → **Setup Panel** → **Display**).

.. _AdvancedSubsubsection:

Advanced
^^^^^^^^

By marking **Only selected objects** you can include chosen objects of your assembly in the simulation. 
That means the selected objects rotate and the others do not. 

.. note::

   To do this, you should select the corresponding components in the :ref:`Parameter Panel <ParameterPanel>` beforehand. Select a single object by clicking on it. 
   Select two or more by holding down the :kbd:`Ctrl` key and clicking on the other components to be included in the simulation. 
   The components are selected when they are highlighted in blue.

* **Direction** is used to choose between clockwise or counterclockwise direction.
* **Scattering** is used to choose between off or McRay scatter-attitude.
* **Interval [°]** sets the interval for using the same scatter image (to save some time by not recalculating for each projection).
 
.. _FeldkampSubsection:

Feldkamp
--------

Set the parameters for reconstruction on the second tab - the :guilabel:`Feldkamp` (:numref:`modules-cttfeldk`). 
Check the **Run Feldkamp** box on the first page - the :guilabel:`Setup` - to start reconstruction automatically after the necessary data has been acquired. 

.. _OptionsSubsubsection:

Options
^^^^^^^

.. hint::
    
    Otherwise, you may start reconstruction manually by pressing the :guilabel:`Reconstruct` button in the lower half of the :guilabel:`Feldkamp` page.

**File name**: You may load previously acquired data with a click on the file symbol |16x16_document-open-folder| or use the recently acquired data.

Enable or disable **Interpolation** or/and the **Use of GPU**, with **Use multiple textures** or/and **Use half precision**.

.. _OutputFeldSubsubsection:

Output
^^^^^^

You can choose between different **File type**: :class:`BAM CT`, :class:`VTK` and :class:`RAW` as :class:`8bit`, :class:`16bit`, :class:`32bit` or :class:`float`.

.. _modules-cttfeldk:
.. figure:: pictures/modules-cttfeldk.*
    :alt: Feldkamp
    :width: 71.3%

    CtScan: Parameters for reconstruction.

.. _VolumeViewSubsection:

Volume View
-----------

With the tab :guilabel:`Volume View` (:numref:`modules-cttvv`) it is possible to show sectional image of the finished tomogram in :ref:`Image Viewer <ImageViewerSection>` directly after reconstruction. 
Alternatively, you may load previously acquired data. Supported file types are: :code:`.bd`, :code:`.raw`, :code:`.bin`, :code:`.vtk`.
Press the :guilabel:`Show` button on this page or the first page to start the calculation. This will take a few seconds. 
Then you can view the 3D-Scan of the part in the scene. Deactivate the part or minimize the opacity for an improved view of the 3D-Scan.
With the option **Slice View** → **Show plane** a sectional image of the part for the respectively axis (**X**, **Y** or **Z**) will appear in :ref:`Image Viewer <ImageViewerSection>`. 
If **Show slice** is activated, borders of the object can be seen in the plane. Choose an **Axis** and move the plane with the slider to see a sectional image of the part.

Settings for Volume View:

* **Minimum**
* **Maximum**
* **Level**
* **Contrast**
* Activate/Deactivate **Use 3D texture**
* **Gradient**/ **GradientROI** → choose between **All**, **Min/Max** or **Level/Contrast**

In **Positioning**, the scene is affected. It is possible to **Position** the voxel packet. With **Spacing**, the size of the scene can be influenced (in X, Y, Z).

.. _modules-cttvv:
.. figure:: pictures/modules-cttvv.png
    :alt: Feldkamp
    :width: 71.3%

    CtScan: Parameter for volume rendering.