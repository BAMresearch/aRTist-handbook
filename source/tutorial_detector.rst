.. include:: _templates/icons.rst

.. _detectorTutorialChapter:

Detector
========

This tutorial explains the basics of |artist|'s virtual detector and how to use the *DetectorCalc* module to calculate characteristics for scintillator-based flat panel detectors.

We do not continue with the project file from the last tutorial, but will start with a fresh new |artist| scene.

.. note:: If you still have the previous project loaded in |artist|, choose :guilabel:`File` → :guilabel:`New Project` from the menu to create a new, empty project.


An Example Scene
----------------

In this tutorial, we will reproduce an example projection image taken with a real CT scanner. It is an image of a PMMA step cylinder (:numref:`PMMAcylinderOriginalProjection`). To follow the steps, you can download a package that contains the projection images (in TIFF format) and the STL file for the surface model of the cylinder that we will use in |artist|:

:download:`detector_tutorial_additional_data.zip <files/detector_tutorial_additional_data.zip>` |nbsp| (5.8 MB)

Note that you get three projection images: a free-beam flat field image, a "raw" projection image of the step cylinder, and a flat-field corrected projection image. All three images are already dark-field corrected (i.e. the grey value at zero intensity is also zero). This makes it easier for us to build the detector in |artist|.

.. _PMMAcylinderOriginalProjection:
.. figure:: pictures/tutorial-detector-PMMA-cylinder-original-projection.jpg
    :width: 100%
    
    \(a\) Raw projection image of the PMMA step cylinder, (b) free-beam flat field image and (c) flat-field corrected projection image. All three images are already dark-field corrected.

.. _PMMAcylinderGeometry:
.. figure:: pictures/tutorial-detector-cylinder-setup.png
    :width: 100%

    Geometry used to acquire the example projection image.

The CT geometry shown in :numref:`PMMAcylinderGeometry` was used to acquire the projection image. The first step we will take is to reproduce this geometry in |aRTist|.

.. note:: 1. Set the :guilabel:`Z` position of the source to :code:`500` |nbsp| mm.
    2. Make sure that |32x32_center-new| :guilabel:`Center new parts` is turned off in the toolbar. Our cylinder surface model already comes with the correct coordinates. Otherwise, you will have to place the cylinder yourself (see next step).
    3. Open the file :code:`PMMA_Cylinder.stl` from the downloaded package of additional data for this tutorial, or drag and drop it into the |artist| window. It should appear at a :guilabel:`Z` position of 350 |nbsp| mm (the ODD). If not, set the :guilabel:`Z` position manually.
    4. Create a new material called *PMMA* (:numref:`PMMAcylinderMaterial`). Its chemical composition is C\ :sub:`5`\ H\ :sub:`8`\ O\ :sub:`2`, it has a density of 1.19 |nbsp| g/cm\ :sup:`3`. Use the |22x22_edit-materials| *materials editor* and don't forget to click :guilabel:`Apply` before closing it.
    5. Assign the new *PMMA* material to the step cylinder in the *Assembly List*.

    Your scene should now look like in :numref:`PMMAcylinderVirtualScene01`.

.. _PMMAcylinderMaterial:
.. figure:: pictures/tutorial-detector-PMMA-material-properties.png
    :width: 50%

    PMMA material properties for the virtual step cylinder.

.. _PMMAcylinderVirtualScene01:
.. figure:: pictures/tutorial-detector-cylinder-virtual-scene-01.png
    :width: 100%

    We have prepared the basic CT geometry and material properties. We will take care of the detector size later.


Pixels & Size
-------------

Let's take a look at the detector configuration.

.. note:: Switch to the *Detector* tab in the parameter panel (:numref:`detectorGeometryPanel01`).

.. _detectorGeometryPanel01:
.. figure:: pictures/tutorial-detector-geometry-panel-01.png
    :width: 50%

    The default geometry parameters of the detector.

In the :guilabel:`Geometry` section, we can set up the detector's size, its number of pixels, and the pixel size (resolution). Each of these three parameters is coupled to the other two:

.. math::
    \textsf{Size~[mm]} = (\textsf{Number~of~Pixels}) \cdot (\textsf{Resolution [mm]}).

In the upper row, you can choose which one |artist| should calculate from the other two.

.. note:: Select :guilabel:`Size [mm]`, |artist| should calculate it for us. We will enter the following two other parameters, which we know (:numref:`detectorGeometryPanel02`).

    * :guilabel:`Pixel`: :guilabel:`X`: :code:`1200`, :guilabel:`Y`: :code:`1400`
    * :guilabel:`Res. [mm]`: :guilabel:`X`: :code:`0.2`, :guilabel:`Y`: :code:`0.2`

The detector size is calculated automatically. You should now see a preview image that contains the complete step cylinder (:numref:`PMMAcylinderVirtualScene02`).

.. _detectorGeometryPanel02:
.. figure:: pictures/tutorial-detector-geometry-panel-02.png
    :width: 50%

    The detector's geometry parameters for our projection image.

.. _PMMAcylinderVirtualScene02:
.. figure:: pictures/tutorial-detector-cylinder-virtual-scene-02.png
    :width: 100%

    The detector has the correct size now.

Note that you can set :guilabel:`Multisampling` for each pixel. It works in the same way as for the source. If you activate a certain type of pixel multisampling, a ray will be simulated connecting each source point with each pixel point (or subpixel). As described for the :ref:`Spot Type in the Source tutorial <sourceTutorialSpotChapter>`, you can define regular subpixel grids (e.g. :code:`3x3`) or quasi-random patterns using Poisson Disc Sampling (any integers, e.g. :code:`11`). The number of rays that will be simulated per pixel is the product of the source spot multisampling points and the detector (pixel) multisampling points. If you choose :guilabel:`source dependent` for the pixel multisampling (the default setting), the pattern defined for the source will also be used for each pixel (with the exception that it will be flipped in both spatial directions compared to the source pattern). Each spot point is then connected to its corresponding point on the pixel: the number of rays per pixel will remain the number of spot points and will not multiply (:numref:`DetectorPixelMultisampling`).

.. _DetectorPixelMultisampling:
.. figure:: pictures/QuickStartCT_DetectorMultisamplingGrid.*
	:width: 80%

	Overview of the multi-sampling behavior for different source-detector combinations.

The :guilabel:`Curvature` is an experimental feature that can be used to simulate detectors that are curved in a certain direction of space. A possible application could be the simulation of medical CT, but this feature will not be covered here.

Characteristic
--------------

The function that assigns a grey value to the energy density at a pixel is called the *Characteristic*. The default detector in |artist| is the so-called 1:1 detector. It converts all energy that arrives at a pixel linearly into grey values without losses. Let's take a closer look at the *Characteristic* of the 1:1 detector.

.. note:: 1. Make sure that :guilabel:`1:1` is selected as the :guilabel:`detector type`.
    2. From the menu bar, choose :guilabel:`Tools` → :guilabel:`Detector Properties`. The *DetectorViewer* will open in a new window (:numref:`detectorViewer1to1`).

.. _detectorViewer1to1:
.. figure:: pictures/tutorial-detector-detector-viewer-1to1.png
    :width: 100%

    The *DetectorViewer* displays the *Characteristic* curve of the 1:1 detector.

As you can see, the input unit of the 1:1 detector is the energy density (in J/m\ :sup:`2`), the same as the output unit. This means that a pixel in the projection image will have a grey value that directly corresponds to the energy density at the pixel. The result is a purely linear function. This is a very simple *Characteristic*, but it helps us understand what is going on.

.. note:: Close the DetectorViewer.

When you take a look at the preview image (:numref:`imageViewer1to1`) you will notice that the *Image Viewer* displays the energy density at the detector as a map of grey values. When you move your mouse around the image, the energy density will be displayed as a floating point number. They look suspiciously like "real" grey values, but note that "real" grey values are usually integers. In the *Image Viewer*, you can switch the image between :guilabel:`primary intensities` and the :guilabel:`Energy density (J/m²)`. In terms of visible grey values they are the same, but they represent different physical quantities and are connected by the integration time τ:

.. math::
    \textsf{Energy~density} \left[ \frac{\textsf{J}}{\textsf{m}^2} \right] = \textsf{primary intensity} \left[ \frac{\textsf{J}}{\textsf{s}\cdot\textsf{m}^2} \right] \cdot \tau \left[ \textsf{s} \right].

.. _imageViewer1to1:
.. figure:: pictures/tutorial-detector-image-viewer-1to1.png
    :width: 65%

    The *Image Viewer* displays the energy density at the detector as grey values.


Exposure
--------

The energy density at each pixel depends on the integration time τ. In the current standard settings of the detector (:numref:`detectorExposureSettings`), the integration time is automatically calculated such that the brightest point in the image (point of maximum exposure) will reach an energy density of 50000 |nbsp| J/m². You can see this in the *display range* in :numref:`imageViewer1to1`. To reach such a high energy density, a simulated integration time of more than 11000 weeks is necessary. This might seem confusing, but it is simply the result of the purely linear 1:1 characteristics. In the following section we will build a detector with a grey value characteristic that associates higher grey values with smaller energy densities and therefore reaches realistic integration times.

.. _detectorExposureSettings:
.. figure:: pictures/tutorial-detector-exposure-settings.png
    :width: 50%

    Exposure settings.

Instead of the maximum intensity, you can set a different :guilabel:`reference point` where the expected grey value should be reached. You can also turn off the reference point and enter the :guilabel:`exposure time` manually.


Realistic Detectors
-------------------

The pre-defined detectors in |artist| are usually not of interest if you are trying to reproduce a realistic flat panel CT detector. In the following example, we will reproduce the real-world projection image of the step cylinder and create our own detector using the *DetectorCalc* module. 

Spectrum and Current
~~~~~~~~~~~~~~~~~~~~

We already set the scene geometry and the material of the PMMA cylinder correctly. Before we can take care of the detector, we need to simulate the spectrum and the tube current that were used to take the projection image.

.. note:: Switch to the :guilabel:`Source` parameters and use the |22x22_xray-tube| *Spectrum Calculator* to generate a spectrum with the following parameters: we need a general tube at **130 kV** with a **tungsten (W) reflection target** (45° target and incidence angle), a **0.5 mm Be window** and a **0.1 mm Cu filter** (:numref:`detectorSpectrumCalculator`).
	
	Press |16x16_compute-run| :guilabel:`Compute` to calculate the spectrum, then close the *Spectrum Calculator*.

.. _detectorSpectrumCalculator:
.. figure:: pictures/tutorial-detector-spectrum-calculator.png
    :width: 50%

    Settings to reproduce the X-ray tube spectrum that was used to take the projection image.

You should now see the spectrum shown in :numref:`detectorSourceSettings`. We still need to set the current of 100 |nbsp| µA that was used for the real-world tube when the projection image was taken.

.. note:: For :guilabel:`exposure [mA or GBq]` enter :code:`0.1`. (The unit is mA, :numref:`detectorSourceSettings`).

.. _detectorSourceSettings:
.. figure:: pictures/tutorial-detector-source-settings.png
    :width: 50%

    We calculated a spectrum that matches the real-world tube parameters that were used to take the projection image.

We will need this spectrum as an :code:`.xrs` file later when creating our new detector.

.. note:: Underneath the spectrum graph, click |22x22_document-save-as| to save the current spectrum as an :code:`.xrs` file at a location of your choice. (We will need this file later in the tutorial.)

When you switch back to the *Detector* parameters, you will see that the exposure time dropped from more than 11000 weeks to "just" 5 |nbsp| weeks to reach the 50000 |nbsp| J/m² at the point of maximum intensity (:numref:`detectorExposureSettings02`). Our new tube and current obviously lead to a much higher flux at the detector.

.. _detectorExposureSettings02:
.. figure:: pictures/tutorial-detector-exposure-settings-02.png
    :width: 50%

    The exposure time dropped to "just" 5 weeks with our new tube settings.


DetectorCalc
~~~~~~~~~~~~

We have now prepared everything to build our new detector using the *DetectorCalc* module. This module's purpose is to generate realistic sensitivity, noise and grey value response curves for a given X-ray spectrum and scintillator material.

.. note:: From the menu bar, open :guilabel:`Modules` → :guilabel:`DetectorCalc` (:numref:`detectorCalcSettings`).

.. _detectorCalcSettings:
.. figure:: pictures/tutorial-detector-detectorcalc-settings.png
    :width: 50%

    We describe our general detector settings in the *DetectorCalc* module.

In the *General* section, we enter the obvious parameters of our detector: its size, number of pixels, grey value dynamics and we will give it a name.

.. note:: 1. Give your detector any :guilabel:`name` you like. In this example, we called it the :code:`Step Cylinder Detector`.
	2. Enter the :guilabel:`pixel size`: :code:`0.2` |nbsp| mm.
	3. Enter the :guilabel:`Pixel count X`: :code:`1200` (the width of our projection image).
	4. Enter the :guilabel:`Pixel count Y`: :code:`1400` (the height of our projection image).
	5. :guilabel:`Maximum grey value`: :code:`65535` (i.e. a 16 bit detector).
	6. :guilabel:`Grey value quantum`: :code:`1` (the detector's output are integer grey values in steps of 1).

The next section is called *Sensitivity*. It asks for the detector parameters relevant to its spectral absorption characteristics, namely the scintillator properties. The detector that was used to capture the projection image has a CsI scintillator with a thickness of 150 |nbsp| µm.

.. note:: If CsI is not yet in your materials list, you need to create it using the |22x22_edit-materials| *Materials Editor* (:numref:`detectorMaterials`). You can leave the *DetectorCalc* window open while doing this.

	* Material: :code:`CsI`,
	* Density: :code:`4.51` g/cm³,
	* Composition: :code:`CsI`.

	We also create a material for the carbon fibre in front of the detector. It serves as a protection and (slightly) filters the radiation:

	* Material: :code:`Carbon`,
	* Density: :code:`1.8` g/cm³,
	* Composition: :code:`C`.

.. _detectorMaterials:
.. figure:: pictures/tutorial-detector-materials.png
    :width: 50%

    If they are not yet in your list of materials, you will have to add CsI for the scintillator and Carbon for the protective layer.

We can now set the sensitivity and filtration properties in the *DetectorCalc* module.

.. note:: 1. For the (scintillator) :guilabel:`Material`, choose :code:`CsI`.
	2. For its :guilabel:`Thickness`, set :code:`0.15` mm.
	3. Leave the :guilabel:`Steps` at :code:`2`. This parameter is used in the X-ray generation model and gives the maximum number of consecutive interactions to be simulated.
	4. :guilabel:`Min Energy`: :code:`0`.
	5. :guilabel:`Max Energy`: :code:`Infinity`.
	6. :guilabel:`Signal Type`: :code:`Average Energy`. (Common flat panel detectors are energy-integrating devices, this is what the *average energy* signal type does.)
	7. Add the 0.5 mm Carbon filter to the filtration list.

	(See :numref:`detectorCalcSettings`.)

Reference Exposure
~~~~~~~~~~~~~~~~~~

So far, those are the general properties of the detector. Now we need to switch over to the *Exposure* tab (:numref:`detectorCalcExposure`) and provide reference measurements from the projection image that we try to reproduce. *DetectorCalc* will use those reference values to calculate matching characteristics curves, as we will see later.

.. _detectorCalcExposure:
.. figure:: pictures/tutorial-detector-detectorcalc-exposure.png
    :width: 50%

    In the exposure settings, we will enter reference values that we have measured in our real-world projection images.

The first section, called :guilabel:`Reference exposure settings`, asks for the general circumstances under which the reference image was taken.

.. note:: 1. For the :guilabel:`Spectrum`, select the :code:`.xrs` spectrum file that you saved after we generated the X-ray spectrum.
	2. The image was taken at a tube :guilabel:`current` of :code:`0.1` |nbsp| mA.
	3. The :guilabel:`exposure time` for the image was :code:`0.5` |nbsp| s.
	4. You need to specify the :guilabel:`Number of frames` that have been averaged for the reference image. This is taken into account for the noise characteristics. If you do not intend to simulate any different frame averaging than the one from the reference image, it is advisable to pretend that the number of frames has been :code:`1`. More about the details of frame averaging is explained later.
	5. The :guilabel:`Source detector distance` was :code:`500` |nbsp| mm.
	6. Keep :guilabel:`Filter spectrum with environment material` activated: this will take the X-ray absorption of air into account when reproducing the grey values.

*DetectorCalc* now knows the circumstances under which the reference image was taken and is able to calculate a good estimate for the primary intensity at the detector. It still needs to know how these primary intensities correspond to grey values, and also asks for the noise (SNR, signal-to-noise-ratio) in the reference image and the detector's unsharpness.

Unsharpness
~~~~~~~~~~~

|artist|'s unsharpness definition conforms to the guideline ASTM E2597/E2597M-14 where it is measured using a duplex wire standard :cite:p:`ASTME2597`. The unsharpness is achieved by treating the analytical projection image in |artist| with a Gaussian smoothing kernel. Its standard deviation :math:`\sigma_\mathsf{main}` is chosen such that the resulting unsharpness will match the mentioned guideline.

Apart from this main unsharpness, |artist| offers a second component called the *long range unsharpness*. This component becomes visible when measuring line profiles across an edge image (:numref:`detectorUnsharpnessComponents`).

.. _detectorUnsharpnessComponents:
.. figure:: pictures/tutorial-detector-unsharpness-LR-and-main.png
    :width: 100%

    The main unsharpness and the long range unsharpness have an effect on the line profile across an edge image.

|artist| uses alpha blending to combine the main unsharpness and the long range unsharpness. For a given ideal point function δ as the input, the resulting point spread function (PSF) would be

.. math::
    \mathsf{PSF} = \left[ \alpha \cdot g_\mathsf{LR} \ast \delta + (1-\alpha)\delta \right] \ast g_\mathsf{main},

with the long range ratio :math:`\alpha` (the "prominence" of the long range component), the convolution operator :math:`\ast` and the two Gaussian smoothing kernels

.. math::
    g_\mathsf{main} = \frac{1}{\sqrt{2\pi \sigma_\mathsf{main}^2}} \exp \left( -\frac{x^2}{2\sigma_\mathsf{main}^2} \right) ~~~~~\mathsf{and}~~~~~ g_\mathsf{LR} = \frac{1}{\sqrt{2\pi \sigma_\mathsf{LR}^2}} \exp \left( -\frac{x^2}{2\sigma_\mathsf{LR}^2} \right).

We will not reproduce the long range unsharpness for our detector as this will be beyond the scope of this tutorial.

.. note:: 1. For the :guilabel:`basic spatial resolution`, enter :code:`0.18` |nbsp| mm. This is an unsharpness property of the detector that is known, but cannot be deducted from the projection image of the step cylinder.
    2. For the :guilabel:`long range unsharpness` and the :guilabel:`unsharpness ratio`, enter :code:`0`. This is an advanced topic not covered here, but feel free to try it out on your own.


Grey Value & Noise
~~~~~~~~~~~~~~~~~~

*DetectorCalc* asks for a reference grey value. This is the grey value at the maximum free-beam intensity, which we can measure in the free-beam flat field image (:numref:`detectorFreeBeamGV`). For our example, we get a free-beam grey value of about 8410.

.. _detectorFreeBeamGV:
.. figure:: pictures/tutorial-detector-PMMA-cylinder-projection-freebeam-gv.png
    :width: 100%

    Measuring the reference grey value in the free-beam image.

To measure the SNR, we will use a free-beam region in the flat-field corrected image (:numref:`detectorFreeBeamSNR`). The first reason is that the flat-field corrected image is the only one where we have a homogeneous background intensity where we can measure the noise (in terms of the grey value standard deviation) without the interference of the intensity profile of the flat field. The second reason is that |artist| typically uses an ideal, noise-free flat field image for the flat-field correction, which means that we can simulate the full noise in the raw projection image and won't have to worry about noise contributions from the flat-field image. A more correct way to do this would be to measure the noise in the centre of a flat-field corrected free-beam image instead of choosing an off-centre region like in :numref:`detectorFreeBeamSNR`. However, for simplicity, we continue with this approximation.

.. _detectorFreeBeamSNR:
.. figure:: pictures/tutorial-detector-PMMA-cylinder-projection-stddev-snr.png
    :width: 100%

    Measuring the reference SNR in the flat-field corrected projection image. Note that the mean grey value does not match the previously measured maximum grey value in the flat-field image because our flat-field correction renormalizes to the *mean* intensity of the flat-field image, not its maximum value.

Enter these two reference values into the *DetectorCalc* window:

.. note:: 1. For :guilabel:`grey value`, enter :code:`8410`.
    2. For :guilabel:`SNR unnormalized`, enter :code:`615`.

We have now prepared all parameters to generate our new detector.

.. note:: Press |16x16_compute-run| :guilabel:`Run` to create the new detector. You will be asked to save the new detector as an :code:`.aRTdet` file, which is |artist|'s file format for detector descriptions. Save it where you can find it again, we will inspect the file later.

    After you created the file, the actual computation might take a while, and you might need some patience. When you are asked if you want to load the new detector definition, click :guilabel:`Yes` to import the detector file that you just generated.

The new detector is now selected as the current :guilabel:`detector type` in the parameter panel (:numref:`detectorNewImported`). We now need to switch the exposure to a fixed exposure time.

.. note:: Turn off the :guilabel:`reference point` and manually set an exposure time of :code:`0.5` seconds (:numref:`detectorNewImported`). This was the original exposure time for the real-world projection image that we used to configure *DetectorCalc*.

.. _detectorNewImported:
.. figure:: pictures/tutorial-detector-newdetector-imported.png
    :width: 50%

    The new detector is now imported. We need to set the exposure time manually.

The grey values that you will get in the preview image should now already be close to the grey values in the raw projection image.


Attenuation, Deposit & Sensitivity
----------------------------------

*DetectorCalc* has generated some characteristic curves from the given information. We can inspect them using the *DetectorViewer*.

.. note:: From the menu bar, select :guilabel:`Tools` → :guilabel:`Detector Properties`. Turn on the options :guilabel:`log x` and :guilabel:`log y` underneath the graph.

The *DetectorViewer* shows the general properties of your new detector in the left column, and a graph (or text table) of its spectral characteristics in the window's right-hand area. You can choose the :guilabel:`Curve` from the drop-down menu in the upper left section.

The first important curve is the **Attenuation** (:numref:`detectorViewerAttenuation`). In |artist|'s vocabulary, this is the probability that an incoming photon of a certain energy (keV) interacts with the scintillator (instead of just passing through).

.. _detectorViewerAttenuation:
.. figure:: pictures/tutorial-detector-detectorviewer-attenuation.png
    :width: 100%

    The *DetectorViewer* shows the attenuation curve.

Depending on the underlying physics of the particle interactions, not all photons will deposit their full energy in the scintillator in a detectable way. The second important curve is the **Deposit,** which shows the average amount of "usable" energy that a given photon would store in the scintillator in the event of an attenuation.

.. _detectorViewerDeposit:
.. figure:: pictures/tutorial-detector-detectorviewer-deposit.png
    :width: 100%

    The *DetectorViewer* shows the deposit curve.

The product of these two shown curves is called the **Sensitivity** (:numref:`detectorViewerSensitivity`). It gives the mean deposited energy (keV) in a pixel for an incoming photon of the given energy (keV). The sensitivity curve is the foundation of the detector's spectral energy characteristics and is used, together with the X-ray spectrum, the X-ray current (and overall photon flux), and the area of a pixel, to calculate the primary intensity (in J/m²/s) at the detector pixels.

.. _detectorViewerSensitivity:
.. figure:: pictures/tutorial-detector-detectorviewer-sensitivity.png
    :width: 100%

    The *DetectorViewer* shows the sensitivity curve.

To associate a grey value with the total energy density at a pixel (in J/m², accumulated from the primary intensity during the integration time), another curve is important: the **Characteristic** (:numref:`detectorViewerCharacteristic`). We have already seen it before at the 1:1 detector. For our new detector, *DetectorCalc* has generated a purely linear function which associates no incoming energy with the grey value 0. It has used the maximum free-beam intensity and our reference grey value to extrapolate a second point for the characteristic curve and associated the maximum possible grey value of 65535 (for a 16-bit detector) with its corresponding energy density.

.. _detectorViewerCharacteristic:
.. figure:: pictures/tutorial-detector-detectorviewer-characteristic.png
    :width: 100%

    The *DetectorViewer* shows the characteristic curve.


Noise
-----

The noise amplitude of a pixel is usually a function of the intensity, i.e., in |artist| a function of the energy density. One typical contribution comes from the shot noise of the X-ray source, which scales with the square root of its intensity and finally affects the grey value noise level. In *DetectorCalc*, we have defined the signal-to-noise ratio (SNR) at the maximum free beam intensity. This value was used to compute our detector's noise curve (:numref:`detectorViewerNoise`): it shows a strikingly square-rootish behaviour.

.. note:: Turn off the options :guilabel:`log x` and :guilabel:`log y` underneath the graph.

.. _detectorViewerNoise:
.. figure:: pictures/tutorial-detector-detectorviewer-noise.png
    :width: 100%

    The *DetectorViewer* shows the noise curve.

Typically, the calculated noise curve has two components: an intensity-dependent component that models the shot noise of the X-ray source, and a structural component that models static and systematic differences between the pixel grey values. An analytical value for the shot noise component is calculated from the spectrum, integration time, current and pixel area. If the SNR that you entered in *DetectorCalc* is lower than this analytical value, the remainder will be satisfied using the structural, constant noise component. If the SNR is better than the analytical value, there might be something wrong with your flux or your projection image where you measured the SNR might be filtered to remove noise. In this case, *DetectorCalc* models a purely intensity-dependent (square-root) noise characteristic and ignores its own analytical value. If this is the case, *DetectorCalc* will issue a warning that you can see in the console (:guilabel:`Tools` → :guilabel:`Show Console`).


Grey Value Reproduction
-----------------------

One way to get a better match between the real and simulated grey values is to adapt the detector's characteristics curve. To do so, we need to create a table that lists some simulated energy densities and their associated expected grey values. First, we need a primary intensity image.

.. note:: In the *Image Viewer*, switch to :guilabel:`primary intensities` (:numref:`detectorPrimaryIntensities`).
    
    In the toolbar, press |32x32_compute-radiography| to run a full simulation. In the *Image Viewer*, press |22x22_document-save| to save the primary intensities as an image file.

.. _detectorPrimaryIntensities:
.. figure:: pictures/tutorial-detector-primary-intensities.png
    :width: 60%

    The *Image Viewer* displays the primary intensities.
    
We will now open the primary intensity image and the real CT image side by side in an external image viewer. In this tutorial, we will use ImageJ. For a few small selected regions of interest, we measure the mean primary intensity and the grey value that we would expect from the real CT image.

.. note:: 1. Open the simulated primary intensity image and the uncorrected real CT image (:code:`1636_PMMA_Cylinder_upright00092.tif`) in ImageJ.
    2. Measure the mean primary intensity and mean grey value in a bunch of meaningful regions of interest. The ROIs in both images should be located at roughly the same location with respect to the cylinder. In :numref:`detectorPrimaryIntensitiesVsRealGreyValues` you can see an example for five different regions of interest that cover a representative grey value range.

.. _detectorPrimaryIntensitiesVsRealGreyValues:
.. figure:: pictures/tutorial-detector_primary-intensities_vs_real-grey-values.png
    :width: 100%

    Measuring the mean primary intensity (left) and the mean real grey value (right) for five distinct regions of interest.

We use a spreadsheet to keep track of the values (:numref:`detectorPrimaryIntensitiesVsRealGreyValuesSpreadsheet`). We also add a grey value of zero for a primary intensity of zero (keep in mind that we work with dark-field corrected images here) and we add the grey value 8410 for the maximum free-beam intensity (see :numref:`detectorFreeBeamGV`). To get the maximum free-beam primary intensity value of 0.00411101 |nbsp| W/m², you can deactivate the PMMA cylinder's visibility, run a full free-beam simulation and read the maximum intensity value from the image viewer (see :numref:`detectorPrimaryIntensitiesVsRealGreyValuesMaxFreeBeamPrimary` for more instructions).

.. _detectorPrimaryIntensitiesVsRealGreyValuesSpreadsheet:
.. figure:: pictures/tutorial-detector_primary-intensities_vs_real-grey-values_spreadsheet.png
    :width: 100%
    
    A spreadsheet lists the primary intensity and the target grey value for each ROI.

.. _detectorPrimaryIntensitiesVsRealGreyValuesMaxFreeBeamPrimary:
.. figure:: pictures/tutorial-detector_primary-intensities_vs_real-grey-values_max-primary.png
    :width: 100%
    
    Four steps to get the maximum free-beam primary intensity.
    
For the grey value characteristics (see :numref:`detectorViewerCharacteristic`) we need the energy density (J/m²) per pixel and associate it with a grey value. We can easily calculate the energy density by multiplying the primary intensity with the detector's integration time (0.5 |nbsp| s). For this purpose, we add another column to our spreadsheet (:numref:`detectorPrimaryIntensitiesVsRealGreyValuesSpreadsheet2`).

.. _detectorPrimaryIntensitiesVsRealGreyValuesSpreadsheet2:
.. figure:: pictures/tutorial-detector_primary-intensities_vs_real-grey-values_spreadsheet2.png
    :width: 100%
    
    We added a column for the energy density, which is the primary intensity multiplied by the integration time (0.5 |nbsp| s in our case).

Now we use a text editor to open the detector definition file that we created with the DetectorCalc module (:code:`Step Cylinder Detector.aRTdet`). Find the section that's called :code:`[Characteristics]` (:numref:`detectorArtdetFile`).

.. _detectorArtdetFile:
.. figure:: pictures/tutorial-detector_artdet-file.png
    :width: 80%
    
    The detector definition file opened in a text editor. The relevant grey value characteristics section is highlighted.

From our spreadsheet, we copy the columns for the energy density and target grey value and replace the existing two value pairs. We also need to put an equals sign :code:`=` in between each value pair as the file notation demands (:numref:`detectorArtdetFileCustomCharacteristics`).

.. _detectorArtdetFileCustomCharacteristics:
.. figure:: pictures/tutorial-detector_artdet-file_custom-characteristics.png
    :width: 80%
    
    The detector definition file with our custom grey-value characteristics.

We save this altered detector definition file and open it in aRTist to import our changes (drag&drop or :guilabel:`File` → :guilabel:`Open`). The detector viewer (:guilabel:`Tools` → :guilabel:`Detector Properties`) should now display our custom-made grey value characteristics (:numref:`detectorDetectorViewerCustomCharacteristics`) and you should get grey values in your simulated projection image that match the real measurement much better.

.. _detectorDetectorViewerCustomCharacteristics:
.. figure:: pictures/tutorial-detector_detector-viewer_custom-characteristics.png
    :width: 100%
    
    The detector viewer displays our custom-made grey-value characteristics.

Flat-Field Correction
---------------------

|artist| offers the ability to run a flat-field correction for simulated projection images. For this purpose, it has an internal buffer that can store a flat field image.

When you activate the flat field correction in the detector settings (:numref:`detectorFlatFieldCorrection`), |artist| will use the image from the buffer for the flat field correction. If the buffer is empty (i.e., if you have not yet loaded or computed any flat field image), |artist| will temporarily turn off the visibility of all objects in your scene and temporarily turn off noise to calculate a flat field image. It will then restore the object visibility and noise and compute the actual projection image, complete with a flat-field correction.

This automatic computation of the flat-field image is done **only once!** Once the buffer contains an image, it will be used for any further flat fieldf corrections, even if you change your scene. To re-compute another flat field image, you can delete |22x22_edit-delete| the current flat field image to clear the buffer. Once the buffer is empty, |artist| will automatically calculate a new flat field image when needed.

.. _detectorFlatFieldCorrection:
.. figure:: pictures/tutorial-detector_flat-field-correction.png
    :width: 80%
    
    Controls for the flat-field correction.

During the flat field correction, the projection image :math:`I` will be "flattened" with the flat-field image :math:`I_\text{FF}`. The result is then re-normalized to the **mean free-beam grey value** :math:`\left< I_\text{FF} \right>`, such that you should get a homogenous background that has the mean intensity of a free-beam image.

.. math::
    I_\text{corrected} = \frac{I}{I_\text{FF}} \cdot \left< I_\text{FF} \right>

You can use the button |22x22_aRTist| to compute a new flat field image for the buffer with your current scene settings. Remember to turn off any objects in the beam path yourself, otherwise they will appear in the flat field image.

Frame Averaging
---------------

To simulate the averaging of multiple frames, |artist| does not simulate the requested number of frames and averages them. Instead, it temporarily adjusts the energy density on the detector and therefore looks up a different SNR on your detector's noise curve (:numref:`FrameAveragingExample`).

.. _FrameAveragingExample:
.. figure:: pictures/QuickStartCT_AveragingExample.*
    :width: 100%

    Example for the temporary adjustment of the energy density axis to the original SNR curve for an averaging of two frames.

Note that |artist| uses a linear interpolation if your SNR curve does not reach the high energies that might be required by a high number of averaging frames. Also, depending on your specific SNR curve, you might get a result that differs from what you would expect from a simple arithmetic mean of two frames. |artist| uses this approach to cover the effects of structural pattern noise (which cannot be improved by averaging) and dynamic noise (e.g. Poisson noise of the source, thermal noise of the detector, etc.) in *one* single SNR curve.


Summary
-------

In this tutorial, you learned how to use the *DetectorCalc* module to simulate a real-life detector. You got to know the different curves that |artist| uses to calculate the grey values of a projection image, and you saw an approach to alter the grey value characteristics to get better matching grey values.

| The scene that we created in this tutorial is available for download:
| :download:`tutorial_detector.aRTist <files/tutorial_detector.aRTist>` (2.3 MB)
