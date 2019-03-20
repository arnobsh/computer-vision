# Installing Python and associated libraries

For the project and for installing necessary library build the docker image form the following command

```
 docker-compose build
```
Now run the docker image

```
 .\run.ps1
```
Or for linux
```
  run.sh
```

## Running the program

### Image Filter Program:

Inside the container you can run the program by following commad
```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python image_filter.py
```
## Running the jupyter notebook

Inside the container for running jupyter notebook

```bash
#  jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
Alternatively, from the command prompt, you can run

### Image Filter Program:

```
docker run -it -p 8888:8888 image_processing_image_processing:latest bash
```

inside bash run following

```
# jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
It will allocate the ip and you can browse it from 

http://127.0.0.1:8888/tree

Following URLS consists all of the necessary code you may need for understanding the image filtering code

### Image Filter Program:

http://127.0.0.1:8888/notebooks/image_filter.ipynb


## Problem Domain

### Image Filter Program:

 I want you to modify the values of the variables red_threshold, green_threshold, and blue_threshold until you are able to retain as much of the lane lines as possible, while getting rid of most of the other stuff. 
