.. include:: _templates/icons.rst

.. _DetectorCalcSection:

DetectorCalc
============

.. 3.4	DetectorCalc (incl. menu description)

The DetectorCalc module opens the Detector calculator (:numref:`detectorcalcSettingsgeneral`). It is useful for the detector's flat panel settings and calculating the captured photons. 
In addition to the more general DetectorCalc there is a simplified detector calculator: :ref:`DigRad <DigRadSection>`.

.. _detectorcalcSettingsgeneral:
.. figure:: pictures/modules-artist-detectorcalc-settings.png
    :alt: Detector calculator, Settings
    :width: 60.3%

    Detector calculator, Settings.

.. _DetectorCalcGeneralSettingsSubSection:

General Settings
^^^^^^^^^^^^^^^^

Set the general settings for your new detector:

* **Name**
* **Pixel size (mm)**
* **Pixel count X**
* **Pixel count Y**
* **Maximum grey value**
* **Grey value quantum (GV)**

.. _DetectorCalcGeneralSensitivitySubSection:

Sensitivity
^^^^^^^^^^^

Set the sensitivity for your new detector:

* **Material**
* **Thickness (mm)**
* **Steps**
  
The amount of Steps are relevant for the layer model. The more steps you set, the more accurate the simulation will be. 
Thereby the execution time will increase. Typically two steps will be enough.

* **Min Energy (keV)**
* **Max Energy (keV)**
* **Signal Type**
  
.. _DetectorCalcGeneralFiltrationSubSection:

Filtration
^^^^^^^^^^

It is possible to add a filtration over the new detector.

        |16x16_list-add| Click on the green button to add a filter (default filter is Al with 1.0 mm thickness).

        |16x16_edit-delete| Click on the red button to delete a selected filter.

If you want to change the settings of your filtration, click on the corresponding Material or Thickness. For the Material column you can choose a material of the editor list 
(:guilabel:`Tools` → |16x16_edit-materials| **Materials**). For Thickness just enter your desired value (in mm).

The column Active enables to activate (Yes) or deactivate (No) the selected filter. Therefore use the left mouse button to choose Yes or No.
Press OK to apply or Cancel to quit these settings.

Reference shot
^^^^^^^^^^^^^^

For creating a new detector it is necessary to set reference values. With those, the new detector will be calibrated (with available detector settings) and considered for calculations.

.. _detectorcalc-exposure:
.. figure:: pictures/modules-artist-detectorcalc-exposure.png
    :alt: Detector calculator, Exposure
    :width: 60.3%

    Detector calculator, Exposure.

.. _DetectorCalcReferenceshotSubSection:

Set the reference values for your new detector:

* **Spectrum**
* **Current (mA)**
* **Exposure time (s)**
* **Number of frames**
* **Distance (mm)**
* **Long range unsharpness (mm)**
* **Unsharpness ratio (%)**
* **Grey value**
* **SNR unnormalized**
  
 Afterwards the new detector can be loaded and applied at **Parameter Panel** → **Detector** → **Characteristic** → **detector type** → **Extern**.