import sys
import rclpy
from PyQt5 import QtWidgets
from .submodules.layout import *


class GUI():
    def __init__(self):
        try:
            self.app = QtWidgets.QApplication(sys.argv)
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(self.MainWindow)
            self.MainWindow.show()
            sys.exit(self.app.exec_())
        except RuntimeError as e:
            print(f"an error ocurred: {e}")
        finally:
            print("destroy nodes")
            self.ui.destroy_nodes()


def main(args=None):
    try:
        rclpy.init(args=args)
        global_gui = GUI()
        rclpy.shutdown()
    except KeyboardInterrupt:
        print("Keyboard interrupted")
    finally:
        print("main gui finished")


if __name__ == '__main__':
    main()
