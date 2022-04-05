from msilib import RadioButtonGroup
from re import U
from PIL import ImageGrab
import pyautogui
from os import system


mana_direita = (1832, 323, 1833, 324)
vida_direita = (1841, 311, 1842, 312)
vida_direita_metade = (1810, 311, 1811, 312)

rgb_mana_valor_direita = (116, 113, 255)
rgb_vida_valor_direita = (255, 125, 125)



def pegaRGBPixel(bbox):
    imagem = ImageGrab.grab(bbox).convert("RGB")
    r, g, b = imagem.getpixel((0, 0))
    return (r, g, b)


def main():
    
    i = 0
    
    programa_rodando = True
    while programa_rodando:
        
        
        if pegaRGBPixel(mana_direita) != (rgb_mana_valor_direita):
            pyautogui.press("f12")
            
        if pegaRGBPixel(vida_direita) != (rgb_vida_valor_direita):
            pyautogui.press("f10")
            
        if pegaRGBPixel(vida_direita_metade) != (rgb_vida_valor_direita):
            pyautogui.press("f11")
            

main()

#print(pegaRGBPixel(vida_direita))

