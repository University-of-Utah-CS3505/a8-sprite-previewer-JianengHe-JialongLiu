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
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages', self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.current_fps = 30
        self.is_playing = False

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

        # Sprite image display (empty label with border)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(200, 200)
        main_layout.addWidget(self.image_label)

        # FPS slider and labels
        fps_layout = QHBoxLayout()

        self.fps_text_label = QLabel("Frames per second:")
        fps_layout.addWidget(self.fps_text_label)

        self.fps_slider = QSlider(Qt.Orientation.Horizontal)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(100)
        self.fps_slider.setValue(self.current_fps)
        self.fps_slider.valueChanged.connect(self.update_fps_label)
        fps_layout.addWidget(self.fps_slider)

        self.current_fps_label = QLabel(str(self.current_fps) + " FPS")

        fps_layout.addWidget(self.current_fps_label)

        main_layout.addLayout(fps_layout)

        # Start/Stop button
        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.toggle_animation)
        main_layout.addWidget(self.start_stop_button)

        # Set layout and central widget
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        # Menu bar
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
        self.current_fps_label = QLabel(str(self.current_fps) + " FPS")


    def toggle_animation(self):
        self.is_playing = not self.is_playing
        self.start_stop_button.setText("Stop" if self.is_playing else "Start")

    def pause_animation(self):
        self.is_playing = False
        self.start_stop_button.setText("Start")


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
