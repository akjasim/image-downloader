# Image Downloader

A python based image downloader capable of downloading all the images on a website.

## Installation

Clone the repository into your local system.

```bash
git clone https://github.com/akjasim/image-downloader.git
```

Make a virtual environment, activate it and install all the requirements.
```bash
virtualenv venv
call venv/Scripts/activate (Windows)
source venv/bin/activate (Linux)

pip install -r requirements.txt
```

## Usage

#### Make an ImageCracker instance.
```python
img = ImageCracker(site_url, image_base_path_url, destination_directory)
```
site_url = actual url of fetching site.

image_base_path_url = url of the image root directory.

destination_directory = path in your local machine to which images are to be saved. (If not given, will save the images in the project directory.)




#### Call the get_images method.

```python
img.get_images()
```
Parameters:

1) img_type='data_src' (Default is 'src')

data-src is used in case where images are dynamically loaded using JavaScript. The name may vary to data-slide-bg or similar. In those cases, edit the source code.

2) external=True (Default is False)

external is set to True when the images are hosted externally like in aws. If external is set to True, then, make the image_base_path_url the same as site_url.

## Sample Use Case
```python
img = ImageCracker('https://techzia.in/', 'https://techzia.in/', 'D:/hello/')
img.get_images(external=True)
```
This downloads all the external images in [Techzia](https://techzia.in/) and store it in the destination folder(make sure 'D:/hello/' exists). But, it has a flow that it cannot download internal images and will raise an exception at the end.

## Contributing
This has some flows such as it cannot handle both internal and external images. It could be fixed in future versions. We love to keep in touch with contributors. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)