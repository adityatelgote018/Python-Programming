#from moviepy
#import (TextClip, ColorClip, CompositeVideoClip, concatenate_videoclips)

scenes = [
    ("MINI RESCUE", "Saving Lives in Emergencies"),
    ("HELP PEOPLE IN DANGER", "Stay calm and act quickly."),
    ("RESCUE AND FIRST AID", "Help injured people safely."),
    ("EMERGENCY SERVICES", "Call 112 in India when needed."),
    ("EVERY LIFE MATTERS!", "Every Second Counts!")
]

clips = []

for title, subtitle in scenes:
    background = ColorClip(
        size=(1280, 720),
        color=(15, 45, 75),
        duration=4
    )

    heading = TextClip(
        text=title,
        font_size=65,
        color="white",
        size=(1100, None),
        method="caption"
    ).with_duration(4).with_position(("center", 260))

    caption = TextClip(
        text=subtitle,
        font_size=32,
        color="yellow",
        size=(1100, None),
        method="caption"
    ).with_duration(4).with_position(("center", 390))

    scene = CompositeVideoClip(
        [background, heading, caption]
    )
    clips.append(scene)

video = concatenate_videoclips(clips, method="compose")
video.write_videofile(
    "mini_rescue_video.mp4",
    fps=24,
    codec="libx264",
    audio=False
)