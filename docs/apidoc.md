###Platform Server CRUD API doc

##### Description
This API document contains about how to use CRUD api for it's relevant operations . 

##### Requirements
Python<br/>
Mongodb<br/>
Internal python tools were written in requirements.txt<br/>

#### API Endpoints

##### _*/items/create_item*_
Request type: POST<br/>
Request data format: { 'id': \<item_id\>, 'type': \<item_type\>, 'blob': \<item_blob\> }<br/>
Response: { 'status': \<status of the request\>, 'errors': \<if any errors\> }<br/>

##### __/items/get_item__
Request type: GET<br/>
Request data format: { 'id': \<item_id\>, 'type': \<item_type\> }<br/> 
Response: { 'status': \<status of the request\>, 'errors': \<if any errors\>, 'data': \<array of dict with all items with matched item_data\> }<br/>

##### __/items/update_item__
Request type: POST<br/>
Request data format: { 'id': \<item_id\>, 'type': \<item_type\>, 'blob': \<item_blob\> }<br/>
Response: { 'status': \<status of the request\>, 'errors': \<if any errors\>, 'mcount': \<tells you how many data points have been modified\> }<br/>

##### __/items/delete_item__
Request type: POST<br/>
Request data format: { 'id': \<item_id\>, 'type': \<item_type\> }<br/>
Response: { 'status': \<status of the request\>, 'errors': \<if any errors\>, 'dcount': \<tells you how many data points have been deleted\> }<br/>
