.. include:: _templates/icons.rst

.. _DigRadSection:

DigRad
------

The **DigRad** module (:numref:`DigRadcalculator`) can be used to generate new detector modells for a CR (Computed Radiography) systems or a DDA (Digital Detector Array). The **DigRad** module is a simplified detector model compared to the model used in the :ref:`DetectorCalc <DetectorCalcSection>` module. The input parameters are related to the standards for detector characterisation (ASTM E 2445/E 2445M:2020 *Standard Practice for Performance Evaluation and Long-Term Stability of Computed Radiography Systems*, ASTM E 2597/E 2597M:2022 *Standard Practice for Manufacturing Characterization of Digital Detector Arrays*, and DIN EN ISO 16371-1:2011 *Non-destructive testing — Industrial computed radiography with storage phosphor imaging plates — Part 1: Classification of systems*).

.. _DigRadcalculator:
.. figure:: pictures/modules-digrad1.jpg
    :alt: DigRad calculator
    :width: 60.3%

    DigRad calculator.
    
* **Pixel size (mm)** to set the pixel size of the detector.
* **Basic spatial resolution SRb (mm)** to set the basic spatial resolution (SRb) of the detector, measured according to ASTM-E2002 - 2022 *Standard Practice for Determining Image Unsharpness and Basic Spatial Resolution in Radiography and Radioscopy* or DIN EN ISO 19232-5:2018 *Non-destructive testing — Image quality of radiographs — Part 5: Determination of the image unsharpness and basic spatial resolution value using duplex wire-type image quality indicators*.

.. note::

    The basic spatial resolution (SRb) of an X-ray detector is usually larger than the pixel size. Two times the SRb gives the inner unsharpness of the detector. 

* **Internal scatter radiation ISR (%)** to set the internal scatter radiation ISR (%) describing the scatter radiation within the detector. The percentage can be determined from an edge profile (:numref:`DigRadEdgeProfile`).
* **ISR correlation length (mm)** to set the the ISR correlation length applying only for imaging plates and flat panel detectors. 

.. note::
    Two times the ISR correlation length gives the long range unsharpness of the aRTist detector model. The ISR correlation length can be determined from an edge profile (:numref:`DigRadEdgeProfile`).

* **Gray response (GV/mGy)** to set the gray response given in GV/mGy.
* **SNRn,max** to set the maximum normalilzed signal to noise ratio.
* **Efficiency (SNRn/mGy^0.5)** to set the detector efficiency given in SNRn/mGy^0.5.

.. _DigRadEdgeProfile:
.. figure:: pictures/modules-digrad-edge_profile.*
    :alt: Edge profile indicating internal scatter radiation
    :width: 100%

    Edge profile indicating internal scatter radiation. Simulation of an edge penetration with a DigRad detector model with 5 % ISR and 5 mm correlation length. Right: Edge profile with reading of the ISR measurands (ISR = (2 * a / b) * 100 %; ISR correlation length = c).
