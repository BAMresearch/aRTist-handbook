.. include:: _templates/icons.rst

.. _SourcePanelSection:

Source Panel
============

The :guilabel:`Source` tab of Parameter Panel is important for defining the radiation source settings.

The default setting (:numref:`guiSourceDefault`) of the source is a monochromatic point source with a voltage of 150kV. 
In addition, the graphical display is preselected as well as an **exposure** of **1mA or 1GBq**.

.. _guiSourceDefault:
.. figure:: pictures/gui-parameterP-SourceDefault.png
    :alt: Default settings from the Source
    :width: 41.3%

    Default settings from the Source.

.. _SourceSpectrumSubSection:

Source Spectrum
---------------

The main area of this page displays the source spectrum (:numref:`guiSourceSpectrum1`).

.. _guiSourceSpectrum1:
.. figure:: pictures/gui-parameterP-source_spectrum1.jpg
    :alt: Source spectrum
    :width: 41.3%

    Source spectrum.

Top:
^^^^

* |16x16_document-save-as| Save spectrum graph or data as a .txt file.
* Choose between :guilabel:`Graph` or :guilabel:`Text` via tabs

Bottom:
^^^^^^^

* Enable/Disable **log x, log y, Lines, Grid** via checkboxes.
* |22x22_document-open-folder| Spectrum from |artist| library. You can choose from four different spectra: Co-60, Ir-192, Se-75, Yb-169.
* |22x22_document-save-as| Save current spectrum as a :code:`.xrs` file.
* |22x22_xray-tube| Calculate x-ray tube spectrum opens the Spectrum calculator where you can make detailed adjustments to the tube. Important details of the current tube settings are displayed directly above the Graph/Text tabs. A more in-depth explanation of the spectrum calculator can be found in the :guilabel:`Tools` → :ref:`Spectrum <SpectrumSection>` section of this tutorial.
* |22x22_plot-spectrum| Show current spectrum opens the current spectrum in a seperate window. Click and hold for a second or right-click for more options (**Show original spectrum, Show reduced spectrum or Show preview spectrum**).
* |22x22_show-attenuation| Plot attenuation data displays the attenuation data for the current settings. In the separate section of this tutorial :guilabel:`Tools` under :ref:`Attenuation Data <AttenuationDataSection>` more information can be found.
* |22x22_edit-pickposition| Show attenuated spectrum for picked position opens the Spectrum Picker. The incident beam is shown in black, the attenuated beam in blue (:numref:`guiSpectrumPicker`). You can dock the window in the docking area.

.. _guiSpectrumPicker:
.. figure:: pictures/gui-parameterP-spectrumpicker.jpg
    :alt: Source spectrum
    :width: 41.3%

    Spectrum Picker.

* |16x16_edit-pickposition| Pick image position to calculate attenuation for is used to pick a spectrum reference position in :ref:`Image Viewer <ImageViewerSection>` (click with the left mouse button and hold). Alternatively, you may put in the X- and Y- coordinates manually. The beam shown in :numref:`guiSpectrumPicker` is attenuated by an aluminum cube.
* |16x16_document-save-as| Save current data as a :code:`.txt` file.
* |16x16_aRTist| Recalculate attenuation data

.. _ExporeSubsection:

Exposure
--------

Enter the tube current in mA, or the activity in GBq if you want to use a radionuclide (:numref:`guiParameterPExposure`).
Open the Activity calculator (|16x16_activity-calculator|) to determine a actual activity from a reference activity in the past.

.. _guiParameterPExposure:
.. figure:: pictures/gui-parameterP-exposure.jpg
    :alt: Exposure by radionuclide
    :width: 41.3%

    Exposure by radionuclide.

|22x22_activity-calculator| Activity Calculator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. |gui-parameterP-activityCcalc1| image:: pictures/gui-parameterP-activity_calc1.jpg

* |gui-parameterP-activityCcalc1| Pick reference and exposure dates - « »: year, < >: month. To enquire the present-day activity, you may simply press the :guilabel:`Today` button in the lower part of the window.
* Put in **activity** in [GBq] or [Ci] and **halflife** in [s]. You may also :guilabel:`Convert` to the respective alternative unit.
* Press :guilabel:`Set` to apply changes.
  
.. _guiparameterPActivityCalc:
.. figure:: pictures/gui-parameterP-activity_calc.jpg
    :alt: Activity Calculator
    :width: 41.3%

    Activity Calculator.

.. _FocalSpotSubsection:

Focal spot
----------

Select number and arrangement of focal spot samples from the list or enter your own values (:numref:`guiparameterPFocalSpot`). 
A single integer denotes the number of samples randomly distributed by poisson disk sampling algorithm (weighted by focal spot image if this has been set). 
An entry of the form NxM denotes a regular grid. Geometric unsharpness is negligible. A 5 point source is sufficient to check for possible unsharpness.

**X, Y**: Size of focal spot along X, Y in [mm]. 

 
.. attention::

   This is the overall size, or extent, of the focal spot. If a profile image is used, the effective spot size may be smaller.

.. _guiparameterPFocalSpot:
.. figure:: pictures/gui-parameterP-focal_spot.jpg
    :alt: Focal spot settings
    :width: 41.3%

    Focal spot settings.

|22x22_smooth| Create a spot profile image opens the Focal Spot Profile dialog box.

    Set the Focal Spot Profile (:numref:`guiparameterPFocalSpot5`):

      * effective spot **Width** in mm, :abbr:`FWHM (Full Width at Half Maximum)` of horizontal profile
      * effective spot **Height** in mm, :abbr:`FWHM (Full Width at Half Maximum)` of vertical profile
      * Lorentz **Fraction** of pseudo Voigt profile. The range is from :class:`0.0` (Gaussian profile) to :class:`1.0` (Lorentzian profile). The numbers in between are mixtures of both profiles.
      * pixel dimension of spot profile image (**Resolution**)

 .. |gui-parameterP-focal_spot2| image:: pictures/gui-parameterP-focal_spot2.jpg
 .. |gui-parameterP-focal_spot3| image:: pictures/gui-parameterP-focal_spot3.jpg
 .. |gui-parameterP-focal_spot4| image:: pictures/gui-parameterP-focal_spot4.jpg

.. _guiparameterPFocalSpot5:
.. figure:: pictures/gui-parameterP-focal_spot5.jpg
    :alt: Focal Spot Profile settings
    :width: 31.3%

    Focal Spot Profile settings.

|gui-parameterP-focal_spot2| Load spot profile image from file: Supported files: :code:`.tif`, :code:`.tiff`, :code:`.raw`, :code:`.bin`, :code:`.fld`, :code:`.png`, :code:`.bd`, :code:`.dd`.

|gui-parameterP-focal_spot3| Delete spot profile image

|gui-parameterP-focal_spot4| Show spot profile image