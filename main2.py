import pygame
from pygame import mixer

# Inisialisasi pygame
pygame.init()
pygame.mixer.set_num_channels(50)

# Konfigurasi layar
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Python Piano")

fps = 60
timer = pygame.time.Clock()

# Memuat suara
white_notes = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1',
               'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2',
               'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3',
               'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
               'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
               'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6',
               'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7',
               'A7', 'B7', 'C8']

black_notes = ['Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
               'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
               'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
               'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
               'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
               'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
               'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
               'Bb7']

white_sounds = [mixer.Sound(f'notes\\{note}.wav') for note in white_notes]
black_sounds = [mixer.Sound(f'notes\\{note}.wav') for note in black_notes]

# Key mapping
left_hand = {'Z': 'C4', 'X': 'D4', 'C': 'E4', 'V': 'F4', 'B': 'G4', 'N': 'A4', 'M': 'B4'}
right_hand = {'A': 'C5', 'S': 'D5', 'D': 'E5', 'F': 'F5', 'G': 'G5', 'H': 'A5', 'J': 'B5'}

key_states = {}

# Fungsi memulai suara
def play_note(note):
    if note in white_notes:
        index = white_notes.index(note)
        white_sounds[index].play()
    elif note in black_notes:
        index = black_notes.index(note)
        black_sounds[index].play()

# Fungsi menghentikan suara
def stop_note(note):
    if note in white_notes:
        index = white_notes.index(note)
        white_sounds[index].stop()
    elif note in black_notes:
        index = black_notes.index(note)
        black_sounds[index].stop()

# Program utama
run = True
while run:
    screen.fill('gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            key = event.unicode.upper()
            if key in left_hand and key not in key_states:
                note = left_hand[key]
                play_note(note)
                key_states[key] = True
            elif key in right_hand and key not in key_states:
                note = right_hand[key]
                play_note(note)
                key_states[key] = True

        if event.type == pygame.KEYUP:
            key = event.unicode.upper()
            if key in key_states:
                if key in left_hand:
                    stop_note(left_hand[key])
                elif key in right_hand:
                    stop_note(right_hand[key])
                key_states.pop(key)

    pygame.display.flip()
    timer.tick(fps)

pygame.quit()
