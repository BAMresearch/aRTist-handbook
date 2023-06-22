.. include:: _templates/icons.rst

.. _DigRadSection:

DigRad
------

The **DigRad** module can be used to generate new detector modells for a CR (Computed Radiography) systenm or a DDA (Digital Detectr Array). The input parameters are related to the standarts for detector characterisation (ASTM E 2445, ASTM E 2597, ISO 16371-1).

.. _DigRadcalculator:
.. figure:: pictures/modules-digrad1.jpg
    :alt: DigRad calculator
    :width: 60.3%

    DigRad calculator.
    
* **Pixel size (mm)**
* **Basic spatial resolution SRb (mm)** The double SRb is used as unsharpness of the aRTist detector model.
* **Internal scatter radiation ISR (%)** Scattered radiation within the detector. The percentage can be determined on an edge profile (:numref:`DigRadEdgeProfile`).
* **ISR correlation length (mm)** The double correlation length is used as long range unsharpness of the aRTist detector model (:numref:`DigRadEdgeProfile`).
* **Gray response (GV/mGy)**
* **SNRn,max**
* **Efficiency (SNRn/mGy^0.5)**

.. _DigRadEdgeProfile:
.. figure:: pictures/modules-digrad-edge_profile.*
    :alt: Edge profile indicating internal scatter radiation
    :width: 100.0%

    Edge profile indicating internal scatter radiation. Simulation of an edge penetration with a DigRad detector model with 5 % ISR and 5 mm correlation length. Right: Edge profile with reading of the ISR measurands (ISR = (2 * a / b) * 100 %; correlation length = c).
