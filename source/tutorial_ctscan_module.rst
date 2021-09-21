CtScan Module
================

The *CtScan* module is a modular extension of aRTist which provides the tools to simulate a typical circular CT scan. By default the *CtScan* module is deployed with the aRTist installation and can be accessed via the :guilabel:`Modules` tab.

.. note:: The pagination of the listed modules in the :guilabel:`Modules` depend on the installed modules.

For the following tutorial it is advised to be comfortable with the basic elements of aRTist. Therefore, in section ##2.3 description of the setup panel and the axis definition used within aRTist can be found. In section ##2.4 are the basics of the source panel described, which will be used to define a x-ray source. Section ##2.6 covers the basics of the detector panel, which is also necessary for a CT scan setup. The basic elments of the CtScan module itself, are descried in section ##3.3.

In the following chapters of this description, first a simple CT scan is described, which shows the basics of the module. After that, a typical setup of the module is shown, which can be transferred to every custom CT scan setup. In the section ##7.3 two examples are provided, which shows the difference between a ideal simulation and an experimental model in aRTist. In the last section of this tutorial, the borders of the current models - while using the *CtScan* module are discussed.

A Simple CT Scan
----------------

.. note:: For a fast demonstration the detector resolution will be reduced to 250×250 |nbsp| px.

In the *Parameter Panel* on the left-hand side, open the :guilabel:`Detector` tab. In the :guilabel:`Geometry` group, select :guilabel:`Res. [mm]` to fixate the pixel resolution and enable editing for the actual physical size and the number of pixels along the detector x- and y-axis. For :guilabel:`Pixel`, enter :code:`250` for both :guilabel:`X` and :guilabel:`Y` (:numref:`detectorSettingsPixels`).

.. tip::

	 Always press :guilabel:`Enter` to confirm an user input to avoid unwanted input resets due to the state restoration feature of aRTist.

.. _detectorSettingsPixels:
.. figure:: pictures/tutorial-ctscan-detector-settings.png
    :width: 50%

    Detector geometry settings with a reduced resolution of 250×250 |nbsp| px.

Next open the *CtScan* module from the menu bar: :guilabel:`Modules` → :guilabel:`CtScan` (:numref:`ctScanWindow`).

.. _ctScanWindow:
.. figure:: pictures/tutorial-ctscan-window.png
    :width: 55%

    The *CtScan* module window.

To simulate a full rotation, set the :guilabel:`Total Angle [°]` to :code:`360` degree.

The angular steps define the number of projections simulated. A good estimation to suffice the Nyquist-Shannon theorem for the Feldkamp reconstruction is to choose :math:`P` projections based on the sampling points :math:`S` along the object. :cite:p:`Kharfi2013`

.. math::

  P \ge S \cdot \frac{\pi}{2}

The sampling points along the object are defined by the detector width. Hence, in this case 250 |nbsp| px.

.. math::

  P \ge 250 \cdot \frac{\pi}{2} \approx 392.69

Including a small buffer, the :guilabel:`Number of Steps` (:math:`P`) is set to :code:`400` steps. The :guilabel:`Angle Step Size [°]` should automatically be calculated and display :code:`0.9`.

You can choose a different output :guilabel:`directory` for the projection files. If you leave the :code:`#` directory as it is, everything will be saved in your *Default Directory*. You can set this in your settings: from the menu bar, choose :guilabel:`Tools` → |icon-settings| :guilabel:`Settings` to see your *Default Directory*.

.. |icon-settings| image:: pictures/icons/16x16_preferences-system.png
    :width: 16

.. note:: Enter a :guilabel:`File Name` for your projection files. In this demonstration, we will name it :code:`rotor`.

For the :guilabel:`File Type`, you can choose between a stack of :guilabel:`TIFF` images and the :guilabel:`BAM CT` format.

* **TIFFs:** each projection image will be saved as a single TIFF file. A projection number will be added to the file name. If you choose this format, *aRT*\ ist's reconstruction software will not be able to reconstruct the CT scan.
* **BAM CT** is a format where all projections are stored in a single :code:`.dd` file. It has a header of variable size, followed by the raw data of the projection images. *aRT*\ ist's Feldkamp reconstruction software is able to reconstruct scans from this file format. You can find a documentation in this handbook under `BAM CT File Format <bamct_file_format.html>`_.

.. note:: Go ahead and simulate a TIFF stack by choosing the appropriate settings (as shown for example in :numref:`ctScanWindow`). Click the |icon-run| :guilabel:`Run` button to start the scan. The CT simulation should start and you should be able to observe the *Rotor's* rotation around its own centre in the virtual scene. The *Air Pocket* should follow this rotation as well.

.. |icon-run| image:: pictures/icons/16x16_compute-run.png
    :width: 16

References
----------
.. bibliography::


Test
----

Testlines below here

.. admonition:: Example

  This is an example

More Examples `CtScan Module`_ and another `TesttutorialLink <tutorial_ctscan_module.html>`_.
