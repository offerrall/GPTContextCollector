# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(788, 469)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bt_add_file = QPushButton(Form)
        self.bt_add_file.setObjectName(u"bt_add_file")

        self.horizontalLayout.addWidget(self.bt_add_file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.content_table = QTableWidget(Form)
        if (self.content_table.columnCount() < 2):
            self.content_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.content_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.content_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.content_table.setObjectName(u"content_table")
        self.content_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.content_table)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txt_question = QTextEdit(self.groupBox_2)
        self.txt_question.setObjectName(u"txt_question")

        self.verticalLayout_2.addWidget(self.txt_question)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ck_delete_spaces = QCheckBox(self.groupBox)
        self.ck_delete_spaces.setObjectName(u"ck_delete_spaces")
        self.ck_delete_spaces.setStyleSheet(u"padding: 15px; margin: 0px;")

        self.horizontalLayout_2.addWidget(self.ck_delete_spaces)


        self.verticalLayout.addWidget(self.groupBox)

        self.bt_copy = QPushButton(Form)
        self.bt_copy.setObjectName(u"bt_copy")

        self.verticalLayout.addWidget(self.bt_copy)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bt_add_file.setText(QCoreApplication.translate("Form", u"Add File", None))
        ___qtablewidgetitem = self.content_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Delete", None));
        ___qtablewidgetitem1 = self.content_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Path", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Question", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Options", None))
        self.ck_delete_spaces.setText(QCoreApplication.translate("Form", u"Delete spaces", None))
        self.bt_copy.setText(QCoreApplication.translate("Form", u"Copy Context", None))
    # retranslateUi

