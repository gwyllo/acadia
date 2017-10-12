# acadia
ACADIA machine learning workshop code and resources

## Workshop Resources and Introduction
(TODO - collate key tutorial resources)
E.g. broad overview of machine learning [Machine Learning Is Fun](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471):
(TODO - get proper list of requirements to students)

## Workshop Setup

### Logging in to Paperspace and launching the ACADIA image
- Go to paperspace.com and sign in using your invite
- Launch the console
- Click new Machine
- Use the ACADIA image and p9000 GPU
- Start your new image!

### Accessing your machine on the cloud
- For writing code: Use Notepad++ and follow the instructions on the wiki
- For large files: Use google drive and re-download from chrome in the virtual paperspace desktop. 
- For small files: Use WINSCP and follow the instructions on the wiki
- For running terminal commands: If you have a fast connection, you can use the terminal in the browser. It has a few quirks and you may prefer to simply SSH straight in to your instance using putty. Follow the instructions on the wiki

## Building a Twitter bot
All of our bots will work with the same basic python script. This script will execute different shell scripts for running specific machine learning frameworks. For more info see the wiki.

## Models

### pix2pix
- learns mappings between pairs of images

### cycleGAN
- learns mappings between collections of images

### torchRNN
- generates text character by character 

### imagesearch
- finds similar images using feature vectors from an image classifier

### TODO - NeuralStyle (TODO) / stackGAN / DCGAN
- changes the style of a content image
- generates an image from text
- interpolate between generated images

## Datasets
- Scale
- Programe
- Localities
- Materials
- Drawings / photos
- Interiors
- Sketches

## Bots
- get image between two images (DCGAN)
- generate photo from edges (PIX2PIX)\
- "enhance" an image / zoom in on an image (PIX2PIX)
- texture an image (CYCLEGAN)
- stylise an image (NeuralStyle)
- text to searched image using google api
- find most similar image from a collection of images
- text to more text using torchRNN
- content image to stylised image (NeuralStyle)

(Hard)
- text to image (stackGAN)
- content image to semantic labels (PIX2PIX)
- semantic labels to stylised image (PIX2PIX)

## Feedback between Bots
- Never-ending wander: Find similar image in a dataset, style this image, repeat
- GAN feeback: CycleGAN/pix2pix an image trained on one kind of mapping, feed this into another network trained on another mapping
- Semantic Labelling: One model marks something up (semantic labelling), another one tries to 'fill in' the marked up area, repeat

# Workshop Schedule
## Day 1 - Working with the python toolkit on paperspace
### Morning
* Overview of the project
* Intro lecture from CN + GJ
* Intro lecture from Ben- very brief overview of what a neural network is

* Provisioning VMs with Paperspace
* Intro to bash
* Intro to python
* Intro to tweepy

### Afternoon
* Intro to scrapy & xpath markup
* Intro to photoshop batch
* Intro to pix2pix
* Break in to groups
* Work with leaders of the groups to scrape data and begin training models 

## Day 2 - Introduction to machine learning, Building models with Tensorflow and Torch
### Morning
* Gene lecture
* Neural network overview - how to effectively train, basic maths
* Convolutional networks
* Visualisation - tSNE, latent space

### Afternoon

* Working with torch + tensorflow
* Tweaking frameworks / project goals with gene - e.g. visualising layers, working with stackGan etc
* Retrain models / calibrate

## Day 3 - Building an ecosystem of autonomous agents
### Morning
* Presentation of results
* Feedback loops on local machine
* Calibration

### Afternoon
* Publishing bots
* Calibrating the ecosystem
* Setup exhibition
