from translate import Translator

translator=Translator(to_lang="Devanagari")
translation=translator.translate("How are you")
print(translation)