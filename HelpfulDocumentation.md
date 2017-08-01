# Helpful Documentation for creating Multiple HITS

To create multiple ```HITS``` per ```Batch``` via GUI on MTurks follow the instructions below:

  1. First thing is to create a ```CSV``` file. This can be made via ```Microsoft Excel```. A CSV file is basically a tabular way to 
      organize data to be read. Where The very first line is the heading for each column and every following line is a row with commas
      seperating columns. Here is an example:
      
      Excel:
      
      ![Alt text](https://user-images.githubusercontent.com/25187819/28840157-186f4ee2-76c4-11e7-9f72-f8a83792d00e.png "WorkFlow")
      
      CSV:
      
      ![Alt text](https://user-images.githubusercontent.com/25187819/28840297-882e43d2-76c4-11e7-870a-3ccc63bf5d84.png "WorkFlow")
      
      
  2. Next when you are creating your HIT, you can call the different columns in the ```Excel or CSV``` file by doing:               ```${COLUMN_TITLE}``` . The Batch will create X number of ```HITs``` based on the number of rows you have supplied in the ```CSV``` file. That part is taken care of by ```AWS```.

