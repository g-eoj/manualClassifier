# manualClassifier
A tool for manually classifying images

# Setup

Set up directory structure like:

```
.
├── original
├── output
├── public
└── thumbs
```

You will need matplotlib and possibly PIL

There are scripts for moving stuff to public and resizing thumbs...

You ought to check them though before using because the paths are a little specific

# Usage
Simply run `python manualClassifier.py` in the directory set up as above.

An image will be displayed and the console will ask you to classify it. Enter a number or a name of a directory that does not yet exist. The program will write what it has done, so you can manually fix it if you make a mistake.

Additionally, `n` and `b` will skip forward and back one image from your image set. Entering `q` at the "What is it?" prompt will quit.

Remember that this script will move the image and not just copy it. This way you can quit and start again from where you left off later.
