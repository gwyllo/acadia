# acadia
ACADIA machine learning workshop code and resources

## Workshop Resources and Introduction
(TODO - collate key tutorial resources)
E.g. broad overview of machine learning [Machine Learning Is Fun](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471):
(TODO - setup learning materials folder on git)
E.g. Refer to [Reference Material](/Reference/reference.md) for more resources.
(TODO - get proper list of requirements to students)

## Workshop Setup

### Spinning up a Deep Learning Instance
- Log in to RMIT-ACADIA Amazon EC2 account using (TODO - setup account w/ $2000 rmit funds)
- Create a new instance using image (TODO - our image)

### SSH into your instance
- Mac users
- Windows users

### Get the code
- Clone this repo:
```bash
git clone https://github.com/gwyllo/acadia
cd acadia
```

### Software
- Notepad ++
- WinSCP?
- Jupyter notebook?
- tensorboard?
- screen

## Models

### NeuralStyle
- train a basic model

### StackGAN
- get basic text to image working

### pix2pix
- train two models and get them to feedback
- generating datasets in GH

### cycleGAN
- train two models and get them to feedback
- generating datasets in GH

### torchRNN
- setup tutorial for scrapy on AWS
- get jack to proof it

### tSNE / search
- n-dimensional layout algorithm
- need to research how to do image search based on high-level features (high priority)

## Bots
- text to searched image using google api
- (HARD) text to generated image using stackGAN 
- image to similar image using CNN latent space
- text to more text using torchRNN
- content image to stylised image 
- content image to semantic labels
- semantic labels to stylised image

## Feedback between Bots
- Never-ending wander: Find similar image in a dataset, style this image, repeat
- GAN feeback: CycleGAN/pix2pix an image trained on one kind of mapping, feed this into another network trained on another mapping
- Semantic Labelling: One model marks something up (semantic labelling), another one tries to 'fill in' the marked up area, repeat

## Implementation
- python server listening for tweets
- on receiving tweet run bash script (we have a list of bash scripts setup for each framework)
- bash script needs to return whether content is image or text in order to correctly tweet result
- tweet

## First goal: 
- two python servers each running pix2pix models and listening for tweets
- then setup feedback between the two
- Jack needs to figure out what to train the networks on 
-- edges to photo (can use facades dataset that comes with pix2pix, or scrape archdaily) and vice versa
-- image to zoomed image and vice versa
-- etc - anything you can batch process in photoshop
-- or anything you can easily generate from GH (animate sliders)
