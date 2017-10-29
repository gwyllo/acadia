# acadia
ACADIA machine learning workshop code and resources

## Workshop Setup

### Logging in to Paperspace and launching the ACADIA image
- Go to paperspace.com and sign in using your invite
- Launch the console
- Click new Machine
- Use the ACADIA image and p6000 GPU
- Start your new image!

### Accessing your machine on the cloud
- For writing code: Use Gedit on the paperspace virtual desktop or Notepad++ and follow the instructions on the wiki
- For transferring files: Use google drive and re-download from chrome in the virtual paperspace desktop, or use WINSCP and follow the instructions on the wiki
- For running terminal commands: Use the terminal in the paperspace virtual desktop. It has a few quirks and you may prefer to simply SSH straight in to your instance using putty. Follow the instructions on the wiki

## Building a Twitter bot
All of our bots will work with the same basic python script. This script will execute different shell scripts for running specific machine learning frameworks. For more info see the wiki.

## Models

### pix2pix
- learns mappings between pairs of images

### cycleGAN
- learns mappings between collections of images

### NeuralStyle
- applies the style of one image to the content of another

### torchRNN
- generates text character by character 

### imagesearch
- finds similar images using feature vectors from an image classifier


## Datasets
- Scale
- Programe
- Localities
- Materials
- Drawings / photos
- Interiors
- Sketches
- Screengrabs
- Pre-made datasets (flowers, birds, art, landscapes)

## Ecosystem Tools
- text to searched image using google api / instagram api etc
- feature search with TENSORFLOW

# Workshop Schedule
## Day 1 - Working with the python toolkit on paperspace
### Morning
* 9:00am Overview of the project and Intro from CN+GJ
* 10:00am Intro lecture from Ben - very brief overview of what a neural network is

* 10:30am Setup: Creating accounts and Provisioning VMs with Paperspace
* 11:00am Setup: Twitter accounts (test and developer) / secrets

* 11:30am Intro to bash (navigation, installation and running and creating scripts)
* 11:45am Intro to python (syntax, variables, hello world, functions)

### Afternoon
* 2:00pm Intro to tweepy (go over bot framework)
* 2:45pm Bot test (receive and generate image)
* 3:00pm Intro to photoshop batch
* 3:30pm Batch processes: Find Edges -> Photo, Zooming, Missing content -> Full Image, Greyscale -> Colour, Posterize -> Photo
* 4:00pm Intro to pix2pix. Examples, Training Script + Sampling Script, LightDisplay
* If time - post results of trained model to twitter

## Day 2 - Introduction to machine learning, Building models with Tensorflow and Torch
### Morning
* 9:00am Gene Kogan lecture - context and projects
* 10:00am Neural network overview (mathmatical models, layers, heuristics)
* 10:30am Convolutional networks (max pooling etc) and GAN overview (explanation of how pix2pix and cycleGAN works)
* 11:00am Overview of available models: Pix2Pix, CycleGAN, Style Transfer, FeatureSearch, CharRNN
* 11:30am Project discussion - productive models of feedback between these bots. Content generation vs content transfer, 'markup' and 'critique', real-time similary search etc.

### Afternoon
* 2:00pm Intro to scrapy and xpath (modifying scraper for new data sets
* 3:00pm Project work

## Day 3 - Building an ecosystem of autonomous agents
### Morning
* 9:00am Presentations and discussion
* 11:00am Feedback loops on local machine and between twitter bots
* 12:00pm Project work

### Afternoon
* 2:00pm Project work
* 4:00pm Setup exhibition
