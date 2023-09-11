.. include:: _templates/icons.rst

.. _CtScanSection:

CtScan
======

The **CtScan** module can be used to simulate cone beam :abbr:`CT (computerized tomography)` scans, applying the conventional circular scanning trajectory.
The module is accomplished by a Feldkamp reconstruction and volume visualization. 
The simulated projections can be processed in the same way as experimental CT projections by external reconstruction programs. 

.. note::
    
    It is recommended to use the :abbr:`TIFF (Tagged Image File Format)` file format for easy data exchange, while the internal Feldkamp reconstruction requires projections in *BAM CT* format.

The CtScan module consists of three separate pages that can be navigated using the tabs at the top of the window - the **Setup**, the **Feldkamp**, and the **Volume View** (:numref:`modules-CtScan1`). 
At bottom of module window, you can find a :guilabel:`Run` button to start or to :guilabel:`Stop` the simulation and a progress bar. 
The first two pages offer settings for the scan and for reconstruction (|artist| uses the Feldkamp algorithm for reconstruction). 
The finished tomogram can be viewed in the scene with the help of the first (**Setup**) or third (**Volume View**) tab by clicking on the :guilabel:`Show` button. 

.. note::
    
    In the :ref:`Image Viewer <ImageViewerSection>` the sectional image can be seen selcted by the Slice View in the third (Volume View) tab. 

All three pages will be explained in detail below.



.. _modules-CtScan1:
.. figure:: pictures/modules-CtScan1.*
    :alt: CtScan1
    :width: 71.3%
    
    CtScan: General settings.


.. _SetupSubsection:

Setup
-----

The :guilabel:`Setup` tab is used to configure the CT (:numref:`modules-CtScan1`).

.. _ScanParametersSubsubsection:

Scan Parameters
^^^^^^^^^^^^^^^

The adjustable **Scan Parameters** are **Total Angle [°]**, **Number of Steps**, and
**Angle Step Size [°]**. The **Total Angle [°]** is preset to 360°. When setting the **Number of Steps**, the **Angle Step Size [°]** is automatically updated and cannot be set by the user.

.. _OutputSubsubsection:

Output
^^^^^^

At the **Output** choose the **Directory** and the **File Type** and set a **File Name**. The **File Type** can be chosen between :class:`BAM CT` or :class:`TIFF` and :class:`16 bit` or :class:`float` with the two pull-down menus. 

.. note::

    If fields are left empty, they will be filled in automatically. For example, the **File Name** is derived from the current project name.

If you wish to start reconstruction directly after the scan is finished check the corresponding box, **Run Feldkamp**. 
You may set the parameters for Feldkamp on the second page. Press the :guilabel:`Run` button on either one of the three pages when finished with the settings. 
If you choose not to check the **Run Feldkamp** box before starting the simulation you may initiate reconstruction manually (see: :ref:`Feldkamp <FeldkampSubsection>`). 
Click on the :guilabel:`Show` button when the simulation is finished to see the tomogram in the scene. 

.. hint::
    
    For an improved view of the reconstruction result deactivate the part or minimize its opacity (**Parameter Panel** → **Setup** → **Assembly List**).

.. _AdvancedSubsubsection:

Advanced
^^^^^^^^

By marking **Only selected objects** you can exclude parts from moving during CT simulation. 
This means that only the selected objects rotate and the others do not. 

.. note::

   To do this, you should select the corresponding components in the :ref:`Parameter Panel <ParameterPanel>` beforehand. Select a single object by clicking on it. 
   Select two or more by holding down the :kbd:`Ctrl` key and clicking on the other components to be included in the CT simulation. 
   The components are selected when they are highlighted in blue.

* **Direction** is used to choose between clockwise or counterclockwise direction.
* **Scattering** is used to control the scattered radiation simulation, where "as configured" uses the general settings (**Parameter Panel** → **Scattering**) as they are, and "force McRay" overrides the general settings to enable Monte Carlo scatter-simulation.
* **Interval [°]** sets the interval for using the same scatter image (to save computing time by not recalculating the scatter contribution for each projection).
 
.. _FeldkampSubsection:

Feldkamp
--------

This tap :guilabel:`Feldkamp` (:numref:`modules-cttfeldk`) presents the parameters for the CT reconstruction. 
You may start the reconstruction manually by pressing the :guilabel:`Reconstruct` button in the lower half of the :guilabel:`Feldkamp` page. But generally there is no need to start the reconstruction manually as there is the **Run Feldkamp** check box on the :guilabel:`Setup` page to start the reconstruction automatically after the necessary data has been acquired. 

.. _OptionsSubsubsection:

Options
^^^^^^^

**File name** specifies the file in BAM CT format with the projection data to be processed.

Enable or disable **Interpolation** or/and the **Use of GPU**, with **Use multiple textures** or/and **Use half precision**.

.. _OutputFeldSubsubsection:

Output
^^^^^^

**File name** will show the path of the output file, which is derived from the path of the projection date file.

You can choose between different **File type**: :class:`BAM CT`, :class:`VTK`, and :class:`RAW` as :class:`8bit`, :class:`16bit`, :class:`32bit` or :class:`float`.

.. _modules-cttfeldk:
.. figure:: pictures/modules-cttfeldk.*
    :alt: Feldkamp
    :width: 71.3%

    CtScan: Parameters for reconstruction.

.. _VolumeViewSubsection:

Volume View
-----------

This tab :guilabel:`Volume View` (:numref:`modules-cttvv`) contains the parameters to control the vizualization of the reconstructed volume.
When the :guilabel:`Show` button is enabled, the reconstructed volume is rendered in the scene view as well as an orthogonal slice of the volume is displayed in the :ref:`Image Viewer <ImageViewerSection>`.
 
**File** specifies the volume data to read in. Supported file types are: :code:`.bd` (BAM CT), :code:`.raw`, :code:`.bin`, and :code:`.vtk`.

The following settings for the Volume View are available:

* **Minimum**, **Maximum**, **Level**, and **Contrast** are controls for the opacity of the volume view.
* **Use 3D texture** provides an alternative view mode.

Press the :guilabel:`Show` button to read in the volume data. This may take a few seconds. 

With the **Slice View** → **Show plane** option, the slice shown in the image viewer is additionally visualized in the scene. Additional controls are available for selecting the slice to be displayed. Select an **axis** and move the slider accordingly.

The **Positioning** controls are used to define the **Position** of the voxel packet center in the scene and the **Spacing** (size) of the voxels.

.. _modules-cttvv:
.. figure:: pictures/modules-cttvv.png
    :alt: Feldkamp
    :width: 71.3%

    CtScan: Parameter for volume rendering.