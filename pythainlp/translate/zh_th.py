# -*- coding: utf-8 -*-
"""
Lalita Chinese-Thai Machine Translation

from Ai builder

- GitHub: https://github.com/LalitaDeelert/lalita-mt-zhth
- Facebook post https://web.facebook.com/aibuildersx/posts/166736255494822
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class ThZhTranslator:
    def __init__(self, pretrained: str = "Lalita/marianmt-th-zh_cn") -> None:
        self.tokenizer_thzh = AutoTokenizer.from_pretrained(pretrained)
        self.model_thzh = AutoModelForSeq2SeqLM.from_pretrained(pretrained)

    def translate(self, text: str) -> str:
        """
        Translate text from Thai to Chinese

        :param str text: input text in source language
        :return: translated text in target language
        :rtype: str

        :Example:

        Translate text from Thai to Chinese::

            from pythainlp.translate import ThZhTranslator

            thzh = ThZhTranslator()

            thzh.translate("ผมรักคุณ")
            # output: 我爱你

        """
        self.translated = self.model_thzh.generate(
            **self.tokenizer_thzh(text, return_tensors="pt", padding=True)
        )
        return [
            self.tokenizer_thzh.decode(
                t, skip_special_tokens=True
            ) for t in self.translated
        ][0]


class ZhThTranslator:
    def __init__(self, pretrained: str = "Lalita/marianmt-zh_cn-th") -> None:
        self.tokenizer_zhth = AutoTokenizer.from_pretrained(pretrained)
        self.model_zhth = AutoModelForSeq2SeqLM.from_pretrained(pretrained)

    def translate(self, text: str) -> str:
        """
        Translate text from Chinese to Thai

        :param str text: input text in source language
        :return: translated text in target language
        :rtype: str

        :Example:

        Translate text from Chinese to Thai::

            from pythainlp.translate import ZhThTranslator

            zhth = ZhThTranslator()

            zhth.translate("我爱你")
            # output: ผมรักคุณนะ

        """
        self.translated = self.model_zhth.generate(
            **self.tokenizer_zhth(text, return_tensors="pt", padding=True)
        )
        return [
            self.tokenizer_zhth.decode(
                t, skip_special_tokens=True
            ) for t in self.translated
        ][0]
