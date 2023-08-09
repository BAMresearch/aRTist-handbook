.. include:: _templates/icons.rst

.. _SpectrumSection:

|32x32_xray-tube| Spectrum
==========================

The **Spectrum calculator** offers specific settings for the radiation source . 
When you open the spectrum calculator, here for a monochromatic radiation source (:numref:`tools-spectruMono`), the following window appears:

.. _tools-spectruMono:
.. figure:: pictures/tools-spectrumcalculatorMono.png
    :alt: Spectrum calculator, start window
    :width: 50.3%

    Spectrum calculator, start window.

To see the advanced settings from :numref:`tools-spectruMono`, select :class:`General` under **Tube**. 
More settings appear, which can be seen in :numref:`tools-spectru` on the left-hand side. With these setting an X-ray tube can de defined. 
The schematic drawing on the right side of :numref:`tools-spectru` only appears if the **Show principle** checkbox is marked.

.. hint::
    It can also be opened from the Parameter Panel → :guilabel:`Source` → |16x16_xray-tube|. 
    You may dock with |16x16_window-undock| the Spectrum calculator in the docking area.



.. _SpectrumSettingSubSection:

Settings
--------
On the upper left side of :numref:`tools-spectru` you will find the **Settings**. 
You can select the **Tube**, i.e., the radiation source, between :class:`Mono` and :class:`General` and set the **voltage (kV)** and **resolution (keV)**. **Resolution** sets the size of the energy bins, with which the source spectrum will be calculated. 
You can also set the **filter material** and **thickness (mm)**. The following **window materials** are available in the standard distribution of |artist|:
:class:`Al`, :class:`Be`, :class:`Cu`, :class:`Fe`, :class:`Mg`, :class:`Mo`, :class:`Ni`, :class:`Pb`, :class:`Pt`, :class:`Ti`, :class:`W`, :class:`air`, :class:`water`, and :class:`VOID`. Additional materials can be defined with the :ref:`Materials <Tools-materials>` tool. 

    .. |gray-savebutton| image:: pictures/gray-savebutton.png
    .. |gui-parameterP-focal_spot3| image:: pictures/gui-parameterP-focal_spot3.jpg

Below the **Settings** section the follwoing buttons appear:

* |16x16_document-open| Load tube definitions from file: :code:`.dict`.
* |gray-savebutton| Save tube definition to file (hold or right-click for options).
* |gui-parameterP-focal_spot3| Delete tube definition from database.

.. note::
    
    To use no filter, :class:`VOID` must be selected or the filter thickness set to 0 mm.

.. _SpectrumTubeSettingsSubSection:

Tube Settings
-------------

Under **Tube Settings** (:numref:`tools-spectru`) you can set values for an reflection X-ray tube and adjust the **target_material**, **target thickness (mm)**, and the **target angle (deg)**, the **angle of e- incidence (deg)**, and the **window material** as well as the **window thickness (mm)**. For the angles to be set see the tube principle for reflection X-ray tubes which will be shown by marking the **Show principle** checkbox in the bottom row. The **windows material** can be selected from the drop-down menue showing all available materials. As mentiond above, additional materials can be defined with the :ref:`Materials <Tools-materials>` tool.

.. note::
    
    If only the **target angle (deg)** is set but the **angle of e- incidence (deg)** not, the **angle of e- incidence (deg)** will be set automatically that way, that the sum of both angles is equal to 90°.

It is also possible to simulate the spectrum of a transmission X-ray tube. For this mark the **Transmission** checkbox. The tube principle will be updated and the **target angle (deg)** and the **angle of e- incidence (deg)** automatically be set to 90°. 

Press the :guilabel:`Compute` button in the lower part of the window to apply changes when finished and to calculate the X-ray tube spectrum for the choosen settings.

.. _tools-spectru:
.. figure:: pictures/tools-spectrumcalculator.png
    :alt: Spectrum calculator
    :width: 100%

    Spectrum calculator.

.. hint::
    
    If the tube voltage is set larger :class:`128 kV`, a window will appear with the note: 
    
    “This spectrum contains 150 spectrum entries for the example above in :numref:`tools-spectru`, the currently recommended value is 128. Reduce?” 

    The reduction of the number of spectrum entries yields to a reduction of the calvulation time.
    
    It can be choose between :guilabel:`Yes` or :guilabel:`No`.
    
    By selecting :guilabel:`Yes`, you can see a reduced spectrum at the Parameter Panel → :guilabel:`Source` → **Source spectrum** (see :ref:`Source Panel <SourcePanelSection>`). Keep holding the left-click on the mouse or right-click the symbol |16x16_plot-spectrum|. There you can open **Show original spectrum**, **Show reduced spectrum** or **Show prewiew spectrum** to see the different spectrums (:numref:`tools-spec`). 
    
    By selecting :guilabel:`No`, the spectrum is not reduced to 128 entries (preset value) and will stay as the original spectrum. 
    If needed, it is possible to change the number of reduced spectrums bin at :guilabel:`Tools` → |16x16_preferences-system| **Settings** → :guilabel:`Advanved`.

.. _tools-spec:
.. figure:: pictures/tools-spec.png
    :alt: Spectrum calculator
    :width: 25.3%

    Spectrum selection.

