import sys
import random
from PySide6.QtWidgets import QLineEdit, QPushButton
from PySide6.QtWidgets import QApplication, QVBoxLayout
from PySide6.QtWidgets import QDialog, QTextEdit 
from PySide6.QtGui import QColor


class Form(QDialog):                

    def __init__(self, parent=None):          
        # layout 구성요소          
        super(Form, self).__init__(parent)
        self.user_edit = QLineEdit()
        self.user_edit.setPlaceholderText(" form: '가위  ' 한 칸 띄어쓰기 필수!! ")
        self.computer_edit = QLineEdit("상대의 선택")
        self.winlose_edit = QLineEdit("승패 결과")
        self.excute_button = QPushButton("실행하기") 
        self.image = QTextEdit(' 결과 출력창 ')

        # window 크기 조절
        self.resize(530,400)
        
        # layout에 추가 
        layout = QVBoxLayout()
        layout.addWidget(self.user_edit)      
        layout.addWidget(self.computer_edit)
        layout.addWidget(self.winlose_edit)
        layout.addWidget(self.excute_button)
        layout.addWidget(self.image)
        self.setLayout(layout)
        
        # 버튼 - 함수 연동
        self.excute_button.clicked.connect(self.excute) 
        
    # 컴퓨터 선택 랜덤 추출 
    def excute(self) : 
        example = ["가위 " , "바위 " , "보 "]
        example_index = random.randrange(0,3)
        self.result = example[example_index]
        self.computer_edit.setText(self.result)
        self.who_winloss()
    
    # 사용자 입력, 컴퓨터 입력 비교 후 결과 도출
    def who_winloss(self) :
        user_form = ["가위 " , "바위 ", "보 "]
        
        # 양식과 다른 입력이 들어온 경우 
        if str(self.user_edit.text()) not in user_form : 
            self.result_index = -1 
            self.user_edit.setText("양식에 맞춰 다시 입력하세요. ex) '가위 ' ")
            self.computer_edit.setText("----")
            self.winlose_edit.setText("----")
            self.print_image()
            return 
        
        # 무승부인 경우 
        if str(self.user_edit.text()) == str(self.computer_edit.text())  : 
            self.result_index = 2
            self.winlose_edit.setText("무승부")
        
        # 그외 승부가 나는 경우
        else : 
            if str(self.user_edit.text()) == "가위 " : 
                if self.result == "바위 " : 
                    self.result_index = 1
                    self.winlose_edit.setText("패배")
                else : 
                    self.result_index = 0
                    self.winlose_edit.setText("승리")
            elif str(self.user_edit.text()) == "바위 " : 
                if self.result == "보 " : 
                    self.result_index = 1
                    self.winlose_edit.setText("패배")
                else : 
                    self.result_index = 0
                    self.winlose_edit.setText("승리")      
            else : 
                if self.result == "가위 " : 
                    self.result_index = 1
                    self.winlose_edit.setText("패배")
                else : 
                    self.result_index = 0
                    self.winlose_edit.setText("승리")     
        self.print_image()
        return 
    
    # 맨 아래 결과 창에 결과 출력 
    def print_image(self) : 
        # 결과 경우의 수 
        result_text = ["  win " , " Lose" , " Draw"]
        self.image.setFontItalic(True)
        self.image.setFontPointSize(180)
        if self.result_index == 0 : 
            self.image.setTextColor( QColor(0,0,255))
        elif self.result_index == 1 : 
            self.image.setTextColor( QColor(255,0,0))
        elif self.result_index == 2 : 
            self.image.setTextColor( QColor(0,255,0))
        else : 
            # 입력 form이 맞지 않는 경우 
            self.image.setTextColor( QColor(255,255,255))
            self.image.setFontPointSize(30)
            self.image.setText("please fill in the form ")
            return 
        self.image.setText(result_text[self.result_index])
        return 
        
if __name__ == '__main__':
    app = QApplication(sys.argv)                    
    form = Form()                                      
    form.show()                                       
    sys.exit(app.exec())