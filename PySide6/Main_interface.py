import sys

from PySide6 import  QtGui,QtWidgets
from PySide6.QtCore import Qt


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFrame")
        self.resize(1000, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        """左侧文件管理区界面"""
        scroll_area = QtWidgets.QScrollArea(self)
        scroll_area.resize(200, 600)
        scroll_area.move(0, 0)

        #设置滚动区域为标签区域的父控件
        label_area = QtWidgets.QWidget(scroll_area)

        #设置标签区域为标签的父控件
        label_01 = QtWidgets.QLabel("文件名01", label_area)
        label_02 = QtWidgets.QLabel("文件名02", label_area)
        label_03 = QtWidgets.QLabel("文件名03", label_area)
        label_04 = QtWidgets.QLabel("文件名04", label_area)

        # 创建布局管理器对象，创建时指定布局方向为垂直从上至下
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        # 将布局管理器添加给标签区域，用于管理标签区域的控件
        label_area.setLayout(layout)
        # 将控件添加到布局管理器中，就像setWidget，不添加，就不纳入布局管理器的管理
        layout.addWidget(label_01)
        layout.addWidget(label_02)
        layout.addWidget(label_03)
        layout.addWidget(label_04)
        
        # 添加为滚动区域的子控件，并不能作为滚动区域的滚不动内容展示。只有用下列这行代码将控件添加为滚动区域的视图控件，才会变为滚动展示的内容,并且setWidget只能添加一个控件作为视图控件，所以多个标签要放在label_area中
        scroll_area.setWidget(label_area)

        # 设置视图控件的对齐方式，这是滚动区域用于管理自己的视图控件的方法
        scroll_area.setAlignment(
            Qt.AlignLeft
        )  # 设置为水平居中
        
        """中间对话界面"""
        frame = QtWidgets.QFrame(self)
        frame.setStyleSheet("background-color: white;")
        frame.resize(500, 600)
        frame.move(200, 0)
        # 设置风格与线宽
        frame.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Sunken)
        frame.setLineWidth(3)

        # 创建对话窗口
        text_browser = QtWidgets.QTextBrowser(frame)
        #text_browser.setText(self.text)
        text_browser.resize(500, 400)
        text_browser.move(0, 0)
        text_browser.setStyleSheet("""
        QTextBrowser {
            border: none;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
            border-left: 1px solid rgba(0, 0, 0, 0.1);
            border-right: 1px solid rgba(0, 0, 0, 0.1);
            border-bottom: 1px solid rgba(0, 0, 0, 0.2);
        }
        """)
        
        # pte = QtWidgets.QPlainTextEdit(self)  # 创建
        pte = QtWidgets.QPlainTextEdit(frame)
        pte.resize(500, 200)
        pte.move(0, 400)
        pte.setStyleSheet("background-color: white;")

        button = QtWidgets.QPushButton()
        button.setParent(pte)  # 创建时父对象为None,可用setParent方法指定
        button.setText("发送")  # 设置按钮上的文字
        # 定位按钮到右下角
        button.resize(100, 40)  # 设置按钮大小
        button.move(pte.width() - button.width() - 10, pte.height() - button.height() - 10)

        """右侧多媒体播放与功能界面"""
        # 创建并嵌入MediaPlayerWidget
        self.media_player = MediaPlayerWidget(self)
        self.media_player.resize(300, 207)
        self.media_player.move(700, 0)

        ribbon = QtWidgets.QFrame(self)
        ribbon.resize(300, 393)
        ribbon.move(700, 207)
        ribbon.setStyleSheet("background-color: #FAFAFA;")
        # 设置风格与线宽
        ribbon.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Sunken)
        ribbon.setLineWidth(3)
   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
