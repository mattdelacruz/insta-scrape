_A simple Python script for downloading images on Instagram_

## Installation instructions

- Clone the repository
- `cd to your repository`
- `chmod +x insta-scrape`
- create a .env file to set "DEFAULT_SAVE_DIRECTORY"
### Linux/MacOS

- `export PATH=$PATH:$(pwd)`

### Windows

- Add the script's directory to your PATH environment variable
- Run the script as `insta-scrape [instagram url] {save directory}`

### Issues

- [ ] Cannot run the scrape all images using a single link if it's a slideshow
- [ ] Cannot scrape videos
- [x] `?img_index=` sometimes does not grab the correct image corresponding that index
