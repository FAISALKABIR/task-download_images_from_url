# task-download_images_from_url

<h2>Introducion</h2>

In this repository, I describe how I download all the images from the given text file containing image URL.

<h2>Description</h2>

<h3>My method has two steps:</h3>

<h4>Step 1:</h4>

The first step is to gather URL links of the images from the given **_url.txt_** file that contains the URL link of the images. 

<h4>Step 2:</h4>

The second step is to download images from each URL using Python.

First, let's take a look at the **_url.txt_** file. 

```path_text = "url.txt"```

let's look at the lines of the **_url.txt_** and the number of lines.

```ur = o.read()```
    
Next download the images from each of the URL using ```requests.get()``` . I included the ```try catch``` as some requests fail with error messages. Runinng the following script create a folder data if it does not exist in the current directory and save images in **_jpg_** format.
