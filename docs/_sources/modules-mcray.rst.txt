.. include:: _templates/icons.rst

.. _McRaySection:

McRay
=====

**McRay** is a Monte Carlo raytracing implementation of electron and photon transport. 
This module forms a graphical interface for McRay, in order to configure and run simulations using it from within |artist|. 
If you activate the inline help icon |16x16_system-help| an additional tab :guilabel:`Help` will appear (see: :ref:`Help menu <HelpMenuSubsection>`).

.. note::
    
    In this user guide, the McRay module topics :guilabel:`Expert`, :guilabel:`Manual`, :guilabel:`Cluster` and :guilabel:`Interactive` are not being explained.

A :guilabel:`Run` or :guilabel:`Stop` button and a progress bar are located at bottom of module window. The first four tabs expose the configuration in order of increasing complexity.

.. _McRayBasicSubSection:

:guilabel:`Basic`
-----------------

This page contains everything necessary to run a Monte Carlo simulation with the default settings (:numref:`mcrayy`). 
At the top there are two buttons, :guilabel:`Set defaults` to reset all settings to the default, and :guilabel:`View default output` to load the images normally resulting from a successful simulation run.

.. _mcrayy:
.. figure:: pictures/modules-mcrayy.png
    :alt: McRay: Basic
    :width: 71.3%

    McRay: Basic.

.. _McRayBasicOptionsSubsubSection:

Options
^^^^^^^

* **Number of particles** is used to specify the desired number of particles (photons / electrons).
* **Data energy resolution [keV]** is used to influence the energy resolution of these structures (by this parameter).

    .. hint::
    
        Internally most material data (attenuation-coefficients, differential scatter cross-sections, etc.) is kept in lookup structures for fast access. 
        The default value of 1 keV does not normally need to be changed, but for low-energy calculations, especially including fluorescence, a smaller value of e.g. 0.1 keV may be advisable.

* **File prefix** is used to set a project name in this field. Default name is :class:`New`.

.. _McRayBasicOutputSubsubSection:

Output directory
^^^^^^^^^^^^^^^^

Here you may change and inspect the **Output directory**, which will hold the configuration files, data files, and all output files (images, spectra, etc.). 
The four buttons at the top allow you to :guilabel:`Choose` the directory via a graphical dialog, :guilabel:`Open` it in an external file browser, or :guilabel:`Clear` all contained files (but not subdirectories). 
With the :guilabel:`Default` button it is possible to reset the settings to the default values. 

.. note::
    You may also change the directory by typing or pasting into the text field below the buttons.

The remaining space is filled by the file listing and associated buttons. A double click in the listing will open the currently selected files with their associated application, 
as will pressing the :guilabel:`Open` button. :guilabel:`Show Image`, :guilabel:`Scatter Image`, and :guilabel:`TraceView` will load the currently selected files in the :ref:`ImageViewer <ImageViewerSection>` module, as the scatter image for subsequent 
calculations, and in the TraceView module (if installed) respectively. The TraceView module is intended to visualize trajectories saved by McRay in the 3D scene view. 
:guilabel:`View Spectrum` will attempt to pass the selected file to the included spectrum plotter.

.. _McRayAdvancedSubSection:

:guilabel:`Advanced`
--------------------

.. _McRayAdvancedSimulationOptionsSubsubSection:

Simulation Options
^^^^^^^^^^^^^^^^^^

The options on the left hand side are mostly concerned with physical effects and geometry handling. The right hand side allows configuration of the output to produce (:numref:`mcrayy1`).
If the command is selected it is necessary to change the number. While if the command is not selected the default setting will be set.

.. _mcrayy1:
.. figure:: pictures/modules-mcrayy1.png
    :alt: McRay: Advanced
    :width: 71.3%

    McRay: Advanced.

Left hand side of Simlulation Options:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Photo effect** considers photoabsorption when elected. Should almost always be selected.

    .. note::
    
        This photoemission is the emission of electrons or other free carriers when light is shone onto a material.

* **Rayleigh scattering** considers Rayleigh scattering when elected.

    .. note::
        
        This electromagnetic interaction is the mostly elastic scattering of light or other electromagnetic radiation by particles (atoms or molecules) much smaller than the wavelength of the radiation. Rayleigh scattering is a parametric process.

* **Compton scattering** considers Compton scattering when elected.

    .. note:: 
    
        Compton scattering occurs when the incident X-ray photon is deflected from its original path by an interaction with an electron. 
        The electron is ejected from its orbital position and the X-ray photon loses energy because of the interaction but continues to travel through the material along an altered path. 
        Energy and momentum are conserved in this process. The energy shift depends on the angle of scattering and not on the nature of the scattering medium. 
        Since the scattered X-ray photon has less energy, it has a longer wavelength and less penetrating than the incident photon.

* **Pair production** considers pair production when elected.

    .. note::

        Pair production often refers specifically to a photon creating an electron-positron pair near a nucleus but can more generally refer to any neutral boson creating a 
        particle-antiparticle pair. In order for pair production to occur, the incoming energy of the interaction must be above a threshold in order to create the pair - at least the total 
        rest mass energy of the two particles - and that the situation allows both energy and momentum to be conserved.

* **Fluorescence** considers flourescence when elected. Photons, and electrons if enabled, can excite the bound electrons of the material's atoms. During relaxation fluorescence photons, fluorescence electrons, and Auger electrons may be emitted.

    .. note::
    
        Fluorescence is the emission of light by a substance that has absorbed light or other electromagnetic radiation. 
        It is a form of luminescence and in most cases, the emitted light has a longer wavelength, and therefore lower energy, than the absorbed radiation.

* **Electron transport** considers electron transport when elected. When fluorescence or bremsstrahlung is enabled, secondary particles will be created.

    .. note::

        The Monte Carlo method for electron transport is a semiclassical Monte Carlo (MC) approach of modeling semiconductor transport. 
        Assuming the carrier motion consists of free flights interrupted by scattering mechanisms, a computer is utilized to simulate the trajectories of particles as they move across 
        the device under the influence of an electric field using classical mechanics. The scattering events and the duration of particle flight is determined through the use of random numbers.

* **Bremsstahlung** (photons) are created during electron interactions when elected and requires electron transport.

    .. note::
        The braking radiation or deceleration radiation is electromagnetic radiation produced by the deceleration of a charged particle when deflected by another charged particle, 
        typically an electron by an atomic nucleus. The moving particle loses kinetic energy, which is converted into a photon, thus satisfying the law of conservation of energy. 
        The term is also used to refer to the process of producing the radiation. Bremsstrahlung has a continuous spectrum, which becomes more intense and whose peak intensity shifts toward 
        higher frequencies as the change of the energy of the decelerated particles increases.

* **Noninteractive** starts/stops calculation without further user interaction.
* **Photonsplitting** applies variance reduction scheme. Photonsplitting takes into account the possible interaction process when a photon is penetrated by a medium.
* **Check object overlap** notes the overlapping of parts when elected.
* **Save trajectories** writes trajectory segments to disk (slow).
* **Target pixels** aims photons toward each pixel (mostly for visualization purpose).

right hand side of Simlulation Options:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Image type** is used to choose between different image types: TIFF, Isee, RAW, PGM or TXT. The default setting is TIFF.
* **Pixel type** is used to choose between different pixel types: UInt 16, Float, Double. Usually the Float is used.
* **Pixel columns** enters the number of pixel in columns.
* **Pixel rows** enters the number of pixel in rows.
* **Normalize Errors** normalizes a relative error of 1 to this value (relative statistically error).
* **Detector model** is used to choose between different detector models: aRTist, Photons, Leptons, Electrons, Positrons or All. The default detector model is aRTist.
* **Scatter data** registers data for this many scatter events separately.
* **Spectrum bins** sets the number of spectrum bins. The maximum energy divide by the number of bins reveals the spectrum for each energy.
* **Max threads** sets the maximum number of threads.
* **Batch size** sets the batch size of trajectories.
* **Random seed** sets the random seed.

.. _McRayAdvancedExecutionOptionsSubsubSection:

Execution Options
^^^^^^^^^^^^^^^^^

**Process priority** is used to adjust the process priority of the background process carrying out the actual simulation with this parameter. 
You can choose between :class:`Idle`, :class:`Below`, :class:`Normal`, :class:`Above` and :class:`High`. 

.. hint::
    
    As calculations can potentially take a long time, a reduced priority is generally advisable (default setting: :class:`Below`).

Set the **Number of threads**.
