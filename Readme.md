# **NXYI2C Python sample (for Raspberry Pi)**

These are the programs to control NXYI2C with python.
Please refer to the file name for the lighting pattern to be displayed.

|File|description|
|:---|:---|
|0_off.py|Turns off the Nixie tube at the specified I2C address.|
|1_show.py|Displays a number on the nixie tube of the specified I2C address.|
|2_fade_in.py|Displays a number on the nixie tube of the specified I2C address.|
|3_fade_out.py|Displays a number on the nixie tube of the specified I2C address.|
|4_fade_change.py|Displays a number on the nixie tube of the specified I2C address.|
|5_rotation.py|Displays a number on the nixie tube of the specified I2C address.|
|6_from_cloud.py|Displays a number on the nixie tube of the specified I2C address.|
|7_into_cloud.py|Displays a number on the nixie tube of the specified I2C address.|

# Setup

Run the following command on your Raspberry Pi.

```
curl https://www.nixielive.com/setup-nxyi2c-python-samples.sh | bash
```

After executing the above command, the sample script will be installed according to the following steps.

* git will be installed (if it is not already installed)
* python3-smbus:armhf will be installed (if not already installed)
* The ~/nixielive directory will be created
* This repository will be cloned into ~/nixielive

You can see the sample scripts in  ~/nixielive/nxyi2c-python-samples.
