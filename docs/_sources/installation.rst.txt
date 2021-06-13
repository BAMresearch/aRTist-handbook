Installation
============

System requirements
-------------------

The *aRT*\ ist program comes as a Microsoft Windows application. The system requirements narrow down to the required platform: Microsoft Windows 7 or superior. The program is provided as 64-bit application.

It is possible to use *aRT*\ ist on low prize netbook hardware. But it is recommended to run it on computers with multi (core) processor and accelerated graphical processing unit (OpenGL 2.1) to have the necessary calculation speed for treating ambitious simulation tasks efficiently.


Licenses
--------

The *aRT*\ ist program is equipped with software protection mechanisms and needs license activation for full functionality. Without activation, the program runs in Lite mode of reduced functionality. In case of licensing errors, e.g. broken license file, the program might still be usable to arrange and review virtual scenes, but it is not possible to make any simulations (viewer mode).

.. note:: An **evaluation period** of 30 days is granted without any license activation (DEMOMODE).

An *aRT*\ ist license is shipped as serial number, which can be used to activate an *aRT*\ ist installation.

.. note:: Licenses can be bound to a specific PC **(node-locked license)** or shared among different installations **(network license).**

The *aRT*\ ist licenses can be used either node-locked or shared within a network. A node-locked license is assigned to one specific PC. With network licensing the *aRT*\ ist program can be installed on several PCs with access to the same license file. In this case *aRT*\ ist can be alternately used on different PCs (floating license). To run several *aRT*\ ist installations at the same time it is possible to assign more than one license to the shared license file.


Installation instructions
-------------------------

The radiographic simulator *aRT*\ ist comes with an installation routine :file:`aRTistSetup-X.X.X.exe` (where X.X.X is replaced by the version number). For installation execute the setup routine you got with your distribution. A dialog will appear (:numref:`installationWelcomeScreen`) and guide you through the installation process.

.. warning:: If *aRT*\ ist is already installed, the installation routine will ask for de-installation of the current version before proceeding with the installation process, if necessary. Consequently, installations with the same version number will be replaced, while installations with different version numbers can coexist on the same PC.

During the installation process, you can choose options like the generation of a Windows Start Menu entry and a Windows Desktop icon for convenient program execution. After installation *aRT*\ ist is ready to use. Without an active and valid license aRTist will run with the restricted functionality of Lite/Viewer mode only.

In the next section you will find information on reqesting an evaluation or permanent license activation.

.. _installationWelcomeScreen:
.. figure:: pictures/artist-2.12-setup1.png
    :alt: Installer welcome screen
    :width: 65%

    Installer welcome screen.


.. _installationOptions:
.. figure:: pictures/artist-2.12-setup2.png
    :alt: Installer option selection
    :width: 65%

    Installer option selection.


License activation
------------------

*aRT*\ ist needs to be installed before proceeding with the license activation. The activation is a two-step process: first, a dedicated activation request has to be sent to the supplier of the software and secondly, the activated license file provided in response has to be installed.

The actual license status can be displayed under :guilabel:`License information` from the :guilabel:`Help` menu (:numref:`licenseInformationDialog`).


Activation request
^^^^^^^^^^^^^^^^^^

The activation request requires information about your *aRT*\ ist installation. The necessary information can be collected at the license information dialog of *aRT*\ ist (:guilabel:`Help` menu → :guilabel:`License information`). There are options to apply for node-locked or network licensing and to request an evaluation period. E-mail the request to `aRTist@bam.de <mailto:aRTist@bam.de>`_.

In response to an activation request, you will get back an activated license file within the next business days.

.. note:: To request a network license, a shared network folder has to be prepared in advance. It is required to store the common license file. 

.. note:: All users of the network license need to have write permission for the license file. 

.. _licenseInformationDialog:
.. figure:: pictures/artist-licenseinformation.png
    :alt: License information dialog
    :scale: 100%

    License information dialog.


License file installation
^^^^^^^^^^^^^^^^^^^^^^^^^

The final step to activate a license is to install the license file provided in response to the activation request. Generally, this means overwriting the temporary license file by the activated one.

The license file installation can be done just by opening the license file in *aRT*\ ist.

.. note:: Just Drag'n'Drop the license file over the *aRT*\ ist window to install it.

.. note:: The same applies to use an already activated network license at additional PCs: Just Drag'n'Drop the license file from the network folder over the *aRT*\ ist window. Answer the subsequent dialog **"Use (not install) this network license?"** with :guilabel:`Yes`. 