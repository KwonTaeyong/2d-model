# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# import pyqtgraph as pg
#
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         btn = QPushButton("테스트")
#         btn.move(10, 10)
#         btn.clicked(self.btn_clicked())
#
#         w = pg.PlotWidget()
#         self.setCentralWidget(w)
#
#         a1 = [1, 2, 3, 4]
#         a2 = [5, 6, 7, 8]
#
#         b1 = [1, 2, 3, 4]
#         b2 = [1, 4, 9, 16]
#
#         c1 = [1, 2, 3, 4]
#         c2 = [1, 2, 3, 4]
#
#         d1 = [1, 2, 3, 4]
#         d2 = [1, 2, 3, 4]
#
#         w.setBackground('w')
#         w.setTitle("테스트 2D 모델링")
#         w.addLegend()
#         w.showGrid(x = True, y = True)
#
#         w.plot(x=a1, y=a2, pen=pg.mkPen(width=2, color='r'), name="1면")
#         w.plot(x=b1, y=b2, pen=pg.mkPen(width=2, color='b'), name="2면")
#         w.plot(x=c1, y=c2, pen=pg.mkPen(width=2, color='g'), name="3면")
#         w.plot(x=d1, y=d2, pen=pg.mkPen(width=2, color='y'), name="4면")
#
#     def btn_clicked(self):
#         self.close()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()
