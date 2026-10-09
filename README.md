<div align="center">

# 🅿️ Parking Space Detector

**A computer-vision tool that marks parking spots on a video and shows in real time how many are free.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![cvzone](https://img.shields.io/badge/cvzone-overlay-informational)

</div>

---

## ✨ How it works

1. 🎞️ **Prepare the video** - resize it to a target resolution (`convert_video.py`).
2. 🖼️ **Capture a reference frame** - `screenshot_for_train.py` saves frames from the video into `data/` at a set interval.
3. 🖱️ **Mark the parking spots** - in `Train_via_screenshot.py` **left-click** to add a spot and **right-click** to remove it. Spot positions are saved to a `carpositions` pickle file.
4. 🚗 **Detect occupancy** - `app.py` thresholds each frame, counts non-zero pixels inside every spot, and colors it 🟩 **free** (count < 30) or 🟥 **occupied**. A live counter shows `Free : N / total`.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/parking_cv.git
cd parking_cv
pip install opencv-python cvzone numpy moviepy
```

Place your parking video as `output_video.mp4` in the project folder, then:

```bash
python screenshot_for_train.py     # extract reference frames to ./data
python Train_via_screenshot.py     # mark the parking spots
python app.py                      # run the detector
```

## 📁 Project Structure

```
.
├── convert_video.py          # Resize / re-encode the source video
├── screenshot_for_train.py   # Extract frames from the video
├── Train_via_screenshot.py   # Click to define parking spots
└── app.py                    # Real-time free-space detection
```

## 🛠️ Tech Stack

`OpenCV` · `cvzone` · `NumPy` · `MoviePy`
