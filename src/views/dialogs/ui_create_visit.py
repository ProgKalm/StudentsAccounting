# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_visit.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDialog,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreatorVisit(object):
    def setupUi(self, CreatorVisit):
        if not CreatorVisit.objectName():
            CreatorVisit.setObjectName(u"CreatorVisit")
        CreatorVisit.resize(600, 200)
        CreatorVisit.setMinimumSize(QSize(600, 200))
        CreatorVisit.setMaximumSize(QSize(600, 200))
        CreatorVisit.setModal(True)
        self.verticalLayout = QVBoxLayout(CreatorVisit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dialog_title_lbl = QLabel(CreatorVisit)
        self.dialog_title_lbl.setObjectName(u"dialog_title_lbl")
        self.dialog_title_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dialog_title_lbl)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.info_lbl_1 = QLabel(CreatorVisit)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_lbl_1.sizePolicy().hasHeightForWidth())
        self.info_lbl_1.setSizePolicy(sizePolicy)
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.hLayout_1.addWidget(self.info_lbl_1)

        self.visit_date_edit = QDateEdit(CreatorVisit)
        self.visit_date_edit.setObjectName(u"visit_date_edit")
        self.visit_date_edit.setAlignment(Qt.AlignCenter)
        self.visit_date_edit.setReadOnly(False)
        self.visit_date_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.visit_date_edit.setCalendarPopup(True)

        self.hLayout_1.addWidget(self.visit_date_edit)


        self.verticalLayout.addLayout(self.hLayout_1)

        self.hLine_1 = QFrame(CreatorVisit)
        self.hLine_1.setObjectName(u"hLine_1")
        self.hLine_1.setFrameShape(QFrame.HLine)
        self.hLine_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.hLine_1)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setObjectName(u"hLayout_4")
        self.hLayout_3 = QHBoxLayout()
        self.hLayout_3.setObjectName(u"hLayout_3")
        self.info_lbl_2 = QLabel(CreatorVisit)
        self.info_lbl_2.setObjectName(u"info_lbl_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_lbl_2.sizePolicy().hasHeightForWidth())
        self.info_lbl_2.setSizePolicy(sizePolicy1)
        self.info_lbl_2.setAlignment(Qt.AlignCenter)

        self.hLayout_3.addWidget(self.info_lbl_2)

        self.timespan_spinbox = QDoubleSpinBox(CreatorVisit)
        self.timespan_spinbox.setObjectName(u"timespan_spinbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.timespan_spinbox.sizePolicy().hasHeightForWidth())
        self.timespan_spinbox.setSizePolicy(sizePolicy2)
        self.timespan_spinbox.setWrapping(False)
        self.timespan_spinbox.setFrame(True)
        self.timespan_spinbox.setAlignment(Qt.AlignCenter)
        self.timespan_spinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timespan_spinbox.setDecimals(1)
        self.timespan_spinbox.setMaximum(24.000000000000000)
        self.timespan_spinbox.setValue(1.000000000000000)

        self.hLayout_3.addWidget(self.timespan_spinbox)

        self.info_lbl_4 = QLabel(CreatorVisit)
        self.info_lbl_4.setObjectName(u"info_lbl_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.info_lbl_4.sizePolicy().hasHeightForWidth())
        self.info_lbl_4.setSizePolicy(sizePolicy3)
        self.info_lbl_4.setAlignment(Qt.AlignCenter)

        self.hLayout_3.addWidget(self.info_lbl_4)


        self.hLayout_4.addLayout(self.hLayout_3)

        self.vLine_1 = QFrame(CreatorVisit)
        self.vLine_1.setObjectName(u"vLine_1")
        self.vLine_1.setFrameShape(QFrame.VLine)
        self.vLine_1.setFrameShadow(QFrame.Sunken)

        self.hLayout_4.addWidget(self.vLine_1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unspecial_rbtn = QRadioButton(CreatorVisit)
        self.unspecial_rbtn.setObjectName(u"unspecial_rbtn")
        self.unspecial_rbtn.setChecked(True)

        self.gridLayout.addWidget(self.unspecial_rbtn, 0, 2, 1, 1)

        self.info_lbl_3 = QLabel(CreatorVisit)
        self.info_lbl_3.setObjectName(u"info_lbl_3")
        self.info_lbl_3.setAlignment(Qt.AlignCenter)
        self.info_lbl_3.setWordWrap(True)

        self.gridLayout.addWidget(self.info_lbl_3, 2, 0, 1, 1)

        self.currency_lbl = QLabel(CreatorVisit)
        self.currency_lbl.setObjectName(u"currency_lbl")
        self.currency_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.currency_lbl, 2, 2, 1, 1)

        self.special_rbtn = QRadioButton(CreatorVisit)
        self.special_rbtn.setObjectName(u"special_rbtn")
        self.special_rbtn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.special_rbtn, 0, 1, 1, 1)

        self.sp_sum_spinbox = QDoubleSpinBox(CreatorVisit)
        self.sp_sum_spinbox.setObjectName(u"sp_sum_spinbox")
        self.sp_sum_spinbox.setAlignment(Qt.AlignCenter)
        self.sp_sum_spinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_sum_spinbox.setDecimals(1)
        self.sp_sum_spinbox.setMaximum(9999999.000000000000000)

        self.gridLayout.addWidget(self.sp_sum_spinbox, 2, 1, 1, 1)

        self.info_lbl_5 = QLabel(CreatorVisit)
        self.info_lbl_5.setObjectName(u"info_lbl_5")

        self.gridLayout.addWidget(self.info_lbl_5, 0, 0, 1, 1)


        self.hLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.hLayout_4)

        self.hLine_2 = QFrame(CreatorVisit)
        self.hLine_2.setObjectName(u"hLine_2")
        self.hLine_2.setFrameShape(QFrame.HLine)
        self.hLine_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.hLine_2)

        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_2.addItem(self.hSpacer_1)

        self.done_btn = QPushButton(CreatorVisit)
        self.done_btn.setObjectName(u"done_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.done_btn.sizePolicy().hasHeightForWidth())
        self.done_btn.setSizePolicy(sizePolicy4)

        self.hLayout_2.addWidget(self.done_btn)


        self.verticalLayout.addLayout(self.hLayout_2)


        self.retranslateUi(CreatorVisit)

        QMetaObject.connectSlotsByName(CreatorVisit)
    # setupUi

    def retranslateUi(self, CreatorVisit):
        CreatorVisit.setWindowTitle(QCoreApplication.translate("CreatorVisit", u"VisitCreator", None))
        self.dialog_title_lbl.setText(QCoreApplication.translate("CreatorVisit", u"Creating Visit", None))
        self.info_lbl_1.setText(QCoreApplication.translate("CreatorVisit", u"Date", None))
        self.info_lbl_2.setText(QCoreApplication.translate("CreatorVisit", u"Timespan", None))
        self.info_lbl_4.setText(QCoreApplication.translate("CreatorVisit", u"hour", None))
        self.unspecial_rbtn.setText(QCoreApplication.translate("CreatorVisit", u"Unspecial", None))
        self.info_lbl_3.setText(QCoreApplication.translate("CreatorVisit", u"Special Sum", None))
        self.currency_lbl.setText(QCoreApplication.translate("CreatorVisit", u"Currency", None))
        self.special_rbtn.setText(QCoreApplication.translate("CreatorVisit", u"Special", None))
        self.info_lbl_5.setText("")
        self.done_btn.setText(QCoreApplication.translate("CreatorVisit", u"Create", None))
    # retranslateUi
