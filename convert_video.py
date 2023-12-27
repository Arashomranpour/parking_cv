from moviepy.editor import VideoFileClip


def convert_resolution(input_path, output_path, target_resolution):
    # Load video clip
    video_clip = VideoFileClip(input_path)

    # Resize video to the target resolution
    resized_clip = video_clip.resize(newsize=target_resolution)

    # Write the resized video to the output file
    resized_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the video clips
    video_clip.close()
    resized_clip.close()


if __name__ == "__main__":
    input_video_path = "./parking_1920_1080_loop.mp4"
    output_video_path = "output_video.mp4"
    target_resolution = (1280, 720)

    convert_resolution(input_video_path, output_video_path, target_resolution)
