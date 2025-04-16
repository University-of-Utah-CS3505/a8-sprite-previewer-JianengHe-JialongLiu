# https://github.com/University-of-Utah-CS3505/a8-sprite-previewer-JianengHe-JialongLiu
# created by Jianeng He
import math
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages', self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.current_fps = 10
        self.current_frame_index = 0
        self.is_playing = False

        # Timer to control sprite animation playback
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        main_layout = QVBoxLayout()

        # Top horizontal layout: sprite image and vertical slider
        top_layout = QHBoxLayout()

        # Sprite image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(150, 150)
        top_layout.addWidget(self.image_label)

        # FPS vertical slider
        self.fps_slider = QSlider(Qt.Orientation.Vertical)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(100)
        self.fps_slider.setValue(self.current_fps)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.fps_slider.setTickInterval(10)
        self.fps_slider.valueChanged.connect(self.update_fps_label)
        top_layout.addWidget(self.fps_slider)

        main_layout.addLayout(top_layout)

        # FPS label and current value
        fps_layout = QHBoxLayout()
        self.fps_text_label = QLabel("Frames per second")
        fps_layout.addWidget(self.fps_text_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.current_fps_label = QLabel(str(self.current_fps))
        fps_layout.addWidget(self.current_fps_label, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(fps_layout)

        # Start/Stop button
        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.toggle_animation)
        main_layout.addWidget(self.start_stop_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Set layout and central widget
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        # Menu bar with Pause and Exit
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.pause_animation)
        file_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)


    # You will need methods in the class to act as slots to connect to signals

    def update_fps_label(self):
        self.current_fps = self.fps_slider.value()
        self.current_fps_label.setText(str(self.current_fps))
        if self.timer.isActive():
            delay = int(1000 / self.current_fps)
            self.timer.start(delay)

    def toggle_animation(self):
        if self.is_playing:
            self.timer.stop()
            self.start_stop_button.setText("Start")
            self.is_playing = False
        else:
            delay = int(1000 / self.current_fps)
            self.timer.start(delay)
            self.start_stop_button.setText("Stop")
            self.is_playing = True

    def pause_animation(self):
        self.timer.stop()
        self.start_stop_button.setText("Start")
        self.is_playing = False

    def update_frame(self):
        self.image_label.setPixmap(self.frames[self.current_frame_index])
        self.current_frame_index = (self.current_frame_index + 1) % self.num_frames


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
