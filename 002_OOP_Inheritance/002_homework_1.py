# Создать класс Editor, который содержит методы view_document и edit_document. Пусть метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной версии. Создать подкласс ProEditor, в котором данный метод будет переопределён.
# Ввести с клавиатуры лицензионный ключ и, если он корректный, создать экземпляр класса ProEditor,
# иначе Editor. Вызвать методы просмотра и редактирования документов.


# Класс редактора
class Editor():
    # Метод просмотра
    def view_document(self):
        print('View document')

    # Метод редактирования
    def edit_document(self):
        print('Edit document is available only in the Pro version!')


# Класс Про редактора
class ProEditor(Editor):
    # Переопределение метода редактирования
    def edit_document(self):
        print('Edit document')


# Главная функция
def main():
    pro_key = 'Pro_2021'
    user_key = input('Enter Key Pro version for try edit document: ')
    if user_key == pro_key:
        print('You use Pro version and can edit document')
        doc = ProEditor()
    else:
        print('You use free version and can\'t edit document')
        doc = Editor()

    doc.view_document()
    doc.edit_document()


# Начало программы
if __name__ == '__main__':
    main()
