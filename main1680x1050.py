from msilib import RadioButtonGroup
from re import U
from PIL import ImageGrab
import pyautogui
from os import system


mana_direita = (1590, 323, 1591, 324)
vida_direita = (1594, 311, 1595, 312)
vida_direita_metade = (1571, 311, 1572, 312)

rgb_mana_valor_direita = (116, 113, 255)
rgb_vida_valor_direita = (255, 125, 125)



def pegaRGBPixel(bbox):
    imagem = ImageGrab.grab(bbox).convert("RGB")
    r, g, b = imagem.getpixel((0, 0))
    return (r, g, b)


def main():
    
    i = 0
    
    print("Autoflask rodando!")
    
    programa_rodando = True
    while programa_rodando:
        
        
        if pegaRGBPixel(mana_direita) != (rgb_mana_valor_direita):
            pyautogui.press("f12")
            print("Potion de mana usado!")
            
        if pegaRGBPixel(vida_direita) != (rgb_vida_valor_direita):
            pyautogui.press("f10")
            print("Spell de cura usado!")
            
        if pegaRGBPixel(vida_direita_metade) != (rgb_vida_valor_direita):
            pyautogui.press("f11")
            print("Potion de vida usado!")

main()

#print(pegaRGBPixel(vida_direita))

