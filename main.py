from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup, QListWidget, QTextEdit, QLineEdit, QInputDialog, QFileDialog
import os
from PIL import Image
from PyQt5.QtGui import QPixmap
from PIL import ImageEnhance

class ImageProcessor():
    def __init__(self):
        self.this_image = None
        self.filename = None
        self.subfolder = 'Modified/'

    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.this_image = Image.open(image_path)

    def showImage(self, path):
        image.hide()
        pixmapimage = QPixmap(path)
        w, h = image.width(), image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image.setPixmap(pixmapimage)
        image.show()

    def do_bw(self):
        self.this_image = self.this_image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.subfolder, self.filename)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(workdir, self.subfolder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.this_image.save(image_path)

    def do_flip(self):
        self.this_image = self.this_image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.subfolder, self.filename)
        self.showImage(image_path)

    def turn_left(self):
        self.this_image = self.this_image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.subfolder, self.filename)
        self.showImage(image_path)

    def turn_right(self):
        self.this_image = self.this_image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.subfolder, self.filename)
        self.showImage(image_path)

    def do_contrast(self):
        self.this_image = ImageEnhance.Contrast(self.this_image)
        self.this_image = self.this_image.enhance(1.5)
        self.saveImage()
        image_path = os.path.join(workdir, self.subfolder, self.filename)
        self.showImage(image_path)

def showChoosenImage():
    if images_field.currentRow() >= 0:
        filename = images_field.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)
        

def filter(files, extensions):
    result = list()
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result

def showFilenamesList():
    chooseWorkdir()
    extensions = ['.png', '.jpg', '.jpeg']
    try:
        files = filter(os.listdir(workdir), extensions)
        images_field.clear()
        images_field.addItems(files)
    except:
        error = QMessageBox()
        error.setWindowTitle('Ошибка!')
        error.setText('Не выбрана папка!')
        error.exec_()
        
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

    
app = QApplication([])# обьект приложение (ОБЪЯВЛЯТЬ ОБЯЗАТЕЛЬНО!!!)
workdir = ''
app_content = QWidget()#окно приложения
app_content.setWindowTitle('Easy Editor')
app_content.move(950, 80)
app_content.resize(850, 325)
button_1 = QPushButton('Папка')
button_2 = QPushButton('Лево')
button_3 = QPushButton('Право')
button_4 = QPushButton('Зеркало')
button_5 = QPushButton('Резкость')
button_6 = QPushButton('Ч/Б')
images_field = QListWidget()
image = QLabel('Картинка')
vertical_line_1 = QVBoxLayout()
vertical_line_2 = QVBoxLayout()
horizontal_line_1 = QHBoxLayout()
horizontal_line_2 = QHBoxLayout()
vertical_line_1.addWidget(button_1)
vertical_line_1.addWidget(images_field)
horizontal_line_2.addWidget(button_2)
horizontal_line_2.addWidget(button_3)
horizontal_line_2.addWidget(button_4)
horizontal_line_2.addWidget(button_5)
horizontal_line_2.addWidget(button_6)
vertical_line_2.addWidget(image)
vertical_line_2.addLayout(horizontal_line_2)
horizontal_line_1.addLayout(vertical_line_1, 20)
horizontal_line_1.addLayout(vertical_line_2, 80)
app_content.setLayout(horizontal_line_1)
workimage = ImageProcessor()
button_1.clicked.connect(showFilenamesList)
images_field.currentRowChanged.connect(showChoosenImage)
button_6.clicked.connect(workimage.do_bw)
button_4.clicked.connect(workimage.do_flip)
button_2.clicked.connect(workimage.turn_left)
button_3.clicked.connect(workimage.turn_right)
button_5.clicked.connect(workimage.do_contrast)
'''print('Путь к выбранной папке:', workdir)
files = os.listdir(workdir)
print('Список файлов', files)'''
'workdir = QFileDialog.getExistingDirectory()'





app_content.show()# отбражение окна (виджета)
app.exec_()
'''print('Цветовой тип', picture_original.format)
    picture_original.show()
    black_and_white = picture_original.convert('L')
    black_and_white.save('gray.jpg')
    print('Размер', black_and_white.size)
    print('Формат', black_and_white.format)
    print('Цветовой тип', black_and_white.format)
    black_and_white.show()
    picture_blured = picture_original.filter(ImageFilter.BLUR)
    picture_blured.save('blured.jpg')
    picture_blured.show()
    picture_up = picture_original.transpose(Image.ROTATE_180)
    picture_up.save('up.jpg')
    picture_up.show()
    mirror_picture = picture_original.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_picture.save('mirror.jpg')
    mirror_picture.show()
    picture_contrast = ImageEnhance.Contrast(picture_original)
    picture_contrast = picture_contrast.enhance(1.5)
    picture_contrast.save('contr.jpg')
    picture_contrast.show()'''

'''def print_information():# Создание нового окна и печать на нём информации
    victory_winner = QMessageBox()
    victory_winner.setWindowTitle('Результат теста')
    victory_winner.setText(f'Статистика\n Всего вопросов: {app_content.total}\n Правильных ответов: {app_content.score}\n Рейтинг {round((app_content.score / app_content.total) * 100, 2)}')
    victory_winner.exec_()'''


'''from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup, QListWidget, QTextEdit, QLineEdit, QInputDialog
import json

def show_note():
    name = notes_list.selectedItems()[0].text()
    text_place.setText(notes[name]['текст'])
    tegs_list.clear()
    tegs_list.addItems(notes[name]['теги'])

def add_note():
    note, result = QInputDialog.getText(notes_list, 'Добавить заметку', 'Название заметки')
    if result and note != '':
        notes[note] = {'текст': '', 'теги': []} 
        notes_list.addItem(note)

def del_note():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        del notes[key]
        notes_list.clear()
        tegs_list.clear()
        text_place.clear()
        notes_list.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def save_note():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        notes[key]['текст'] = text_place.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def add_tag():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = write_teg.text()
    if not tag in notes[key]['теги']:
        notes[key]['теги'].append(tag)
        tegs_list.addItem(tag)
        write_teg.clear()
    with open('notes_data.json', 'w') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_tag():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = tegs_list.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        tegs_list.clear()
        tegs_list.addItems(notes[key]['теги'])
    with open('notes_data.json', 'w') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def search_note():
    tag = write_teg.text()
    if button_6.text() == 'Искать заметки по тегу' and tag:
        notes_filtered = {} # здесь хранятся заметки с выделенным тегом
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        button_6.setText('Сбросить поиск')
        notes_list.clear()
        tegs_list.clear()
        notes_list.addItems(notes_filtered)
    elif button_6.text() == 'Сбросить поиск':
        write_teg.clear()
        notes_list.clear()
        tegs_list.clear()
        notes_list.addItems(notes)
        button_6.setText('Искать заметки по тегу')



app = QApplication([])# обьект приложение (ОБЪЯВЛЯТЬ ОБЯЗАТЕЛЬНО!!!)
app_content = QWidget()#окно приложения
app_content.setWindowTitle('Умные заметки')
app_content.move(950, 80)
app_content.resize(850, 325)
text = QLabel('Список заметок')
text_2 = QLabel('Список тегов')
button_1 = QPushButton('Создать заметку')
button_2 = QPushButton('Удалить заметку')
button_3 = QPushButton('Сохранить заметку')
button_4 = QPushButton('Добавить к заметке')
button_5 = QPushButton('Открепить от заметки')
button_6 = QPushButton('Искать заметки по тегу')
text_place = QTextEdit()
notes_list = QListWidget()
tegs_list = QListWidget()
write_teg = QLineEdit()
write_teg.setPlaceholderText('Введите тег')
vertical_line_1 = QVBoxLayout()# размещение QTextEdit()
vertical_line_2 = QVBoxLayout()# 
horisontal_line_1 = QHBoxLayout()
horizontal_line_2 = QHBoxLayout()
horizontal_line_3 = QHBoxLayout()
vertical_line_1.addWidget(text_place)
vertical_line_2.addWidget(text)
vertical_line_2.addWidget(notes_list)
horizontal_line_2.addWidget(button_1, alignment = Qt.AlignCenter)
horizontal_line_2.addWidget(button_2, alignment = Qt.AlignCenter)
vertical_line_2.addLayout(horizontal_line_2)
vertical_line_2.addWidget(button_3)
vertical_line_2.addWidget(text_2)
vertical_line_2.addWidget(tegs_list)
vertical_line_2.addWidget(write_teg)
horizontal_line_3.addWidget(button_4)
horizontal_line_3.addWidget(button_5)
vertical_line_2.addLayout(horizontal_line_3)
vertical_line_2.addWidget(button_6)
horisontal_line_1.addLayout(vertical_line_1)
horisontal_line_1.addLayout(vertical_line_2)
app_content.setLayout(horisontal_line_1)
notes_list.itemClicked.connect(show_note)
button_1.clicked.connect(add_note)
button_2.clicked.connect(del_note)
button_3.clicked.connect(save_note)
button_4.clicked.connect(add_tag)
button_5.clicked.connect(del_tag)
button_6.clicked.connect(search_note)

with open('notes_data.json', 'r') as file:
    notes = json.load(file)
print(notes)
notes_list.addItems(notes)
app_content.show()# отбражение окна (виджета)
app.exec_()'''