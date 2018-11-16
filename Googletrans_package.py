from googletrans import Translator

translator = Translator()
print(translator.translate('你好.'))
# Translated(src=zh-CN, dest=en, text=Hello there., pronunciation=None, extra_data="{'translat...")

translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='zh-tw')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)

'''
The quick brown fox  ->  快速的棕色狐狸
jumps over  ->  跳過來
the lazy dog  ->  懶狗
'''

print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))
#Detected(lang=ko, confidence=1)
print(translator.detect('我是一隻豬.'))
#Detected(lang=zh-CN, confidence=1)
