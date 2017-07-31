# MTurks Workflow
This python project utilizes the ```Amazon Mechanical Turks Boto API``` to make an auto-granting qualification request workflow based on answers. 

It is used to differentiate workers between HITS. It follows the workflow model below:

![Alt text](https://user-images.githubusercontent.com/25187819/28787507-73559f12-75ea-11e7-8bef-0b8078718174.png "WorkFlow")


# Boto Install
To install use: ```pip install boto```


# Changes that need to be made to API
For this too work, the ```BOTO API``` checks if the ```answer_key``` parameter is an instance of ```'basestring'``` format, which is no longer available in the new versions of ```Python 3.x```. Therefore, when it checks if the parameters answer_key is an instance of ```'basestring'``` you need to change that to ```'str'``` for it to read it properly. 
