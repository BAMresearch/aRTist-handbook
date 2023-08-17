.. include:: _templates/icons.rst

.. _McRaySection:

McRay
=====

**McRay** is a Monte Carlo ray tracing implementation for photon and electron transport in |artist|. 

For the photon transport **McRay** solves the stationary Bolzmann equation. It describes not only the attenuation of photons as the exponential attenuations law, giving only the part of the photons that do no interact with die object (primary radiation), but also counts for contributions of Compton and Rayleigh scattering as well as for pair production. Additionally, internal sources as X-ray fluorescence (emission of photons as a result of the photo absorption), electron-positron annihilation (emission of two photons with exactely 511 keV in opposite direction as a result of pair production), and Bremsstrahlung production can be considered. 

The **McRay** module can also trace electrons which is for most of the applications of |artist| not necessary and consumes a very large amount of computing resources. 

This module provides a graphical user interface for **McRay** in order to configure and run simulations within |artist|. 
If the inline help icon |16x16_system-help| is activated an additional tab :guilabel:`Help` will appear (see: :ref:`Help menu <HelpMenuSubsection>`).

.. note::
    
    In this user guide, the **McRay** module the topics :guilabel:`Expert`, :guilabel:`Manual`, :guilabel:`Cluster`, and :guilabel:`Interactive` are not being explained. The topic :guilabel:`Expert` requires detailed knowledge about the underlaying physics and the Monte Carlo method. The topic  :guilabel:`Manual` require detaild knowledge about the implementation of the ray tracer. The topic :guilabel:`Cluster` is created to run **McRay** on a computer cluster under linux for parallel computing. The actual implementation runs also on multi processor multi core Windows systems in parallel mode. The topic :guilabel:`Interactive` summarizes the simulation and the calculation progess, i.e., is just informative. 

A :guilabel:`Run` or alternately a :guilabel:`Stop` button and a progress bar are located at bottom of module window. To start the calculation press the :guilabel:`Run` button. After this the :guilabel:`Run` button turns to the :guilabel:`Stop` button to stop the running calculation. 

.. _McRayBasicSubSection:

:guilabel:`Basic`
-----------------

The **Basic** tab contains everything necessary to run a Monte Carlo simulation with the default settings (:numref:`mcrayy`). 
At the top there are two buttons, :guilabel:`Set defaults` to reset all settings to the default one, and :guilabel:`View default output` to load the images normally resulting from a successful simulation.

.. _mcrayy:
.. figure:: pictures/modules-mcrayy.png
    :alt: McRay: Basic
    :width: 71.3%

    McRay: Basic.

.. _McRayBasicOptionsSubsubSection:

Options
^^^^^^^

The following options are available:

* **Number of particles** is used to specify the desired number of particles (photons / electrons) to be traced for the Monte Carlo simulation.
* **Data energy resolution [keV]** is used to set the energy resolution for the interaction cross sections.

    .. hint::
    
        Internally most material data (attenuation-coefficients, differential scatter cross-sections, etc.) is privided in lookup tables for fast access. 
        The default value of 1 keV does not normally need to be changed, but for low-energy calculations, for instance if fluorescence is included, a smaller value of, e.g., 0.1 keV may be advisable.

* **File prefix** is used to set the project name in this field. Default name is :class:`New`.

.. _McRayBasicOutputSubsubSection:

Output directory
^^^^^^^^^^^^^^^^

Here the **Output directory** may be changed and viewed, which will hold the configuration files and the subdirectories for the *Geometry*, the *MaterialData*, and after successful simulation the *Results* for all output files (images, spectra, etc.). 
The four buttons at the top allow to :guilabel:`Choose` the directory via a graphical dialog, :guilabel:`Open` the directory in an external file browser, or :guilabel:`Clear` to delete all files in the output directory including all subdirectories. 
With the :guilabel:`Default` button it is possible to reset the settings to the default values. The default value for the output directory is :class:`#McRay/New`. After the calculation has been successfully finished an additional subdirectory named *Results* is created, where all simulation results are stored.

.. note::
    The directory may also be changed by typing or pasting the directory into the text field below the buttons.

The remaining space is filled by the file listing and associated buttons. A double click in the list will open the currently selected files with their associated application, 
as while pressing the :guilabel:`Open` button. To view the content of the subdirectories (*Geometry*, *MaterialData*, and *Results*) the **+** infromt of the subdirectory name must be pressed. :guilabel:`Show Image` and :guilabel:`Scatter Image` (**Remark: by pressing the button** :guilabel:`Scatter Image` **no image will automatically loaded**) are to load the currently selected image files in the :ref:`ImageViewer <ImageViewerSection>` module. The :guilabel:`TraceView` is build to visualize trajectories saved by **McRay** if *Safe trajectories* is selected in the :ref:`Advanced <McRayAdvancedSubSection>` tab (see below) in the 3D scene viewer. In :guilabel:`TraceView` a dialog will be opend to filter trajectories to be visualized. In 
:guilabel:`View Spectrum` the spectrum used for the Monte Carlo simulation is shown in the included spectrum plotter.

.. _McRayAdvancedSubSection:

:guilabel:`Advanced`
--------------------

.. _McRayAdvancedSimulationOptionsSubsubSection:

Simulation Options
^^^^^^^^^^^^^^^^^^

The options on the left hand side are mostly concerned with physical effects and geometry handling. The right hand side allows configurating the output to be produce (:numref:`mcrayy1`).
If the command is selected by clicking on the checkbox it is necessary to change the number right to the selected option. If the command is not selected the default setting will be used.

.. _mcrayy1:
.. figure:: pictures/modules-mcrayy1.png
    :alt: McRay: Advanced
    :width: 71.3%

    McRay: Advanced.

Left hand side of Simlulation Options:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Photo effect**: It should always be selected for photon transport.

    .. note::
    
        The photoabsorption results in the emission of an electron, mainly from an inner electron shell, when electromagnetic radiation is absorbed in the material. The emitted photoelectron obtains a kinetic energy given by the difference between the photon’s energy and the binding energy of that particular electron. The photoelectron produces Bremsstrahlung radiation with energies smaller or equal to the kinetic energy of the electron. Additionally, recombination processes within the electron shell yield to X-ray fluorescence.

* **Rayleigh scattering** 

    .. note::
        
        The coherent or Rayleigh scattering is an elastic process and involves no energy loss of the X-ray photon but continues to travel through the material along an altered path upon being scattered by an atom. It is only a photon process that does not produce electrons. In case of Rayleigh scattering at a bound electron the angle distribution of the scattered photon is mainly forward orientated within a very small angle range. In the lower energy region its interaction cross section is dominated by that of the the photoabsorption, for medium energy by that of Compton scattering, and for high energies by that of pair production. This means, Rayleigh scattering is independently of the photon energy never the dominant interaction mechanism. 

* **Compton scattering**: It should always be selected for photon transport. 

    .. note:: 
    
        Compton scattering occurs when the incident X-ray photon is deflected from its original path by an interaction with an outer shell electron. 
        The electron is ejected from its orbital position and the X-ray photon loses energy because of the interaction but continues to travel through the material along an altered path. 
        Energy and momentum are conserved in this process. If scattering at a free electron is considered the energy shift depends only on the scattering angle and not on the nature of the scattering material. In reality, the scattering occurs at a bound electron which has to be considered in the scattering cross section, i.e., it depends on the scattering material.
        As for the photoabsoption Bremsstrahlung radiation with energies smaller or equal to the kinetic energy of the electron is produced as secondary effect of the Compton scattering.

* **Pair production** considers the production of an electron-positron pair.   

    .. note::

        If the photon energy exceeds double the electron mass of rest, i.e., if its energy is larger than 1.022 MeV, the photon is converted in the electrical field of the nucleus into an electron and a positron. This process is called pair production. Photons with lower energy are not able to produce an electron positron pair. The photon energy that exceeds the needed minimal energy appears as kinetic energy of the pair. The produced pair loses its kinetic energy within a short time of about 10 `-12`:superscript: s. The remaining resting electron positron pair has a lifetime of about 10 `-9`:superscript: s before annihilation. As result of annihilation two gamma photons are emitted in opposite direction because of momentum conservation both with energy of exactly 511 keV because of energy conservation. 
        

* **Fluorescence**: Photons and electrons, if enabled, can excite or eject bound electrons of the material's electron shell. During the recombination in the electron shell X-ray fluorescence photons, fluorescence electrons, and Auger electrons may be emitted.

    .. note::
    
        X-ray fluorescence is the emission of characteristic or fluorescence X-rays from a material that has been excited by being exposed with high-energy X-rays or gamma rays, ionization of their component atoms may take place. Ionization consists of the ejection of one or more electrons from the electron shell, and may occur if the atom is exposed to radiation with an energy greater than its ionization energy. Each element has electron orbitals of characteristic energy. Following the removal of an inner electron by an high-energy photon provided by a primary radiation source, an electron from an outer shell drops into its place, also called recombination. Each of the possible transitions yields a X-ray fluorescence photon with a characteristic energy, that is equal to the difference in energy of the initial and final orbital of the electron. 
        

* **Electron transport**: When fluorescence or Bremsstrahlung radiation is enabled, secondary electrons will be traced, created, e.g., by photoabsorption or Compton scattering. 

    .. note::

        The transport of electrons and other charged particles is fundamentally different from that of uncharced particles, such as neutrons and photons. The transport of electrons is dominated by the long-range Coulomb force, resulting in large numbers of individual interactions. Elastig and inelastic interactions of electrons with matter are considered: Elastic scattering, ionisation, excitation, and radiative energy loss (Bremsstrahlung radiation) are considered. In the |artist| Monte Carlo implementetion of the electron transport the model of individual collitions (MIC) is used. The energy-loss fluctuations are  taken into account according to the Landau theory.

    .. attention::
        The electron transport requires large computing resorces, i.e., memory and computing power. The calculation time may be very large. For radiographic applications electron transport is not recommended.

      

* **Bremsstahlung** (photons) are created during electron interactions when selected and it requires to switch on the electron transport. **Remark: Is this really true?**

    .. note::
        Bremsstrahlung radiation is an electromagnetic radiation produced by the deceleration of a charged particle when deflected by another charged particle, 
        typically an electron by an atomic nucleus. The moving particle loses kinetic energy, which is converted into one photon or more, satisfying the law of conservation of energy. 
        Bremsstrahlung has a continuous spectrum, which becomes more intense and whose peak intensity shifts toward 
        higher energies as the change of the energy of the decelerated particles increases.

* **Noninteractive** starts/stops calculation without further user interaction.
* **Photonsplitting** applies a variance reduction scheme. Photonsplitting takes into account the possible interaction processes when a photon is penetrating a medium.
* **Check object overlap** notes the overlapping of parts when selected.
* **Save trajectories** writes trajectory segments to disk. 

    .. attention::

        Slow and memory intensive depending on the number of photon to be traced.

* **Target pixels** aims photons toward each pixel (mostly for visualization purpose).

right hand side of Simlulation Options:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Image type** is used to choose between different image types: :code:`.tiff`, :code:`.ISee`, :code:`.raw`, :code:`.pgm` or :code:`.txt`. The default setting is :code:`.tiff`.
* **Pixel type** is used to choose between different pixel types: :class:`UInt 16`, :class:`Float`, or :class:`Double`. Usually :class:`Float` is used.
* **Pixel columns** enters the number of pixel in columns.
* **Pixel rows** enters the number of pixel in rows.
* **Normalize Errors** gives the relative statistical error.
* **Detector model** is used to choose between different detector models: :class:`aRTist`, :class:`Photons`, :class:`Leptons`, :class:`Electrons`, :class:`Positrons` or :class:`All`. The default detector model is :class:`aRTist`.
* **Scatter data** registers data for this many scatter events separately.
* **Spectrum bins**: The maximum energy divide by the number of bins gives the spectrum resolution in keV for each energy bin.
* **Max threads** sets the maximum number of threads to be used for the calculation.

    .. note::
        Physical cores are the number of cores per processor. Logical cores are the number of physical cores times the number of threads that can run on each physical core through the use of hyperthreading. One CPU kernal may have 2 threads.
        
* **Batch size** sets the number of trajectories in one batch.
* **Random seed**: The random seed is a number used to initilize a pseudorandom number generator. 

    .. note::
        A pseudorandom number generator's random number sequence is completely determined by the seed: thus, if a pseudorandom number generator is reinitialized with the same seed, it will produce the same sequence of random numbers. If the seed is set randomly the randomnumber generator  will produce different sequences of random numbers,which is recommended.  

.. _McRayAdvancedExecutionOptionsSubsubSection:

Execution Options
^^^^^^^^^^^^^^^^^

**Process priority** is used to set the priority of the background process carrying out the actual simulation with this parameter. 
It can be choosen between :class:`Idle`, :class:`Below`, :class:`Normal`, :class:`Above`, and :class:`High`. 

.. hint::
    
    As calculations can potentially take a long time, a reduced priority is generally advisable (default setting: :class:`Below`).

Set the **Number of threads** to be executed for the Monte Carlo simulation.
