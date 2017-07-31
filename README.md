# MTurks Workflow
This python project utilizes the ```Amazon Mechanical Turks Boto API``` to make an auto-granting qualification request workflow based on an ```answer_key``` in ```XML``` format.

It is used to differentiate workers between HITS. It follows the workflow model below:

![Alt text](https://user-images.githubusercontent.com/25187819/28787507-73559f12-75ea-11e7-8bef-0b8078718174.png "WorkFlow")


# Boto Install
To install use: ```pip install boto```


# Changes that need to be made to API
For this too work, the ```boto API``` checks if the ```answer_key``` parameter is an instance of ```'basestring'``` format, which is no longer available in the new versions of ```Python 3.X```. Therefore, when it checks if the parameters answer_key is an instance of ```basestring``` you need to change that to ```str``` for it to read it properly. 

This is located at ```/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/boto/mturk/connection.py``` 
at ```line 679```. Do the following change to the ```API```:

![Alt text](https://user-images.githubusercontent.com/25187819/28793607-819d5f6c-7601-11e7-9684-4cf226ff0494.png "WorkFlow")

